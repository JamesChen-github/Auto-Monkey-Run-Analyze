@REM ::清理现有logcat日志
@REM echo "adb logcat -c"
@REM .\adb logcat -c

::拉取logcat
echo "adb logcat"
.\adb logcat -d -v time > .\Logs\logcat.log

pause
pause