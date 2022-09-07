import subprocess
import os
import time


def clicker():
    # 按下500 300处
    subp1 = subprocess.call("adb shell input tap 500 300", shell=True)
    time.sleep(2)

    # home按键
    supb2 = subprocess.call("adb shell input keyevent 3", shell=True)
    time.sleep(2)
    
    subp3 = subprocess.call('adb shell "ps -A  |  grep system_server"', shell=True)
    subp4 = subprocess.call('adb shell "ps -A  |  grep launcher"', shell=True)


if __name__ == "__main__":
    for i in range(1, 100000):
        print("第%d次测试:" % i)
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
        clicker()
        print()