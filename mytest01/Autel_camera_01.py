# coding:utf-8
import  time
from appium import webdriver
from mytest01.AutelCam import intoGrid,setGrid,setHVline,intoCam,connectWizard,login
import unittest


class cameraTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        desired_caps =  {
          'platformName': 'Android',
          'platformVersion': '4.4',
          'deviceName': '50a72b24260b',
          'automationName': 'UiAutomator2',
          'appPackage': 'com.autel.explorer',
          'appActivity': 'com.autel.modelb.view.autelhome.AutelHomeActivity'
                }
        cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        cls.driver.implicitly_wait(20)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    #网格设置
    def test_01_setGrid(self):
        #进入相机设置
        intoCam(self.driver)
        intoGrid(self.driver)
        #设置网格
        setGrid(self.driver)

    #设置水平线
    def test_02_hvline(self):
        #进入相机设置
        intoCam(self.driver)
        intoGrid(self.driver)
        #设为水平线
        setHVline(self.driver)


    def test_03_connectWizard(self):
        #首页点击"连接向导"
        connectWizard(self.driver)

    def test_04_login(self):
        login(self.driver)



if __name__ == "__main__":
    unittest.main()