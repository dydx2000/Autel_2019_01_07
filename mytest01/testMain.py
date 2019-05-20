# coding:utf-8
from AutelCam import CamSetting
import os,time

from appium import webdriver
desired_caps={}
desired_caps['platformName']='Android'
desired_caps['platformVersion']='4.4'
desired_caps['deviceName']='50a72b24260b'
# desired_caps['app']=''

desired_caps['appPackage']='com.autel.explorer'
desired_caps['appActivity']='com.autel.modelb.view.autelhome.AutelHomeActivity'
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
driver.implicitly_wait(10)
time.sleep(3)

CamSetting.intoCam()

