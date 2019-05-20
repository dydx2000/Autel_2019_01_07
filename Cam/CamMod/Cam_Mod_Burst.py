import warnings
import unittest
import  time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

def  CamModeBur_3(driver):
        time.sleep(0.5)
        driver.tap([(0.5,0.82)],100)
        time.sleep(0.5)
        driver.swipe(0.16,0.82 ,0.856,0.82,300) #左滑到右
        time.sleep(0.8)
        driver.swipe(0.16,0.82, 0.856, 0.82,300 ) #再左滑到右


def CamModeBur_5(driver):
        time.sleep(0.5)
        driver.tap([(0.5, 0.82)], 100)
        time.sleep(1)
        driver.swipe(0.16, 0.82, 0.856, 0.82, 300)  # 左滑到右
        time.sleep(0.8)
        driver.swipe(0.16, 0.82, 0.856, 0.82, 300)  # 再左滑到右
        time.sleep(0.8)
        driver.swipe(0.75,0.82,0.5,0.82,300)

def CamModeBur_7(driver):
    time.sleep(0.5)
    driver.tap([(0.5, 0.82)], 100)
    time.sleep(1)
    driver.swipe(0.98, 0.82, 0.03, 0.82)  # 最右滑到最左
    time.sleep(0.8)
    driver.swipe(0.5, 0.82, 0.8, 0.82) #滑到10
    time.sleep(0.8)
    driver.swipe(0.5, 0.82, 0.8, 0.75) #滑到7
    time.sleep(1)


def CamModeBur_10(driver):
    time.sleep(0.5)
    driver.tap([(0.5, 0.82)], 100)
    time.sleep(1)
    driver.swipe(0.98, 0.82, 0.03, 0.82)  # 最右滑到最左
    time.sleep(0.8)
    driver.swipe(0.5,0.82,0.8,0.82)
    time.sleep(1)

def CamModeBur_14(driver):
    time.sleep(0.5)
    driver.tap([(0.5, 0.82)], 100)
    time.sleep(1)
    driver.swipe(0.98, 0.82, 0.03, 0.82)  # 最右滑到最左
    time.sleep(1)







