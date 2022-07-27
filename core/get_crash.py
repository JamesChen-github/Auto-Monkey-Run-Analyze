from msilib.schema import Font
import os
import get_path
import openpyxl as xl

def get_crash_key_info():
    crash_log_path = find_last_crash_log()
    with open(crash_log_path, "r", encoding='UTF-8') as rf:
        file = []
        for line in rf:
            file.append(line.strip())
        write_crash_key_info(file)
    
    
def write_crash_key_info(file):
    # 写log
    #with open(os.path.join(get_path.get_tmp_dir_path(), "all_crash.log"), "a", encoding="UTF_8") as wf:
    #    wf.writelines(file)
    
    # 写xlsx
    del file[0]
    xlsx_path = get_path.get_xlsx_path()
    workbook = xl.load_workbook(xlsx_path)
    sheet = workbook.active
    write = 1
    crash_times = {}
    crash_content = {}
    last_crash = []
    crash_key = ""
    for line in file:
        if 'FATAL EXCEPTION' in line:
            if write == 1:
                crash_content[crash_key] = last_crash.copy()
            # print(crash_content[crash_key])
            last_crash.clear()
            continue
        elif 'Process:' in line:
            crash_key = line[49:80]
            if crash_key in crash_times:
                crash_times[crash_key] += 1
                write = 0
            else:
                crash_times[crash_key] = 1
                last_crash.append(line.strip())
                write = 1
            continue
        if write == 1:
            last_crash.append(line.strip())
            # location = "B" + (str)(count-2)
            # sheet[location].value = line[58:90]
            # sheet[location].font = Font(bold = True)
    # print(crash_content)
    if write == 1:
        crash_content[crash_key] = last_crash.copy()
    last_crash.clear()
    for key in crash_times:
        sheet.append(["java_crash(发生%d次)" % crash_times[key]])
        #print(crash_content[key])
        for line in crash_content[key]:
            sheet.append(["", line.strip()])

    workbook.save(xlsx_path)


def find_last_crash_log():
    if not os.path.exists(get_path.get_crash_list_path()):
        return
    crash_logs = {}
    with open(get_path.get_crash_list_path(), "r", encoding="UTF_8") as rf:
        for line in rf:
            crash_log_path = os.path.join(get_path.get_sde_path(), line.strip(), "crash.log")
            if not os.path.exists(crash_log_path):
                print("WARNING: %s 文件不存在" % crash_log_path)
                continue
            crash_logs[crash_log_path] = os.path.getsize(crash_log_path)
            #print(os.path.getsize(crash_log_path))
    last_crash_log = max(crash_logs, key=crash_logs.get)
    print("INFO: 最新crash.log文件目录：%s" % last_crash_log)
    return last_crash_log


if __name__ == '__main__':
    get_crash_key_info()