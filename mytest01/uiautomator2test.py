#coding:utf-8

import random
import uiautomator2 as u2
import time
pkg_name='com.autel.explorer'
# pkg_name='com.taobao.taobao'
d=u2.connect_wifi('192.168.1.12')
# d=u2.connect_usb('8f21c9ba')
# d=u2.connect_usb('12dd6e53')


d.app_start(pkg_name)
# d.wait_timeout = 30.0
time.sleep(3)
for i in range(1,11):
    # time.sleep(2)

    d(resourceId="com.autel.explorer:id/tv_autel_home_start").click_exists(timeout=5000)
    # d(resourceId="com.autel.explorer:id/tv_autel_home_start").click(timeout=5000)
    time.sleep(3)
    # d(resourceId="com.autel.explorer:id/tv_mode").exists(timeout=5000)
    d(resourceId="com.autel.explorer:id/tv_mode").click(timeout=5000)
    time.sleep(1)

    d(resourceId="com.autel.explorer:id/model_choice_bg").click()
    time.sleep(0.5)
    inst=random.randint(1,11)
    d(className="android.widget.ImageView", instance=11).click()
    time.sleep(0.5)
    # d(resourceId="com.autel.explorer:id/tv_aircraft_settings_item_title", text=u"飞控").click()
    time.sleep(1)
    a=random.randint(1,90)
    text=str(a)
    d(resourceId="com.autel.explorer:id/distance_cur_value_et").send_keys(text)
    d.press('enter')
    d(resourceId="com.autel.explorer:id/rb_standard").click()
    d(resourceId="com.autel.explorer:id/iv_setting_close").click()
    d(className="android.widget.ImageView", instance=5).click()
    time.sleep(2)
    print('Ran for %s times'%i)

# d.app_stop(pkg_name)


# d(className="android.widget.ImageView", instance=55).click()
# # d(className="android.widget.ImageView", instance=9).click
# d(className="android.view.View", instance=4).click()
# d(className="android.widget.ImageView", instance=11).click()
# d(resourceId="com.taobao.taobao:id/rate_favor_icon").click()


# # print(d.info)
# d(resourceId='com.autel.explorer:id/tv_autel_home_start').click()
# # time.sleep(2)
# # d(resourceId="com.autel.explorer:id/tv_mode").wait(exists=4)
# d(text='未连接').click()

# d(className="android.widget.ImageView", instance=11).wait(timeout=4)
# d(className="android.widget.ImageView", instance=11).click()
# d.click(0.942, 0.046)
# d(resourceId="com.autel.explorer:id/tv_aircraft_settings_item_title", text=u"飞控").click()
# d(resourceId="com.autel.explorer:id/distance_cur_value_et").set_text('40')
# d.press('enter')
#
#
# d(resourceId="com.autel.explorer:id/rb_standard").click()
#d(resourceId="com.autel.explorer:id/iv_setting_close").click()
'''
'''


# d(resourceId="com.autel.explorer:id/iv_user_icon_default").click()  #登录
# d(resourceId="com.autel.explorer:id/ed_email").send_keys('abc123@qq.com')
# d(resourceId="com.autel.explorer:id/ed_pwd").send_keys('abc123456')
# d(resourceId="com.autel.explorer:id/btn_login").click()


#
# # d(resourceId="com.autel.explorer:id/iv_user_icon_default")
# d(resourceId="com.autel.explorer:id/iv_user_icon_default").click()  #注册
# d(resourceId="com.autel.explorer:id/tv_register").click()
# d(resourceId="com.autel.explorer:id/ed_email").send_keys('abc123@qq.com')
# d(resourceId="com.autel.explorer:id/ed_pwd").send_keys('abc123456')
# d(resourceId="com.autel.explorer:id/ed_repeat_pwd").send_keys('abc123456')
# d(resourceId="com.autel.explorer:id/btn_login").click()
#
# d.app_stop(pkg_name)




