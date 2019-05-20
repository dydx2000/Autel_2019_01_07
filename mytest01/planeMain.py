# coding:utf-8
import os, time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction



desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4'
# desired_caps['deviceName'] = '8f21c9ba'
desired_caps['deviceName'] = '50a72b24260b'
desired_caps['unicodeKeyboard']=True
desired_caps['resetKeyboard']=True
# desired_caps['app']=''

desired_caps['appPackage'] = 'com.autel.explorer'
# desired_caps['appActivity'] = 'com.autel.modelb.view.personalcenter.userinfo.activity.LoginRegisterActivity'
desired_caps['appActivity'] = 'com.autel.modelb.view.autelhome.AutelHomeActivity'
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
driver.implicitly_wait(10)
# driver.implicitly_wait(10)
time.sleep(3)



#进入主选单
def intoMainsetting():
     driver.find_element_by_id("com.autel.explorer:id/tv_autel_home_start").click()
     driver.find_element_by_id("com.autel.explorer:id/rl_setting").click()
#飞控选项卡
def flyControl():
    clsAddText='resourceId("com.autel.explorer:id/tv_aircraft_settings_item_title").text("飞控")'
    driver.find_element_by_android_uiautomator(clsAddText).click()
    #调节返航高度
    # driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.autel.explorer:id/distance_cur_value_et")').send_keys("50")
    # driver.keyevent('66')
    driver.flick(500,432,1021,432)

    #加速模式 狂暴
    time.sleep(2)
    driver.find_element_by_id("com.autel.explorer:id/rb_frenzy").click()
    #屏幕上划
    driver.swipe(400,690,400,20)
    #高度限制
    time.sleep(2)
    driver.find_element_by_id("com.autel.explorer:id/distance_cur_value_et").send_keys("90")
    driver.keyevent('66')
    #高级设置
    driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.autel.explorer:id/tv_item_arrow_title")').click()

def generalSetting():
    #设置--通用
    driver.swipe(150,690,150,200)
    tongyongbtn='resourceId("com.autel.explorer:id/tv_aircraft_settings_item_title").text("通用")'
    driver.find_element_by_android_uiautomator(tongyongbtn).click()
    length='resourceId("com.autel.explorer:id/tv_item_arrow_text_state").text("公制(km/h)")'
    driver.find_element_by_android_uiautomator(length).click()
    driver.tap([(1100,360)],100)
    time.sleep(5)
    # driver.back()

    #设置--云台
def yuntaiSetting():
    time.sleep(2)
    driver.swipe(150,690,150,200)
    driver.find_element_by_android_uiautomator('new UiSelector().text("云台")').click()
    time.sleep(2)
    # TouchAction().long_press(x=485,y=543).move_to(x=1000,y=543).release()
    driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.autel.explorer:id/distance_cur_value_et")').send_keys("55")
    driver.keyevent(66)
    # driver.flick(485,543,30,0) #这里也是相对偏移量



def closeMap():
    driver.find_element_by_id("com.autel.explorer:id/tv_autel_home_start").click()
    driver.find_element_by_id("com.autel.explorer:id/intercept_img_shrink_add").click()


def showPlaneStatus():
    driver.find_element_by_id("com.autel.explorer:id/tv_autel_home_start").click()
    driver.find_element_by_id("com.autel.explorer:id/show_history_iv").click()
    time.sleep(2)

def noConnectbtn():
    driver.find_element_by_id("com.autel.explorer:id/tv_autel_home_start").click()
    time.sleep(2)
    # driver.find_element_by_android_uiautomator('ClassName("com.autel.explorer:id/tv_mode").text("未连接")').click()
    # driver.find_element_by_android_uiautomator('className("android.widget.TextView").textContains("连接")').click()
    # driver.find_element_by_android_uiautomator('new UiSelector().textMatches(".*连.*")').click() #正则匹配1
    # driver.find_element_by_android_uiautomator('new UiSelector().textMatches("^未.*")').click() #正则匹配2
    driver.find_element_by_android_uiautomator('new UiSelector().text("未连接")').click()

    # driver.find_elements_by_android_uiautomator('new UiSelector().resourceId("com.autel.explorer:id/model_choice_bg")')[2].click() #id ,class相同样,用index,
    eles=driver.find_elements_by_android_uiautomator('new UiSelector().resourceId("com.autel.explorer:id/model_choice_bg")') #id ,class相同样,用index,


    for i in eles:
        print(i)
    # eles[2].click()
    driver.find_elements_by_android_uiautomator('new UiSelector().resourceId("com.autel.explorer:id/model_choice_bg")')[1].click()
    time.sleep(2)
    # driver.swipe(930,325,330,325,duration=200)
    driver.swipe(930,325,330,325)
    time.sleep(1)
    driver.tap([(831,594)],200)

def run_flyControl():
    intoMainsetting()
    flyControl()

def run_yuntaiSetting():
    intoMainsetting()
    yuntaiSetting()


# closeMap()
# showPlaneStatus()
# noConnectbtn()
# run_flyControl()
run_yuntaiSetting()

