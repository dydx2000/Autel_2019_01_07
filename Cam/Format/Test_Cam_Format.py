# encoding=utf-8
from appium import webdriver
import warnings
import time
from appium.webdriver.common.touch_action import TouchAction
import unittest

from Cam.Format.Cam_Format_Main import  CameraFormat_Setting_Jpg,CameraFormat_Setting_RAW,CameraFormat_Setting_JR

class CameraFormatTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        warnings.simplefilter("ignore",ResourceWarning)
        des_cap = {}
        des_cap['platformName'] = 'Android'

        #
        # des_cap['platformVersion']='6'
        # des_cap['deviceName']='7cc8c0d9' #onplus3

        des_cap['platformVersion'] = '8'
        des_cap['deviceName'] = '192.168.1.17:5555'  # LG wifi

        des_cap['automationName'] = 'Appium'
        des_cap['noReset'] = True
        des_cap['appPackage'] = 'com.autel.explorer'
        des_cap['appActivity'] = 'com.autel.modelb.view.autelhome.AutelHomeActivity'
        des_cap['skipDeviceInitialization']=True
        des_cap['disableAndroidWatchers']=True
        # des_cap['autoLaunch']=False
        des_cap['unicodeKeyboard']=True
        des_cap['resetKeyboard']=True
        des_cap['autoLaunch']=False


        cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", des_cap)
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        # cls.driver.quit()



    def test_01_CameraFormat_Setting_JPG(self): # 图像格式 JPG
          CameraFormat_Setting_Jpg(self.driver)



    def test_02_CameraFormat_Setting_RAW(self): # 图像格式 RAW
          CameraFormat_Setting_RAW(self.driver)


    def test_03_CameraFormat_Setting_JR(self): # 图像格式 JPG+RAW
          CameraFormat_Setting_JR(self.driver)









if __name__ == '__main__':
    unittest.main()






