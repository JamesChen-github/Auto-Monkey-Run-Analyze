from array import array
import get_crash as crash
import get_anr as anr
import get_native_crash as native
import time
import os
import sys


# last_log_path = "date_dir"
# print("sys.argv[0] = ", sys.argv[0])
# os.path.join(sys.argv[0])

def get_date_dir():
    today = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    #print(today)
    #print(type(today))
    date_dir = today
    return "2000-01-01"


# 获取sde文件夹路径
def get_sde_path():
    #获取今日日期的文件夹
    date_dir = get_date_dir()
    
    #找到sde文件夹
    current_dir = os.getcwd()
    #print(os.getcwd())
    sde_path = os.path.join(current_dir, date_dir, "last_log", "sde")
    #print(sde_path)
    return sde_path


# 
def get_key_info_dir_path():
    while os.path.exists("key_info"):
        print("请删除当前文件夹下的key_info文件夹后继续程序")
        os.system("pause")
    os.mkdir("key_info")
    key_info_dir_path = os.path.join(os.getcwd(), "key_info")
    return key_info_dir_path


# 这个函数没用到
def get_app_name(file_name):
    if 'native_crash' in file_name:
        app_name_rear = file_name.index("202")
        app_name = file_name[13:app_name_rear-1]
    elif 'crash' in file_name:
        app_name_rear = file_name.index("202")
        app_name = file_name[6:app_name_rear-1]
    elif 'anr' in file_name:
        app_name_rear = file_name.index("202")
        app_name = file_name[4:app_name_rear-1]
    else:
        app_name = "this is not an app"
    return app_name



# 获取出错的apk名称并且去重
def list_apk(sde_path):
    # os.listdir()方法获取文件夹名字，返回数组
    file_name_list = os.listdir(sde_path)
    
    # 创建并打开文件list.txt
    f = open(sde_path + "\\" + "filename_list.txt", "w")
    
    app_names = []
    # 将文件下名称写入到"list.txt"
    for file_name in file_name_list:
        f.write(file_name+"\n")
        
        #一个app只选一个文件
        # app_name = get_app_name(file_name)
        # if not app_name in app_names and not app_name == "this is not an app":
        #     app_names.append(app_name)
        #     f.write(file_name+"\n")
            #print(app_name)


def auto_get_log():
    sde_path = get_sde_path()
    list_apk(sde_path)
    key_info_dir_path = get_key_info_dir_path()
    f = open(sde_path+"\\filename_list.txt", "r")
    for line in f:
        a = line.strip()
        #app_name = get_app_name(a)
        key_info_path = os.path.join(key_info_dir_path, a + ".log")
        if 'native_crash_' in line:
            native_crash_tombstone_path = os.path.join(sde_path,a,"tombstone")
            #print(native_crash_tombstone_path)
            native.get_native_crash_key_info(native_crash_tombstone_path, key_info_path)
        elif 'crash_' in line:
            crash_log_path = os.path.join(sde_path,a,"crash.log")
            #print(crash_log_path)
            crash.get_crash_key_info(crash_log_path, key_info_path)
        elif 'anr_' in line:
            anr_log_path = os.path.join(sde_path,a,"event.log")
            #print(anr_log_path)
            anr.get_anr_key_info(anr_log_path, key_info_path)
            #还没写
    f.close()
    print("key_info提取完成\n")
    # crash.get_crash_key_info()
    # native.get_native_crash_key_info()

if __name__ == '__main__':
    auto_get_log()