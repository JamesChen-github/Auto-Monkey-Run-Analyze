import uiautomator2 as u2
from time import sleep
import logging,os,re


# config logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
sleep(1)

try:
	d=u2.connect()
	d.info
except Exception:
	print("无法连接到设备\n请检查连接")
	exit(1)

def test_contro_key():
    d.xpath(
        '//*[@resource-id="com.android.systemui:id/maps_nav"]/android.widget.LinearLayout[1]/android.widget.ImageButton[1]').click()
    sleep(0.01)
    d.xpath(
        '//*[@resource-id="com.android.systemui:id/music_nav"]/android.widget.LinearLayout[1]/android.widget.ImageButton[1]').click()
    sleep(0.01)
    d.xpath(
        '//*[@resource-id="com.android.systemui:id/phone_nav"]/android.widget.LinearLayout[1]/android.widget.ImageButton[1]').click()
    sleep(0.01)
    d.xpath(
        '//*[@resource-id="com.android.systemui:id/grid_nav"]/android.widget.LinearLayout[1]/android.widget.ImageButton[1]').click()
    sleep(0.01)
    d(resourceId="com.android.systemui:id/notifications").click()
    sleep(0.01)
    d.xpath(
        '//*[@resource-id="com.android.systemui:id/assist"]/android.widget.LinearLayout[1]/android.widget.ImageButton[1]').click()
    sleep(0.01)
    d.xpath(
        '//*[@resource-id="com.android.systemui:id/home"]/android.widget.LinearLayout[1]/android.widget.ImageButton[1]').click()
    sleep(0.01)

if __name__ == '__main__':
    i=0
    while 1:
    #for i in range(0,100):
        test_contro_key()
        print("第"+str(i+1)+"轮测试完成！！！")
        i=i+1
