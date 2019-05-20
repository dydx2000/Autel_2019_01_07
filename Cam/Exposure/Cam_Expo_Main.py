# encoding=utf-8
from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction



def CameraExpo_Setting_Auto(driver): #自动曝光
        time.sleep(2)

        driver.find_element_by_id("com.autel.explorer:id/tv_autel_home_start").click()  # go fly
        time.sleep(4)

        driver.tap([(0.31,0.94)])
        time.sleep(0.5)
        driver.swipe(0.31,0.82,0.7,0.82)
        time.sleep(0.5)


def CameraExpo_Setting_Manual(driver): #手动曝光
        time.sleep(2)

        driver.find_element_by_id("com.autel.explorer:id/tv_autel_home_start").click()  # go fly
        time.sleep(4)

        driver.tap([(0.31,0.94)])
        time.sleep(0.5)
        driver.swipe(0.7,0.82,0.31,0.82)
        time.sleep(0.5)