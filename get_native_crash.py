import os
import get_path
import openpyxl as xl

def get_native_crash_key_info(native_crash_tombstone_path, key_info_path):
    if not os.path.exists(native_crash_tombstone_path):
        print("%s 文件不存在" % native_crash_tombstone_path)
        return
    write = 0
    backtrace = 0
    
    # 记录这是一个文件
    xlsx_path = get_path.get_xlsx_path()
    workbook = xl.load_workbook(xlsx_path)
    sheet = workbook.active
    sheet.append(["native_crash"])
    workbook.save(xlsx_path)
    
    with open(native_crash_tombstone_path, "r", encoding='UTF-8') as rf:
        for line in rf:
            if 'Cmdline:' in line:
                write = 1
                #print(line)
            if write == 1:
                write_line(key_info_path, line)
            if 'backtrace' in line:
                backtrace = 1
            if backtrace == 1 and ( '--- ---' in line or line.strip() == ""):
                write = 0
                break
    
    
def write_line(key_info_path, line):
    # 写log
    with open(key_info_path, "a", encoding="UTF_8") as wf:
        wf.write(line)
    
    # 写xlsx
    xlsx_path = get_path.get_xlsx_path()
    workbook = xl.load_workbook(xlsx_path)
    sheet = workbook.active
    sheet.append(["", line.strip()])
    workbook.save(xlsx_path)
    

if __name__ == '__main__':
    native_crash_tombstone_path = "tombstone"
    key_info_path = "native_crash_com.abc.log"
    get_native_crash_key_info(native_crash_tombstone_path, key_info_path)