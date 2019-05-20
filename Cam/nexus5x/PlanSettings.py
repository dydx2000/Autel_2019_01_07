import datetime
from PIL import Image
import logging
import logging
logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a,%d %b %Y %H:%M:%S',
                    filename='CamShots.log',
                    filemode='a')
import random
import Cam.nexus5x.uiautomator2_cam_shots_filter as uiauto
import time
d = uiauto.d
test=uiauto.Camera()


#1-11 设置飞行就度限制，和返航高度限制
def GoHomeAltitude(num,limitnum):
    test.GotoSettingsWindow()
    # NoviceMode('off')
    d(resourceId="com.autel.explorer:id/tv_aircraft_settings_item_title", text=u"Flight Control").click()
    time.sleep(0.5)
    d.swipe(0.5,0.8,0.5,0.4)
    d(resourceId="com.autel.explorer:id/distance_cur_value_et").set_text(limitnum) #设置高度限制
    d.press('enter')
    time.sleep(0.5)
    d.swipe(0.5,0.2,0.5,0.8)
    d(resourceId="com.autel.explorer:id/distance_cur_value_et").set_text(num)   #设置返航高度
    d.press('enter')
    time.sleep(0.5)
    d(resourceId="com.autel.explorer:id/iv_setting_close").click()   #退出设置
    test.GotoSettingsWindow()  #重回设置
    d(resourceId="com.autel.explorer:id/tv_aircraft_settings_item_title", text=u"Flight Control").click()
    altitude = d(resourceId="com.autel.explorer:id/distance_cur_value_et").get_text()  #获取当前返航高度
    print('Current altitude is %s'%altitude)
    return altitude

#设置exp
def expSetting(num):
    test.GotoSettingsWindow()
    NoviceMode('off')
    d(resourceId="com.autel.explorer:id/tv_aircraft_settings_item_title", text=u"Flight Control").click()
    time.sleep(0.5)
    d.swipe(0.5,0.9,0.5,0.1)
    time.sleep(0.5)
    d(resourceId="com.autel.explorer:id/tv_item_arrow_title").click()
    time.sleep(0.5)
    d(resourceId="com.autel.explorer:id/tv_item_arrow_title").click()
    d(resourceId="com.autel.explorer:id/tv_ratio").set_text(num)
    d.press('enter')
    time.sleep(1)

#设置新手模式开关
def NoviceMode(num):
    test.GotoSettingsWindow()

    d(resourceId="com.autel.explorer:id/tv_aircraft_settings_item_title", text=u"Flight Control").click()
    time.sleep(0.5)

    d.screenshot('screen.jpg')
    im = Image.open("screen.jpg")
    r, g, b = im.split()
    color = b.getpixel((1737, 232))  # oneplus 3
    print(color)
    if num =='on':
        if color==254:
            print('Novice Mode is on')
        else:
            d(resourceId="com.autel.explorer:id/switch_item_switcher").click()
    elif num == 'off':
        if color == 254:
            d(resourceId="com.autel.explorer:id/switch_item_switcher").click()
        else:
            print('Novice Mode is off')

#图传模式至切换
def imgTrans(num):
    test.GotoSettingsWindow()
    d(resourceId="com.autel.explorer:id/tv_aircraft_settings_item_title", text=u"Image Transmission").click()
    d.swipe(0.5,0.6,0.5,0.3)
    time.sleep(0.5)
    text=d(resourceId="com.autel.explorer:id/tv_item_arrow_text_state")[1].get_text()

    print(text)
    if text == num:
        print('Image Transmission is already set to %s\n'%num)
    else:
        d(resourceId="com.autel.explorer:id/tv_item_arrow_text_title", text=u"Image Transmission Mode").click()
        time.sleep(0.5)
        if num == "Normal":
            d(resourceId="com.autel.explorer:id/tv_item_value").click()
            print('Image Transmissio is set to %s\n'%num)

        elif num == 'High':
            d(resourceId="com.autel.explorer:id/tv_item_value", text=u"High Definition").click()
            print('Image Transmissio is set to %s\n'%num)

        elif num == 'Smooth':
            d(resourceId="com.autel.explorer:id/tv_item_value", text=u"Smooth").click()
            print('Image Transmissio is set to %s\n'%num)
        else:
            print('You might input a wrong parameter!\n')

#宽带设置
def bandwiths(num):
    test.GotoSettingsWindow()
    d(resourceId="com.autel.explorer:id/tv_aircraft_settings_item_title", text=u"Image Transmission").click()
    time.sleep(0.5)
    d.swipe(0.5,0.6,0.5,0.3)
    text = d(resourceId="com.autel.explorer:id/tv_item_arrow_text_state").get_text()
    if text == num:
        print("Bandwiths is already set to %s"%num)
    else:
        d(resourceId="com.autel.explorer:id/tv_item_arrow_text_state").click()
        time.sleep(0.5)
        if num == '5 MHz':
            d(resourceId="com.autel.explorer:id/tv_item_value").click()
            print("Bandwiths is set to %s" % num)
        elif num == '10 MHz':
            d(resourceId="com.autel.explorer:id/tv_item_value", text=u"10 MHz").click()
            print("Bandwiths is set to %s" % num)
        elif num == '20 MHz':
            d(resourceId="com.autel.explorer:id/tv_item_value", text=u"20 MHz").click()
            print("Bandwiths is set to %s" % num)
        else:
            print("You might input a wrong parameter!")

#1-11 ，1-2非新手模式下，高度限制的值决定返航高度的设置u29 30 100..
def GoHomeAlttest1_13():
    NoviceMode('off')
    altlist =['29m','30m','100m','101m','200m']
    for num in altlist:
        print('trying to set altitude to %s'%num)
        altitude = GoHomeAltitude(num,'100m')
        if altitude ==  num:
            print('Altitude is set to %s successfully! \n'%num)
        else:
            print('Altitude must be between 30 to 200\n')

#1-16 非新手模式，手动输入修改高度限制
def GoHomeAlttest1_16():
    NoviceMode('off')
    altlist =['29m','30m','200m','201','800']
    for num in altlist:
        print('trying to set altitude to %s'%num)
        altitude = GoHomeAltitude(num,'800m')
        if altitude ==  num:
            print('Altitude is set to %s successfully! \n'%num)
        else:
            print('Altitude must be between 30 to 200\n')


#1-20 非新手模式下，在高级设置中设置exp
def expSetting_test1_20():
    for num in [0.1,0.2,0.8,0.3,0.4,0.5, 0.6,0.7]:
        expSetting(num)
        exp =d(resourceId="com.autel.explorer:id/tv_ratio").get_text()
        time.sleep(0.5)
        print('current exp value is %s'%exp)
        if float(exp) ==num:
            print('exp value is successfully set to %s\n'%num)
        else:
            print('exp value must be between 0.2 and 0.7\n')
        time.sleep(2)
        d.press('back')
        d(resourceId="com.autel.explorer:id/iv_setting_close").click()

#4-4,4-5, 4-6 各图传模式式拍视频
def  imgTrans4_456():
    test.setVideoReso('4K')
    for num in ['Normal','High','Smooth']:
        imgTrans(num)
        test.record()
        time.sleep(5)
        test.record()

#4-7#设置不同的broadband settings
def broadband4_7():
        for num in ['5 MHz','10 MHz','20 MHz']:
         bandwiths(num)
         time.sleep(3)
         d(resourceId="com.autel.explorer:id/iv_setting_close").click()

#7-1 进入通用设置
def intoGenSettings7_1():
    test.GotoSettingsWindow()
    d.swipe(0.1,0.6,0.1,0.3)
    time.sleep(0.5)
    d(resourceId="com.autel.explorer:id/tv_aircraft_settings_item_title", text=u"General").click()
    time.sleep(0.5)

#7-2 通用设置ui显示完整性
def GenSettingsui7_2():
    intoGenSettings7_1()
    if d(resourceId="com.autel.explorer:id/tv_item_arrow_title").exists():
        print('Home Point exists')
    if d(resourceId="com.autel.explorer:id/tv_item_arrow_text_title").exists():
        print('Units Exists')
    if d(resourceId="com.autel.explorer:id/tv_item_arrow_title", text=u"Firmware Version").exists():
        print('Firmware version exists')
    if d(resourceId="com.autel.explorer:id/tv_item_btn_text_title").exists():
        print('Restore ""Do not show again" exists')
    d.swipe(0.5,0.6,0.5,0.3)
    time.sleep(0.5)
    if d(resourceId="com.autel.explorer:id/tv_item_arrow_title", text=u"About").exists():
        print("about is exist")

#7-3 通用设置固件版本显示准确完整性
def GenSettingsFirmUI7_3():
    intoGenSettings7_1()
    d(resourceId="com.autel.explorer:id/tv_item_arrow_title", text=u"Firmware Version").click()
    time.sleep(0.5)
    if d(resourceId="com.autel.explorer:id/item_text_title").exists():
        print("flight control version exists")
    if d(resourceId="com.autel.explorer:id/item_text_title", text=u"Camera").exists():
        print("Camera version exists")
    if d(resourceId="com.autel.explorer:id/item_text_title", text=u"Remote Control").exists():
        print('Remote controller version exists')
    if d(resourceId="com.autel.explorer:id/item_text_title", text=u"Remote Control Panel"):
        print('Remote control panel version exists')
    if d(resourceId="com.autel.explorer:id/item_text_title", text=u"Image Transmission").exists():
        print('Image Transmission version exists')
    if d(resourceId="com.autel.explorer:id/item_text_title", text=u"Remote Control Image Transmission").exists():
        print("Remote Control Image Transmission version exists")
    d.swipe(0.5,0.8,0.5,0.2)
    if d(resourceId="com.autel.explorer:id/item_text_title").exists():
        print('Gimbal version exist')
    if d(resourceId="com.autel.explorer:id/item_text_title", text=u"Battery").exists():
        print("battery version exists")
    if d(resourceId="com.autel.explorer:id/item_text_title", text=u"Vision Module").exists():
        print('Vision Module version exist')
    if  d(resourceId="com.autel.explorer:id/item_text_title", text=u"Sonar").exists():
        print("Sonar version exists")
    if d(resourceId="com.autel.explorer:id/item_text_title", text=u"ESC1").exists():
        print('Esc1 exists')
    if d(resourceId="com.autel.explorer:id/item_text_title", text=u"ESC2").exists():
        print("Esc2 exists")
    d.swipe(0.5,0.6,0.5,0.3)
    if d(resourceId="com.autel.explorer:id/item_text_title", text=u"ESC3").exists():
        print('Esc3 exists')
    if d(resourceId="com.autel.explorer:id/item_text_title", text=u"ESC4").exists():
        print('Esc4 exists')
    time.sleep(1)
    d(resourceId="com.autel.explorer:id/iv_setting_close").click()


#7-4 通用设置未接飞行器固件版本显示
def GensettingFirmUI7_4():
    intoGenSettings7_1()
    d(resourceId="com.autel.explorer:id/tv_item_arrow_title", text=u"Firmware Version").click()
    time.sleep(0.5)
    text=d(resourceId="com.autel.explorer:id/tv_device_state").get_text()
    if text == 'Device Disconnected':
        print('Plane is disconnected')


# GoHomeAlttest1_13()
# GoHomeAlttest1_16()
# expSetting_test1_20()
# imgTrans4_456()
# broadband4_7()
# intoGenSettings7_1()
# GenSettingsui7_2()
# GenSettingsFirmUI7_3()
# GensettingFirmUI7_4()

i = 0
while True:
    i = i+1
    print("\n第", i , '次运行开始\n--------------------------------------------------------------------------')
    print(datetime.datetime.now())

    print('\n1-11 ，1-2非新手模式下，高度限制的值决定返航高度的设置u29 30 100')
    GoHomeAlttest1_13()
    time.sleep(2)

    print('\n#1-16 非新手模式，手动输入修改高度限制')
    GoHomeAlttest1_16()
    time.sleep(2)

    print('\n1-20 非新手模式下，在高级设置中设置exp')
    expSetting_test1_20()
    time.sleep(2)

    print('\n4-4,4-5, 4-6 各图传模式式拍视频')
    imgTrans4_456()
    time.sleep(2)

    print('\n4-7#设置不同的broadband settings')
    broadband4_7()
    time.sleep(2)

    print('\n7-1 进入通用设置')
    intoGenSettings7_1()
    time.sleep(2)

    print('\n7-2 通用设置ui显示完整性')
    GenSettingsui7_2()
    time.sleep(2)

    print('\n7-3 通用设置固件版本显示准确完整性')
    GenSettingsFirmUI7_3()
    time.sleep(2)

    # print('\n')
    #
    # time.sleep(2)
    #
    # print('\n')
    #
    # time.sleep(2)
    #
    # print('\n')
    #
    # time.sleep(2)
    #
    # print('\n')
    #
    # time.sleep(2)
    #
    # print('\n')
    #
    # time.sleep(2)
    #



    print("\n第", i , '次运行结束\n--------------------------------------------------------------------------')
    print(datetime.datetime.now())
    # time.sleep(300)