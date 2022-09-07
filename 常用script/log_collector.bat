::version 20220715
::revised by cjh

@echo OFF


::编码=UTF-8
chcp 65001


@REM @REM 存放目录
@REM echo "mkdirs"
@REM @REM 不同编码%date%不同
@REM set datedir=logs\%date:~3,4%-%date:~8,2%-%date:~11,2%
@REM if exist %datedir% (
@REM 	echo dir already exists!!!
@REM 	echo %datedir%已存在,本次将存放在%datedir%-1文件夹中
@REM 	set datedir=logs\%date:~3,4%-%date:~8,2%-%date:~11,2%-1
@REM )
@REM echo %datedir%
@REM md %datedir%
@REM set filename=%datedir%\last_log
@REM echo %filename%
@REM md %filename%

echo **********************************************************************************************
echo 开始下载LOG报告
echo **********************************************************************************************


echo "Log_Collect"


set filename=last_log

echo "sync"
adb shell sync

echo "sync"
adb shell sync


echo "adb root"
adb root
echo "adb shell sleep 2"
adb shell sleep 2
echo "adb remount"
adb remount
echo "adb shell sleep 2"
adb shell sleep 2
echo "adb pull /data/sdrv_logs"
adb pull /data/sdrv_logs %filename%
echo "adb pull /data/misc/bluetooth"
adb pull /data/misc/bluetooth %filename%
echo "adb pull /data/sdrv_deviceinfo"
adb pull /data/sdrv_deviceinfo %filename%
echo "adb pull /data/anr"
adb pull /data/anr %filename%
echo "adb pull /data/sde"
adb pull /data/sde %filename%
echo "adb pull /data/tombstones"
adb pull /data/tombstones %filename%
echo "dumpsys meminfo"
adb shell dumpsys meminfo > %filename%/meminfo.txt
echo "cat /proc/meminfo"
adb shell cat /proc/meminfo > %filename%/meminfo2.txt
echo "dumpsys cpuinfo"
adb shell dumpsys cpuinfo > %filename%/cpuinfo.txt
echo "dumpsys input"
adb shell dumpsys input > %filename%/input.txt
echo "dumpsys surfaceflinger"
adb shell dumpsys SurfaceFlinger > %filename%/sf.txt
echo "procrank"
adb shell procrank > %filename%/procrank.txt
echo "getprop"
adb shell getprop > %filename%/build_prop.txt
echo "ps -elf"
adb shell ps -elf > %filename%/ps.txt
echo "adb pull binder"
adb pull /sys/kernel/debug/binder %filename%
echo "df"
adb shell df > %filename%/df.txt
echo "screenshot"
adb shell screencap -p /sdcard/screenshot.png
adb pull /sdcard/screenshot.png %filename%
echo "adb pull DB"
adb pull data/system/users/0 %filename%
echo "adb bugreport"
adb bugreport

@REM ::拉取logcat
@REM echo "adb logcat"
@REM adb logcat -d -v time > .\Logs\logcat.log

echo **********************************************************************************************
echo 报告下载完成：
echo **********************************************************************************************


pause