import os
import get_path
import openpyxl as xl

def get_anr_key_info(anr_event_log_path, key_info_path):
    if not os.path.exists(anr_event_log_path):
        print("%s 文件不存在" % anr_event_log_path)
        return

    with open(anr_event_log_path, "r", encoding='UTF-8') as rf:
        for line in rf:
            if 'I am_anr' in line:
                write_line(key_info_path, line)

    
    
def write_line(key_info_path, line):
    # 写log
    with open(os.path.dirname(key_info_path)+"\\all_anr.log", "a", encoding="UTF_8") as wf:
        wf.write(line)
    
    # 写xlsx
    xlsx_path = get_path.get_xlsx_path()
    workbook = xl.load_workbook(xlsx_path)
    sheet = workbook.active
    sheet.append(["anr", line.strip()])
    workbook.save(xlsx_path)
    

if __name__ == '__main__':
    anr_event_log_path = "event.log"
    key_info_path = "anr_com.abc.log"
    get_anr_key_info(anr_event_log_path, key_info_path)