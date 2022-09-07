#！/usr/bin/env python38
# coding=utf-8

import time
import subprocess

def cmd(command):
    subp = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding="utf-8")
    out = subp.communicate()
    print(out)
    if subp.poll()==0:
        print(subp.communicate()[1])
    else:
        print("失败")  

def mainRunner():
    for i in range(0,5000):
        print("\n第"+str(i+1)+"次测试开始:\n")
        cmd("adb reboot")
        time.sleep(50)
mainRunner()



