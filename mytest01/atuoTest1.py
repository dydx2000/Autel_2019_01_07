# coding:utf-8
import os, time
from appium import webdriver
from AutelCam import CamSetting,GridSetting
from mytest01 import planeMain

import unittest
import time


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4'
desired_caps['deviceName'] = '50a72b24260b'
# desired_caps['app']=''

desired_caps['appPackage'] = 'com.autel.explorer'
desired_caps['appActivity'] = 'com.autel.modelb.view.autelhome.AutelHomeActivity'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)


class autoest(unittest.TestCase):



    def setUp(self):
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        # driver.implicitly_wait(10)

    def tearDown(self):
        pass


    # def test_01(self):
    #     cam=CamSetting()
    #     cam.intoCam()#进入相机设置
    #     grid=GridSetting()
    #     grid.intoGrid()#进入网格设置

    def test_01(self):

        self.intoMainsetting()
        self.generalSetting()


if __name__ == "__main__":
    unittest.main()