import os
import get_path
import openpyxl as xl

def abc():
    pass
def get_native_crash_key_info():
    if not os.path.exists(get_path.get_native_crash_list_path()):
        return
    with open(get_path.get_native_crash_list_path(), "r", encoding="UTF_8") as rf:
        for line in rf:
            native_crash_tombstone_path = os.path.join(get_path.get_sde_path(), line.strip(), "tombstone")
            if not os.path.exists(native_crash_tombstone_path):
                print("WARNING: %s 文件不存在" % native_crash_tombstone_path)
                continue
            
            write = 0
            backtrace = 0
            
            # xlsx标题
            xlsx_path = get_path.get_xlsx_path()
            workbook = xl.load_workbook(xlsx_path)
            sheet = workbook.active
            sheet.append(["native_crash"])
            workbook.save(xlsx_path)
            
            with open(native_crash_tombstone_path, "r", encoding='UTF-8') as rf:
                file = []
                for line in rf:
                    if 'Cmdline:' in line:
                        write = 1
                        #print(line)
                    if 'backtrace' in line:
                        backtrace = 1
                    if backtrace == 1 and ( '--- ---' in line or line.strip() == ""):
                        write = 0
                        break
                    if write == 1:
                        file.append(line.strip())
                        #write_line(line)
                write_native_crash_key_info(file)
    
    
def write_native_crash_key_info(file):
    # 写log
    #with open(os.path.join(get_path.get_key_info_dir_path(), "all_native_crash.log"), "a", encoding="UTF_8") as wf:
    #    wf.writelines(file)
    
    # 写xlsx
    xlsx_path = get_path.get_xlsx_path()
    workbook = xl.load_workbook(xlsx_path)
    sheet = workbook.active
    for line in file:
        sheet.append(["", line])
    workbook.save(xlsx_path)
    

if __name__ == '__main__':
    get_native_crash_key_info()