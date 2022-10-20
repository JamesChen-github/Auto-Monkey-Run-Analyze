adb root
adb remount
::打开sdrv_log，即常规日志
adb shell setprop persist.log.start 1
adb shell sync
adb shell sync

pause