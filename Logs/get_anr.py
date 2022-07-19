import os


def get_anr_key_info(anr_event_log_path, key_info_path):
    if not os.path.exists(anr_event_log_path):
        print("%s 文件不存在" % anr_event_log_path)
        return

    rf = open(anr_event_log_path, "r", encoding='UTF-8')
    for line in rf:
        if 'I am_anr' in line:
            write_line(key_info_path, line)

    rf.close()
    
    
def write_line(key_info_path, line):
    wf = open(key_info_path, "a", encoding="UTF_8")
    wf.write(line)
    wf.close()
    

if __name__ == '__main__':
    anr_event_log_path = "event.log"
    key_info_path = "anr_com.abc.log"
    get_anr_key_info(anr_event_log_path, key_info_path)