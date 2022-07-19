::清理现有日志
echo "adb logcat -c"
.\adb logcat -c

::开始记录logcat
echo "adb logcat"
.\adb logcat -v time > .\logcat.log