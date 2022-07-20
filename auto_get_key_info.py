import get_crash as crash
import get_anr as anr
import get_native_crash as native
import os
import get_path
import create_xlsx


# 获取sde文件夹下的文件夹名称
def list_apk():
    sde_path = get_path.get_sde_path()
    # os.listdir()方法获取文件夹名字，返回数组
    file_name_list = os.listdir(sde_path)
    
    # 创建并打开文件filename_list.txt
    with open(get_path.get_errorname_list_path(), "w") as f:
    
        # 将文件下名称写入到"errorname_list.txt"
        for file_name in file_name_list:
            if not '.txt' in file_name:
                f.write(file_name+"\n")
        
        #一个app只选一个文件
        # app_name = get_app_name(file_name)
        # if not app_name in app_names and not app_name == "this is not an app":
        #     app_names.append(app_name)
        #     f.write(file_name+"\n")
            #print(app_name)




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


def create_key_info_dir():
    key_info_dir_path = get_path.get_key_info_dir_path()
    while os.path.exists(key_info_dir_path):
        print("请删除当前Logs文件夹下的key_info文件夹后继续程序")
        os.system("pause")
    os.mkdir(key_info_dir_path)


def auto_get_key_log():
    create_key_info_dir()
    list_apk()
    create_xlsx.create_xlsx()
    key_info_dir_path = get_path.get_key_info_dir_path()
    sde_path = get_path.get_sde_path()
    with open(get_path.get_errorname_list_path(), "r") as f:
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

    
    print("key_info提取完成\n")
    # crash.get_crash_key_info()
    # native.get_native_crash_key_info()


    

if __name__ == '__main__':
    auto_get_key_log()