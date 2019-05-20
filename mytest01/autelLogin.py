# coding:utf-8
import os, time
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4'
desired_caps['deviceName'] = '50a72b24260b'
desired_caps['unicodeKeyboard']=True
# desired_caps['resetKeyboard']=True
# desired_caps['app']=''

desired_caps['appPackage'] = 'com.autel.explorer'
# desired_caps['appActivity'] = 'com.autel.modelb.view.personalcenter.userinfo.activity.LoginRegisterActivity'
desired_caps['appActivity'] = 'com.autel.modelb.view.autelhome.AutelHomeActivity'
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
# driver.implicitly_wait(10)
time.sleep(3)
class regLogin:
    def login(self):
        driver.find_element_by_id("com.autel.explorer:id/iv_user_icon_default").click()
        driver.find_element_by_id("com.autel.explorer:id/ed_email").send_keys("yxy@163.com")
        driver.find_element_by_id("com.autel.explorer:id/ed_pwd").send_keys("123456")
        driver.find_element_by_id("com.autel.explorer:id/btn_login").click()

    def register(self):
        driver.find_element_by_id("com.autel.explorer:id/iv_user_icon_default").click()
        driver.find_element_by_id("com.autel.explorer:id/tv_register").click()
        driver.find_element_by_id("com.autel.explorer:id/ed_email").send_keys("xxx@163.com")
        driver.find_element_by_id("com.autel.explorer:id/ed_pwd").send_keys("123456")
        driver.find_element_by_id("com.autel.explorer:id/ed_repeat_pwd").send_keys("123456")
        driver.find_element_by_id("com.autel.explorer:id/btn_login").click()

    def forgetpwd(self):
        driver.find_element_by_id("com.autel.explorer:id/iv_user_icon_default").click()
        driver.find_element_by_id("com.autel.explorer:id/tv_forget_pwd").click()
        driver.find_element_by_id("com.autel.explorer:id/et_email").send_keys("yyy@163.com")
        driver.find_element_by_id("com.autel.explorer:id/btn_send_email").click()

testreg=regLogin()
testreg.register()




