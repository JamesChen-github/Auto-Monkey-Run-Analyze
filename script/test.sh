function dumplog()
{
	mkdir /sdcard/log
	screencap -p /sdcard/log/screen0.png
	logcat -d > /sdcard/log/logcat.log
	bugreportz
	mv /data/user_de/0/com.android.shell/files/bugreports/* /sdcard/log
}

# num=0
# systemui_pid=`ps -A | grep systemui | awk '{print $2}'`
# while ((num<50000))
# do
# 	echo "start  $num test."
# 	input tap 1200 680
# 	sleep 1
# 	pid=`ps -A | grep systemui | awk '{print $2}'`
# 	if [ "$pid" != "$systemui_pid" ]; then
# 		dumplog
# 		exit 1
# 	fi
# 	((num++))
# done

killall com.android.car.sddemo
sleep 2
am start -n com.android.car.sddemo/.DisplayShareActivity
sleep 3

sddemo_pid=`ps -A | grep sddemo | awk '{print $2}'`
num=0
while ((num<50000))
do
	echo "start  $num test."
	input tap 10 270
	sleep 1
	pid=`ps -A | grep sddemo | awk '{print $2}'`
	if [ "$pid" != "$sddemo_pid" ]; then
		dumplog
		exit 1
	fi
	((num++))
done