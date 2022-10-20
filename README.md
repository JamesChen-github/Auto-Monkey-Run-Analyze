# 使用步骤
version:20221020
revised by chenjiahao
---
1. 连接设备，试一下adb root和adb remount能否成功

2. 打开串口并记录数据（与本脚本无关，可选）

3. 修改monkey脚本（monkey_test.bat），然后双击脚本运行

4. monkey停止后，用script里的Log_Collector抓取log，然后运行auto_get_key_info.py {last_log所在文件夹}，将自动生成xlsx报告
