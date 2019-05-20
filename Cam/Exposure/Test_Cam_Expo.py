# encoding=utf-8
from appium import webdriver
import warnings
import time
from appium.webdriver.common.touch_action import TouchAction
import unittest
from Cam.Exposure.Cam_Expo_Main import CameraExpo_Setting_Auto,CameraExpo_Setting_Manual

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
        des_cap['unicodeKeyboard']=False
        # des_cap['resetKeyboard']=True
        des_cap['autoLaunch']=False


        cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", des_cap)
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        time.sleep(60)
        # cls.driver.quit()



    def test_01_CameraExpo_Setting_Auto(self): # 自动曝光
          CameraExpo_Setting_Auto(self.driver)

    def test_02_CameraExpo_Setting_Manual(self): # 自动曝光
          CameraExpo_Setting_Manual(self.driver)







if __name__ == '__main__':
    unittest.main()






