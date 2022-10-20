::version 20210813

@ECHO OFF
::set filename=%date:~0,4%_%date:~5,2%_%date:~8,2%_%time:~0,2%_%time:~3,2%_%time:~6,2%
set filename=last_log
if exist %filename% (
	echo last_log already exists!!!
	echo please delete the last_log first!!!
	pause
	exit
)

echo "mkdir %filename%"
md %filename%
echo "adb root"
.\adb root
echo "adb remount"
.\adb remount
echo "adb pull /data/sdrv_logs"
.\adb pull /data/sdrv_logs %filename%
echo "adb pull /data/sdrv_deviceinfo"
.\adb pull /data/sdrv_deviceinfo %filename%
echo "adb pull /data/anr"
.\adb pull /data/anr %filename%
echo "adb pull /data/sde"
.\adb pull /data/sde %filename%
echo "adb pull /data/tombstones"
.\adb pull /data/tombstones %filename%
echo "dumpsys meminfo"
.\adb shell dumpsys meminfo -a > %filename%/meminfo.txt
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
echo "adb bugreport"
.\adb bugreport %filename%
pause
