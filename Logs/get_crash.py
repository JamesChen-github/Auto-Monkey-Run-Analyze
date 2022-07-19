import os


def find_count(crash_log_path):
    count = 0
    rf = open(crash_log_path, "r", encoding='UTF-8')
    for line in rf:
        if 'FATAL EXCEPTION' in line:
            count+=1
    rf.close()
    #print("这个crash.log文件中有%d个FATAL EXCEPTION" % count)
    return count


def read_write_last_fatal_exception(crash_log_path, key_info_path, count):
    write = 0
    rf = open(crash_log_path, "r", encoding='UTF-8')
    for line in rf:
        if 'FATAL EXCEPTION' in line:
            count-=1
            if count == 0:
                write = 1
        if write == 1:
            write_last_fatal_exception(key_info_path, line)
    rf.close()
    
def write_last_fatal_exception(key_info_path, line):
    wf = open(key_info_path, "a", encoding="UTF_8")
    wf.write(line)
    wf.close()


def get_crash_key_info(crash_log_path, key_info_path):
    if not os.path.exists(crash_log_path):
        print("%s 文件不存在" % crash_log_path)
        return
    count = find_count(crash_log_path)
    read_write_last_fatal_exception(crash_log_path, key_info_path, count)
    
    
if __name__ == '__main__':
    crash_log_path = "crash.log"
    key_info_path = "crash_com.abc.log"
    get_crash_key_info(crash_log_path, key_info_path)