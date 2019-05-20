# encoding=utf-8
from appium import webdriver
import time

from appium.webdriver.common.touch_action import TouchAction

des_cap = {}
des_cap['platformName'] = 'Android'
# LG
des_cap['platformVersion']='7'
des_cap['deviceName']='192.168.1.12:5555'

# 一加手机
# des_cap['platformVersion'] = '9'
# des_cap['deviceName'] = '12dd6e53'

des_cap['automationName'] = 'Appium' #uiautomator2
des_cap['noReset'] = True
des_cap['appPackage'] = 'com.autel.explorer'
des_cap['appActivity'] = 'com.autel.modelb.view.autelhome.AutelHomeActivity'
des_cap['skipDeviceInitialization']=True
des_cap['disableAndroidWatchers']=True
# des_cap['autoLaunch']=False
des_cap['unicodeKeyboard']=True
des_cap['resetKeyboard']=True

# des_cap['unicodeKeyboard'] = True
# des_cap['resetKeyboard'] = True
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", des_cap)
driver.implicitly_wait(60)
time.sleep(2)
driver.find_element_by_id("com.autel.explorer:id/tv_autel_home_start").click()
time.sleep(2)
#shot
# driver.find_element_by_id("com.autel.explorer:id/rel_camera_takephoto_controller").click()
# driver.find_element_by_id("com.autel.explorer:id/rel_camera_controller").click()
# 拍照模式选择
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]")
#选择连拍
driver.find_element_by_android_uiautomator('new UiSelector().text("SINGLE")').click()




time.sleep(5)
driver.back()
driver.back()
time.sleep(2)
driver.quit()