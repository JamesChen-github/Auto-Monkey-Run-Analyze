import time
import os

# 这个py文件中包含有可能要修改的路径信息
# 和测试过程中常改的信息


# 本地相关路径

def get_date():
    today = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    # return "2000-01-01"
    return today


# date_dir_path
def get_date_dir_path():
    return os.path.join(os.getcwd(), "Logs", get_date())


# 获取last_log文件夹路径
def get_last_log_path():
    return os.path.join(get_date_dir_path(), "last_log")


# 获取logcat路径
def get_logcat_path():
    return os.path.join(get_date_dir_path(), "logcat.log")


def get_version_path():
    return os.path.join(get_date_dir_path(), "测试版本.txt")


# key_info提取到哪个文件夹
def get_key_info_dir_path():
    return os.path.join(get_date_dir_path(), "tmp")

def get_native_crash_list_path():
    return os.path.join(get_key_info_dir_path(), "native_crash_list.txt")
def get_crash_list_path():
    return os.path.join(get_key_info_dir_path(), "crash_list.txt")
def get_anr_list_path():
    return os.path.join(get_key_info_dir_path(), "anr_list.txt")


# 获取sde文件夹路径
def get_sde_path():
    return os.path.join(get_last_log_path(), "sde")


# 获取filename_list文件路径，这个文件里面放着sde文件夹下的每个error文件夹的名字
def get_errorname_list_path():
    return get_key_info_dir_path()+"\\errorname_list.txt"

def get_xlsx_path():
    return os.path.join(get_date_dir_path(), get_date() + "压测报告.xlsx")


# 共享域相关路径定义
# logcat路径
def get_logcat_hyperlink():
    return os.path.join(r"\\192.168.0.195\RND Share\SW\Android\05_Log\monkey_test_Jiahao", get_date(), "logcat.log")

# monkey_info路径
def get_monkey_info_hyperlink():
    return os.path.join(r"\\192.168.0.195\RND Share\SW\Android\05_Log\monkey_test_Jiahao", get_date(), "monkey_info_log.log")

# monkey_error路径
def get_monkey_error_hyperlink():
    return os.path.join(r"\\192.168.0.195\RND Share\SW\Android\05_Log\monkey_test_Jiahao", get_date(), "monkey_error_log.log")

# 串口信息路径
def get_serial_hyperlink():
    return os.path.join(r"\\192.168.0.195\RND Share\SW\Android\05_Log\monkey_test_Jiahao", get_date())

# last_log文件夹路径
def get_last_log_hyperlink():
    return os.path.join(r"\\192.168.0.195\RND Share\SW\Android\05_Log\monkey_test_Jiahao", get_date(), "last_log")








# 其它通用函数


# 输入error文件夹名提取其中包名
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