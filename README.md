version:20220720
revised by cjh

![image](https://user-images.githubusercontent.com/70957022/180348759-d4f52ed9-92cd-46ca-bdde-687c3b8f668b.png)

使用步骤
1. 连接设备，试一下adb root和adb remount能否成功
2. 打开串口并记录数据（与本脚本无关，可选）
3. 打开monkey自动测试脚本（选择一个monkey脚本运行，with resources或without resources的那个）
4. monkey运行结束后会自动下载log，如果monkey过程中卡住，要按Ctrl+C退出并输入"N"不要退出脚本，脚本会继续运行
5. last_log下载完之后，运行auto_get_key_info.py文件，将自动提取关键信息到Logs\key_info文件夹
