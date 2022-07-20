import time
import os

# 这个py文件中包含有可能要修改的路径信息
# 和测试过程中常改的信息

def get_date():
    today = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    return "2000-01-01"
    #return today


# 获取last_log文件夹路径
def get_last_log_path():
    date_dir = get_date()
    return os.path.join(os.getcwd(), "Logs", date_dir, "last_log")


# 获取logcat路径
def get_logcat_path():
    #获取今日日期的文件夹
    date_dir = get_date()
    
    #找到logcat
    logcat_path = os.path.join(os.getcwd(), "Logs", date_dir, "logcat.log")
    return logcat_path


# key_info提取到哪个文件夹
def get_key_info_dir_path():
    return os.path.join(os.getcwd(), "Logs", "key_info")


# 获取sde文件夹路径
def get_sde_path():
    return os.path.join(get_last_log_path(), "sde")


# 获取filename_list文件路径，这个文件里面放着sde文件夹下的每个error文件夹的名字
def get_errorname_list_path():
    return get_key_info_dir_path()+"\\errorname_list.txt"


def get_xlsx_path():
    return os.path.join(get_key_info_dir_path(), "key_info.xlsx")


# 共享域相关路径定义
# logcat路径
def get_logcat_hyperlink():
    return os.path.join("\\\\192.168.0.195\\RND Share\\SW\\Android\\05_Log\\monkey_test_Jiahao", get_date(), "logcat.log")

# monkey_info路径
def get_monkey_info_hyperlink():
    return os.path.join("\\\\192.168.0.195\\RND Share\\SW\\Android\\05_Log\\monkey_test_Jiahao", get_date(), "monkey_info_log.log")

# monkey_error路径
def get_monkey_error_hyperlink():
    return os.path.join("\\\\192.168.0.195\\RND Share\\SW\\Android\\05_Log\\monkey_test_Jiahao", get_date(), "monkey_error_log.log")

def get_serial_hyperlink():
    return os.path.join("\\\\192.168.0.195\\RND Share\\SW\\Android\\05_Log\\monkey_test_Jiahao", get_date())

