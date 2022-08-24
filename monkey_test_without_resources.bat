::version 20220715
::revised by cjh


@ECHO OFF

::编码=UTF-8
chcp 65001




@REM 存放目录
echo "mkdirs"
@REM 不同编码%date%不同
set datedir=logs\%date:~3,4%-%date:~8,2%-%date:~11,2%
if exist %datedir% (
	echo dir already exists!!!
	echo %datedir%已存在,本次将存放在%datedir%-1文件夹中
	set datedir=logs\%date:~3,4%-%date:~8,2%-%date:~11,2%-1
)
echo %datedir%
md %datedir%
set filename=%datedir%\last_log
echo %filename%
md %filename%


echo "adb root"
.\adb root

echo "adb shell sleep 2"
.\adb shell sleep 2

echo "adb remount"
.\adb remount

echo "adb shell sleep 2"
.\adb shell sleep 2


::清理现有日志
echo "adb logcat -c"
.\adb logcat -c
echo "adb shell rm -rf /data/sdrv_logs/*"
.\adb shell rm -rf /data/sdrv_logs/*
echo "adb shell rm -rf /data/misc/bluetooth/*"
.\adb shell rm -rf /data/misc/bluetooth/*
echo "adb shell rm -rf /data/sdrv_deviceinfo/*"
.\adb shell rm -rf /data/sdrv_deviceinfo/*
echo "adb shell rm -rf /data/anr/*"
.\adb shell rm -rf /data/anr/*
echo "adb shell rm -rf /data/sde/*"
.\adb shell rm -rf /data/sde/*
echo "adb shell rm -rf /data/tombstones/*"
.\adb shell rm -rf /data/tombstones/*


echo **********************************************************************************************
echo 开始执行Monkey Test
echo 测试开始时间：
echo %date%  %time%
echo **********************************************************************************************
echo "Monkey_Test"
echo monkey_test_all_packeages_except_settings



@REM ::拉取logcat
@REM echo "adb logcat"
@REM .\adb logcat -d -v time > .\logs\logcat.log

::打开sdrv_log，即常规日志
echo ".\adb shell setprop persist.log.start 1"
.\adb shell setprop persist.log.start 1

echo "adb shell sleep 2"
.\adb shell sleep 2

echo "adb push blacklist.txt /data/local/tmp/"
.\adb push blacklist.txt /data/local/tmp/

echo "sync"
.\adb shell sync

echo "sync"
.\adb shell sync

echo "adb shell monkey --pkg-blacklist-file /data/local/tmp/blacklist.txt --ignore-crashes --ignore-timeouts --ignore-security-exceptions --ignore-native-crashes --pct-syskeys 0 --throttle 200 -v -v -v 864000 1>%datedir%\monkey_info_log.log 2>%datedir%\monkey_error_log.log"
.\adb shell monkey --pkg-blacklist-file /data/local/tmp/blacklist.txt --ignore-crashes --ignore-timeouts --ignore-security-exceptions --ignore-native-crashes --pct-syskeys 0 --throttle 200 -v -v -v 864000 1>%datedir%\monkey_info_log.log 2>%datedir%\monkey_error_log.log

@REM echo "adb shell monkey --pkg-blacklist-file /data/local/tmp/blacklist.txt --ignore-crashes --ignore-timeouts --ignore-security-exceptions --ignore-native-crashes --pct-syskeys 0 --throttle 200 -v -v -v 864000 >%datedir%\monkey.txt"
@REM .\adb shell monkey --pkg-blacklist-file /data/local/tmp/blacklist.txt --ignore-crashes --ignore-timeouts --ignore-security-exceptions --ignore-native-crashes --pct-syskeys 0 --throttle 200 -v -v -v 864000 >%datedir%\monkey.txt


echo **********************************************************************************************
echo MONKEY测试结束时间：
echo %date%  %time%
echo 开始下载LOG报告
echo **********************************************************************************************


echo "Log_Collect"

echo "sync"
.\adb shell sync

echo "sync"
.\adb shell sync


echo "adb root"
.\adb root
echo "adb shell sleep 2"
.\adb shell sleep 2
echo "adb remount"
.\adb remount
echo "adb shell sleep 2"
.\adb shell sleep 2
echo "adb pull /data/sdrv_logs"
.\adb pull /data/sdrv_logs %filename%
echo "adb pull /data/misc/bluetooth"
.\adb pull /data/misc/bluetooth %filename%
echo "adb pull /data/sdrv_deviceinfo"
.\adb pull /data/sdrv_deviceinfo %filename%
echo "adb pull /data/anr"
.\adb pull /data/anr %filename%
echo "adb pull /data/sde"
.\adb pull /data/sde %filename%
echo "adb pull /data/tombstones"
.\adb pull /data/tombstones %filename%
echo "dumpsys meminfo"
.\adb shell dumpsys meminfo > %filename%/meminfo.txt
echo "cat /proc/meminfo"
.\adb shell cat /proc/meminfo > %filename%/meminfo2.txt
echo "dumpsys cpuinfo"
.\adb shell dumpsys cpuinfo > %filename%/cpuinfo.txt
echo "dumpsys input"
.\adb shell dumpsys input > %filename%/input.txt
echo "dumpsys surfaceflinger"
.\adb shell dumpsys SurfaceFlinger > %filename%/sf.txt
echo "procrank"
.\adb shell procrank > %filename%/procrank.txt
echo "getprop"
.\adb shell getprop > %filename%/build_prop.txt
echo "ps -elf"
.\adb shell ps -elf > %filename%/ps.txt
echo "adb pull binder"
.\adb pull /sys/kernel/debug/binder %filename%
echo "df"
.\adb shell df > %filename%/df.txt
echo "screenshot"
.\adb shell screencap -p /sdcard/screenshot.png
.\adb pull /sdcard/screenshot.png %filename%
echo "adb pull DB"
.\adb pull data/system/users/0 %filename%
echo ".\adb bugreport %datedir%"
.\adb bugreport %datedir%


@REM ::拉取logcat
@REM echo "adb logcat"
@REM .\adb logcat -d -v time > .\logs\logcat.log

echo **********************************************************************************************
echo 报告下载完成：
echo **********************************************************************************************


pause