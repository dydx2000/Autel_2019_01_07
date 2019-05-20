# encoding=utf-8
from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction



def CameraFormat_Setting_Jpg(driver): #图像类型 JPG
        time.sleep(2)

        driver.find_element_by_id("com.autel.explorer:id/tv_autel_home_start").click()  # go fly
        time.sleep(4)
        driver.swipe(0.25,0.94,0.75,0.94) #滑到最左边
        time.sleep(0.5)


        driver.tap([(0.31,0.94)])
        time.sleep(0.5)
        driver.swipe(0.31,0.82,0.7,0.82)
        time.sleep(0.5)

def CameraFormat_Setting_RAW(driver): #图像类型 raw
        time.sleep(2)

        driver.find_element_by_id("com.autel.explorer:id/tv_autel_home_start").click()  # go fly
        time.sleep(4)
        driver.swipe(0.25,0.94,0.75,0.94) #滑到最左边
        time.sleep(0.5)


        driver.tap([(0.31,0.94)])
        time.sleep(0.5)
        driver.swipe(0.31,0.82,0.7,0.82)
        time.sleep(0.5)
        driver.swipe(0.66,0.82,0.5,0.82)

        time.sleep(0.5)

def CameraFormat_Setting_JR(driver): #图像类型 JPG+RAW
        time.sleep(2)

        driver.find_element_by_id("com.autel.explorer:id/tv_autel_home_start").click()  # go fly
        time.sleep(4)
        driver.swipe(0.25,0.94,0.75,0.94) #滑到最左边
        time.sleep(0.5)


        driver.tap([(0.31,0.94)])
        time.sleep(0.5)
        driver.swipe(0.7,0.82,0.31,0.82)
        time.sleep(0.5)