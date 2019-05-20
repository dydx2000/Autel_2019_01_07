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

# des_cap['platformVersion'] = '9'  #oneplus 6 9
# des_cap['deviceName'] = '192.168.1.17:5555'  # oneplus6 wifi
des_cap['platformVersion'] = '8.1.0' #lgG 7
des_cap['deviceName'] = '192.168.1.17:5555'  # LG wifi

des_cap['automationName'] = 'Appium'  #uiautomator2,uiautomator
des_cap['noReset'] = True
des_cap['appPackage'] = 'com.autel.explorer'
des_cap['appActivity'] = 'com.autel.modelb.view.autelhome.AutelHomeActivity'
des_cap['skipDeviceInitialization']=True
des_cap['disableAndroidWatchers']=True
# des_cap['autoLaunch']=False
# des_cap['unicodeKeyboard']=True
# des_cap['resetKeyboard']=True
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub", des_cap)

#设置照片大小
def SetPictureSize(Size):
    time.sleep(2)

    driver.find_element_by_id("com.autel.explorer:id/tv_autel_home_start").click()  # go fly
    time.sleep(1)
    # time.sleep(1.5)
    # 判断底栏是否存在,存在刚往右滑,显示最左边的内存
    if driver.find_element_by_id("com.autel.explorer:id/rv_camera_modes_view"):
            # time.sleep(1.5)
            driver.swipe(0.32,0.94,0.68,0.94)  #右滑
            # time.sleep(1.5)

    #检查 size元素是否存在

    if driver.find_element_by_android_uiautomator('new UiSelector().text("SIZE")'):
            # time.sleep(1.5)
            driver.find_element_by_android_uiautomator('new UiSelector().text("SIZE")').click()
            time.sleep(1)


    #检查输入参数
    if Size == "4000x3000":
            # time.sleep(2)
            driver.find_element_by_android_uiautomator('new UiSelector().text("4000x3000(4:3)")')
            # driver.find_element_by_('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.TextView').click()
            time.sleep(1)
    else:
            # driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.TextView').click()
            driver.find_element_by_android_uiautomator('new UiSelector().text("4000x2250(16:9)")')
            time.sleep(1)


    #设置完成点击屏幕中央
    driver.tap([(0.5,0.5)])


def SetPictureFomat(format):
    time.sleep(2)

    driver.find_element_by_id("com.autel.explorer:id/tv_autel_home_start").click()  # go fly
    time.sleep(1)
    # time.sleep(1.5)
    # 判断底栏是否存在,存在刚往右滑,显示最左边的内存
    if driver.find_element_by_id("com.autel.explorer:id/rv_camera_modes_view"):
        time.sleep(1.5)
        driver.swipe(0.32, 0.94, 0.68, 0.94)  # 右滑
        time.sleep(1.5)

    # 检查 format元素是否存在

    # if driver.find_element_by_android_uiautomator('new UiSelector().text("FORMAT")'):
    #    time.sleep(1.5)
    driver.find_element_by_android_uiautomator('new UiSelector().text("FORMAT")').click()

    # 检查输入参数
    if format == "JPG":
        driver.find_element_by_android_uiautomator('new Uiselector().text("JPG")').click()
        # driver.find_element_by_('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.TextView').click()
        time.sleep(1)

    elif format == "RAW":
        driver.find_element_by_android_uiautomator('new UiSelector().text("RAW")').click()

    else:
        driver.find_element_by_android_uiautomator('new UiSelector().text("RAW+JPG")').click()
        time.sleep(1)

    # 设置完成点击屏幕中央
    driver.tap([(0.5, 0.5)])


def SetPictureMode(mode,num=None):
    time.sleep(2)

    driver.find_element_by_id("com.autel.explorer:id/tv_autel_home_start").click()  # go fly
    time.sleep(4)


    driver.find_element_by_android_uiautomator('new UiSelector().text("MODE")').click()
        # pass# driver.find_element_by_xpath("	/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView")
    time.sleep(1.5)

    try:
            selectormode='new UiSelector().text(\"'+mode+'\")'
            driver.find_element_by_android_uiautomator(selectormode).click()  #先看有没有在显示,
    except:                                                                                #没有的话就往左或者往右翻找找吧
            if mode=="SINGLE":      #给每个选项编号
                seq=0
            elif mode=="BURST":
                seq=1
            elif mode=="TIMELAPSE":
                seq=2
            else:
                seq=3

            listMode=["SINGLE","BURST","TIMELAPSE","AEB"]  #把参放进列表里头:
            i=0
            while i<=len(listMode) :   #通过参数指定模式的参数编号 seq 与 当前滑块 最左边的 所见元素的编号比较, seq比较大,就左移,否则右移
                print(listMode[i])
                # print(mode_text)
                # if driver.find_element_by_link_text(listMode[i]).click():
                selector='new UiSelector().text(\"' + listMode[i]+  '\")'
                          # 'new UiSelector().text(\"' + mode + '\")'

                if driver.find_element_by_android_uiautomator(selector):

                      flag = False
                      if i>seq:
                          j=0

                          while j<=10:
                              driver.swipe(0.32, 0.82, 0.68, 0.82) #往左边滑
                              try:
                                  driver.find_element_by_android_uiautomator('new UiSelector().text(mode)').click()
                                  flag=True

                              except:
                                  print("not found,continue...")
                              finally:
                                 if flag:
                                   break
                          j+=1


                      else:
                          j = 0
                          while j <= 10:
                              driver.swipe(0.68, 0.82, 0.32, 0.82)  # 往右边滑
                              try:
                                  driver.find_element_by_android_uiautomator('new UiSelector().text(mode)').click()
                                  flag = True

                              except:
                                  print("not found,continue...")

                              finally:
                                 if flag:
                                   break
                          j += 1

                if flag:
                     break
                i+=1    #   #



    # 设置完成点击屏幕中央
    driver.tap([(0.5, 0.5)])






# SetPictureSize("4000x2250")
# SetPictureFomat("RAW+JPG")
SetPictureMode("BURST")



