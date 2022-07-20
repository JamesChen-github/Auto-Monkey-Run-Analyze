import os
import get_path
import openpyxl as xl

def how_many_fatal_exceptions(crash_log_path):
    count = 0
    with open(crash_log_path, "r", encoding='UTF-8') as rf:
        for line in rf:
            if 'FATAL EXCEPTION' in line:
                count+=1
    #print("这个crash.log文件中有%d个FATAL EXCEPTION" % count)
    return count


def read_write_last_fatal_exception(crash_log_path, key_info_path, count):
    write = 0
    
    # 记录这是一个文件
    xlsx_path = get_path.get_xlsx_path()
    workbook = xl.load_workbook(xlsx_path)
    sheet = workbook.active
    sheet.append(["crash"])
    workbook.save(xlsx_path)
    
    with open(crash_log_path, "r", encoding='UTF-8') as rf:
        for line in rf:
            if 'FATAL EXCEPTION' in line:
                count-=1
                if count == 0:
                    write = 1
            if write == 1:
                write_last_fatal_exception(key_info_path, line)
    
def write_last_fatal_exception(key_info_path, line):
    # 写log
    with open(key_info_path, "a", encoding="UTF_8") as wf:
        wf.write(line)
    
    # 写xlsx
    xlsx_path = get_path.get_xlsx_path()
    workbook = xl.load_workbook(xlsx_path)
    sheet = workbook.active
    sheet.append(["", line.strip()])
    workbook.save(xlsx_path)


def get_crash_key_info(crash_log_path, key_info_path):
    if not os.path.exists(crash_log_path):
        print("%s 文件不存在" % crash_log_path)
        return
    count = how_many_fatal_exceptions(crash_log_path)
    read_write_last_fatal_exception(crash_log_path, key_info_path, count)
    
    
if __name__ == '__main__':
    crash_log_path = "crash.log"
    key_info_path = "crash_com.abc.log"
    get_crash_key_info(crash_log_path, key_info_path)