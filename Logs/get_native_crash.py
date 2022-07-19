import os


def get_native_crash_key_info(native_crash_tombstone_path, key_info_path):
    if not os.path.exists(native_crash_tombstone_path):
        print("%s 文件不存在" % native_crash_tombstone_path)
        return
    write = 0
    backtrace = 0
    rf = open(native_crash_tombstone_path, "r", encoding='UTF-8')
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
    rf.close()
    
    
def write_line(key_info_path, line):
    wf = open(key_info_path, "a", encoding="UTF_8")
    wf.write(line)
    wf.close()
    

if __name__ == '__main__':
    native_crash_tombstone_path = "tombstone"
    key_info_path = "native_crash_com.abc.log"
    get_native_crash_key_info(native_crash_tombstone_path, key_info_path)