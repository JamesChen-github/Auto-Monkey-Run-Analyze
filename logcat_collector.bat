::清理现有logcat日志
echo "adb logcat -c"
.\adb logcat -c

::拉取logcat
echo "adb logcat"
.\adb logcat -v time > .\Logs\logcat.log