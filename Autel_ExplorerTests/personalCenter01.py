# encoding=utf-8
from appium import webdriver
import warnings
import time
from appium.webdriver.common.touch_action import TouchAction
import unittest


class PersonalCenterTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        warnings.simplefilter("ignore",ResourceWarning)
        des_cap = {}
        des_cap['platformName'] = 'Android'
        # des_cap['platformVersion']='4.4'
        # # des_cap['deviceName']='7cc8c0d9' #一加3手机
        # des_cap['deviceName']='50a72b2426

        des_cap['platformVersion']='7'
        # des_cap['deviceName']='192.168.1.12:5555' #LG wifi
        des_cap['deviceName']='LGH932bd3966d4' #LG

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
        time.sleep(3)
        cls.driver.quit()



    def test_01_personal_shots(self):
        pass

    def test_02_personal_reg(self): #注册
        time.sleep(2)
        self.driver.find_element_by_id("com.autel.explorer:id/iv_user_icon_default").click() #登录按钮
        self.driver.find_element_by_id("com.autel.explorer:id/tv_register").click() #登录界面点注册按钮
        self.driver.find_element_by_id("com.autel.explorer:id/ed_email").send_keys("abc123@qq.com")
        self.driver.find_element_by_id("com.autel.explorer:id/ed_pwd").send_keys("abc123456")
        self.driver.find_element_by_id("com.autel.explorer:id/ed_repeat_pwd").send_keys("abc123456")

        self.driver.find_element_by_id("com.autel.explorer:id/tv_register").click()

    def test_03_personal_login(self): #登录
        time.sleep(2)
        self.driver.find_element_by_id("com.autel.explorer:id/iv_user_icon_default").click()  # 登录按钮
        self.driver.find_element_by_id("com.autel.explorer:id/ed_email").click()
        self.driver.find_element_by_id("com.autel.explorer:id/ed_email").send_keys("abc123@qq.com")
        self.driver.find_element_by_id("com.autel.explorer:id/ed_pwd").send_keys("abc123456")
        self.driver.find_element_by_id("com.autel.explorer:id/btn_login").click()

    def test_04_personal_fogetpwd(self):
        time.sleep(2)
        self.driver.find_element_by_id("com.autel.explorer:id/iv_user_icon_default").click()  # 登录按钮
        self.driver.find_element_by_id("com.autel.explorer:id/tv_forget_pwd").click()
        self.driver.find_element_by_id("com.autel.explorer:id/et_email").send_keys("abc123@qq.com")
        self.driver.find_element_by_id("com.autel.explorer:id/btn_send_email").click()

    def test_05_personal_fogetpwd_iflogined(self):
        time.sleep(2)
        self.driver.find_element_by_id("com.autel.explorer:id/iv_user_icon_default").click()  # 用户按钮
        try:
            if self.driver.find_element_by_id("com.autel.explorer:id/iv_user_setting").is_displayed():

                    self.driver.find_element_by_id("com.autel.explorer:id/iv_user_photo").click()
                    self.driver.find_element_by_id("com.autel.explorer:id/tv_logout").click()
                    self.driver.tap([(0.6,0.67)],100)
                    self.driver.find_element_by_id("com.autel.explorer:id/iv_user_icon_default").click()


        except:
            pass


        self.driver.find_element_by_id("com.autel.explorer:id/tv_forget_pwd").click()
        self.driver.find_element_by_id("com.autel.explorer:id/et_email").send_keys("abc123@qq.com")
        self.driver.find_element_by_id("com.autel.explorer:id/btn_send_email").click()

    def test_06_personal_login_iflogined(self):  # 登录,含已经登录的情况再次登录
        time.sleep(2)
        self.driver.find_element_by_id("com.autel.explorer:id/iv_user_icon_default").click()  # 用户按钮
        self.driver.find_element_by_id("com.autel.explorer:id/iv_user_icon_default").click()  # 登录按钮
        try:
            if self.driver.find_element_by_id("com.autel.explorer:id/iv_user_setting").is_displayed():
                self.driver.find_element_by_id("com.autel.explorer:id/iv_user_photo").click()
                self.driver.find_element_by_id("com.autel.explorer:id/tv_logout").click()
                self.driver.tap([(0.6, 0.67)], 100)
                self.driver.find_element_by_id("com.autel.explorer:id/iv_user_icon_default").click()
        except:
            pass

        self.driver.find_element_by_id("com.autel.explorer:id/ed_email").click()
        self.driver.find_element_by_id("com.autel.explorer:id/ed_email").send_keys("abc123@qq.com")
        self.driver.find_element_by_id("com.autel.explorer:id/ed_pwd").send_keys("abc123456")
        self.driver.find_element_by_id("com.autel.explorer:id/btn_login").click()



if __name__ == '__main__':
    unittest.main()






