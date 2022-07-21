import get_crash as crash
import get_anr as anr
import get_native_crash as native
import os
import get_path
import create_xlsx


# 获取sde文件夹下的文件夹名称并分类
def list_error():
    sde_path = get_path.get_sde_path()
    # os.listdir()方法获取文件夹名字，返回数组
    file_name_list = os.listdir(sde_path)
    for file_name in file_name_list:
        a = file_name.strip()
        #app_name = get_app_name(a)
        key_info_path = os.path.join(get_path.get_key_info_dir_path(), a + ".log")
        if 'native_crash_' in file_name:
            with open(get_path.get_native_crash_list_path(), "a", encoding="UTF_8") as f:
                f.write(file_name+"\n")
        elif 'crash_' in file_name:
            with open(get_path.get_crash_list_path(), "a", encoding="UTF_8") as f:
                f.write(file_name+"\n")
        elif 'anr_' in file_name:
            with open(get_path.get_anr_list_path(), "a", encoding="UTF_8") as f:
                f.write(file_name+"\n")
        elif 'exceptionRecord.txt' in file_name:
            pass
        else:
            with open(get_path.get_key_info_dir_path()+"\\others.txt", "a") as f:
                f.write(file_name+"\n")
        
        #一个app只选一个文件
        # app_name = get_app_name(file_name)
        # if not app_name in app_names and not app_name == "this is not an app":
        #     app_names.append(app_name)
        #     f.write(file_name+"\n")
            #print(app_name)


def create_key_info_dir():
    key_info_dir_path = get_path.get_key_info_dir_path()
    if os.path.exists(key_info_dir_path):
        # 删除key_info文件夹
        import shutil
        try:
            shutil.rmtree(key_info_dir_path)
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))
        # print("请删除当前Logs\日期文件夹下的key_info文件夹后继续程序")
        # os.system("pause")
    os.mkdir(key_info_dir_path)


def auto_get_key_log():
    create_key_info_dir()
    list_error()
    create_xlsx.create_xlsx()
    print("正在提取......")
    native.get_native_crash_key_info()
    crash.get_crash_key_info()
    anr.get_anr_key_info()
        
    print("key_info提取完成\n")
    # crash.get_crash_key_info()
    # native.get_native_crash_key_info()


    

if __name__ == '__main__':
    auto_get_key_log()