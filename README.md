version:20220722
revised by cjh
---
## 使用步骤
1. 连接设备，试一下adb root和adb remount能否成功  


2. 打开串口并记录数据（与本脚本无关，可选）   


3. 运行sdrv_logs.bat，运行完关掉即可

4. 打开monkey自动测试脚本（选择一个monkey脚本运行，with resources或without resources二选一，with resources会先像设备/sdcard/中传输音视频等数据）

    显示到这里就代表已经开始执行monkey

5. monkey运行结束后会自动下载log，如果monkey过程中卡住，要按Ctrl+C退出并输入"N"不要退出脚本，脚本会继续运行

6. 显示报告下载完成之后关掉脚本，在Logs文件夹下建立当天日期命名的文件夹，如2022-07-22，并把Logs文件夹下所有生成的文件移入该文件夹(当前无法自动完成，后续可能会优化)

7. 运行auto_get_key_info.py文件，将自动生成xlsx报告到Logs\2022-07-22\目录下
