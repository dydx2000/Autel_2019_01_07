# encoding=utf-8
from appium import webdriver
import time,warnings
from appium.webdriver.common.touch_action import TouchAction
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
des_cap['resetKeyboard']=True
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub", des_cap)



def SetPictureSize(Size):
    time.sleep(2)

    driver.find_element_by_id("com.autel.explorer:id/tv_autel_home_start").click()  # go fly
    time.sleep(4)
    # time.sleep(1.5)
    try:
        # BottomSetBarElement = driver.find_elements_by_id("com.autel.explorer:id/rv_camera_modes_view")
        BottomSetBarElement = driver.find_elements_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView")
        time.sleep(1.5)
        driver.swipe(0.32,0.94,0.68,0.94)  #右滑


    except:
        pass #log
    else:
        pass
    try:
        PhotoSizeSetElement = driver.find_element_by_android_uiautomator('new UiSelector().text("SIZE")')
        time.sleep(1.5)
    except:
        pass
        # self.logger.logger.warn(
        #     "Can not find Photo size setting item in capture mode***")
    else:
        try:
            PhotoSizeSetElement.click()
            time.sleep(1.5)
        except:
            pass
            # self.logger.logger.warn(
            #     "Go to the Photo size setting interface in capture mode error***")
        try:
            if Size == "4000x3000":
                SizeElement = driver.find_element_by_android_uiautomator('new UiSelector().text(Size + "(4:3)")')
                time.sleep(3)
            else:
                SizeElement = driver.find_element_by_android_uiautomator('new UiSelector().text(Size + "(16:9)")')
                time.sleep(3)

        except Exception as e:
             pass
             # self.logger.logger.warn(
             #    "Can not find Photo size setting value %s in capture mode***" % Size)
        else:
            try:
                SizeElement.click()
                time.sleep(1)
            except:
                pass
                # self.logger.logger.warn(
                #     "Set %s Photo size setting value in capture mode***" % Size)
            else:
                driver.tap([(0.5,0.5)])



def CameraSize_Setting_43(driver): #图像大小选择 4:3
        time.sleep(2)

        driver.find_element_by_id("com.autel.explorer:id/tv_autel_home_start").click()  # go fly
        time.sleep(4)
        driver.swipe(0.25,0.94,0.75,0.94)
        time.sleep(0.5)
        driver.tap([(0.18,0.94)],100)
        time.sleep(0.5)
        driver.swipe(0.75,0.82,0.5,0.82)
        time.sleep(0.5)

CameraSize_Setting_43(driver)
# SetPictureSize("4000x3000")