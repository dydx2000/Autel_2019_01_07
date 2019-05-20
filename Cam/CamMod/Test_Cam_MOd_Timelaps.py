# encoding=utf-8
from appium import webdriver
import warnings
import time
from appium.webdriver.common.touch_action import TouchAction
import unittest
from Cam.CamMod.Cam_Mod_Main import CameraMode_SettingSingle,CameraMode_SettingBurst,CameraMode_Setting_AEB,CameraMode_Setting_TIMELAPSE
from Cam.CamMod.Cam_Mod_Burst import CamModeBur_3,CamModeBur_5,CamModeBur_7,CamModeBur_14,CamModeBur_10
from Cam.CamMod.Cam_Mod_Timelaps import CamModeLaps_2s,CamModeLaps_5s,CamModeLaps_7s,CamModeLaps_60s,CamModeLaps_30s,CamModeLaps_20s,CamModeLaps_10s


class CameraModeTest(unittest.TestCase):
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
        # des_cap['unicodeKeyboard']=True
        # des_cap['resetKeyboard']=True
        des_cap['autoLaunch']=False


        cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", des_cap)
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        time.sleep(60)
        cls.driver.quit()



    def test_01_CameraMode_Setting_TIMELAPSE_2s(self): #延时拍照 2秒
          CameraMode_Setting_TIMELAPSE(self.driver)
          CamModeLaps_2s(self.driver)

    def test_02_CameraMode_Setting_TIMELAPSE_5s(self): #延时拍照 5秒
          CameraMode_Setting_TIMELAPSE(self.driver)
          CamModeLaps_5s(self.driver)

    def test_03_CameraMode_Setting_TIMELAPSE_7s(self): #延时拍照 7秒
          CameraMode_Setting_TIMELAPSE(self.driver)
          CamModeLaps_7s(self.driver)

    def test_04_CameraMode_Setting_TIMELAPSE_10s(self): #延时拍照 10秒
          CameraMode_Setting_TIMELAPSE(self.driver)
          CamModeLaps_10s(self.driver)

    def test_05_CameraMode_Setting_TIMELAPSE_20s(self): #延时拍照 20秒
          CameraMode_Setting_TIMELAPSE(self.driver)
          CamModeLaps_20s(self.driver)

    def test_06_CameraMode_Setting_TIMELAPSE_30s(self): #延时拍照 30秒
          CameraMode_Setting_TIMELAPSE(self.driver)
          CamModeLaps_30s(self.driver)

    def test_07_CameraMode_Setting_TIMELAPSE_60s(self): #延时拍照 60秒
          CameraMode_Setting_TIMELAPSE(self.driver)
          CamModeLaps_60s(self.driver)









if __name__ == '__main__':
    unittest.main()






