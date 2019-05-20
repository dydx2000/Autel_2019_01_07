# encoding=utf-8
from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction



def CameraSize_Setting_169(driver): #图像大小选择 16:9
        time.sleep(2)

        driver.find_element_by_id("com.autel.explorer:id/tv_autel_home_start").click()  # go fly
        time.sleep(4)
        driver.swipe(0.25,0.94,0.75,0.94)
        time.sleep(0.5)
        driver.tap([(0.18,0.94)],100)
        time.sleep(0.5)
        driver.swipe(0.5,0.82,0.75,0.82)
        time.sleep(0.5)

def CameraSize_Setting_43(driver): #图像大小选择 4:3
        time.sleep(2)

        driver.find_element_by_id("com.autel.explorer:id/tv_autel_home_start").click()  # go fly
        time.sleep(4)
        driver.swipe(0.25,0.94,0.75,0.94)
        time.sleep(0.5)
        driver.tap([(0.18,0.94)],100)
        time.sleep(0.5)
        driver.swipe(0.75,0.82,0.5,0.82)
        time.sleep(0.5)

