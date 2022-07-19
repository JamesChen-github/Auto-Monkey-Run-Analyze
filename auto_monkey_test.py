import time
import os
import sys

today = time.strftime('%Y-%m-%d',time.localtime(time.time()))
print(today)
print(type(today))
date_dir = today

# while True:
#     if not os.path.exists(date_dir):  # 是否存在这个文件夹
#         break
#     else:
#         date_dir = date_dir + "(1)"
# os.makedirs(date_dir)  # 创建文件夹

# last_log_path = "date_dir"
# print("sys.argv[0] = ", sys.argv[0])
# os.path.join(sys.argv[0])

current_dir = os.getcwd()
print(os.getcwd())
log_path = os.path.join(current_dir, date_dir, "last_log", "sde")
print(log_path)