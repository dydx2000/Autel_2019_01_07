# coding:utf-8
import time
# from appium import webdriver
desired_caps =  {
          'platformName': 'Android',
          'platformVersion': '4.4',
          'deviceName': '50a72b24260b',
          'automationName': 'UiAutomator2',
          'appPackage': 'com.autel.explorer',
          'appActivity': 'com.autel.modelb.view.autelhome.AutelHomeActivity'
                }
# driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

#相机
def intoCam(driver):
    # 点击开始
    driver.find_element_by_id("com.autel.explorer:id/tv_autel_home_start").click()
    # 相机设置
    driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.autel.explorer:id/rI_camera_setting")').click()

#接接向导
def connectWizard(driver):
    driver.find_element_by_id("com.autel.explorer:id/tv_connect_status").click()
    time.sleep(5)
    driver.back()

def login(driver):
    driver.find_element_by_id("com.autel.explorer:id/iv_user_icon_default").click()
    time.sleep(5)
    driver.back()


def intoGrid(driver):
    # 相机设置--网格模块
    camSets=driver.find_elements_by_id("com.autel.explorer:id/item_general_setting_value_tv")
    camSets[0].click()

def setGrid(driver):
    camGrids = driver.find_elements_by_android_uiautomator(
        'new UiSelector().resourceId("com.autel.explorer:id/general_setting_image_item_value_text")')
    camGrids[1].click()
    driver.find_element_by_id("com.autel.explorer:id/camera_general_setting_back_iv").click()
    time.sleep(5)
    driver.back()
    driver.back()

def setHVline(driver):
    camGrids = driver.find_elements_by_android_uiautomator(
        'new UiSelector().resourceId("com.autel.explorer:id/general_setting_image_item_value_text")')
    camGrids[2].click()
    driver.find_element_by_id("com.autel.explorer:id/camera_general_setting_back_iv").click()
    time.sleep(5)
    driver.back()
    driver.back()







