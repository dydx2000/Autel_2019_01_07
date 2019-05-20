# conding:utf-8
import uiautomator2 as u2
import time
import datetime
from PIL import Image
import logging
import Cam.nexus5x.uiautomator2_cam_shots_filter as uiauto
test = uiauto.Camera()

logging.basicConfig(level=logging.INFO,
                    format="\n%(asctime)s %(filename)s   line:%(lineno)d  %(levelname)s  %(funcName)s %(message)s",
                    datefmt='%Y %m %d %H:%M:%S',
                    filename='CamShots_'+time.strftime("%Y-%m-%d_%H_%M_%S")+".log",
                    filemode='a')

logger = logging.getLogger(__name__)
d = uiauto.d
# pkg_name = 'com.autel.explorer'
# d = u2.connect_wifi('192.168.1.105')

# d.wait_timeout = 30.0
time.sleep(1)
# d.implicitly_wait(10.0)


class ParaError(Exception):
    pass
    # print("Parameter input error")

class SwitchError(Exception):
    pass
    # print("Switch windows Error!")

####----------------------------------------------飞控设置界面----------------------------------------------####
def flyControlSet():
    # 已经在设置界面
    if d(resourceId="com.autel.explorer:id/tv_setting_title").exists(3):
        print('is  in settings!')
    # 在开始界面
    elif d(resourceId="com.autel.explorer:id/tv_autel_home_start").exists(3):
        d(resourceId="com.autel.explorer:id/tv_autel_home_start").click_exists(5)
        time.sleep(5)
        d(resourceId="com.autel.explorer:id/rl_setting").click_exists(5)
        time.sleep(0.5)
    # 在地图界面
    elif d(resourceId="com.autel.explorer:id/compass_iv").exists(3):
        d(resourceId="com.autel.explorer:id/rl_setting").click_exists(5)
        time.sleep(0.5)
    # 在媒体拍摄界面
    elif d(resourceId="com.autel.explorer:id/iv_camera_outer").exists(3):
        d(resourceId="com.autel.explorer:id/rl_setting").click_exists(5)
        time.sleep(0.5)
    # 在各智能飞行界面
    elif d(resourceId="com.autel.explorer:id/rl_left").exists(3):
        d(resourceId="com.autel.explorer:id/rl_setting").click_exists(5)
        time.sleep(0.5)
    # 在智能飞行选择界面
    elif d(text=u"Intelligent Flight").exists(3):
        d(resourceId="com.autel.explorer:id/layout_cancel").click_exists(5)
        time.sleep(0.5)
        d(resourceId="com.autel.explorer:id/rl_setting").click_exists(5)
    # 在VR模式界面
    elif d(resourceId="com.autel.explorer:id/iv_vr_settings").exists(3):
        d(resourceId="com.autel.explorer:id/iv_back").click_exists(5)
        time.sleep(2)
        d(resourceId="com.autel.explorer:id/tv_autel_home_start").click_exists(5)
        time.sleep(5)
        d(resourceId="com.autel.explorer:id/rl_setting").click_exists(5)
    else:
        pass


####----------------------------------------------地图界面----------------------------------------------####
'''   1-2  地图手动放大、缩小   '''
def fangdasuoxiaoMap1_2():
    logging.info("function start")

    test.SwitchtoCaptureMode()
    d.implicitly_wait(10)

    try:
        d(resourceId="com.autel.explorer:id/map_dragmarkerontouchlayer").click_exists(5)
        time.sleep(2)
        d().gesture((0.331, 0.694),(0.726, 0.329),(0.46, 0.555),(0.567, 0.457))
        time.sleep(1)
        if d(resourceId="com.autel.explorer:id/scale_text").exists:
            pass
        else:
            print('未显示比例尺')
        time.sleep(3)
        if d(resourceId="com.autel.explorer:id/scale_text").exists:
            print('缩小地图比例尺未消失')
        else:
            pass
        d().gesture( (0.46, 0.555), (0.567, 0.457),(0.331, 0.694), (0.726, 0.329))
        time.sleep(1)
        if d(resourceId="com.autel.explorer:id/scale_text").exists(3):
            pass
        else:
            print('未显示比例尺')
        time.sleep(3)
        if d(resourceId="com.autel.explorer:id/scale_text").exists(3):
            print('放大地图比例尺未消失')
        else:
            pass
    except:
        test.catchError()

    logging.info("function ends")


'''   1-4  顶部栏信息显示   '''
def topmessageMap1_4():
    logging.info("function start")

    test.SwitchtoCaptureMode()

    try:
        if d(resourceId="com.autel.explorer:id/rl_left").exists(3):
            pass
        else:
            print('返回首页消失')
        if d(resourceId="com.autel.explorer:id/rl_mode").exists(3):
            pass
        else:
            print('飞行模式消失')
        if d(resourceId="com.autel.explorer:id/tv_battery").exists(3):
            text = d(resourceId="com.autel.explorer:id/tv_battery").get_text()
            print(text)
        else:
            print('电池电量消失')
        if d(resourceId="com.autel.explorer:id/rl_altitude").exists(3):
            text = d(resourceId="com.autel.explorer:id/tv_altitude").get_text()
            print(text)
        else:
            print('当前高度消失')
        if d(resourceId="com.autel.explorer:id/rl_distance").exists(3):
            text = d(resourceId="com.autel.explorer:id/tv_distance").get_text()
            print(text)
        else:
            print('当前距离消失')
        if d(resourceId="com.autel.explorer:id/rl_speed").exists(3):
            text = d(resourceId="com.autel.explorer:id/tv_speed").get_text()
            print(text)
        else:
            print('当前速度消失')
    except:
        test.catchError()

    logging.info("function ends")

'''   1-5  右侧功能显示   '''
def rightfunctionMap1_5():
    logging.info("function start")

    test.SwitchtoCaptureMode()

    try:
        d(resourceId="com.autel.explorer:id/map_dragmarkerontouchlayer").click_exists(5)
        time.sleep(2)
        if d(resourceId="com.autel.explorer:id/compass_iv").exists(3):
            pass
        else:
            print('地图朝向锁定丢失')
        if d(resourceId="com.autel.explorer:id/location_iv").exists(3):
            pass
        else:
            print('快速定位丢失')
        if d(resourceId="com.autel.explorer:id/map_type_change_iv").exists(3):
            pass
        else:
            print('地图设置丢失')
        if d(resourceId="com.autel.explorer:id/find_my_drone_iv").exists(3):
            pass
        else:
            print('找飞机功能丢失')
    except:
        test.catchError()

    logging.info("function ends")

'''   2-1  地图朝向锁定   '''
def directionMap2_1():
    logging.info("function start")

    test.SwitchtoCaptureMode()

    try:
        d(resourceId="com.autel.explorer:id/map_dragmarkerontouchlayer").click_exists(5)
        time.sleep(2)

        d.screenshot('screen.jpg')
        im = Image.open('screen.jpg')
        r, g, b = im.split()
        color = b.getpixel((0.942, 0.183))
        print(color)
        if color == 105:
            d(resourceId="com.autel.explorer:id/compass_iv").click_exists(5)
            print('地图锁定')
        else:
            d(resourceId="com.autel.explorer:id/compass_iv").click_exists(5)
            print('地图朝北')
    except:
        test.catchError()

    logging.info("function ends")

'''   3-1  地图模式   '''
def modeMap3_1():
    logging.info("function start")

    test.goStart()

    try:
        d(resourceId="com.autel.explorer:id/tv_autel_home_start").click_exists(5)
        time.sleep(4)
        d(resourceId="com.autel.explorer:id/map_dragmarkerontouchlayer").click_exists(5)
        d.implicitly_wait(10)
        d(resourceId="com.autel.explorer:id/map_type_change_iv").click_exists(5)
        d.implicitly_wait(5.0)
        d(resourceId="com.autel.explorer:id/map_normal_iv").click_exists(5)
        d.implicitly_wait(5.0)
        d(resourceId="com.autel.explorer:id/map_hybrid_iv").click_exists(5)
        d.implicitly_wait(5.0)
        d(resourceId="com.autel.explorer:id/map_gps_iv").click_exists(5)
        d.implicitly_wait(5.0)
        d(resourceId="com.autel.explorer:id/map_type_change_iv").click_exists(5)
        d.implicitly_wait(5.0)
    except:
        test.catchError()

    logging.info("function ends")

####----------------------------------------------智能飞行模式----------------------------------------------####
'''   4-1  智能飞行模式界面   '''
def flyMode4_1():                                                         #未添加个人中心、相册、直播模块

    logging.info("function start")

    try:
        # 在首页
        if d(resourceId="com.autel.explorer:id/tv_autel_home_start").exists(3):
            d(resourceId="com.autel.explorer:id/tv_autel_home_start").click_exists(5)
            time.sleep(4)
            d(resourceId="com.autel.explorer:id/rl_mode").click_exists(5)

        # 在拍照、录像界面
        elif d(resourceId="com.autel.explorer:id/iv_camera_outer").exists(3):
            d(resourceId="com.autel.explorer:id/rl_mode").click_exists(5)

        # 在地图界面
        elif d(resourceId="com.autel.explorer:id/compass_iv").exists(3):
            d(resourceId="com.autel.explorer:id/rl_mode").click_exists(5)

        # 在飞控设置界面
        elif d(resourceId="com.autel.explorer:id/tv_setting_title").exists(3):
            # d(resourceId="com.autel.explorer:id/iv_setting_close").click_exists(5)
            d.press("back")
            time.sleep(1)
            d(resourceId="com.autel.explorer:id/rl_mode").click_exists(5)

        # 在左侧飞行器状态界面
        elif d(resourceId="com.autel.explorer:id/warn_history_title_tv").exists(3):
            d.click(0.5,0.5)
            time.sleep(1)
            d(resourceId="com.autel.explorer:id/rl_mode").click_exists(5)

        # 在相机设置界面
        elif d(resourceId="com.autel.explorer:id/camera_general_setting_title"):
            d.click(0.45,0.45)
            time.sleep(1)
            d(resourceId="com.autel.explorer:id/rl_mode").click_exists(5)

        # 在VR界面
        elif d(resourceId="com.autel.explorer:id/iv_back"):
            d(resourceId="com.autel.explorer:id/iv_back").click_exists(5)
            time.sleep(10)
            if d(resourceId="com.autel.explorer:id/rl_left").exists(3):
                d(resourceId="com.autel.explorer:id/rl_left").click_exists(5)
                time.sleep(10)
            d(resourceId="com.autel.explorer:id/tv_autel_home_start").click_exists(5)
            time.sleep(6)
            d(resourceId="com.autel.explorer:id/rl_mode").click_exists(5)

        # 在飞行模式选择界面
        elif d(resourceId="com.autel.explorer:id/model_choice_bg"):
            print('已在智能飞行模式界面')
            pass

        #在其他飞行模式界面
        elif d(resourceId="com.autel.explorer:id/rl_mode").exists(3) and (not d(resourceId="com.autel.explorer:id/tv_mode", text=u"Standby", className="android.widget.TextView").exists(3)):
             d(resourceId="com.autel.explorer:id/rl_mode").click_exists(5)

        else:
            pass

        time.sleep(2)
    except:
        test.catchError()

    logging.info("function ends")


'''   0-1  追踪模式   '''
def DynamicTrackMode0_1():
    logging.info("function start")

    flyMode4_1()

    try:
        d(resourceId="com.autel.explorer:id/model_choice_txt", text=u"Dynamic Track").click_exists(5)
        time.sleep(1.5)
        d.implicitly_wait(5.0)
        if d(resourceId="com.autel.explorer:id/bottom_left_title").exists(3):
            d(resourceId="com.autel.explorer:id/bottom_left_title").click_exists(5)
            time.sleep(0.5)
            if d(resourceId="com.autel.explorer:id/iv_remote_control_right_stick").exists(3):
                d(resourceId="com.autel.explorer:id/bottom_right_title").click_exists(5)
            else:
                print('提示页面不完全')
        else:
            print('已在追踪模式下')
        time.sleep(3)
    except:
        test.catchError()

    logging.info("function ends")


'''   0-2  指点飞行模式   '''
def     ViewpointMode0_2():
    logging.info("function start")

    flyMode4_1()

    try:
        d(resourceId="com.autel.explorer:id/model_choice_txt", text=u"Viewpoint").click_exists(5)
        time.sleep(1.5)
        d.implicitly_wait(5.0)

        if d(resourceId="com.autel.explorer:id/bottom_left_title").exists(3):
            d(resourceId="com.autel.explorer:id/bottom_left_title").click_exists(5)
            time.sleep(1.5)
            if d(resourceId="com.autel.explorer:id/iv_remote_control_right_stick").exists(3):
                d(resourceId="com.autel.explorer:id/bottom_right_title").click_exists(5)
            else:
                print('提示页面不完全')
        else:
            print('已在指点飞行模式下')
        time.sleep(3)
    except:
        test.catchError()

    logging.info("function ends")


'''   0-3  环绕模式   '''
def OrbitMode0_3():
    logging.info("function start")

    flyMode4_1()

    try:
        d(resourceId="com.autel.explorer:id/model_choice_txt", text=u"Orbit").click_exists(5)
        # time.sleep(1.5)
        # d.implicitly_wait(5)
        if d(resourceId="com.autel.explorer:id/iv_mission_guidance_exit", className="android.widget.ImageView").exists(timeout=5):
            d(resourceId="com.autel.explorer:id/bottom_left_title").click_exists(3)
            # time.sleep(0.5)
            if d(className="android.widget.ImageView", instance=12).exists(timeout=5):
                d(resourceId="com.autel.explorer:id/bottom_left_title").click_exists(3)
                # time.sleep(0.5)
                if d(resourceId="com.autel.explorer:id/iv_remote_control_right_stick").exists(timeout=5):
                    d(resourceId="com.autel.explorer:id/bottom_right_title").click_exists(3)
                else:
                    print('提示页面不完全')
            else:
                print('提示页面不完全')
        else:
            print('已在环绕飞行模式下')
    except:
        test.catchError()

    time.sleep(3)

    logging.info("function ends")


'''   0-4  航点模式   '''
def WaypointMode0_4():
    logging.info("function start")

    flyMode4_1()
    time.sleep(1.5)

    try:
        d(resourceId="com.autel.explorer:id/model_choice_txt", text=u"Waypoint").click_exists(5)
        time.sleep(3)
        # d.implicitly_wait(5)
        # if d(resourceId="com.autel.explorer:id/iv_learning_center").exists(3):
        if d(resourceId="com.autel.explorer:id/iv_mission_guidance_exit").exists(3):
            d(resourceId="com.autel.explorer:id/bottom_left_title").click_exists(5)
            time.sleep(1.5)
            if d(className="android.widget.ImageView", instance=3).exists(3):
                d(resourceId="com.autel.explorer:id/bottom_left_title").click_exists(5)
                time.sleep(1.5)
                if d(resourceId="com.autel.explorer:id/iv_remote_control_right_stick").exists(3):
                    d(resourceId="com.autel.explorer:id/bottom_right_title").click_exists(5)
                    time.sleep(1.5)
                else:
                    print('提示页面不完全')
            else:
                print('提示页面不完全')
        else:
            print('已在指点飞行模式下')
        time.sleep(3)
    except:
        test.catchError()

    logging.info("function ends")


'''   0-5  VR模式   '''
def VRMode0_5():
    logging.info("function start")

    flyMode4_1()
    try:
        d(resourceId="com.autel.explorer:id/model_choice_txt", text=u"VR").click_exists(5)
        time.sleep(2)
        if d(resourceId="com.autel.explorer:id/iv_vr_settings").exists(3):
            print('已在VR模式下')
        else:
            print('未进入VR模式')
    except:
        test.catchError()

    logging.info("function ends")


'''   4-2  智能飞行模式项   '''
def choiceflyMode4_2():
    logging.info("function start")

    DynamicTrackMode0_1()
    time.sleep(1)
    OrbitMode0_3()
    time.sleep(1)
    WaypointMode0_4()
    time.sleep(1)
    VRMode0_5()
    time.sleep(1)
    ViewpointMode0_2()
    time.sleep(1)


    logging.info("function ends")

'''   5-2  简单环绕模式   '''
def simpleOrbitMode5_2():
    logging.info("function start")

    OrbitMode0_3()
    time.sleep(1.5)
    d.implicitly_wait(10)
    try:
        d(resourceId="com.autel.explorer:id/cl_mission_btn").click_exists(5)
    except:
        test.catchError()
    time.sleep(1)
    if d(resourceId="com.autel.explorer:id/iv_warn_toast").exists(3):
        pass
    else:
        print('缺少提示语')
    time.sleep(3)

    logging.info("function ends")


'''   5-4  简单环绕模式设置   '''
def simploOrbitMode5_4():
    logging.info("function start")

    OrbitMode0_3()

    try:
        d(className="android.widget.ImageView", instance=8).click_exists(5)
        time.sleep(1.5)
        d(resourceId="com.autel.explorer:id/rl_left").click_exists(5)
        time.sleep(2)
    except:
        test.catchError()

    logging.info("function ends")


#5-7 1 高级环绕，选择地图取点，会自动切换到地图
def advanceOrbitMode5_71():
    logging.info("function start")

    OrbitMode0_3()
    # d(className="android.widget.ImageView", instance=8).long_click()
    try:
        d(resourceId="com.autel.explorer:id/title_name_tv", text=u"Orbit", className="android.widget.TextView").right(className="android.widget.ImageView").long_click()
        time.sleep(0.5)
        # d.implicitly_wait(5)
        # d(className="android.view.ViewGroup", instance=8).click_exists(5)
        d(resourceId="com.autel.explorer:id/mission_drop_select_view").click_exists(5)
        # time.sleep(0.5)
        # d.implicitly_wait(5)
        d(resourceId="com.autel.explorer:id/mission_drop_item_title", text=u"Map Point").click_exists(5)
        # time.sleep(1)
        d(resourceId="com.autel.explorer:id/rl_left").click_exists(5)
        time.sleep(2)
    except:
        test.catchError()

    logging.info("function ends")


#5-72 高级环绕，地图取点，提示未选择兴趣点
def advanceOrbitMode5_72():
    logging.info("function start")

    OrbitMode0_3() #进入环绕界面，自动去除教程
    time.sleep(0.5)

    try:
        d(resourceId="com.autel.explorer:id/title_name_tv", text=u"Orbit", className="android.widget.TextView").right(
            className="android.widget.ImageView").long_click()

        d(resourceId="com.autel.explorer:id/mission_drop_select_view").click_exists(5)
        d(resourceId="com.autel.explorer:id/mission_drop_item_title", text=u"Map Point").click_exists(5)
        d(resourceId="com.autel.explorer:id/bottom_title").click_exists(5)
        if d(resourceId="com.autel.explorer:id/tv_warn_toast").exists(timeout=5):
            print('add a  center point,用例成功 ')
        d(resourceId="com.autel.explorer:id/rl_left").click_exists(5)
        time.sleep(2)
    except:
        test.catchError()

    logging.info("function ends")


#5-8 兴趣点参数设置

def advanceOrbitMode5_8():
    logging.info("function start")

    OrbitMode0_3()

    try:
        d(className="android.widget.ImageView", instance=8).long_click()
        time.sleep(1.5)

        d.implicitly_wait(5)
        d(className="android.view.ViewGroup", instance=8).click_exists(5)
        time.sleep(1.5)

        d.implicitly_wait(5)
        d(resourceId="com.autel.explorer:id/mission_drop_item_title", text=u"Map Point").click_exists(5)
        time.sleep(1.5)

        d(className="android.widget.ImageView", instance=10).long_click()
        d.click(0.3,0.5)
        d(resourceId="com.autel.explorer:id/bottom_title").click_exists(5)
        time.sleep(1.5)

        d(className="android.widget.ImageView", instance=10).long_click()
        time.sleep(1.5)

        d(resourceId="com.autel.explorer:id/mission_drop_item_title", text=u"CCW").click_exists(5)
        time.sleep(1.5)

        d(resourceId="com.autel.explorer:id/rl_left").click_exists(5)
        time.sleep(2)
    except:
        test.catchError()

    logging.info("function ends")


'''   7-1、7-2、7-5  执行智能追踪   '''
def runDTMode7_5():
    logging.info("function start")

    DynamicTrackMode0_1()
    try:
        d(resourceId="com.autel.explorer:id/orbit_position_select_one_tv").click_exists(5)                 #普通跟踪
        time.sleep(0.5)
        d(resourceId="com.autel.explorer:id/mission_drop_item_title").click_exists(5)
        time.sleep(0.5)
        d.click(0.5,0.5)
        time.sleep(2)
        d(resourceId="com.autel.explorer:id/dynamic_start").click_exists(5)
        time.sleep(0.5)
        if d(resourceId="com.autel.explorer:id/iv_warn_toast").exists(3):
            pass
            time.sleep(1)
        else:
            print('缺少提示信息')
        d(resourceId="com.autel.explorer:id/orbit_position_select_one_tv").click_exists(5)                 #三脚架跟踪
        time.sleep(0.5)
        d(resourceId="com.autel.explorer:id/mission_drop_item_title", text=u"Tripod").click_exists(5)
        time.sleep(0.5)
        d.click(0.5,0.5)
        time.sleep(2)
        d(resourceId="com.autel.explorer:id/dynamic_start").click_exists(5)
        time.sleep(1)
        if d(resourceId="com.autel.explorer:id/iv_warn_toast").exists(3):
            pass
            time.sleep(1)
        else:
            print('缺少提示信息')
        d(resourceId="com.autel.explorer:id/orbit_position_select_one_tv").click_exists(5)
        time.sleep(1.5)
        #平行跟踪
        d(resourceId="com.autel.explorer:id/mission_drop_item_title", text=u"Parallel").click_exists(5)
        time.sleep(0.5)
        d.click(0.5, 0.5)
        time.sleep(2)
        if d(resourceId="com.autel.explorer:id/edit_dg_content").exists(3):
            d(resourceId="com.autel.explorer:id/tv_ok").click_exists(5)
        else:
            print('缺少提示信息')
        time.sleep(1)
    except:
        test.catchError()

    logging.info("function ends")


#7-4视觉设置
def runDTMode7_4():
    logging.info("function start")

    DynamicTrackMode0_1()

    try:
        d(resourceId="com.autel.explorer:id/imageSetting").click_exists(5)
    except:
        test.catchError()

    logging.info("function ends")


'''   8-2  进入VR   '''
def intoVR8_2():
    logging.info("function start")

    flyMode4_1()

    try:
        d(resourceId="com.autel.explorer:id/model_choice_txt", text=u"VR").click_exists(5)
        time.sleep(1.5)
        if d(resourceId="com.autel.explorer:id/iv_vr_settings").exists(3):
            print('已进入VR')
        else:
            print('界面显示不完全')
    except:
        test.catchError()

    logging.info("function ends")


'''   8-3  退出VR   '''
def exitVR8_3():
    logging.info("function start")

    flyMode4_1()

    try:
        d(resourceId="com.autel.explorer:id/model_choice_txt", text=u"VR").click_exists(5)
        time.sleep(1)
        if d(resourceId="com.autel.explorer:id/iv_vr_settings").exists(3):
            print('已进入VR')
            d(resourceId="com.autel.explorer:id/iv_back").click_exists(5)
            time.sleep(2)
            if d(resourceId="com.autel.explorer:id/tv_autel_home_start").exists(3):
                print('正常退出')
            else:
                print('未退出')
        else:
            print('界面显示不完全')
    except:
        test.catchError()

    logging.info("function ends")


'''   10-1、10-2  VR参数设置   '''
def setVR10_1():
    logging.info("function start")

    intoVR8_2()

    try:
        d(resourceId="com.autel.explorer:id/iv_vr_settings").click_exists(5)
        time.sleep(0.5)
        d(resourceId="com.autel.explorer:id/iv_vrsettings_close").click_exists(5)
        time.sleep(0.5)
        if d(resourceId="com.autel.explorer:id/tv_title").exists(3):
            print('未退出VR设置')
        else:
            pass
        d(resourceId="com.autel.explorer:id/iv_vr_settings").click_exists(5)
        time.sleep(0.5)
        d(resourceId="com.autel.explorer:id/tv_item_arrow_text_title").click_exists(5)
        d.drag(0.292, 0.867,0.581, 0.867)
        time.sleep(0.5)
        d.drag(0.5, 0.758,0.499, 0.345)
        time.sleep(0.5)
        d.drag(0.581, 0.867,0.292, 0.867)
        time.sleep(0.5)
        d.drag(0.499, 0.345,0.5, 0.758)
        time.sleep(0.5)
        d(resourceId="com.autel.explorer:id/iv_back").click_exists(5)
        time.sleep(0.5)
        d(resourceId="com.autel.explorer:id/iv_back").click_exists(5)
    except:
        test.catchError()

    logging.info("function ends")


'''   10-3  VR云台模式   '''
def gimbalVR10_3():
    logging.info("function start")

    flyMode4_1()
    time.sleep(2)

    try:
        d(resourceId="com.autel.explorer:id/model_choice_txt", text=u"VR").click_exists(5)
        time.sleep(1)
        d(resourceId="com.autel.explorer:id/iv_vr_settings").click_exists(5)
        time.sleep(1)
        d.screenshot('screen.jpg')
        im = Image.open('screen.jpg')
        r ,g ,b = im.split()
        # x =im.size[0]*
        # y = im.size[1]*
        color = r.getpixel((737, 393))
        print(color)
        if color == 218:
            d(resourceId="com.autel.explorer:id/rb_left_btn").click_exists(5)
            print('VR云台模式切换为FPV')
            time.sleep(1)
            d(resourceId="com.autel.explorer:id/rb_right_btn").click_exists(5)
            print('VR云台模式切换为增稳')
        else:
            d(resourceId="com.autel.explorer:id/rb_right_btn").click_exists(5)
            print('VR云台模式切换为增稳')
        time.sleep(1)
        d(resourceId="com.autel.explorer:id/iv_back").click_exists(5)
        time.sleep(0.5)
    except:
        test.catchError()

    logging.info("function ends")


'''   10-4  显示VR参数   '''
def showparameter10_4():
    logging.info("function start")

    flyMode4_1()

    try:
        d(resourceId="com.autel.explorer:id/model_choice_txt", text=u"VR").click_exists(5)
        time.sleep(1)
        d(resourceId="com.autel.explorer:id/iv_vr_settings").click_exists(5)
        time.sleep(1.5)
        d.screenshot('screen.jpg')
        im = Image.open('screen.jpg')
        r,g,b = im.split()
        print(im.size)
        x=im.size[0]*0.713
        y=im.size[1]*0.686
        print(r)
        color = r.getpixel((x, y))
        print(color)
        if color == 3:
            d(resourceId="com.autel.explorer:id/tv_item_switcher_state").click_exists(5)
            time.sleep(1)
            if d(resourceId="com.autel.explorer:id/tv_home_distance").exists(3):
                print('关闭参数显示失败')
            else:
                print('关闭参数显示成功！')
            d(resourceId="com.autel.explorer:id/tv_item_switcher_state").click_exists(5)
            time.sleep(1)
            if d(resourceId="com.autel.explorer:id/tv_home_distance").exists(3):
                print('开启参数显示成功！')
            else:
                print('开启参数显示失败')

        else:
            d(resourceId="com.autel.explorer:id/tv_item_switcher_state").click_exists(5)
            time.sleep(1.5)
            if d(resourceId="com.autel.explorer:id/tv_home_distance").exists(3):
                print('开启参数显示成功！')
            else:
                print('开启参数显示失败')
            d(resourceId="com.autel.explorer:id/tv_item_switcher_state").click_exists(5)
            time.sleep(1)
            if d(resourceId="com.autel.explorer:id/tv_home_distance").exists(3):
                print('关闭参数显示失败')
            else:
                print('关闭参数显示成功！')
        d(resourceId="com.autel.explorer:id/iv_back").click_exists(5)
        time.sleep(1)
    except:
        test.catchError()

    logging.info("function ends")


'''   14-1、14-2、14-3  简单航点模式   '''
def simpleWaypointMode14_3():
    logging.info("function start")

    WaypointMode0_4()

    try:
        d(resourceId="com.autel.explorer:id/cl_mission_btn").click_exists(5)
        time.sleep(0.5)
        if d(resourceId="com.autel.explorer:id/iv_warn_toast").exists(3):
            pass
        else:
            print('提示信息丢失')
        d(resourceId="com.autel.explorer:id/rl_left").click_exists(5)
    except:
        test.catchError()

    logging.info("function ends")


'''14-6 地图取点创建航点'''
def advanceWaypointMode14_6():
    logging.info("function start")

    WaypointMode0_4()

    try:
        d(resourceId="com.autel.explorer:id/advance_click_area").click_exists(5)
        time.sleep(1.5)

        d(resourceId="com.autel.explorer:id/cl_mission_btn", className="android.view.ViewGroup", instance=1).click_exists(5)
        time.sleep(1.5)

        d(className="android.widget.ImageView", instance=10).long_click()
        time.sleep(1.5)

        d(resourceId="com.autel.explorer:id/mission_drop_item_title", text=u"Point on Map").click_exists(5)
        d.click(0.2,0.5)
        time.sleep(0.5)
        d.click(0.2,0.3)
        time.sleep(0.5)
        d.click(0.4,0.2)
        time.sleep(0.5)
        d.click(0.6,0.52)
        d(resourceId="com.autel.explorer:id/cl_mission_btn", className="android.view.ViewGroup", instance=1).click_exists(5)
        d(resourceId="com.autel.explorer:id/rl_left").click_exists(5)
    except:
        test.catchError()

    logging.info("function ends")


'''14-6 '''
# def advanceWaypointMode14_6():
#     WaypointMode0_4()
#     d(resourceId="com.autel.explorer:id/advance_click_area").click_exists(5)
#     d(resourceId="com.autel.explorer:id/cl_mission_btn", className="android.view.ViewGroup", instance=1).click_exists(5)
#     d(className="android.widget.ImageView", instance=10).click_exists(5)
#     d(resourceId="com.autel.explorer:id/mission_drop_item_title", text=u"Point on Map").click_exists(5)
#     d.click(0.2,0.5)
#     time.sleep(0.5)
#     d.click(0.2,0.3)
#     time.sleep(0.5)
#     d.click(0.4,0.2)
#     time.sleep(0.5)
#     d.click(0.6,0.52)
#     d(resourceId="com.autel.explorer:id/cl_mission_btn", className="android.view.ViewGroup", instance=1).click_exists(5)
#     d(resourceId="com.autel.explorer:id/rl_left").click_exists(5)

'''14-7 划线生成航点'''
def advanceWaypointMode14_7():
    logging.info("function start")

    WaypointMode0_4()

    try:
        d(resourceId="com.autel.explorer:id/advance_click_area").long_click()
        time.sleep(1.5)

        d(resourceId="com.autel.explorer:id/cl_mission_btn", className="android.view.ViewGroup", instance=1).click_exists(5)
        time.sleep(1.5)

        d(className="android.widget.ImageView", instance=10).long_click()
        time.sleep(1.5)

        d(resourceId="com.autel.explorer:id/mission_drop_item_title", text=u"Draw on Map").long_click()
        time.sleep(1.5)

        d.swipe(0.05,0.5,0.12,0.53)
        d.swipe(0.12, 0.6,0.36,0.408)
        d(resourceId="com.autel.explorer:id/cl_mission_btn", className="android.view.ViewGroup", instance=1).click_exists(5)
        time.sleep(1.5)

        d(resourceId="com.autel.explorer:id/rl_left").click_exists(5)
    except:
        test.catchError()

    logging.info("function ends")


'''14-10.1 航点编辑，增加航点'''
def advanceWaypointMode14_101():
    logging.info("function start")

    WaypointMode0_4()

    try:
        d(resourceId="com.autel.explorer:id/advance_click_area").long_click()
        time.sleep(1.5)

        d(resourceId="com.autel.explorer:id/cl_mission_btn", className="android.view.ViewGroup", instance=1).click_exists(5)
        time.sleep(1.5)

        d(className="android.widget.ImageView", instance=10).long_click()
        time.sleep(1.5)

        d(resourceId="com.autel.explorer:id/mission_drop_item_title", text=u"Point on Map").click_exists(5)
        time.sleep(1.5)

        if d(resourceId="com.autel.explorer:id/warn_status_tv").exists(3):
            d(resourceId="com.autel.explorer:id/warn_status_close").click_exists(5)
            time.sleep(0.5)

        d.click(0.101, 0.64)
        time.sleep(0.5)
        d.click(0.615, 0.433)
        time.sleep(0.5)
        d.click(0.2,0.45)
        time.sleep(0.5)
        d(resourceId="com.autel.explorer:id/rl_left").click_exists(5)
    except:
        test.catchError()

    logging.info("function ends")


'''14-10.2 航点编辑，删除航点'''
def advanceWaypointMode14_102():
    logging.info("function start")

    WaypointMode0_4()

    try:
        d(resourceId="com.autel.explorer:id/advance_click_area").long_click()
        time.sleep(1.5)

        d(resourceId="com.autel.explorer:id/cl_mission_btn", className="android.view.ViewGroup", instance=1).click_exists(5)
        time.sleep(1.5)

        d(className="android.widget.ImageView", instance=10).long_click()
        time.sleep(1.5)

        d(resourceId="com.autel.explorer:id/mission_drop_item_title", text=u"Point on Map").click_exists(5)
        time.sleep(1.5)

        if d(resourceId="com.autel.explorer:id/warn_status_tv").exists(3):
            d(resourceId="com.autel.explorer:id/warn_status_close").click_exists(5)
            time.sleep(0.5)
        d.click(0.101, 0.64)
        time.sleep(0.5)
        d.click(0.615, 0.433)
        time.sleep(0.5)
        d.click(0.2,0.45)
        time.sleep(2)
        d(resourceId="com.autel.explorer:id/common_delete").click_exists(5)
        time.sleep(1)
        d(resourceId="com.autel.explorer:id/rl_left").click_exists(5)
    except:
        test.catchError()

    logging.info("function ends")


'''14-10.3 航点编辑，单个航点编辑'''
def advanceWaypointMode14_103():
    logging.info("function start")

    WaypointMode0_4()

    try:
        d(resourceId="com.autel.explorer:id/advance_click_area").long_click()
        time.sleep(1.5)

        d(resourceId="com.autel.explorer:id/cl_mission_btn", className="android.view.ViewGroup", instance=1).click_exists(5)
        time.sleep(1.5)

        d(className="android.widget.ImageView", instance=10).long_click()
        time.sleep(1.5)

        d(resourceId="com.autel.explorer:id/mission_drop_item_title", text=u"Point on Map").click_exists(5)
        time.sleep(1.5)

        if d(resourceId="com.autel.explorer:id/warn_status_tv").exists(3):
            d(resourceId="com.autel.explorer:id/warn_status_close").click_exists(5)
            time.sleep(0.5)
        d.click(0.101, 0.64)
        time.sleep(0.5)
        d.click(0.615, 0.433)
        time.sleep(0.5)
        d.click(0.2,0.45)
        time.sleep(2)
        d.click(0.615, 0.433)
        time.sleep(1)
        d(resourceId="com.autel.explorer:id/rl_left").click_exists(5)
    except:
        test.catchError()

    logging.info("function ends")


'''14-11.1执行航点任务-开始航点任务'''
def WayponitMode14_11_1():
    logging.info("function start")

    WaypointMode0_4()

    try:
        d(resourceId="com.autel.explorer:id/advance_click_area").long_click()
        time.sleep(1.5)

        d(resourceId="com.autel.explorer:id/content").click_exists(5)
        time.sleep(1.5)

        d(resourceId="com.autel.explorer:id/btn_start").click_exists(5)
        time.sleep(1.5)

        d(resourceId="com.autel.explorer:id/rl_left").click_exists(5)
        time.sleep(1.5)

    except:
        test.catchError()

    logging.info("function ends")


'''14-11.2执行航点任务-地图与图传界面切换'''
def WayponitMode14_11_2():
    logging.info("function start")

    WaypointMode0_4()

    try:
        d(resourceId="com.autel.explorer:id/advance_click_area").long_click()
        time.sleep(1.5)
        d(resourceId="com.autel.explorer:id/content").click_exists(5)
        time.sleep(1.5)

        d(resourceId="com.autel.explorer:id/intercept_img_shrink").click_exists(5)
        time.sleep(1.5)

        d.click(0.152,0.228)
        time.sleep(1)
        d.click(0.152,0.228)
        time.sleep(2)
        d(resourceId="com.autel.explorer:id/rl_left").click_exists(5)
    except:
        test.catchError()

    logging.info("function ends")


'''14-11.3执行航点任务-保存航点任务 '''
def WayponitMode14_11_3():
    logging.info("function start")

    WaypointMode0_4()

    try:
        d(resourceId="com.autel.explorer:id/advance_click_area").long_click()
        time.sleep(1.5)
        d(resourceId="com.autel.explorer:id/content").click_exists(5)
        time.sleep(1.5)

        d(resourceId="com.autel.explorer:id/common_save").long_click()
        time.sleep(1.5)

        d.set_fastinput_ime(True)
        timestamp=time.strftime('%H_%M_%S')
        d(resourceId="com.autel.explorer:id/gs_fly_point_save_name").set_text('testwayPointName!'+timestamp)
        d.press('enter')
        d(resourceId="com.autel.explorer:id/tv_ok").click_exists(5)
        d.set_fastinput_ime(False)

        time.sleep(2)
        d(resourceId="com.autel.explorer:id/rl_left").click_exists(5)
    except:
        test.catchError()

    logging.info("function ends")


'''14-13.1执行航点任务-航点任务收藏删除'''
def WayponitMode14_13_1():
    logging.info("function start")

    WaypointMode0_4()

    try:
        d(resourceId="com.autel.explorer:id/advance_click_area").long_click()
        time.sleep(0.5)

        d(resourceId="com.autel.explorer:id/iv_mission_edit").click_exists(5)
        time.sleep(0.5)

        d(resourceId="com.autel.explorer:id/tv_item_value").click_exists(5)
        time.sleep(0.5)

        d(resourceId="com.autel.explorer:id/content").click_exists(5)
        time.sleep(0.5)

        d(resourceId="com.autel.explorer:id/btn_left").click_exists(5)
        time.sleep(0.5)

        d(resourceId="com.autel.explorer:id/tv_ok").click_exists(5)
        time.sleep(0.5)

        d(resourceId="com.autel.explorer:id/btn_right").click_exists(5)
    except:
        test.catchError()

    time.sleep(2)
    d(resourceId="com.autel.explorer:id/rl_left").click_exists(5)

    logging.info("function ends")


'''14-13.2执行航点任务-航点任务收藏重命名'''    #要预先收藏一起些航点任务
def WayponitMode14_13_2():
    logging.info("function start")

    WaypointMode0_4()
    time.sleep(1.5)
    # d(className="android.view.ViewGroup", instance=6).child(className="android.widget.ImageView").long_click()
    # d(resourceId="com.autel.explorer:id/title_name_tv").right(className="android.widget.ImageView").long_click()
    d(resourceId="com.autel.explorer:id/advance_click_area").long_click()
    time.sleep(1.5)
    d.swipe(0.942, 0.304,0.756,0.304)
    d(resourceId="com.autel.explorer:id/btnUnRead").click_exists(5)
    timestamp = time.strftime('%H_%M_%S')
    d.set_fastinput_ime(True)

    d(resourceId="com.autel.explorer:id/gs_fly_point_save_name").clear_text()
    d(resourceId="com.autel.explorer:id/gs_fly_point_save_name").set_text('testWayPointName'+timestamp)
    d.press('enter')
    d(resourceId="com.autel.explorer:id/tv_ok").click_exists(5)
    d.set_fastinput_ime(False)

    time.sleep(2)
    d(resourceId="com.autel.explorer:id/rl_left").click_exists(5)

    logging.info("function ends")


'''   15-1、15-2  执行智能飞行与新手模式   '''
def runflyAndsprog15_1():
    logging.info("function start")

    a = d(resourceId="com.autel.explorer:id/model_choice_txt", text=u"Dynamic Track")
    b = d(resourceId="com.autel.explorer:id/model_choice_txt", text=u"Viewpoint")
    c = d(resourceId="com.autel.explorer:id/model_choice_txt", text=u"Orbit")
    e = d(resourceId="com.autel.explorer:id/model_choice_txt", text=u"Waypoint")
    list = [a,b,c,e]
    for i in list:
        flyMode4_1()

        try:
            d(resourceId="com.autel.explorer:id/model_choice_txt").click_exists(5)
            time.sleep(1)
            flyControlSet()
            d(resourceId="com.autel.explorer:id/tv_aircraft_settings_item_title", text=u"Flight Control").click_exists(5)
            time.sleep(1.5)
            d.screenshot('screen.jpg')
            im = Image.open('screen.jpg')
            r,g,b = im.split()
            # coordinate =im.size
            x = im.size[0] * 0.919
            y = im.size[1] * 0.185
            print(r)
            color = r.getpixel((x,y))
            print(color)
            if color == 255:
                d(resourceId="com.autel.explorer:id/switch_item_switcher").click_exists(5)
                time.sleep(0.5)
                flyMode4_1()
                i.click_exists(5)
                time.sleep(0.5)
                if d(className="android.widget.ScrollView").exists(3):
                    d(resourceId="com.autel.explorer:id/tv_cancel").click_exists(5)
                    time.sleep(0.5)
                    i.click_exists(5)
                    time.sleep(1)
                    if d(className="android.widget.ScrollView").exists(3):
                        d(resourceId="com.autel.explorer:id/tv_ok").click_exists(5)
                        time.sleep(2)
                        if d(resourceId="com.autel.explorer:id/iv_mission_guidance_exit").exists(3):
                            d(resourceId="com.autel.explorer:id/iv_mission_guidance_exit").click_exists(5)
                            time.sleep(3)
                        else:
                            pass
                    else:
                        print('新手模式提示语丢失')
                        if d(resourceId="com.autel.explorer:id/iv_mission_guidance_exit").exists(3):
                            d(resourceId="com.autel.explorer:id/iv_mission_guidance_exit").click_exists(5)
                            time.sleep(3)
                        else:
                            pass
                else:
                    print('新手模式提示语丢失')
                    if d(resourceId="com.autel.explorer:id/iv_mission_guidance_exit").exists(3):
                        d(resourceId="com.autel.explorer:id/iv_mission_guidance_exit").click_exists(5)
                        time.sleep(3)
                    else:
                        pass
            else:
                d(resourceId="com.autel.explorer:id/switch_item_switcher").click_exists(5)
                time.sleep(1)
                if d(resourceId="com.autel.explorer:id/model_choice_no_pop_cb").exists(3):
                    d(resourceId="com.autel.explorer:id/tv_ok").click_exists(5)
                    time.sleep(0.5)
                    flyMode4_1()
                    i.click_exists(5)
                    time.sleep(0.5)
                    if d(className="android.widget.ScrollView").exists(3):
                        d(resourceId="com.autel.explorer:id/tv_cancel").click_exists(5)
                        time.sleep(0.5)
                        i.click_exists(5)
                        time.sleep(1)
                        if d(className="android.widget.ScrollView").exists(3):
                            d(resourceId="com.autel.explorer:id/tv_ok").click_exists(5)
                            time.sleep(2)
                            if d(resourceId="com.autel.explorer:id/iv_mission_guidance_exit").exists(3):
                                d(resourceId="com.autel.explorer:id/iv_mission_guidance_exit").click_exists(5)
                                time.sleep(3)
                            else:
                                pass
                        else:
                            print('新手模式提示语丢失')
                            if d(resourceId="com.autel.explorer:id/iv_mission_guidance_exit").exists(3):
                                d(resourceId="com.autel.explorer:id/iv_mission_guidance_exit").click_exists(5)
                                time.sleep(3)
                            else:
                                pass
                    else:
                        print('新手模式提示语丢失')
                        if d(resourceId="com.autel.explorer:id/iv_mission_guidance_exit").exists(3):
                            d(resourceId="com.autel.explorer:id/iv_mission_guidance_exit").click_exists(5)
                            time.sleep(3)
                        else:
                            pass
                else:
                    pass
        except:
            test.catchError()
    logging.info("function ends")


'''   16-1  进入指点飞行界面   '''
def intoViewpoint16_1():
    logging.info("function start")

    ViewpointMode0_2()
    logging.info("function ends")


'''   16-2  点取指点飞行的位置   '''
def choiceViewpoint16_2():
    logging.info("function start")

    test.SwitchtoCaptureMode()
    test.GimbalAngle('0°')
    ViewpointMode0_2()
    time.sleep(0.5)
    d.click(0.5,0.4)
    print('点击地平线以上位置')
    time.sleep(1)
    if d(resourceId="com.autel.explorer:id/tvStart").exists(3):
        pass
    else:
        print('选取失败')
    d.click(0.5, 0.6)
    print('点击地平线以上位置')
    time.sleep(1)
    if d(resourceId="com.autel.explorer:id/tvStart").exists(3):
        pass
    else:
        print('选取失败')
    d.click(0.492, 0.93)
    print('点击红色区域')
    time.sleep(1)
    if d(resourceId="com.autel.explorer:id/iv_warn_toast").exists(3):
        pass
    else:
        print('选取失败')
    time.sleep(1)

    logging.info("function ends")


'''   16-2.2  点取指点飞行的位置，视觉设置   '''
def choiceViewpoint16_2_2():
    logging.info("function start")

    ViewpointMode0_2()
    time.sleep(0.5)
    try:
        d(resourceId="com.autel.explorer:id/imageSetting").click_exists(5)
        time.sleep(0.5)
        d(resourceId="com.autel.explorer:id/rl_left").click_exists(5)
        time.sleep(1.5)
    except:
        test.catchError()

    logging.info("function ends")


'''   16-3  执行指点飞行   '''
def runViewpoint16_3():
    logging.info("function start")

    test.SwitchtoCaptureMode()
    test.GimbalAngle('0°')
    ViewpointMode0_2()
    d.click(0.5, 0.4)
    print('点击地平线以上位置')
    time.sleep(1)
    if d(resourceId="com.autel.explorer:id/tvStart").exists(3):
        try:
            d(resourceId="com.autel.explorer:id/dynamic_start").click_exists(5)
        except:
            test.catchError()
        if d(resourceId="com.autel.explorer:id/iv_warn_toast").exists(3):
            print('已执行指点飞行')
            time.sleep(3)
        else:
            print('提示信息丢失')
    else:
        print('选取失败')

    logging.info("function ends")


# simploOrbitMode5_4()
# advanceOrbitMode5_5()
# advanceOrbitMode5_71()
# advanceOrbitMode5_72()
# advanceOrbitMode5_8()
# runDTMode7_4()
# runDTMode7_5()
# advanceWaypointMode14_6()
# advanceWaypointMode14_7()
# advanceWaypointMode14_101()
# time.sleep(2)
# advanceWaypointMode14_102()
# time.sleep(2)
# advanceWaypointMode14_103()
# WayponitMode14_11_1()
# WayponitMode14_11_2()
# WayponitMode14__3()
# WayponitMode14_13_2()
# choiceViewpoint16_2_2()

i = 0

while True:
    i = i+1
    print("\n第", i , '次运行开始\n--------------------------------------------------------------------------')
    print(datetime.datetime.now())




    print('\n1-2 地图手动放大、缩小')
    fangdasuoxiaoMap1_2()
    time.sleep(3)

    print('\n1-4 顶部栏信息显示')
    topmessageMap1_4()

    print('\n1-5 地图右侧功能显示')
    rightfunctionMap1_5()
    time.sleep(2)

    print('\n2-1 地图朝向锁定')
    directionMap2_1()
    time.sleep(2)

    print('\n3-1 地图模式')
    modeMap3_1()
    time.sleep(2)

    print('\n4-1  智能飞行模式界面')
    flyMode4_1()

    print('\n4-2  智能飞行模式项')
    choiceflyMode4_2()

    print('\n5-2  简单环绕模式 ')
    simpleOrbitMode5_2()  #debug
   

    print("\n5-4  简单环绕模式设置")
    simploOrbitMode5_4()
    time.sleep(2)


    print('\n5-71高级环绕，选择地图取点，会自动切换到地图')
    advanceOrbitMode5_71()
    time.sleep(2)

    print('\n5-72高级环绕，地图取点，提示未选择兴趣点')
    advanceOrbitMode5_72()
    time.sleep(2)

    print("\n5-8 兴趣点参数设置")
    advanceOrbitMode5_8()
    time.sleep(2)


    print("\n7-1、7-2、7-5  执行智能追踪")
    runDTMode7_5()
    time.sleep(3)

    print("\n7-4视觉设置")
    runDTMode7_4()
    time.sleep(3)


    print('\n8-2  进入VR')
    intoVR8_2()
    time.sleep(2)

    print('\n8-3  退出VR')
    exitVR8_3()
    time.sleep(2)

    print('\n10-1、10-2  VR参数设置')
    setVR10_1()
    time.sleep(2)

    print('\n10-3  VR云台模式')
    gimbalVR10_3()
    time.sleep(2)
   

    print('\n10-4  显示VR参数 ')
    showparameter10_4()
    time.sleep(2)
    
    print('\n14-1、14-2、14-3  简单航点模式  ')
    simpleWaypointMode14_3()
    time.sleep(2)
   

    print('\n14-6 地图取点创建航点')
    advanceWaypointMode14_6()
    time.sleep(2)
     

    print('\n14-7 划线生成航点')
    advanceWaypointMode14_7()
    time.sleep(2)


    print('\n14-10.1 航点编辑，增加航点')
    advanceWaypointMode14_101()
    time.sleep(2)


    print('\n14-10.2 航点编辑，删除航点')
    advanceWaypointMode14_102()
    time.sleep(2)

    print('\n14-10.3 航点编辑，单个航点编辑')
    advanceWaypointMode14_103()
    time.sleep(2)


    print('\n14-11.1执行航点任务-开始航点任务')
    WayponitMode14_11_1()
    time.sleep(2)


    print('\n14-11.2执行航点任务-地图与图传界面切换')
    WayponitMode14_11_2()
    time.sleep(2)

    print('\n14-11.3执行航点任务-保存航点任务')
    WayponitMode14_11_3()
    time.sleep(2)
    

    # print('\n14-13.1执行航点任务-航点任务收藏删除')    #不要随便删除航点收藏，因为在飞的时候才能创建。
    # WayponitMode14_13_1()
    # time.sleep(2)
    


    print('\n14-13.2执行航点任务-航点任务收藏重命名')
    WayponitMode14_13_2()
    time.sleep(2)

  
    # print('\n15-1、15-2  执行智能飞行与新手模式')   #bug 学习中心关不掉
    #     runflyAndsprog15_1()
    #     time.sleep(2)
  

    print('\n16-1  进入指点飞行界面 ')
    intoViewpoint16_1()
    time.sleep(2)


    print('\n16-2  点取指点飞行的位置')
    choiceViewpoint16_2()
    time.sleep(2)

    print('\n16-2.2  点取指点飞行的位置，视觉设置')
    choiceViewpoint16_2_2()
    time.sleep(2)

    print('\n16-3  执行指点飞行')
    runViewpoint16_3()
    time.sleep(2)






# advanceOrbitMode5_71()
# advanceOrbitMode5_72()
# advanceOrbitMode5_8()

'''
    print('\n智能飞行模式界面')
    flyMode4_1()
    time.sleep(2)

    print('\n追踪模式')
    DynamicTrackMode0_1()
    time.sleep(2)

    print('\n指点模式')
    ViewpointMode0_2()
    time.sleep(2)

    print('\n环绕模式')
    OrbitMode0_3()
    time.sleep(2)

    print('\n航点模式')
    WaypointMode0_4()
    time.sleep(2)

    print('\nVR模式')
    VRMode0_5()
    time.sleep(2)


    print('\n智能飞行模式项')
    choiceflyMode4_2()
    time.sleep(1)

    print('\n简单环绕模式')
    simpleOrbitMode5_2()
    time.sleep(1)



    print('\n执行智能追踪')
    runDTMode7_5()
    time.sleep(1)

    print('\n进入VR')
    intoVR8_2()
    time.sleep(1)

    print('\n退出VR')
    exitVR8_3()
    time.sleep(1)

    print('\nVR参数设置')
    setVR10_1()
    time.sleep(2)

    print('\nVR云台模式')
    gimbalVR10_3()
    time.sleep(1)

    print('\n显示VR参数')
    showparameter10_4()
    time.sleep(1)

    print('\n简单航点模式')
    simpleWaypointMode14_3()
    time.sleep(1)

    # print('执行智能飞行与新手模式')              #崩溃BUG
    # runflyAndsprog15_1()
    # time.sleep(1)

    print('\n进入指点飞行界面')
    intoViewpoint16_1()
    time.sleep(1)

    print('\n点取指点飞行的位置')
    choiceViewpoint16_2()
    time.sleep(1)

    print('\n执行指点飞行')
    runViewpoint16_3()
    time.sleep(1)

    print("\n第", i , '次运行结束\n--------------------------------------------------------------------------')
    print(datetime.datetime.now())
    # time.sleep(300)
   '''