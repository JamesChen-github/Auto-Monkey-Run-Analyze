echo "adb root"
adb root
echo "adb remount"
adb remount

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

echo "sync"
adb shell sync
echo "sync"
adb shell sync

pause