# encoding=utf-8
from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction

'''
des_cap = {}
des_cap['platformName'] = 'Android'


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
# des_cap['autoLaunch']=False
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", des_cap)


def   CameraMode_SettingSingle():
        time.sleep(2)
        driver.find_element_by_id("com.autel.explorer:id/tv_autel_home_start").click() # go fly
        time.sleep(2)

        driver.find_element_by_android_uiautomator('new UiSelector().text("MODE")').click() #进入 mode
        time.sleep(1)
        driver.find_element_by_android_uiautomator('new UiSelector().text("BURST") ').click() #选择 burst

        time.sleep(2)
'''

def CameraMode_SettingSingle(driver): #单拍设置
        time.sleep(2)

        driver.find_element_by_id("com.autel.explorer:id/tv_autel_home_start").click()  # go flay
        time.sleep(4)
        driver.tap([(0.188, 0.945)], 100)  # 点击进入 mode
        time.sleep(0.5)
        driver.swipe(0.247, 0.856,0.738, 0.856,300)  # 从最左滑到最事,选中SINGLE
        # driver.find_element_by_android_uiautomator('new UiSelector().text("SINGLE") ').click()  # 选择 SINGLE
        time.sleep(2)


def    CameraMode_SettingBurst(driver): #14连拍设置
        time.sleep(2)
        driver.find_element_by_id("com.autel.explorer:id/tv_autel_home_start").click()  # go fly
        time.sleep(4)

        driver.tap([(0.188,0.945)],100) # 点击进入 mode
        # driver.find_element_by_android_uiautomator('new UiSelector().text("MODE")').click()  # 进入 mode
        time.sleep(1)
        driver.swipe(0.247, 0.856, 0.738, 0.856,500)  # 从最左滑到最右,选中SINGLE
        time.sleep(0.5)
        driver.swipe(0.75, 0.856, 0.5, 0.856)  # 滑动选中 BURST

        # driver.find_element_by_android_uiautomator('new UiSelector().text("BURST") ').click()  # 选择 BURST

        time.sleep(2)

def   CameraMode_Setting_TIMELAPSE(driver): #延时拍照
        time.sleep(2)
        driver.find_element_by_id("com.autel.explorer:id/tv_autel_home_start").click()  # go fly
        time.sleep(4)
        driver.tap([(0.188, 0.945)], 100)  # 点击进入 mode
        time.sleep(2)
        driver.swipe(0.738,0.856,0.247,0.856,300) #从最右滑到最左,选中AEB
        time.sleep(0.8)
        driver.swipe(0.5,0.80,0.8,0.80)        #滑动选中 TIMELAPSE
        # driver.swipe(0.738,0.914,0.247,0.914,300) #从最右滑到最左,选中AEB
        # driver.find_element_by_android_uiautomator('new UiSelector().text("BURST") ').click()  # 选择 BURST
        time.sleep(2)


def   CameraMode_Setting_AEB(driver): #AEB设置
        time.sleep(2)
        driver.find_element_by_id("com.autel.explorer:id/tv_autel_home_start").click()  # go fly
        time.sleep(4)
        driver.tap([(0.188, 0.945)], 100)  # 点击进入 mode
        time.sleep(2)
        driver.swipe(0.738,0.856,0.247,0.856,500) #从最右滑到最左,选中AEB
        # driver.swipe(0.738,0.914,0.247,0.914,300) #从最右滑到最左,选中AEB
        # driver.find_element_by_android_uiautomator('new UiSelector().text("BURST") ').click()  # 选择 BURST
        time.sleep(2)







