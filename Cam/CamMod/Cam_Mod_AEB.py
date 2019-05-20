import warnings
import unittest
import  time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

def  CamModeAEB_3(driver):
        time.sleep(0.5)
        driver.tap([(0.5,0.82)],100)
        time.sleep(0.5)
        driver.swipe(0.25,0.82 ,0.5,0.82,500) #左滑到右



def  CamModeAEB_5(driver):
        time.sleep(0.5)
        driver.tap([(0.5, 0.82)], 100)
        time.sleep(1)
        driver.swipe(0.75, 0.82, 0.25, 0.82, 500)  # 右滑到左







