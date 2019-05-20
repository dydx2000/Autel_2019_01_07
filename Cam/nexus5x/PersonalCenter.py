import datetime
from PIL import Image
import logging
# import logging
# logging.basicConfig(level=logging.ERROR,
#                     format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%a,%d %b %Y %H:%M:%S',
#                     filename='CamShots.log',
#                     filemode='a')
import random
import Cam.nexus5x.uiautomator2_cam_shots_filter as uiauto
# import Cam.nexus5x.GroundStation_Test as GroundStationTest
# import Cam.nexus5x.codeLock as codeLock
import time
d = uiauto.d
test=uiauto.Camera()

'''相关接口'''
#回到首页
def goStart():
    #在首页
    if  d(resourceId="com.autel.explorer:id/tv_autel_home_start", text=u"GO FLY",
      className="android.widget.TextView").exists(3):
       print('is in start page')
       time.sleep(1)
    # 在已登录界面
    elif d(resourceId="com.autel.explorer:id/tv_logout", text=u"Logout", className="android.widget.TextView").exists(3):
        print('is in login interface!')
        d(resourceId="com.autel.explorer:id/iv_common_back", className="android.widget.ImageView").click_exists(5)
        time.sleep(5)

    #在登录界面
    elif d(resourceId="com.autel.explorer:id/btn_login", text=u"Login", className="android.widget.Button").exists(3):
        d(resourceId="com.autel.explorer:id/iv_back", className="android.widget.ImageView").click_exists(5)
        time.sleep(5)

    #在注册界面
    elif d(resourceId="com.autel.explorer:id/btn_login", text=u"Register", className="android.widget.Button").exists(3):
        d(resourceId="com.autel.explorer:id/iv_back", className="android.widget.ImageView").click_exists(5)
        d.implicitly_wait(10)
        d(resourceId="com.autel.explorer:id/iv_back", className="android.widget.ImageView").click_exists(5)
        time.sleep(5)




        # 在功能界面

    #在个人信息中心
    elif d(resourceId="com.autel.explorer:id/tv_common_title", text=u"Personal Information", className="android.widget.TextView").exists(3):
        d(resourceId="com.autel.explorer:id/iv_back", className="android.widget.ImageView").click_exists(5)
        time.sleep(5)

     #在功能界面
    elif d(resourceId="com.autel.explorer:id/rl_left", className="android.widget.RelativeLayout").exists(3):
        d(resourceId="com.autel.explorer:id/rl_left", className="android.widget.RelativeLayout").click_exists(5)
        time.sleep(8)

    # 在设置界面
    elif d(resourceId="com.autel.explorer:id/tv_setting_title", text=u"Settings",className="android.widget.TextView").exists(3):
        d(resourceId="com.autel.explorer:id/iv_setting_close", className="android.widget.ImageView").click_exists(5)
        d.implicitly_wait(15)
        d(resourceId="com.autel.explorer:id/rl_left", className="android.widget.RelativeLayout").click_exists(5)
        d.implicitly_wait(15)
        d(resourceId="com.autel.explorer:id/iv_user_icon_default", className="android.widget.ImageView").click_exists(5)
        time.sleep(8)

    # 在相机设置界面
    elif d(resourceId="com.autel.explorer:id/camera_general_setting_title", text=u"Camera Settings",className="android.widget.TextView").exists(3):
        d.click(0.5, 0.5)
        time.sleep(0.5)
        d(resourceId="com.autel.explorer:id/rl_left", className="android.widget.RelativeLayout").click_exists(5)
        time.sleep(8)

    else:
        pass


    # def intoPerCenter():
    #     #在首页的情景
    #     if d(resourceId="com.autel.explorer:id/tv_autel_home_start", text=u"GO FLY", className="android.widget.TextView").exists(3):
    #         d(resourceId="com.autel.explorer:id/iv_user_icon_default", className="android.widget.ImageView").click_exists(5)
    #     #在注册登录界面
    #     if d(resourceId="com.autel.explorer:id/ed_pwd", className="android.widget.EditText").exists(3):
    #         print('is in registration or login interface!')
    #     #在功能界面
    #     elif d(resourceId="com.autel.explorer:id/rl_left", className="android.widget.RelativeLayout").exists(3):
    #         d(resourceId="com.autel.explorer:id/rl_left", className="android.widget.RelativeLayout").click_exists(5)
    #         d.implicitly_wait(15)
    #         d(resourceId="com.autel.explorer:id/iv_user_icon_default", className="android.widget.ImageView").click_exists(5)
    #      #在设置界面
    #     elif d(resourceId="com.autel.explorer:id/tv_setting_title", text=u"Settings", className="android.widget.TextView").exists(3):
    #         d(resourceId="com.autel.explorer:id/iv_setting_close", className="android.widget.ImageView").click_exists(5)
    #         d.implicitly_wait(15)
    #         d(resourceId="com.autel.explorer:id/rl_left", className="android.widget.RelativeLayout").click_exists(5)
    #         d.implicitly_wait(15)
    #         d(resourceId="com.autel.explorer:id/iv_user_icon_default", className="android.widget.ImageView").click_exists(5)
    #     #在相机设置界面
    #     elif d(resourceId="com.autel.explorer:id/camera_general_setting_title", text=u"Camera Settings", className="android.widget.TextView").exists(3):
    #         d.click(0.5,0.5)
    #         time.sleep(0.5)
    #         d(resourceId="com.autel.explorer:id/rl_left", className="android.widget.RelativeLayout").click_exists(5)
    #         d.implicitly_wait(15)
    #         d(resourceId="com.autel.explorer:id/iv_user_icon_default", className="android.widget.ImageView").click_exists(5)
    #     else:
    #         pass

#进入个人中心
def intoPerCenter():
    goStart()
    if d(resourceId="com.autel.explorer:id/iv_user_icon").exists(3):
        d(resourceId="com.autel.explorer:id/iv_user_icon").click_exists(5)
        time.sleep(0.5)
    else:
        try:
            d(resourceId="com.autel.explorer:id/iv_user_icon_default", className="android.widget.ImageView").click_exists(5)
        except:
            test.catchError()
        time.sleep(0.5)


#进入忘记密码界面
def intoForgetPwd():
    goStart()
    d(resourceId="com.autel.explorer:id/iv_user_icon_default", className="android.widget.ImageView").click_exists(5)

    if  d(resourceId="com.autel.explorer:id/iv_user_setting", className="android.widget.ImageView").exists(3):
        d(resourceId="com.autel.explorer:id/iv_user_photo", className="android.widget.ImageView").click_exists(5)
        d(resourceId="com.autel.explorer:id/tv_logout", text=u"Logout", className="android.widget.TextView").click_exists(5)
        d(resourceId="com.autel.explorer:id/tv_ok", text=u"OK", className="android.widget.TextView").click_exists(5)
        time.sleep(6)

    # :
    #     pass
    #在登录页
    if d(resourceId="com.autel.explorer:id/tv_register", text=u"Register", className="android.widget.TextView").exists(3):
        d(resourceId="com.autel.explorer:id/tv_forget_pwd", text=u"Forget your password?",
          className="android.widget.TextView").click_exists(5)
     #在注册页
    elif d(resourceId="com.autel.explorer:id/tv_register", text=u"Login", className="android.widget.TextView").exists(3):
        d(resourceId="com.autel.explorer:id/tv_register", text=u"Login", className="android.widget.TextView").click_exists(5)
        d.implicitly_wait(5)
        d(resourceId="com.autel.explorer:id/tv_forget_pwd", text=u"Forget your password?",
          className="android.widget.TextView").click_exists(5)
     #在首页
    elif    d(resourceId="com.autel.explorer:id/tv_autel_home_start", text=u"GO FLY", className="android.widget.TextView").exists(3):
        d(resourceId="com.autel.explorer:id/iv_user_icon_default", className="android.widget.ImageView").click_exists(5)
        d.implicitly_wait(5)
        d(resourceId="com.autel.explorer:id/tv_forget_pwd", text=u"Forget your password?",
          className="android.widget.TextView").click_exists(5)

#修改用户名
def  modifyUserName(name):
    if d(resourceId="com.autel.explorer:id/tv_common_title", text=u"Personal Information", className="android.widget.TextView").exists(3):
        print('is in Personal Information.')
    else:
        intoPerInfo()
    d(resourceId="com.autel.explorer:id/tv_left_title", text=u"Name", className="android.widget.TextView").click_exists(5)
    time.sleep(1.5)
    d.implicitly_wait(5)
    if d(resourceId="com.autel.explorer:id/et_username",  className="android.widget.EditText").get_text() == name:
        d(resourceId="com.autel.explorer:id/iv_common_back", className="android.widget.ImageView").click_exists(5)
        print('already set this name.')
    else:
        try:
            d.implicitly_wait(5)
            d(resourceId="com.autel.explorer:id/et_username", className="android.widget.EditText").set_text(name)
            time.sleep(1)
            d.implicitly_wait(5)
            d(resourceId="com.autel.explorer:id/btn_submit", text=u"Submit", className="android.widget.Button").click_exists(5)
            print('\nset name %s successfully.'%name)
        except:
            print("name format or length is wrong")
            time.sleep(1)
            d(resourceId="com.autel.explorer:id/iv_common_back", className="android.widget.ImageView").click_exists(5)

#修改性别
def modifyGender(sex):
    if    d(resourceId="com.autel.explorer:id/tv_common_title", text=u"Personal Information",
            className="android.widget.TextView").exists(3):
            print('is in Personal Information.')
    else:
           intoPerInfo()
    d(resourceId="com.autel.explorer:id/tv_left_title", text=u"Gender", className="android.widget.TextView").click_exists(5)
    time.sleep(1)
    if sex=='Private':
        d(resourceId="com.autel.explorer:id/tv_name", text=u"Private", className="android.widget.TextView").click_exists(5)
    elif sex =='Female':
        d(resourceId="com.autel.explorer:id/tv_name", text=u"Female", className="android.widget.TextView").click_exists(5)
    elif sex =='Male':
        d(resourceId="com.autel.explorer:id/tv_name", text=u"Male", className="android.widget.TextView").click_exists(5)
    else:
        print('input a wrong gender parameter.')

#修改国家地区
def modifyCountry(country):
    #判断是否在个人信息中心
    if    d(resourceId="com.autel.explorer:id/tv_common_title", text=u"Personal Information",
            className="android.widget.TextView").exists(3):
            print('is in Personal Information.')
    else:
           intoPerInfo()

    curCountry = d(resourceId="com.autel.explorer:id/tv_right_content", className="android.widget.TextView")[
         2].get_text()

    # 判断国家地区是否空
    if curCountry =="": #空
            d.implicitly_wait(5)
            print('个人中心未设置国家或地区！')
            d(resourceId="com.autel.explorer:id/iv_more_info_indicator", className="android.widget.ImageView", instance=2).click_exists(5)
            i = 0
            while i <= 30:
                d.swipe(0.72, 0.8, 0.72, 0.23)
                time.sleep(0.5)
                if d(resourceId="com.autel.explorer:id/tv_name", text=country,
                     className="android.widget.TextView").exists(3):
                    d(resourceId="com.autel.explorer:id/tv_name", text=country,
                      className="android.widget.TextView").click_exists(5)
                    break
                i += 1

    # 不空
    else:
        #个人中心可见要设置的国家地区
        if country == curCountry:
            print('country is already set.')

        else:
            #点击进入国家列表
            d(resourceId="com.autel.explorer:id/tv_left_title", text=u"Country/Region",
              className="android.widget.TextView").click_exists(5)
            time.sleep(1)
            d.implicitly_wait(5)
            #国家地区是否出现在可见区域中
            if d(resourceId="com.autel.explorer:id/tv_name", text=country, className="android.widget.TextView").exists(3):
                d(resourceId="com.autel.explorer:id/tv_name", text=country, className="android.widget.TextView").click_exists(5)
            else:
                # firstcounry = d(resourceId="com.autel.explorer:id/tv_name", className="android.widget.TextView")[0].get_text()
                # print(firstcounry)
                #循环判断是否在列表中，是就选中中断循环
                a =curCountry[:1]
                print(a)
                b = country[:1]
                print(b)
                time.sleep(0.5)
                if b > a:
                    i =0
                    while i <= 40:
                        d.swipe(0.72,0.83,0.72,0.23)
                        time.sleep(0.8)
                        if d(resourceId="com.autel.explorer:id/tv_name", text=country,
                             className="android.widget.TextView").exists(3):
                            d(resourceId="com.autel.explorer:id/tv_name", text=country,
                              className="android.widget.TextView").click_exists(5)
                            time.sleep(0.5)
                            break
                        i += 1
                else:
                    i = 0
                    while i <= 40:
                        d.swipe(0.72, 0.23, 0.72, 0.83)
                        time.sleep(0.8)
                        # d.implicitly_wait(2)
                        if d(resourceId="com.autel.explorer:id/tv_name", text=country,
                             className="android.widget.TextView").exists(3):
                            d(resourceId="com.autel.explorer:id/tv_name", text=country,
                              className="android.widget.TextView").click_exists(5)
                            time.sleep(0.5)

                            break
                        i += 1




#登录，已登录时不退出再次登录
def loginifnotlogin(mail,passwd):
    goStart()
    d.implicitly_wait(5.0)
    if  d(resourceId="com.autel.explorer:id/iv_user_icon_default"):
      d(resourceId="com.autel.explorer:id/iv_user_icon_default").click_exists(5)
    else:
        d(resourceId="com.autel.explorer:id/iv_user_icon").click_exists(5)
    time.sleep(1)

    if d(resourceId="com.autel.explorer:id/tv_register").exists(3):
        d(resourceId="com.autel.explorer:id/ed_email").set_text(mail)
        d(resourceId="com.autel.explorer:id/ed_pwd").set_text(passwd)
        d.implicitly_wait(5.0)
        d(resourceId="com.autel.explorer:id/btn_login").click_exists(5)
        time.sleep(5)
        d.click(0.3,0.5)
    elif d(resourceId="com.autel.explorer:id/iv_user_setting").exists(3):
        print('you have logged in!')
        d.click(0.3,0.5)
    else:
        pass





#登录
def login(mail,passwd):
    test.goStart()
    d.set_fastinput_ime(True)
    if  d(resourceId="com.autel.explorer:id/iv_user_icon_default"):
      d(resourceId="com.autel.explorer:id/iv_user_icon_default").click_exists(5)
    else:
        d(resourceId="com.autel.explorer:id/iv_user_icon").click_exists(5)
    #已登录情况下
    if d(resourceId="com.autel.explorer:id/iv_user_setting", className="android.widget.ImageView").exists(3):
        d(resourceId="com.autel.explorer:id/iv_user_photo", className="android.widget.ImageView").click_exists(5)
        d.implicitly_wait(10)
        d(resourceId="com.autel.explorer:id/tv_logout", text=u"Logout", className="android.widget.TextView").click_exists(5)
        time.sleep(0.5)
        d(resourceId="com.autel.explorer:id/tv_ok", text=u"OK", className="android.widget.TextView").click_exists(5)
        time.sleep(6)
        d(resourceId="com.autel.explorer:id/iv_user_icon_default", className="android.widget.ImageView").click_exists(5)
        d.implicitly_wait(10)
        d(resourceId="com.autel.explorer:id/ed_email").set_text(mail)
        d(resourceId="com.autel.explorer:id/ed_pwd").set_text(passwd)
        d(resourceId="com.autel.explorer:id/btn_login").click_exists(5)
        time.sleep(5)
        d.click(0.3, 0.5)

    else:

        d(resourceId="com.autel.explorer:id/ed_email").set_text(mail)
        d(resourceId="com.autel.explorer:id/ed_pwd").set_text(passwd)
        d.implicitly_wait(5.0)
        d(resourceId="com.autel.explorer:id/btn_login").click_exists(5)
        time.sleep(5)
        d.click(0.3,0.5)



'''用例'''

#1-1 进入个人中心
def test_intoPerCenter1_1():
    intoPerCenter()
    d.click(0.3, 0.5)
    pass

#1-2 退出个人中心
def test_outPerCenter1_2():
    intoPerCenter()
    if d(resourceId="com.autel.explorer:id/iv_user_photo", className="android.widget.ImageView").exists(3):
        d.click(0.3,0.5)

    else:
        pass
        # d.implicitly_wait(10)
        # d(resourceId="com.autel.explorer:id/iv_back", className="android.widget.ImageView").click_exists(5)

#1-3 进出个人中心10次
def test_inoutPerCenter1_3():
    for i in range(0,10):
        test_intoPerCenter1_1()
        # d(resourceId="com.autel.explorer:id/iv_back", className="android.widget.ImageView").click_exists(5)
        # time.sleep(5)

#2-1 进入个人中心注册界面
def RegisterUi2_1():
    intoPerCenter()
    time.sleep(5)
    #在登录界面
    if d(resourceId="com.autel.explorer:id/tv_register", text=u"Register", className="android.widget.TextView").exists(3):
        d(resourceId="com.autel.explorer:id/tv_register", text=u"Register", className="android.widget.TextView").click_exists(5)
    #己经登录
    elif  d(resourceId="com.autel.explorer:id/iv_user_setting", className="android.widget.ImageView").exists(3):
          d(resourceId="com.autel.explorer:id/iv_user_photo", className="android.widget.ImageView").click_exists(5)
          d.implicitly_wait(5)
          d(resourceId="com.autel.explorer:id/tv_logout", text=u"Logout", className="android.widget.TextView").click_exists(5)
          d.implicitly_wait(10)
          d(resourceId="com.autel.explorer:id/tv_ok", text=u"OK", className="android.widget.TextView").click_exists(5)
          time.sleep(5)
          intoPerCenter()
          d(resourceId="com.autel.explorer:id/tv_register", text=u"Register", className="android.widget.TextView").click_exists(5)
    #己在注册画面
    elif d(resourceId="com.autel.explorer:id/tv_register", text=u"Login", className="android.widget.TextView").exists(3):
        print('is in registration interface!')

#2-21,2-28 注册个人中心帐号
def test_RegisterUser2_21_28():
    RegisterUi2_1()
    d(resourceId="com.autel.explorer:id/ed_email", text=u"Email", className="android.widget.EditText").set_text('yxy2019@qq.com')
    d(resourceId="com.autel.explorer:id/ed_pwd", className="android.widget.EditText").set_text('abc123456')
    d(resourceId="com.autel.explorer:id/ed_repeat_pwd", className="android.widget.EditText").set_text('abc123456')
    d(resourceId="com.autel.explorer:id/btn_login", text=u"Register", className="android.widget.Button").click_exists(5)
    d.implicitly_wait(10)
    if d(resourceId="com.autel.explorer:id/tv_dlg_msg", text=u"Registration successful",
      className="android.widget.TextView").exists(3):
        print("Registration successful")
    elif d(resourceId="com.autel.explorer:id/tv_bottom", text=u"This email has been registered. Please re-enter.", className="android.widget.TextView").exists(3):
        print('已注册过该用户！')
    else:
        pass

#2-2.4 注册个人中心帐号_邮箱有误
def test_RegisterUser2_24():
    RegisterUi2_1()
    d(resourceId="com.autel.explorer:id/ed_email", text=u"Email", className="android.widget.EditText").set_text('yxy2019qq.com')
    d(resourceId="com.autel.explorer:id/ed_pwd", className="android.widget.EditText").set_text('abc123456')
    d(resourceId="com.autel.explorer:id/ed_repeat_pwd", className="android.widget.EditText").set_text('abc123456')
    d(resourceId="com.autel.explorer:id/btn_login", text=u"Register", className="android.widget.Button").click_exists(5)
    d.implicitly_wait(10)
    if d(resourceId="com.autel.explorer:id/tv_dlg_msg", text=u"Registration successful",
      className="android.widget.TextView").exists(3):
        print("Registration successful")
    elif d(resourceId="com.autel.explorer:id/tv_bottom", text=u"Please enter a valid email address.", className="android.widget.TextView").exists(3):
        print("Email Address format error!\n用例通过！")

#2-2.5 注册个人中心帐号_密码格式有误
def test_RegisterUser2_25():
    RegisterUi2_1()
    d.implicitly_wait(5)
    d(resourceId="com.autel.explorer:id/ed_email", text=u"Email", className="android.widget.EditText").set_text('yxy2019@qq.com')
    d(resourceId="com.autel.explorer:id/ed_pwd", className="android.widget.EditText").set_text('123456')
    d(resourceId="com.autel.explorer:id/ed_repeat_pwd", className="android.widget.EditText").set_text('123456')
    d(resourceId="com.autel.explorer:id/btn_login", text=u"Register", className="android.widget.Button").click_exists(5)
    d.implicitly_wait(10)
    if d(resourceId="com.autel.explorer:id/tv_dlg_msg", text=u"Registration successful",
      className="android.widget.TextView").exists(3):
        print("Registration successful")
    elif d(resourceId="com.autel.explorer:id/tv_bottom", text=u"Please enter a valid email address.", className="android.widget.TextView").exists(3):
        print("Email Address format error!")
    if d(resourceId="com.autel.explorer:id/tv_bottom", text=u"Your password must contain at least 1 letter and 1 number.", className="android.widget.TextView").exists(3):
        print('password format error!\n用例通过！')

#2-2.6 注册个人中心帐号_两次密码不一致
def test_RegisterUser2_26():
    RegisterUi2_1()
    d.implicitly_wait(5)
    d(resourceId="com.autel.explorer:id/ed_email", text=u"Email", className="android.widget.EditText").set_text('yxy2019@qq.com')
    d(resourceId="com.autel.explorer:id/ed_pwd", className="android.widget.EditText").set_text('abc123456')
    d(resourceId="com.autel.explorer:id/ed_repeat_pwd", className="android.widget.EditText").set_text('ab123456')
    d(resourceId="com.autel.explorer:id/btn_login", text=u"Register", className="android.widget.Button").click_exists(5)
    d.implicitly_wait(10)
    if d(resourceId="com.autel.explorer:id/tv_dlg_msg", text=u"Registration successful",
      className="android.widget.TextView").exists(3):
        print("Registration successful")
    elif d(resourceId="com.autel.explorer:id/tv_bottom", text=u"Please enter a valid email address.", className="android.widget.TextView").exists(3):
        print("Email Address format error!")
    elif d(resourceId="com.autel.explorer:id/tv_bottom", text=u"Your password must contain at least 1 letter and 1 number.", className="android.widget.TextView").exists(3):
        print('password format error!')
    elif d(resourceId="com.autel.explorer:id/tv_bottom", text=u"Passwords do not match, please re-enter.", className="android.widget.TextView").exists(3):
        print('input tow different password!\n用例通过！')

#2-2.7 注册个人中心帐号_邮箱被注册过
def test_RegisterUser2_27():
    RegisterUi2_1()
    d.implicitly_wait(5)
    d(resourceId="com.autel.explorer:id/ed_email", text=u"Email", className="android.widget.EditText").set_text('yxy2019@qq.com')
    d(resourceId="com.autel.explorer:id/ed_pwd", className="android.widget.EditText").set_text('abc123456')
    d(resourceId="com.autel.explorer:id/ed_repeat_pwd", className="android.widget.EditText").set_text('abc123456')
    d(resourceId="com.autel.explorer:id/btn_login", text=u"Register", className="android.widget.Button").click_exists(5)
    d.implicitly_wait(10)
    if d(resourceId="com.autel.explorer:id/tv_dlg_msg", text=u"Registration successful",
      className="android.widget.TextView").exists(3):
        print("Registration successful")
    elif d(resourceId="com.autel.explorer:id/tv_bottom", text=u"Please enter a valid email address.", className="android.widget.TextView").exists(3):
        print("Email Address format error!")
    elif d(resourceId="com.autel.explorer:id/tv_bottom", text=u"Your password must contain at least 1 letter and 1 number.", className="android.widget.TextView").exists(3):
        print('password format error!')
    elif d(resourceId="com.autel.explorer:id/tv_bottom", text=u"Passwords do not match, please re-enter.", className="android.widget.TextView").exists(3):
        print('input tow different passwords')
    elif d(resourceId="com.autel.explorer:id/tv_bottom", text=u"This email has been registered. Please re-enter.", className="android.widget.TextView").exists(3):
        print('邮箱已通注册过\n用例通过！')

#2-41,2-48 正常登录个人中心
def test_login2_4148():
    login('yxy2019@qq.com','abc123456')

#2-45 登录个人中心,无效邮箱
def test_login2_45():
    login('yxy2019qq.com', 'abc123456')

    if d(resourceId="com.autel.explorer:id/tv_bottom", text=u"Please enter a valid email address.",
      className="android.widget.TextView").exists(3):
        print('无效邮箱不能登录，用例通过！')
    time.sleep(1)
    d(resourceId="com.autel.explorer:id/iv_back").click_exists(5)

#2-46 未注册邮箱登录
def test_login2_46():
    login('yxy2018@qq.com', 'abc123456')

    if d(resourceId="com.autel.explorer:id/tv_bottom", text=u"This email has not been registered with Autel.", className="android.widget.TextView").exists(3):
        print('未注册邮箱不能登录，用例通过！')

#2-47 错误密码登录
def test_login2_47():
    login('yxy2019@qq.com', 'abc12345')
    # d(resourceId="com.autel.explorer:id/ed_email", text=u"yxy2019@qq.com", className="android.widget.EditText").set_text('yxy2019@qq.com')
    # d(resourceId="com.autel.explorer:id/ed_pwd", className="android.widget.EditText").set_text('abc12345')
    # d(resourceId="com.autel.explorer:id/btn_login", text=u"Login", className="android.widget.Button").click_exists(5)
    # time.sleep(5)
    if d(resourceId="com.autel.explorer:id/tv_bottom", text=u"Your email or password was incorrect. Please try again.", className="android.widget.TextView").exists(3):
        print('邮箱或密码错误，用例通过！')

#2-5.1     2.57正常找回密码
def test_findPwd2_51_57():
    intoForgetPwd()
    d(resourceId="com.autel.explorer:id/et_email", text=u"Email", className="android.widget.EditText").set_text('yxy2019@qq.com')
    d.implicitly_wait(5.0)
    d(resourceId="com.autel.explorer:id/btn_send_email").click_exists(5)
    time.sleep(5)
    d(resourceId="com.autel.explorer:id/iv_common_back").click_exists(5)
    d.implicitly_wait(5.0)
    d(resourceId="com.autel.explorer:id/iv_back").click_exists(5)

#2-5.5输入错误邮箱找回密码
def test_findPwd2_55():
    intoForgetPwd()
    d(resourceId="com.autel.explorer:id/et_email", text=u"Email", className="android.widget.EditText").set_text(
        'yxy2019qq.com')
    d.implicitly_wait(5.0)
    d(resourceId="com.autel.explorer:id/btn_send_email", text=u"Send a Verification Email",
      className="android.widget.Button").click_exists(5)
    time.sleep(0.5)
    if d.xpath("//*[contains(@text,'valid email')]").exists:
        # texttoast=d.xpath("//*[contains(@text,'Please entert')]").get_text
        # print(texttoast)

        d.toast.show('Hello Peter! You have caught a toast!',2.0)
    time.sleep(4)
    d(resourceId="com.autel.explorer:id/iv_common_back").click_exists(5)
    d.implicitly_wait(5.0)
    d(resourceId="com.autel.explorer:id/iv_back").click_exists(5)


#2-5.6 输入未注册邮箱找回密码
def test_findPwd2_56():
    intoForgetPwd()
    d(resourceId="com.autel.explorer:id/et_email", text=u"Email", className="android.widget.EditText").set_text(
        'yxy2018@qq.com')
    d(resourceId="com.autel.explorer:id/btn_send_email", text=u"Send a Verification Email",
      className="android.widget.Button").click_exists(5)
    time.sleep(4)
    d(resourceId="com.autel.explorer:id/iv_common_back").click_exists(5)
    d.implicitly_wait(5.0)
    d(resourceId="com.autel.explorer:id/iv_back").click_exists(5)

#3-1 3-2  3-3 3-4 个人中心界面检查
def test_PercenterUiCheck3_1234():
    goStart()
    d(resourceId="com.autel.explorer:id/iv_user_icon").click_exists(5)
    d(resourceId="com.autel.explorer:id/iv_user_photo").click_exists(5)
    time.sleep(5)
    d(resourceId="com.autel.explorer:id/iv_common_back").click_exists(5)
    time.sleep(5)
    d(resourceId="com.autel.explorer:id/tv_item_content").click_exists(5)
    time.sleep(10)
    d(resourceId="com.autel.explorer:id/flight_record_back").click_exists(5)
    time.sleep(5)
    d(resourceId="com.autel.explorer:id/tv_item_content", text=u"My Devices").click_exists(5)
    time.sleep(0.5)
    d(resourceId="com.autel.explorer:id/iv_common_back").click_exists(5)
    time.sleep(0.5)

    d.click(0.3,0.5)

#4-1 进入个人信息
def intoPerInfo():
    loginifnotlogin('yxy2019@qq.com', 'abc123456')
    d.implicitly_wait(3)
    if d(resourceId="com.autel.explorer:id/iv_user_icon").exists(3):
        d(resourceId="com.autel.explorer:id/iv_user_icon").click_exists(5)
    else:
        d(resourceId="com.autel.explorer:id/iv_user_icon_default").click_exists(5)

    time.sleep(0.5)
    d(resourceId="com.autel.explorer:id/iv_user_photo").click_exists(5)

'''设置我的头像区域，app弹出相册，拍照两种获取头像方式 '''
#4-2.1 点击头像app弹出相册，拍照两种获取头像方式
def PerInfoClickicon():
    goStart()
    intoPerInfo()
    d(resourceId="com.autel.explorer:id/iv_user_info_photo", className="android.widget.ImageView").click_exists(5)
    time.sleep(1)
    if d(resourceId="com.autel.explorer:id/tv_album", text=u"Album", className="android.widget.TextView").exists(3) and \
        d(resourceId="com.autel.explorer:id/tv_take_photo", text=u"Take a photo", className="android.widget.TextView").exists(3):
        print('点击个人中心用户头像图标，有弹出相册，拍照获取头像两种方式，用例通过！')
    d.click(0.5,0.5)
    d(resourceId="com.autel.explorer:id/iv_common_back").click_exists(5)
    time.sleep(0.5)
    d.click(0.3, 0.5)

#从手机相册选取照片
def selectPhoto():
    d(resourceId="com.android.documentsui:id/icon_thumb").click_exists(5)
    d(resourceId="com.google.android.apps.photos:id/cpe_save_button").click_exists(5)
    time.sleep(5)


#从手机相机拍照
def takePhoto():
    d(resourceId="com.autel.explorer:id/tv_take_photo", text=u"Take a photo",
      className="android.widget.TextView").click_exists(5)
    d(resourceId="com.google.android.GoogleCamera:id/shutter_button").click_exists(5)
    time.sleep(1.5)

    d(resourceId="com.google.android.GoogleCamera:id/shutter_button").click_exists(5)
    d(resourceId="com.google.android.apps.photos:id/cpe_save_button").click_exists(8)
    time.sleep(5)


#4-2.4 有网时点击头像从相册选择
def PerInfoClickiconfromAlbum4_24():
    goStart()
    intoPerInfo()
    d(resourceId="com.autel.explorer:id/iv_user_info_photo", className="android.widget.ImageView").click_exists(5)
    d(resourceId="com.autel.explorer:id/tv_album").click_exists(5)

    selectPhoto()

    time.sleep(10)



    print('从相册选择头像完成，用例完成！')

    d(resourceId="com.autel.explorer:id/iv_common_back").click_exists(5)
    print('back to outside.')
    time.sleep(1.5)
    d(resourceId="com.autel.explorer:id/iv_user_photo").exists(5)
    time.sleep(1.5)
    d.click(0.3, 0.5)




#4-2.7. 有网时点击头像从相机拍照
def PerInfoClickiconfromCam4_27():
    goStart()
    intoPerInfo()
    d(resourceId="com.autel.explorer:id/iv_user_info_photo", className="android.widget.ImageView").click_exists(5)
    time.sleep(1)

    d(resourceId="com.autel.explorer:id/tv_take_photo", text=u"Take a photo", className="android.widget.TextView").click_exists(5)



    takePhoto()

    time.sleep(10)




    print('从相机拍摄选择头像完成，用例完成！')
    d(resourceId="com.autel.explorer:id/iv_common_back").click_exists(5)
    time.sleep(0.5)
    d.click(0.3, 0.5)


'''修改用户名'''

#4-3.5 修改用户名
def test_ModifyName4_35():
    for name in ['goulun2','diaodiao','goulun123','23243goulun','adb cdfd','pu mei232','goulun123456789012345678901234567890','goulun2']:
        modifyUserName(name)
        time.sleep(5)
    d(resourceId="com.autel.explorer:id/iv_common_back").click_exists(5)
    time.sleep(0.5)
    d.click(0.3, 0.5)


#4.-4.5 #修改性别
def test_ModifyGender4_45():
    for sex in ['Female','Male','Private']:
        modifyGender(sex)
        if d(resourceId="com.autel.explorer:id/tv_right_content", className="android.widget.TextView")[1].get_text() == sex:
            print('性别设置成功，用例执行成功')
        else:
            print('性别设置失败，用例执行失败')

#4_5.5 设置国家
def test_ModifyCountry4_55():
    for country in ['Vietnam','Oman','Palau','Myanmar','Kenya','Mali']:
        modifyCountry(country)
        print('%s set!'%country)
        time.sleep(3)
    d.implicitly_wait(5.0)
    d(resourceId="com.autel.explorer:id/iv_common_back").click_exists(5)
    time.sleep(0.5)
    d.click(0.3, 0.5)

#5-2立即购买
def test_buyRightnow():
    goStart()
    # loginifnotlogin('yxy2019@qq.com', 'abc123456')

    if d(resourceId="com.autel.explorer:id/tv_common_title").exists(3):
        print('is at My Devices')
    elif d(resourceId="com.autel.explorer:id/tv_autel_home_start").exists(3):
        loginifnotlogin('yxy2019@qq.com', 'abc123456')
        time.sleep(0.5)
        if d(resourceId="com.autel.explorer:id/iv_user_icon_default").exists(3):
            d(resourceId="com.autel.explorer:id/iv_user_icon_default").click_exists(5)
        else:
            d(resourceId="com.autel.explorer:id/iv_user_icon").click_exists(5)
        # time.sleep(1)
        time.sleep(0.5)
        d.implicitly_wait(5)
        d(resourceId="com.autel.explorer:id/tv_item_content", text=u"My Devices").click_exists(5)
    d.implicitly_wait(4)
    d(resourceId="com.autel.explorer:id/stv_purchase").click_exists(5)
    time.sleep(8)
    d.press('home')
    time.sleep(5)

    if d(text=u"Autel Explorer").exists(3):
        d(text=u"Autel Explorer").click_exists(5)
    else:
        i = 0
        while i <= 5:
            d.swipe(0.8,0.7,0.15,0.7)
            time.sleep(0.8)
            if d(text=u"Autel Explorer").exists(3):
                d(text=u"Autel Explorer").click_exists(5)
                break
            i +=1
            j = 0
            while j <= 5:
                d.swipe(0.8, 0.7, 0.15, 0.7)
                time.sleep(0.8)
                if d(text=u"Autel Explorer").exists(3):
                    d(text=u"Autel Explorer").click_exists(5)
                    break
    time.sleep(3)
    d(resourceId="com.autel.explorer:id/iv_common_back").click_exists(5)
    time.sleep(0.5)
    d.click(0.3,0.5)




# test_outPerCenter1_2()
# test_inoutPerCenter1_3()
# test_RegisterUser2_21_28()
# test_RegisterUser2_24()
# test_RegisterUser2_25()
# test_RegisterUser2_26()
# test_RegisterUser2_27()
# test_login2_4148()

# test_login2_45()

# test_login2_46()
# test_login2_47()
# intoForgetPwd()
# test_findPwd2_51_57()
# test_findPwd2_54()
# test_findPwd2_56()
# login('147258369@qq.com','a123456')
# goStart()
# intoPerInfo()
# PerInfoClickicon()
# PerInfoClickiconfromAlbum()
# PerInfoClickiconfromCam4_27()
# test_ModifyName4_35()
# test_ModifyGender4_45()

# modifyCountry('Albania')
# modifyCountry('Oman')
# test_ModifyGender4_45()
# test_ModifyCountry4_55()
# test_buyRightnow()
# test_PercenterUiCheck3_1234()

i = 0
while True:
    d.set_fastinput_ime(True)
    i = i + 1



    # GroundStationTest
    # codeLock

    print("\n第", i, '次运行开始\n--------------------------------------------------------------------------')
    print(datetime.datetime.now())

    print('\n-1 进入个人中心')
    test_intoPerCenter1_1()
    time.sleep(5)

    print('\n1-2 退出个人中心')
    test_outPerCenter1_2()
    time.sleep(5)

    print('\n1-3 进出个人中心10次')
    test_inoutPerCenter1_3()
    time.sleep(5)

    print('\n2-1 进入个人中心注册界面')
    RegisterUi2_1()
    time.sleep(5)

    print('\n2-21,2-28 注册个人中心帐号')
    test_RegisterUser2_21_28()
    time.sleep(5)

    print('\n2-2.4 注册个人中心帐号_邮箱有误')
    test_RegisterUser2_24()
    time.sleep(5)

    print('\n2-2.5 注册个人中心帐号_密码格式有误')
    test_RegisterUser2_25()
    time.sleep(5)

    print('\n2-2.6 注册个人中心帐号_两次密码不一致')
    test_RegisterUser2_26()
    time.sleep(5)

    print('\n2-2.7 注册个人中心帐号_邮箱被注册过')
    test_RegisterUser2_27()
    time.sleep(5)

    print('\n 2-41,2-48 正常登录个人中心')
    test_login2_4148()
    time.sleep(5)

    print('\n2-45 登录个人中心,无效邮箱')
    test_login2_45()
    time.sleep(5)

    print('\n2-46 未注册邮箱登录')
    test_login2_46()
    time.sleep(5)

    print('\n2-47 错误密码登录')
    test_login2_47()
    time.sleep(5)

    print('\n2-5.1   2.5.7正常找回密码')
    test_findPwd2_51_57()
    time.sleep(5)

    print('\n2-5.5输入错误邮箱找回密码')
    test_findPwd2_55()
    time.sleep(5)

    print('\n2-5.6 输入未注册邮箱找回密码')
    test_findPwd2_56()
    time.sleep(5)

    loginifnotlogin('yxy2019@qq.com','abc123456')

    # print('\n3-1 3-2  3-3 3-4 个人中心界面检查')
    # test_PercenterUiCheck3_1234()
    # time.sleep(5)


    # print('\n4-1 进入个人信息')
    # intoPerInfo()
    # time.sleep(1)
    # d(resourceId="com.autel.explorer:id/iv_common_back").click_exists(5)
    # time.sleep(0.8)
    # d.click(0.3,0.5)
    # time.sleep(5)
  


    print('\n4-2.1 点击头像区域，app弹出相册，拍照两种获取头像方式')
    PerInfoClickicon()
    time.sleep(5)


    print('\n4-2.4 有网时点击头像从相册选择')
    PerInfoClickiconfromAlbum4_24()
    time.sleep(5)



    print('\n4-2.7. 有网时点击头像从相机拍照')
    PerInfoClickiconfromCam4_27()
    time.sleep(5)


    print('\n4-3.5 修改用户名')
    test_ModifyName4_35()
    time.sleep(5)

    print('\n4.-4.5 #修改性别')
    test_ModifyGender4_45()
    time.sleep(5)

    print('\n4_5.5 设置国家')
    test_ModifyCountry4_55()
    time.sleep(5)

    print('\n5-2立即购买')
    test_buyRightnow()
    time.sleep(5)


    print("\n第", i, '次运行结束\n--------------------------------------------------------------------------')
    print(datetime.datetime.now())