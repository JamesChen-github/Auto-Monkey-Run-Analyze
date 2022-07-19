# Auto-Monkey-Run-Analyze
自动运行并提取关键信息的monkey自动化测试脚本，包含python和bat


version:20220715
revised by cjh

使用步骤
1. 连接设备，试一下adb root adb remount
2. 打开串口并记录数据（与本脚本无关，可选）
3. 打开logcat_collector（保持运行）
4. 打开monkey（选择一个monkey脚本运行）
5. monkey运行结束后会自动下载log，如果monkey过程中卡住，要按Ctrl+C退出并输入"N"不要退出脚本，脚本会继续运行
6. last_log下载完之后，运行Logs文件夹里的auto_get_log.py文件，自动提取关键信息到key_info文件夹
