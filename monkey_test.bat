@REM version 20221028
echo off

@REM 编码=UTF-8
chcp 65001

set monkey_times=10800000
set monkey_throttle=200
set adb_device_id=
set resources_path=D:\files\resources
set apks_path=
set seed=

adb %adb_device_id% root
adb %adb_device_id% remount

@REM start /min cmd /K "adb %adb_device_id% logcat -b all > .\monkey_logcat.log"

if not "%resources_path%"=="" (
	@REM adb %adb_device_id% push %~dp0resources /sdcard
	echo "adb %adb_device_id% push %resources_path% /sdcard"
	adb %adb_device_id% push %resources_path% /sdcard
)

if not "%apks_path%"=="" (
	for %%i in (%apks_path%\*.apk) do (
			echo "adb %adb_device_id% install %%i"
			adb %adb_device_id% install %%i
		)
)

@REM 打开sdrv_log
adb %adb_device_id% shell setprop persist.log.start 1

adb %adb_device_id% push blacklist.txt /data/local/tmp/
adb %adb_device_id% push whitelist.txt /data/local/tmp/
adb %adb_device_id% shell sync
adb %adb_device_id% shell sync

echo "**********************************************************************************************"
echo "开始执行Monkey Test"
echo "测试开始时间:"
echo "%date%  %time%"
echo "**********************************************************************************************"

echo "adb %adb_device_id% shell monkey --pkg-blacklist-file /data/local/tmp/blacklist.txt --ignore-crashes --ignore-timeouts --ignore-security-exceptions --ignore-native-crashes --pct-syskeys 0 --throttle %monkey_throttle% %seed% -v -v -v %monkey_times% 1>.\monkey_info_log.log 2>.\monkey_error_log.log"
adb %adb_device_id% shell monkey --pkg-blacklist-file /data/local/tmp/blacklist.txt --ignore-crashes --ignore-timeouts --ignore-security-exceptions --ignore-native-crashes --pct-syskeys 0 --throttle %monkey_throttle% %seed% -v -v -v %monkey_times% 1>.\monkey_info_log.log 2>.\monkey_error_log.log

echo "**********************************************************************************************"
echo "MONKEY测试结束时间:"
echo "%date%  %time%"

pause

