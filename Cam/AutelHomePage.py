import datetime
import logging
logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a,%d %b %Y %H:%M:%S',
                    filename='CamShots.log',
                    filemode='a')
import random
import Cam.uiautomator2_cam_shots_filter as uiauto

import time
d = uiauto.d

# 1-2 ,2-2个人中心显示
def  personalCenter():
    if d(resourceId="com.autel.explorer:id/iv_user_icon_default").exists():
        print('personal center is displaying')

#1-3 天气信息显示
def weatherDisplay():
    d(resourceId="com.autel.explorer:id/iv_weather_status").click()

#1-4 连接飞机向导
def HowtoConnect():
    d(resourceId="com.autel.explorer:id/tv_connect_status").click()



#2-4 飞机及遥控器电量显示
def batteryDisplay():
    if d(resourceId="com.autel.explorer:id/tv_home_connect_battery").exists() and \
        d(resourceId="com.autel.explorer:id/tv_home_connect_controller").exists:
            print('battery and remote power is displaying!')



# HowtoConnect()
batteryDisplay()