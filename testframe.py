# coding:utf-8
import os,time
from appium import webdriver
desired_caps={}
desired_caps['platformName']='Android'
desired_caps['platformVersion']='4.4'
desired_caps['deviceName']='8f21c9ba'
# desired_caps['deviceName']='50a72b24260b'
# desired_caps['app']=''

desired_caps['appPackage']='com.autel.explorer'
desired_caps['appActivity']='com.autel.modelb.view.autelhome.AutelHomeActivity'
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
driver.implicitly_wait(10)
time.sleep(1)


# 点击开始
driver.find_element_by_id("com.autel.explorer:id/tv_autel_home_start").click()
# 相机设置
driver.find_element_by_id("com.autel.explorer:id/iv_camera_setting").click()
# # 进入网格设置
# driver.find_element_by_id("com.autel.explorer:id/item_general_setting_value_tv").click()
#
# '''
#
# '''
# # idAddText='resourceID("com.autel.explorer:id/general_setting_image_item_value_text").text("网格")'
# # driver.find_element_by_android_uiautomator(idAddText).click()
# time.sleep(2)
# # camGrid=driver.find_elements_by_id("com.autel.explorer:id/general_setting_image_item_value_text")
# # camGrid[1].click()


#相机设置--网格模块

#无网格
# camGrids=driver.find_elements_by_android_uiautomator('new UiSelector().resourceId("com.autel.explorer:id/general_setting_image_item_value_text")')
# camGrids[0].click()
'''
#网格
camGrids=driver.find_elements_by_android_uiautomator('new UiSelector().resourceId("com.autel.explorer:id/general_setting_image_item_value_text")')
camGrids[1].click()
#网格+横线
camGrids=driver.find_elements_by_android_uiautomator('new UiSelector().resourceId("com.autel.explorer:id/general_setting_image_item_value_text")')
camGrids[2].click()
'''

'''
#相机--中心点模块
camSets=driver.find_elements_by_id("com.autel.explorer:id/rl_general_setting_item")
camSets[1].click()
#相机--中心点模块--正方形
centerPoints=driver.find_elements_by_android_uiautomator('new UiSelector().resourceId("com.autel.explorer:id/general_setting_image_item_value_text")')
centerPoints[1].click()
'''

#相机--直方图
selectDots=driver.find_elements_by_id("com.autel.explorer:id/item_general_setting_autel_ss")
selectDots[0].click()
selectDots[1].click()
time.sleep(2)

selectDots[2].click()





