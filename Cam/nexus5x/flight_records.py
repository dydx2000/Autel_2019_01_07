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
def swipe_leftUp(): #左侧上滑
    d.swipe(0.14,0.7,0.14,0.3)

#进入飞行记录界面
def intoflyrecords():
    #在个人中心
    if d(resourceId="com.autel.explorer:id/tv_item_content",text='Flight Records').exists():
        d(resourceId="com.autel.explorer:id/tv_item_content").click()
        time.sleep(6)
     #在飞行记录界面
    elif    d(resourceId="com.autel.explorer:id/flight_record_collect_img").exists():
        print('already in flight records interface.')
    #在首页
    elif   d(resourceId="com.autel.explorer:id/tv_autel_home_start").exists():
        d(resourceId="com.autel.explorer:id/iv_user_icon").click()
        d.implicitly_wait(5)
        d(resourceId="com.autel.explorer:id/tv_item_content",text='Flight Records').click()
        time.sleep(6)
     #在各飞行界面
    elif d(resourceId="com.autel.explorer:id/rl_left").exists():
        d(resourceId="com.autel.explorer:id/rl_left").click()
        time.sleep(2)
        d(resourceId="com.autel.explorer:id/iv_user_icon").click()
        d.implicitly_wait(5)
        d(resourceId="com.autel.explorer:id/tv_item_content", text='Flight Records').click()
        time.sleep(6)
     #在设置界面
    elif d(resourceId="com.autel.explorer:id/tv_setting_title").exists():
        d(resourceId="com.autel.explorer:id/iv_setting_close").click()
        time.sleep(1)
        d(resourceId="com.autel.explorer:id/rl_left").click()
        time.sleep(2)
        d(resourceId="com.autel.explorer:id/iv_user_icon").click()
        d.implicitly_wait(5)
        d(resourceId="com.autel.explorer:id/tv_item_content", text='Flight Records').click()
        time.sleep(6)
    else:
        pass

def  intoSettings():
    #在设置界面
    if d(resourceId="com.autel.explorer:id/tv_setting_title").exists():
        print('is in settings')
        time.sleep(0.5)
    #在各飞行界面
    elif d(resourceId="com.autel.explorer:id/rl_left").exists():
        d(resourceId="com.autel.explorer:id/rl_setting").click()
        time.sleep(2)
    #在首页
    elif d(resourceId="com.autel.explorer:id/tv_autel_home_start").exists():
        d(resourceId="com.autel.explorer:id/tv_autel_home_start").click()
        time.sleep(6)
        d(resourceId="com.autel.explorer:id/rl_setting").click()
        time.sleep(1)
    #在飞行记录画面
    elif d(resourceId="com.autel.explorer:id/flight_record_cloud").exists():
        d(resourceId="com.autel.explorer:id/flight_record_back").click()
        time.sleep(1)
        d.click(0.3,0.5)
        time.sleep(1)
        d(resourceId="com.autel.explorer:id/tv_autel_home_start").click()
        time.sleep(3)
        d(resourceId="com.autel.explorer:id/rl_setting").click()
        time.sleep(1)
    else:
        pass

def  setUits(num):
    intoSettings()
    swipe_leftUp()
    time.sleep(0.5)
    d(resourceId="com.autel.explorer:id/tv_aircraft_settings_item_title", text=u"General").click()
    time.sleep(0.5)

    if num  == d(resourceId="com.autel.explorer:id/tv_item_arrow_text_state").get_text():
        print('%s is already set'%num)
    else:
        d(resourceId="com.autel.explorer:id/tv_item_arrow_text_title").click()
        if num =='Metric (km/h)':
            d(resourceId="com.autel.explorer:id/tv_item_value").click()
        elif num =='Metric (m/s)':
            d(resourceId="com.autel.explorer:id/tv_item_value", text=u"Metric (m/s)").click()
        elif num =='Imperial (mph)':
            d(resourceId="com.autel.explorer:id/tv_item_value", text=u"Imperial (mph)").click()
        else:
            print('inupt a wrong parameer!')
            d(resourceId="com.autel.explorer:id/iv_setting_close").click()



# 1 -1.2进入飞行记录界面
def test_intoflyrecords1_12():
    intoflyrecords()
    time.sleep(5)
    d(resourceId="com.autel.explorer:id/flight_record_back").click()
    time.sleep(1)
    d.click(0.3,0.5)


#4 -3更改测量单位
def test_changeflyrecordUnits4_3():
    for unit in ['Metric (m/s)','Imperial (mph)']:
        setUits(unit)
        intoflyrecords()
        textunit=d(resourceId="com.autel.explorer:id/flight_record_item_max_height").get_text()
        print(textunit[-1:])
        if textunit[-1:] == 'm':
            print('change Unit to Metric successfully')
        elif textunit[-1:] =='t':
            print('change Unit to Imperial successfully')
        else:
            print('set unit error')
        time.sleep(5)

#6-1.1 查看没有拍照的飞行记录
def test_flyrecordsNophoto6_11():
    intoflyrecords()
    photoNum=d(className="android.widget.ImageView", instance=17).right(resourceId="com.autel.explorer:id/flight_record_item_pic_num" ).get_text()
    if photoNum == '0':
        print('此记录照片数量为0,用例通过')
    # if d(resourceId="com.autel.explorer:id/flight_record_item_record_layout").right(resourceId="com.autel.explorer:id/flight_record_photo"):
    #     print('这条记录有照片缩略图，用例不通过')
    # else:
    #     print('这条记录有照片缩略图，用例通过')

#6-1.2.3 切换照片
def test_flyreordsViewPhoto6_123():
    intoflyrecords()
    d(resourceId="com.autel.explorer:id/flight_record_photo").click()
    time.sleep(1)
    i = 0
    while i <= 5:
        d.swipe(0.8,0.5,0.2,0.05)
        time.sleep(0.5)
        seq=d(resourceId="com.autel.explorer:id/mcustom_page_text").get_text()
        list1= seq.split('/')
        print(list1)
        if list1[0]==list1[1]:
            time.sleep(0.5)
            break
        i += 1

    i = 0
    while i <= 5:
        d.swipe(0.2,0.5,0.8,0.5)
        time.sleep(0.5)
        seq=d(resourceId="com.autel.explorer:id/mcustom_page_text").get_text()
        list1= seq.split('/')
        print(list1)
        if list1[0]=='1':
            time.sleep(0.5)
            break
        i += 1
    d.press('back')

#7-2.1 收藏
def test_favorrecords7_23():
    intoflyrecords()
    d(resourceId="com.autel.explorer:id/flight_record_collect_img", className="android.widget.ImageView", instance=1).click()
    time.sleep(2)
    d(resourceId="com.autel.explorer:id/flight_record_collect_img", className="android.widget.ImageView", instance=1).click()
    time.sleep(2)
    d(resourceId="com.autel.explorer:id/flight_record_collect_img", className="android.widget.ImageView", instance=1).click()
    time.sleep(2)
    d(resourceId="com.autel.explorer:id/flight_record_collect_img", className="android.widget.ImageView", instance=1).click()
    time.sleep(1)
    test.goStart()


print('\n登录预设账号')
test.login('147258369@qq.com','a123456')
i = 0
while True:
    i = i+1

    print("\n第", i , '次运行开始\n--------------------------------------------------------------------------')
    print(datetime.datetime.now())


    print('\n1 -1.2进入飞行记录界面')
    intoflyrecords()
    time.sleep(2)

    print('\n4 -3更改测量单位')
    test_changeflyrecordUnits4_3()
    time.sleep(2)

    print('\n6-1.1 查看没有拍照的飞行记录')
    test_flyrecordsNophoto6_11()
    time.sleep(2)

    print('\n6-1.2.3 切换照片')
    test_flyreordsViewPhoto6_123()
    time.sleep(2)

    print('\n7-2.1 收藏')
    test_favorrecords7_23()
    time.sleep(2)



    print("\n第", i, '次运行结束\n--------------------------------------------------------------------------')
    print(datetime.datetime.now())