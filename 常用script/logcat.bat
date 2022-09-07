::编码=UTF-8
chcp 65001


@ECHO OFF


::拉取logcat
echo "adb logcat"
set datedir=logs\%date:~3,4%-%date:~8,2%-%date:~11,2%-1
if exist %datedir% (
    echo exist %datedir%
) else (
    set datedir=logs\%date:~3,4%-%date:~8,2%-%date:~11,2%
    
)
echo save to %datedir%

echo "adb logcat -b all > %datedir%\logcat.log"
.\adb logcat -b all > %datedir%\logcat.log