::version 20220715
::revised by cjh


@ECHO OFF

::编码=UTF-8
chcp 65001





set filename=last_log
if exist %filename% (
	echo last_log already exists!!!
	echo please delete the last_log first!!!
    echo 请删除当前目录的last_log文件夹，记得保存上一次的log哦
	pause
	exit
)



echo **********************************************************************************************
echo 开始执行Monkey Test
echo 测试开始时间：
echo %date%  %time%
echo **********************************************************************************************
echo "Monkey_Test"
echo monkey_test_all_packeages_except_settings


echo "adb root"
.\adb root

echo "adb shell sleep 2"
.\adb shell sleep 2

echo "adb remount"
.\adb remount

echo "adb shell sleep 2"
.\adb shell sleep 2

::清理现有logcat日志
echo "adb logcat -c"
.\adb logcat -c

@REM ::开始记录logcat
@REM echo "adb logcat"
@REM adb logcat -v time > .\logcat.log

::打开sdrv_log，即常规日志
echo ".\adb shell setprop persist.log.start 1"
.\adb shell setprop persist.log.start 1

echo "adb shell sleep 2"
.\adb shell sleep 2

echo "adb push blacklist.txt /data/local/tmp/"
.\adb push blacklist.txt /data/local/tmp/

echo "adb shell monkey --pkg-blacklist-file /data/local/tmp/blacklist.txt --ignore-crashes --ignore-timeouts --ignore-security-exceptions --ignore-native-crashes --pct-syskeys 0 --throttle 200 -v 864000 1>.\Logs\monkey_info_log.log 2>.\Logs\monkey_error_log.log"
.\adb shell monkey --pkg-blacklist-file /data/local/tmp/blacklist.txt --ignore-crashes --ignore-timeouts --ignore-security-exceptions --ignore-native-crashes --pct-syskeys 0 --throttle 200 -v 864000 1>.\Logs\monkey_info_log.log 2>.\Logs\monkey_error_log.log

::echo "adb shell monkey --pkg-blacklist-file /data/local/tmp/blacklist.txt --ignore-crashes --ignore-timeouts --ignore-security-exceptions --ignore-native-crashes --pct-syskeys 0 --throttle 200 -v 864000 >.\Logs\monkey.log"
::.\adb shell monkey --pkg-blacklist-file /data/local/tmp/blacklist.txt --ignore-crashes --ignore-timeouts --ignore-security-exceptions --ignore-native-crashes --pct-syskeys 0 --throttle 200 -v 864000 >.\Logs\monkey.log


echo **********************************************************************************************
echo MONKEY测试结束时间：
echo %date%  %time%
echo 开始下载LOG报告
echo **********************************************************************************************


echo "Log_Collect"

set filename=Logs\last_log

echo "mkdir %filename%"
md %filename%
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


::拉取logcat
echo "adb logcat"
.\adb logcat -d -v time > .\Logs\logcat.log

echo **********************************************************************************************
echo 报告下载完成：
echo **********************************************************************************************


pause
pause
