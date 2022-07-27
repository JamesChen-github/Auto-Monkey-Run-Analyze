import os
import get_path
import openpyxl as xl

def abc():
    pass
def get_native_crash_key_info():
    if not os.path.exists(get_path.get_native_crash_list_path()):
        return
    
    native_crash_times = {}
    native_crash_content = {}
    native_crash_key = ""
    
    with open(get_path.get_native_crash_list_path(), "r", encoding="UTF_8") as rf:
        for line in rf:
            native_crash_tombstone_path = os.path.join(get_path.get_sde_path(), line.strip(), "tombstone")
            if not os.path.exists(native_crash_tombstone_path):
                print("WARNING: %s 文件不存在" % native_crash_tombstone_path)
                continue
            
            # # xlsx标题
            # xlsx_path = get_path.get_xlsx_path()
            # workbook = xl.load_workbook(xlsx_path)
            # sheet = workbook.active
            # sheet.append(["native_crash"])
            # workbook.save(xlsx_path)
            
            native_crash_key = get_native_crash_key(native_crash_tombstone_path)
            if native_crash_key in native_crash_times:
                native_crash_times[native_crash_key] += 1
                continue
            else:
                native_crash_times[native_crash_key] = 1
                file = get_native_crash_content(native_crash_tombstone_path)
                native_crash_content[native_crash_key] = file.copy()
                file.clear()
    
    xlsx_path = get_path.get_xlsx_path()
    workbook = xl.load_workbook(xlsx_path)
    sheet = workbook.active
    for key in native_crash_times:
        sheet.append(["native_crash(发生%d次)" % native_crash_times[key]])
        #print(crash_content[key])
        for line in native_crash_content[key]:
            sheet.append(["", line.strip()])

    workbook.save(xlsx_path)

def get_native_crash_key(native_crash_tombstone_path):
    with open(native_crash_tombstone_path, "r", encoding='UTF-8') as rf:
        for line in rf:
            if 'Cmdline:' in line:
                return line.strip()

def get_native_crash_content(native_crash_tombstone_path):
    write = 0
    backtrace = 0
    file = []
    with open(native_crash_tombstone_path, "r", encoding='UTF-8') as rf:
        for line in rf:
            if 'Cmdline:' in line:
                write = 1
            if 'backtrace' in line:
                backtrace = 1
            if backtrace == 1 and ( '--- ---' in line or line.strip() == ""):
                write = 0
                break
            if write == 1:
                file.append(line.strip())
    return file



if __name__ == '__main__':
    get_native_crash_key_info()