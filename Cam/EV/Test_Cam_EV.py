# encoding=utf-8
from appium import webdriver
import warnings
import time
from appium.webdriver.common.touch_action import TouchAction
import unittest
from Cam.Exposure.Cam_Expo_Main import CameraExpo_Setting_Auto,CameraExpo_Setting_Manual
from Cam.EV.Cam_EV_Main import CameraEV_Setting_Minus3,CameraEV_Setting_Minus27,CameraEV_Setting_Minus23,CameraEV_Setting_Minus2,\
    CameraEV_Setting_Minus17,CameraEV_Setting_Minus13,CameraEV_Setting_Minus10

class CameraEV_Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        warnings.simplefilter("ignore",ResourceWarning)
        des_cap = {}
        des_cap['platformName'] = 'Android'

        #
        # des_cap['platformVersion']='6'
        # des_cap['deviceName']='7cc8c0d9' #onplus3

        des_cap['platformVersion'] = '7'
        des_cap['deviceName'] = '192.168.1.12:5555'  # LG wifi

        des_cap['automationName'] = 'Appium'
        des_cap['noReset'] = True
        des_cap['appPackage'] = 'com.autel.explorer'
        des_cap['appActivity'] = 'com.autel.modelb.view.autelhome.AutelHomeActivity'
        des_cap['skipDeviceInitialization']=True
        des_cap['disableAndroidWatchers']=True
        # des_cap['autoLaunch']=False
        des_cap['unicodeKeyboard']=True
        des_cap['resetKeyboard']=True
        # des_cap['autoLaunch']=False


        cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", des_cap)
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.quit()



    def test_01_CameraEV_Setting_m30(self): # Ev -3.0
          CameraExpo_Setting_Auto(self.driver)
          CameraEV_Setting_Minus3(self.driver)

    def test_02_CameraEV_Setting_m27(self): # Ev -2.7
          CameraExpo_Setting_Auto(self.driver)
          CameraEV_Setting_Minus27(self.driver)

    def test_03_CameraEV_Setting_m23(self): # Ev -2.3
          CameraExpo_Setting_Auto(self.driver)
          CameraEV_Setting_Minus23(self.driver)

    def test_04_CameraEV_Setting_m20(self):  # Ev -2.0
          CameraExpo_Setting_Auto(self.driver)
          CameraEV_Setting_Minus2(self.driver)

    def test_05_CameraEV_Setting_m17(self):  # Ev -1.7
          CameraExpo_Setting_Auto(self.driver)
          CameraEV_Setting_Minus17(self.driver)

    def test_05_CameraEV_Setting_m13(self):  # Ev -1.3
          CameraExpo_Setting_Auto(self.driver)
          CameraEV_Setting_Minus13(self.driver)


    def test_05_CameraEV_Setting_m10(self):  # Ev -1.0
          CameraExpo_Setting_Auto(self.driver)
          CameraEV_Setting_Minus10(self.driver)

if __name__ == '__main__':
    unittest.main()

