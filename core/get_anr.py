import os
import get_path
import openpyxl as xl

def get_anr_key_info():
    if not os.path.exists(get_path.get_anr_list_path()):
        return
    with open(get_path.get_anr_list_path(), "r", encoding="UTF_8") as rf:
        for line in rf:
            anr_event_log_path = os.path.join(get_path.get_sde_path(), line.strip(), "event.log")
            if not os.path.exists(anr_event_log_path):
                print("WARNING: %s 文件不存在" % anr_event_log_path)
                continue

            with open(anr_event_log_path, "r", encoding='UTF-8') as rf:
                for line in rf:
                    if 'I am_anr' in line:
                        write_anr_key_info(line)

    
    
def write_anr_key_info(line):
    # 写log
    #with open(os.path.join(get_path.get_key_info_dir_path(), "all_anr.log"), "a", encoding="UTF_8") as wf:
    #    wf.write(line)
    
    # 写xlsx
    xlsx_path = get_path.get_xlsx_path()
    workbook = xl.load_workbook(xlsx_path)
    sheet = workbook.active
    sheet.append(["anr", line.strip()])
    workbook.save(xlsx_path)
    

if __name__ == '__main__':
    get_anr_key_info()