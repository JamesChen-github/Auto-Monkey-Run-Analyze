::version 20220715
::revised by cjh


@ECHO OFF

::编码=UTF-8
chcp 65001


echo "adb root"
adb root

echo "adb shell sleep 2"
adb shell sleep 2

echo "adb remount"
adb remount

echo "adb shell sleep 2"
adb shell sleep 2

::清理现有日志
echo "adb logcat -c"
adb logcat -c
echo "adb shell rm -rf /data/sdrv_logs/*"
adb shell rm -rf /data/sdrv_logs/*
echo "adb shell rm -rf /data/misc/bluetooth/*"
adb shell rm -rf /data/misc/bluetooth/*
echo "adb shell rm -rf /data/sdrv_deviceinfo/*"
adb shell rm -rf /data/sdrv_deviceinfo/*
echo "adb shell rm -rf /data/anr/*"
adb shell rm -rf /data/anr/*
echo "adb shell rm -rf /data/sde/*"
adb shell rm -rf /data/sde/*
echo "adb shell rm -rf /data/tombstones/*"
adb shell rm -rf /data/tombstones/*


::打开sdrv_log，即常规日志
echo "adb shell setprop persist.log.start 1"
adb shell setprop persist.log.start 1

echo "sync"
adb shell sync

echo "sync"
adb shell sync

pause