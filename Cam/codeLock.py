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
import Cam.uiautomator2_cam_shots_filter as uiauto


import time
d = uiauto.d
test=uiauto.Camera()
#接口
#  数据访问密码开关
def SetPasswdProtect(switch,pass1,pass2):
    test.intoPerCenter()
    if switch =='on':
        d(resourceId="com.autel.explorer:id/iv_user_setting").click()
        time.sleep(1)
        d.screenshot('datapasswd.jpg')
        im = Image.open("datapasswd.jpg")
        print('mode:', im.mode)
        print('size:', im.size)
        r, g, b = im.split()
        x = im.size[0] * 0.933
        y = im.size[1] * 0.195
        color = b.getpixel((x, y))
        print(color)
        if color == 223:
            print('password protection is  turned on!')
            time.sleep(1)
            d(resourceId="com.autel.explorer:id/iv_common_back").click()
            time.sleep(0.5)
            d.implicitly_wait(5)
            d.click(0.3, 0.5)
        else:
            d.set_fastinput_ime(True)
            d(resourceId="com.autel.explorer:id/setting_switch").click()
            time.sleep(0.5)
            d.implicitly_wait(5)
            d(resourceId="com.autel.explorer:id/et_data_password").set_text(pass1)
            time.sleep(0.5)
            d.implicitly_wait(5)
            d(resourceId="com.autel.explorer:id/et_sure_data_password").set_text(pass2)
            time.sleep(0.5)
            d.implicitly_wait(5)
            d(resourceId="com.autel.explorer:id/tv_ok").click()
            time.sleep(0.5)
            d.implicitly_wait(5)
            d(resourceId="com.autel.explorer:id/iv_common_back").click()
            time.sleep(0.5)
            d.implicitly_wait(5)
            d.click(0.3, 0.5)

    elif switch =='off':
        d(resourceId="com.autel.explorer:id/iv_user_setting").click()
        time.sleep(1)
        d.screenshot('datapasswd.jpg')
        time.sleep(0.5)
        d.implicitly_wait(5)
        im = Image.open("datapasswd.jpg")
        print('mode:', im.mode)
        print('size:', im.size)
        r, g, b = im.split()
        x = im.size[0] * 0.933
        y = im.size[1] * 0.195
        color = b.getpixel((x, y))
        print(color)
        if color == 223:
            print('password protection is  turned on!')
            d(resourceId="com.autel.explorer:id/setting_switch").click()
            time.sleep(0.5)
            d.implicitly_wait(5)
            print('turn it off!')
            d.set_fastinput_ime(True)
            d(resourceId="com.autel.explorer:id/et_data_password").set_text(pass1)
            time.sleep(0.5)
            d.implicitly_wait(5)
            d(resourceId="com.autel.explorer:id/tv_ok").click()

            time.sleep(1)
            d(resourceId="com.autel.explorer:id/iv_common_back").click()
            time.sleep(0.5)
            d.click(0.3, 0.5)
        else:
            print('password protection is  already turned off!')
            time.sleep(1)
            d(resourceId="com.autel.explorer:id/iv_common_back").click()
            time.sleep(0.5)
            d.click(0.3, 0.5)





#1-1  1-2首次访问密码锁
def test_codeLock1_1234():
    test.intoPerCenter()
    # if d(resourceId="com.autel.explorer:id/iv_user_icon").exists():
    #     d(resourceId="com.autel.explorer:id/iv_user_icon").click()
    # else:
    #     d(resourceId="com.autel.explorer:id/iv_user_icon_default", className="android.widget.ImageView").click()
    d(resourceId="com.autel.explorer:id/iv_user_setting").click()
    time.sleep(1)
    d.screenshot('datapasswd.jpg')
    im = Image.open("datapasswd.jpg")
    print('mode:', im.mode)
    print('size:', im.size)
    r, g, b = im.split()
    x =im.size[0]*0.933
    y=im.size[1]*0.195
    color = b.getpixel((x, y))
    print(color)
    if color == 223 :
        print('password protection is  turned on!')
        time.sleep(1)
        d(resourceId="com.autel.explorer:id/iv_common_back").click()
        time.sleep(0.5)
        d.click(0.3, 0.5)
    else:
        d.set_fastinput_ime(True)
        d(resourceId="com.autel.explorer:id/setting_switch").click()
        d(resourceId="com.autel.explorer:id/et_data_password").set_text('123456')
        d(resourceId="com.autel.explorer:id/et_sure_data_password").set_text('123456')
        d(resourceId="com.autel.explorer:id/tv_ok").click()
        # d.set_fastinput_ime(False)
        time.sleep(1)
        d(resourceId="com.autel.explorer:id/iv_common_back").click()
        time.sleep(0.5)
        d.click(0.3,0.5)

#1-3 两次密码不一致开启数据密码保护
def test_cokdeLockNotsampass1_34():
    SetPasswdProtect('off','123456','123456')
    test.intoPerCenter()
    d.set_fastinput_ime(True)
    d(resourceId="com.autel.explorer:id/iv_user_setting").click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    d(resourceId="com.autel.explorer:id/setting_switch").click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    d(resourceId="com.autel.explorer:id/et_data_password").set_text('123456')
    time.sleep(0.5)
    d.implicitly_wait(5)
    d(resourceId="com.autel.explorer:id/et_sure_data_password").set_text('a123456')
    time.sleep(0.5)
    d.implicitly_wait(5)
    d(resourceId="com.autel.explorer:id/tv_ok").click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    if d.xpath("//android.widget.TextView[@text='Password doesn’t match']"):
        print("password doesn't match")
    time.sleep(3)
    d(resourceId="com.autel.explorer:id/tv_cancel").click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    d(resourceId="com.autel.explorer:id/iv_common_back").click()
    time.sleep(1)
    d.click(0.3, 0.5)

#1-4 .1 关闭密码锁 输入正确密码，输入错误密码
def test_closeCodeLock1_41():
    SetPasswdProtect('on','123456','123456')
    time.sleep(0.5)
    d.implicitly_wait(5)
    test.intoPerCenter()
    time.sleep(0.5)
    d.implicitly_wait(5)
    d(resourceId="com.autel.explorer:id/iv_user_setting").click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    d(resourceId="com.autel.explorer:id/setting_switch").click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    d(resourceId="com.autel.explorer:id/et_data_password").set_text('123456')
    time.sleep(0.5)
    d.implicitly_wait(5)
    d(resourceId="com.autel.explorer:id/tv_ok").click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    d(resourceId="com.autel.explorer:id/iv_common_back").click()
    time.sleep(0.5)
    d.click(0.3,0.5)

#1-4 .2 关闭密码锁 输入错误密码
def test_closeCodeLock1_42():
    SetPasswdProtect('on','123456','123456')
    test.intoPerCenter()
    d(resourceId="com.autel.explorer:id/iv_user_setting").click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    d(resourceId="com.autel.explorer:id/setting_switch").click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    d(resourceId="com.autel.explorer:id/et_data_password").set_text('12345')
    time.sleep(0.5)
    d.implicitly_wait(5)
    d(resourceId="com.autel.explorer:id/tv_ok").click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    text = d(resourceId="com.autel.explorer:id/tv_tips").get_text()
    time.sleep(0.5)
    d.implicitly_wait(5)
    if text =='Password is not valid':
        print('无法用错误密码关闭保护，用例成功！')
    d(resourceId="com.autel.explorer:id/tv_cancel").click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    d(resourceId="com.autel.explorer:id/iv_common_back").click()
    time.sleep(0.5)
    d.click(0.3,0.5)

#2 -1 切换帐号验证密码锁 上个帐号开启了密码锁
def test_changeAccountwithcodeLock2_1():
    SetPasswdProtect('on','123456','123456')
    test.login('14567@qq.com','a123456')
    d(resourceId="com.autel.explorer:id/iv_user_icon").click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    d(resourceId="com.autel.explorer:id/iv_user_setting").click()
    time.sleep(1)
    d.screenshot('datapasswd.jpg')
    time.sleep(0.5)
    d.implicitly_wait(5)
    im = Image.open("datapasswd.jpg")
    print('mode:', im.mode)
    print('size:', im.size)
    r, g, b = im.split()
    x = im.size[0] * 0.933
    y = im.size[1] * 0.195
    color = b.getpixel((x, y))
    print(color)
    if color ==223:
        print('切换帐户后数据保护锁仍开启,用例成功！')
    else:
        print('切换帐户后数据保护锁未开启，用例失败！')
    time.sleep(2)
    d(resourceId="com.autel.explorer:id/iv_common_back").click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    d.click(0.3,0.5)
    test.login('147258369@qq.com', 'a123456')

#2 -2 切换帐号验证密码锁 上个帐号未开启密码锁
def test_changeAccountwithcodeLock2_2():
    SetPasswdProtect('off','123456','123456')
    test.login('14567@qq.com','a123456')
    d(resourceId="com.autel.explorer:id/iv_user_icon").click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    d(resourceId="com.autel.explorer:id/iv_user_setting").click()
    time.sleep(1)
    d.screenshot('datapasswd.jpg')
    time.sleep(0.5)
    d.implicitly_wait(5)
    im = Image.open("datapasswd.jpg")
    print('mode:', im.mode)
    print('size:', im.size)
    r, g, b = im.split()
    x = im.size[0] * 0.933
    y = im.size[1] * 0.195
    color = b.getpixel((x, y))
    print(color)
    if color ==223:
        print('切换帐户后数据保护锁开启,用例失功！')
    else:
        print('切换帐户后数据保护锁仍未开启，用例成功！')
    time.sleep(2)
    d(resourceId="com.autel.explorer:id/iv_common_back").click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    d.click(0.3,0.5)
    test.login('147258369@qq.com', 'a123456')


# test_codeLock1_1234()
# SetPasswdProtect('off')
# test_cokdelockNotsampass1_34()
# closeCodeLock1_41()
# closeCodeLock1_42()
# test_changeAccountwithcodeLock2_1()
# test_changeAccountwithcodeLock2_2()

# print('登录账号！')
# test.login('yxy2019@qq.com','abc123456')
i = 0
while True:
    i = i+1

    print("\n第", i , '次运行开始\n--------------------------------------------------------------------------')
    print(datetime.datetime.now())


    print('\n1-1  1-2首次访问密码锁')
    test_codeLock1_1234()
    time.sleep(2)

    print('\n1-3 两次密码不一致开启数据密码保护')
    test_cokdeLockNotsampass1_34()
    time.sleep(2)

    print('\n1-4 .1 关闭密码锁 输入正确密码，输入错误密码')
    test_closeCodeLock1_41()
    time.sleep(2)

    print('\n1-4 .2 关闭密码锁 输入错误密码')
    test_closeCodeLock1_42()
    time.sleep(2)

    print('\n2 -1 切换帐号验证密码锁 上个帐号开启了密码锁')
    test_changeAccountwithcodeLock2_1()
    time.sleep(2)

    print('\n2 -2 切换帐号验证密码锁 上个帐号未开启密码锁')
    test_changeAccountwithcodeLock2_2()
    time.sleep(2)

    print('\n')

    time.sleep(2)

    print('\n')

    time.sleep(2)

    print("\n第", i, '次运行结束\n--------------------------------------------------------------------------')
    print(datetime.datetime.now())