# encoding=utf-8
from appium import webdriver
import time,warnings
from appium.webdriver.common.touch_action import TouchAction
warnings.simplefilter("ignore",ResourceWarning)
des_cap = {}
des_cap['platformName'] = 'Android'

#
# des_cap['platformVersion']='6'
# des_cap['deviceName']='7cc8c0d9' #onplus3

des_cap['platformVersion'] = '7'
des_cap['deviceName'] = '192.168.1.12:5555'  # LG wifi

des_cap['automationName'] = 'Appium'
des_cap['noReset'] = True
des_cap['appPackage'] = 'com.autel.explorer'
des_cap['appActivity'] = 'com.autel.modelb.view.autelhome.AutelHomeActivity'
des_cap['skipDeviceInitialization']=True
des_cap['disableAndroidWatchers']=True
# des_cap['autoLaunch']=False
des_cap['unicodeKeyboard']=True
des_cap['resetKeyboard']=True


def CameraEV_Setting_Minus3(driver): #EV -3.0
        time.sleep(0.5)
        driver.tap([(0.5,0.5)],100)
        time.sleep(0.5)
        driver.tap([(0.7,0.94)],100)
        time.sleep(0.5)
        driver.swipe(0.4, 0.82, 0.85, 0.82,250)
        time.sleep(3)
        driver.swipe(0.4, 0.82, 0.85, 0.82,250)
        time.sleep(3)
        # driver.swipe(0.4, 0.82, 0.85, 0.82,250)
        time.sleep(5)

def CameraEV_Setting_Minus27(driver):  # EV -2.7
        time.sleep(0.5)
        driver.tap([(0.5, 0.5)], 100)
        time.sleep(0.5)
        driver.tap([(0.7, 0.94)], 100)
        time.sleep(0.5)
        driver.swipe(0.4, 0.82, 0.85, 0.82, 250)
        time.sleep(3)
        driver.swipe(0.4, 0.82, 0.85, 0.82, 250) #定位到 -3.0


        time.sleep(0.5)
        driver.tap([(0.66,0.82,)]) #先定位-3.0,再点2.7
        time.sleep(2)

def CameraEV_Setting_Minus23(driver):  # EV -2.3
        time.sleep(0.5)
        driver.tap([(0.5, 0.5)], 100)
        time.sleep(0.5)
        driver.tap([(0.7, 0.94)], 100)
        time.sleep(0.5)
        driver.swipe(0.4, 0.82, 0.85, 0.82, 250)
        time.sleep(3)
        driver.swipe(0.4, 0.82, 0.85, 0.82, 250)  # 定位到 -3.0
        time.sleep(0.5)
        driver.tap([(0.84, 0.82,)])  # 先定位-3.0,再点2..3
        time.sleep(2)

def  CameraEV_Setting_Minus2(driver):  # EV -2
        time.sleep(0.5)
        driver.tap([(0.5, 0.5)], 100)
        time.sleep(0.5)
        driver.tap([(0.7, 0.94)], 100)
        time.sleep(0.5)
        driver.swipe(0.4, 0.82, 0.85, 0.82, 250)
        time.sleep(3)
        driver.swipe(0.4, 0.82, 0.85, 0.82, 250)  # 定位到 -3.0
        time.sleep(0.5)
        driver.tap([(0.84, 0.82,)])  # 先定位-3.0,再点-2.3
        time.sleep(0.8)
        driver.tap([(0.68, 0.82,)])  # 先定位-2.3,再点-2.0 ,1.7 (2.0)

def  CameraEV_Setting_Minus17(driver):  # EV -1.7
        time.sleep(0.5)
        driver.tap([(0.5, 0.5)], 100)
        time.sleep(0.5)
        driver.tap([(0.7, 0.94)], 100)
        time.sleep(0.5)
        driver.swipe(0.4, 0.82, 0.85, 0.82, 250)
        time.sleep(3)
        driver.swipe(0.4, 0.82, 0.85, 0.82, 250)  # 定位到 -3.0
        time.sleep(1)
        driver.tap([(0.84, 0.82,)])  # 先定位-3.0,再点-2.3
        time.sleep(1) #间隔时间一定要长一点,否则可能不会点到
        driver.tap([(0.84, 0.82,)])  # 先定位-2.3,再点-2.0,1.7 (1.7)

def  CameraEV_Setting_Minus13(driver):  # EV -1.3
        time.sleep(0.5)
        driver.tap([(0.5, 0.5)], 100)
        time.sleep(0.5)
        driver.tap([(0.7, 0.94)], 100)
        time.sleep(0.5)
        driver.swipe(0.4, 0.82, 0.85, 0.82, 250)
        time.sleep(3)
        driver.swipe(0.4, 0.82, 0.85, 0.82, 250)  # 定位到 -3.0
        time.sleep(1)
        driver.tap([(0.84, 0.82,)])  # 先定位-3.0,再点-2.3
        time.sleep(1) #间隔时间一定要长一点,否则可能不会点到
        driver.tap([(0.84, 0.82,)])  # 先定位-2.3,再点-2.0,1.7 (1.7)
        time.sleep(1)
        driver.tap([(0.68, 0.82,)])  #定位了1.7, 定(-1.3 -1.0) (-1.3)


def  CameraEV_Setting_Minus10(driver):  # EV -1.0
        time.sleep(0.5)
        driver.tap([(0.5, 0.5)], 100)
        time.sleep(0.5)
        driver.tap([(0.7, 0.94)], 100)
        time.sleep(0.5)
        driver.swipe(0.4, 0.82, 0.85, 0.82, 250)
        time.sleep(3)
        driver.swipe(0.4, 0.82, 0.85, 0.82, 250)  # 定位到 -3.0
        time.sleep(1)
        driver.tap([(0.84, 0.82,)])  # 先定位-3.0,再点-2.3
        time.sleep(1) #间隔时间一定要长一点,否则可能不会点到
        driver.tap([(0.84, 0.82,)])  # 先定位-2.3,再点-2.0,1.7 (1.7)
        time.sleep(0.6)
        driver.tap([(0.84, 0.82,)])  #定位了1.7, 定(-1.3 -1.0) (-1.0)




