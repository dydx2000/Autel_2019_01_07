import datetime
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
d.click_post_delay=1
d.wait_timeout = 30
# d=u2.connect_wifi('192.168.1.11')
# d.wait_timeout = 30.0
test=uiauto.Camera()
time.sleep(1)

# 2-1正在录像，不能进入相册
def test_Album_Video():
    test.SwitchtoCaptureMode()
    time.sleep(2)
    test.setVideoPIV("5S")
    time.sleep(2)
    test.record()
    if d(resourceId="com.autel.explorer:id/iv_child_piv_photo").exists():
        print("正在录像，不能进入相册")
    else:
        print("进入相册")
    time.sleep(5)
    test.record()

# 2-1.2正在拍照不能进入相册
def test_Album_Pict():
    test.SwitchtoCaptureMode()
    time.sleep(2)
    test.SetPictureMode("TIMELAPSE", "20s")
    time.sleep(2)
    test.shot()
    d(resourceId="com.autel.explorer:id/civ_album_playback").click()
    if d(resourceId="com.autel.explorer:id/iv_preview_share").exists():
        print("进入相册")
    else:
        print("正在拍照，不能进入相册")

    time.sleep(5)
    test.shot()

#2-3 .1下载文件
def test_Album_Downing():
    test.test_into_Album()
    d(resourceId="com.autel.explorer:id/iv_preview_download").click()
    if  d(resourceId="com.autel.explorer:id/tv_ok").exists():
        time.sleep(0.5)
        print(
            "Only JPEG images and videos 1080p resolution or less can be downloaded. Others should be copied using the USB cable or SD card")
        d(resourceId="com.autel.explorer:id/tv_ok").click()
    elif  d(text=u"Downloading…").exists():
        print("正在下载")
        time.sleep(15)
        d.implicitly_wait(15)
        d(resourceId="com.autel.explorer:id/tv_preview_back").click()
    elif d(resourceId="com.autel.explorer:id/iv_album_local").exists():
        print("已下载过")
        print("正在下载")
        time.sleep(15)
        d.implicitly_wait(15)
        d(resourceId="com.autel.explorer:id/tv_preview_back").click()
    else:
        print('unknown error!')

#2-3相册列表界面单张下载
def test_Album_Down():
    test.SwitchtoCaptureMode()
    test.SetPictureMode('SINGLE')
    test.shot()
    test.test_into_Album_List()
    time.sleep(1)
    d(resourceId="com.autel.explorer:id/tv_album_select").long_click()
    time.sleep(0.5)
    d(resourceId="com.autel.explorer:id/vf_list_selected").click()
    time.sleep(0.5)
    d(resourceId="com.autel.explorer:id/iv_list_download").click()
    time.sleep(5)
    d.implicitly_wait(10)
    d(resourceId="com.autel.explorer:id/tv_list_back").click()

 #2-3.3相册列表多张下载
def  test_Album_List_multipleDown():
    # test.SwitchtoCaptureMode()
    test.SetPictureMode('SINGLE')
    test.shot()
    time.sleep(0.5)
    test.shot()
    time.sleep(0.5)
    test.shot()
    time.sleep(0.5)
    test.test_into_Album_List()
    time.sleep(0.5)
    d(resourceId="com.autel.explorer:id/tv_album_select").long_click()
    time.sleep(0.5)
    d(resourceId="com.autel.explorer:id/vf_list_selected").click()
    time.sleep(0.5)
    d(className="android.widget.ImageView", instance=6).click()
    time.sleep(0.5)
    d(className="android.widget.ImageView", instance=9).click()
    time.sleep(0.5)
    d(resourceId="com.autel.explorer:id/iv_list_download").click()
    time.sleep(20)
    d.implicitly_wait(10)
    d(resourceId="com.autel.explorer:id/tv_list_back").click()
    time.sleep(0.5)

    # d(resourceId="com.autel.explorer:id/iv_list_delete").click()
    # time.sleep(0.5)
    # d(text=u"Delete 3 items").click()
    # time.sleep(1)
    # d(resourceId="com.autel.explorer:id/tv_list_back").click()



#2-5  多张删除
def  test_Album_List_Dele():

    test.test_into_Album_List()
    time.sleep(0.5)
    d(resourceId="com.autel.explorer:id/tv_album_select").long_click()
    time.sleep(0.5)
    d(resourceId="com.autel.explorer:id/vf_list_selected").click()
    time.sleep(0.5)
    d(className="android.widget.ImageView", instance=10).click()
    time.sleep(0.5)
    d(className="android.widget.ImageView", instance=15).click()
    time.sleep(0.5)
    d(resourceId="com.autel.explorer:id/iv_list_delete").click()
    time.sleep(0.5)
    d(textContains="Delete").click()
    print('delete photos!')

    time.sleep(3)
    d.implicitly_wait(5)
    d(resourceId="com.autel.explorer:id/tv_list_back").click()
    time.sleep(0.5)

def preparePhoto2():
    # 先拍3张照片
    test.SetPictureMode('SINGLE')
    test.shot()
    time.sleep(0.5)
    test.shot()
    time.sleep(0.5)
    test.shot()
    time.sleep(0.5)
    test.test_into_Album_List()
    d(resourceId="com.autel.explorer:id/tv_album_select", text=u"Select", className="android.widget.TextView").long_click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    d(resourceId="com.autel.explorer:id/vf_list_selected", className="android.view.View").click()
    time.sleep(0.5)
    d(className="android.widget.ImageView", instance=9).click()
    time.sleep(0.5)
    d(resourceId="com.autel.explorer:id/iv_list_download", className="android.widget.ImageView").click()
    time.sleep(20)
    d.implicitly_wait(30)
    d(resourceId="com.autel.explorer:id/tv_list_back", text=u"Back", className="android.widget.TextView").click()


#3-1 .1分享facebook 单张
def share_facebook_onephoto():
    test.test_into_Album_List()
    time.sleep(0.5)
    d.implicitly_wait(5)
    d(resourceId="com.autel.explorer:id/tv_album_select").long_click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    d(resourceId="com.autel.explorer:id/vf_list_selected").click()
    # time.sleep(0.5)
    # d.implicitly_wait(5)
    # d(className="android.widget.ImageView", instance=7).click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    d(resourceId="com.autel.explorer:id/iv_list_share").click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    if d(resourceId="com.autel.explorer:id/tv_ok").exists():
        d(resourceId="com.autel.explorer:id/tv_ok").click()
        print('start dowloading File!')
        time.sleep(60)
        d.implicitly_wait(90)

    if d(resourceId="android:id/sem_title_default").exists():
        # d.implicitly_wait(5)
        d.swipe(0.5, 0.49, 0.5, 0.14)
        time.sleep(1)
    d.implicitly_wait(5)
    d(resourceId="android:id/text1", text=u"Facebook").click()
    print('Click facebook share link!')
    time.sleep(5)
    d.implicitly_wait(5)
    d(resourceId="com.facebook.katana:id/(name removed)", text=u"SHARE").click()
    time.sleep(3)
    d.implicitly_wait(5)
    try:
        d(resourceId="com.facebook.katana:id/(name removed)", className="android.widget.ImageView").click()
        d(resourceId="com.facebook.katana:id/(name removed)", text=u"SHARE").click()
        time.sleep(3)
    except:
        pass

    # if d(resourceId="com.facebook.katana:id/(name removed)", text=u"Effects").exists():
    #     print('At editing windows!')
    #     d(resourceId="com.facebook.katana:id/(name removed)", className="android.widget.ImageView").click()
    time.sleep(1)

    d(className="android.view.ViewGroup", instance=8).click()
    time.sleep(0.5)
    d(description=u"SHARE NOW").click()

    time.sleep(2)
    d.implicitly_wait(5)


    d(resourceId="com.autel.explorer:id/tv_list_back").click()

    '''
    # test.SwitchtoCaptureMode()
    # test.SetPictureMode('SINGLE')
    # test.shot()
    # test.test_into_Album()
    test.test_into_Album_List()
    d(resourceId="com.autel.explorer:id/tv_album_select").click()
    time.sleep(0.5)
    d(resourceId="com.autel.explorer:id/vf_list_selected").click()
    time.sleep(0.5)
    d(resourceId="com.autel.explorer:id/iv_list_share").click()
    time.sleep(5)
    d.implicitly_wait(5)
    if  d(resourceId="com.autel.explorer:id/tv_ok").exists():
        d(resourceId="com.autel.explorer:id/tv_ok").click()
        time.sleep(5)
        d.implicitly_wait(10)
    d(resourceId="android:id/text1", text=u"Facebook").click()
    time.sleep(5)
    d.implicitly_wait(5)
    d(resourceId="com.facebook.katana:id/(name removed)", text=u"SHARE").click()
    time.sleep(1)
    d.implicitly_wait(5)
    d(className="android.view.ViewGroup", instance=8).click()
    time.sleep(0.5)
    d(description=u"SHARE NOW").click()
    time.sleep(2)
    d.implicitly_wait(5)
    d(resourceId="com.autel.explorer:id/tv_list_back").click()
    '''

#3-1 .2分享facebook 多张
def share_facebook_multiphoto():
    # #先拍3张照片
    # test.SetPictureMode('SINGLE')
    # test.shot()
    # time.sleep(0.5)
    # test.shot()
    # time.sleep(0.5)
    # test.shot()
    # # time.sleep(0.5)
    # #操作这3张照片
    test.test_into_Album_List()
    time.sleep(0.5)
    d.implicitly_wait(5)
    d(resourceId="com.autel.explorer:id/tv_album_select").click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    d(resourceId="com.autel.explorer:id/vf_list_selected").click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    d(className="android.widget.ImageView", instance=10).click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    d(resourceId="com.autel.explorer:id/iv_list_share").click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    if d(resourceId="com.autel.explorer:id/tv_ok").exists():
        d(resourceId="com.autel.explorer:id/tv_ok").click()
        print('start dowloading File!')
        time.sleep(60)
        d.implicitly_wait(90)

    if d(resourceId="android:id/sem_title_default").exists():
        # d.implicitly_wait(5)
        d.swipe(0.5, 0.49, 0.5, 0.14)
        time.sleep(1)
    d.implicitly_wait(5)
    d(resourceId="android:id/text1", text=u"Facebook").click()
    print('Click facebook share link!')
    time.sleep(5)
    d.implicitly_wait(5)
    d(resourceId="com.facebook.katana:id/(name removed)", text=u"SHARE").click()
    time.sleep(1)
    d.implicitly_wait(5)
    d(className="android.view.ViewGroup", instance=8).click()
    time.sleep(0.5)
    d(description=u"SHARE NOW").click()
    time.sleep(2)
    d.implicitly_wait(5)
    d(resourceId="com.autel.explorer:id/tv_list_back").click()

#3-3.1分享twitter 单张
def share_twitter_onephoto():
    test.test_into_Album_List()
    time.sleep(0.5)
    d.implicitly_wait(5)
    d(resourceId="com.autel.explorer:id/tv_album_select").click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    d(resourceId="com.autel.explorer:id/vf_list_selected").click()
    # time.sleep(0.5)
    # d.implicitly_wait(5)
    # d(className="android.widget.ImageView", instance=7).click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    d(resourceId="com.autel.explorer:id/iv_list_share").click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    if d(resourceId="com.autel.explorer:id/tv_ok").exists():
        d(resourceId="com.autel.explorer:id/tv_ok").click()
        print('start dowloading File!')
        time.sleep(60)
        d.implicitly_wait(90)

    if d(resourceId="android:id/sem_title_default").exists():
        # d.implicitly_wait(5)
        d.swipe(0.5, 0.49, 0.5, 0.14)
        time.sleep(1)
    d.implicitly_wait(5)
    d(resourceId="android:id/text1", text=u"Tweet").click()
    print('Click twitter share link!')
    time.sleep(5)
    d.implicitly_wait(5)
    d(resourceId="com.twitter.android:id/button_tweet").click()
    time.sleep(2)
    d.implicitly_wait(10)
    d(resourceId="com.autel.explorer:id/tv_list_back").click()




#3-4.1，微信单张分享
def share_wechat_onephoto():
    # test.SwitchtoCaptureMode()
    # test.SetPictureMode('SINGLE')
    # test.shot()
    # test.test_into_Album()
    test.test_into_Album_List()
    time.sleep(0.5)
    d.implicitly_wait(5)
    d(resourceId="com.autel.explorer:id/tv_album_select").click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    d(resourceId="com.autel.explorer:id/vf_list_selected").click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    d(resourceId="com.autel.explorer:id/iv_list_share").click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    if d(resourceId="com.autel.explorer:id/tv_ok").exists():
        d(resourceId="com.autel.explorer:id/tv_ok").click()
        print('start dowloading File!')
        time.sleep(60)
        d.implicitly_wait(90)

    if d(resourceId="android:id/sem_title_default").exists():
        # d.implicitly_wait(5)
        d.swipe(0.5, 0.49, 0.5, 0.14)
        time.sleep(1)
    d.implicitly_wait(5)
    d(resourceId="android:id/text1", text=u"WeChat").click()
    print('Click WeChat share link!')
    time.sleep(1)
    d.implicitly_wait(10)
    d(resourceId="com.tencent.mm:id/b8a").set_text('dydx')
    time.sleep(5)
    d.implicitly_wait(10)
    d(resourceId="com.tencent.mm:id/py").click()
    time.sleep(1)
    d.implicitly_wait(10)
    d(resourceId="com.tencent.mm:id/az_").click()
    time.sleep(5)
    d.press('back')
    time.sleep(1)
    d.press('back')
    time.sleep(1)
    d.press('back')

#3-4.2，微信多张分享
def share_wechat_multiphoto():
    # test.SetPictureMode('SINGLE')
    # test.shot()
    # time.sleep(0.5)
    # test.shot()
    # time.sleep(0.5)
    # test.shot()
    # time.sleep(0.5)
    # test.test_into_Album()
    test.test_into_Album_List()
    time.sleep(0.5)
    d.implicitly_wait(5)
    d(resourceId="com.autel.explorer:id/tv_album_select").click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    d(resourceId="com.autel.explorer:id/vf_list_selected").click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    d(className="android.widget.ImageView", instance=10).click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    d(resourceId="com.autel.explorer:id/iv_list_share").click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    if d(resourceId="com.autel.explorer:id/tv_ok").exists():
        d(resourceId="com.autel.explorer:id/tv_ok").click()
        print('start dowloading File!')
        time.sleep(60)
        d.implicitly_wait(90)

    if d(resourceId="android:id/sem_title_default").exists():
        # d.implicitly_wait(5)
        d.swipe(0.5, 0.49, 0.5, 0.14)
        time.sleep(1)
    d.implicitly_wait(5)
    d(resourceId="android:id/text1", text=u"WeChat").click()
    print('Click WeChat share link!')
    time.sleep(1)
    d.implicitly_wait(10)
    d(resourceId="com.tencent.mm:id/b8a").set_text('dydx')
    time.sleep(5)
    d.implicitly_wait(10)
    d(resourceId="com.tencent.mm:id/py").click()
    time.sleep(1)
    d.implicitly_wait(10)
    d(resourceId="com.tencent.mm:id/az_").click()
    time.sleep(8)
    d.press('back')
    time.sleep(1.5)
    d.press('back')
    time.sleep(1.5)
    d.press('back')


#3-5.1 instagram 分享单张：
def share_instagram_onephoto():
    # test.SwitchtoCaptureMode()
    # test.SetPictureMode('SINGLE')
    # test.shot()
    # test.test_into_Album()
    test.test_into_Album_List()
    time.sleep(0.5)
    d.implicitly_wait(5)

    d(resourceId="com.autel.explorer:id/tv_album_select").click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    d(resourceId="com.autel.explorer:id/vf_list_selected").click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    d(resourceId="com.autel.explorer:id/iv_list_share").click()
    time.sleep(5)
    d.implicitly_wait(5)
    if d(resourceId="com.autel.explorer:id/tv_ok").exists():
        d(resourceId="com.autel.explorer:id/tv_ok").click()
        time.sleep(5)
        d.implicitly_wait(10)

    if d(resourceId="android:id/sem_title_default").exists():
        # d.implicitly_wait(5)
        d.swipe(0.5, 0.49, 0.5, 0.14)
        time.sleep(1)
        d.implicitly_wait(5)
        d(resourceId="android:id/text1", text=u"Feed").click()
        time.sleep(0.5)
    d.implicitly_wait(5)
    d(resourceId="com.instagram.android:id/save").click()
    time.sleep(0.5)
    d.implicitly_wait(10)
    d(resourceId="com.instagram.android:id/next_button_textview").click()
    time.sleep(0.5)
    d.implicitly_wait(10)
    d(resourceId="com.instagram.android:id/next_button_textview").click()
    time.sleep(3)
    d.press('back')
    time.sleep(1.5)
    d(resourceId="com.autel.explorer:id/tv_list_back").click()
    time.sleep(0.5)

# 视频分享素材准备
def prepareVideos3():
    test.setVideoPIV('MANUAL')
    test.setVideoReso('720P')
    test.setVideoFramerate('24FPS')
    #录第一个短视频
    test.record()
    time.sleep(0.5)
    test.record()

    # 录第二个短视频
    test.record()
    time.sleep(0.5)
    test.record()
    test.test_into_Album_List()
    d(resourceId="com.autel.explorer:id/tv_album_select").click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    d(resourceId="com.autel.explorer:id/vf_list_selected").click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    d(className="android.widget.ImageView", instance=9).click()
    time.sleep(0.5)
    d(resourceId="com.autel.explorer:id/iv_list_download").click()
    time.sleep(70)
    d(resourceId="com.autel.explorer:id/tv_list_back").click()

#3-6.1 facebook 分享单个短视频：
def share_facebook_onevideo():

    test.test_into_Album_List()
    time.sleep(1)
    d.implicitly_wait(5)
    d(resourceId="com.autel.explorer:id/tv_album_select").click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    d(resourceId="com.autel.explorer:id/vf_list_selected").click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    d(resourceId="com.autel.explorer:id/iv_list_share").click()
    print('点击分享！')
    time.sleep(1)
    d.implicitly_wait(5)
    # 下载
    # if d(resourceId="com.autel.explorer:id/tv_ok").exists():
    #     d(resourceId="com.autel.explorer:id/tv_ok").click()
    #     print('start dowloading File!')
    #     time.sleep(30)
    #     d.implicitly_wait(60)
    # 弹出分享菜单，上划
    if d(resourceId="android:id/sem_title_default").exists():
        # d.implicitly_wait(5)
        d.swipe(0.5, 0.49, 0.5, 0.14)
        time.sleep(2)
    # if d(resourceId="com.autel.explorer:id/tv_ok").exists():
    #     d(resourceId="com.autel.explorer:id/tv_ok").click()
    #     print('start dowloading File!')
    #     time.sleep(20)
    #     d.implicitly_wait(60)
    d.implicitly_wait(5)
    if d(resourceId="android:id/text1", text=u"Facebook").exists():
        d(resourceId="android:id/text1", text=u"Facebook").click()
        print('Click Facebook share link!')

    time.sleep(5)          #facebook 的share 按钮在进入facebook 1~5秒内会可以点击
    d.implicitly_wait(10)
    d(resourceId="com.facebook.katana:id/(name removed)", text=u"SHARE").click()
    print('click share button.')
    time.sleep(3)
    d.implicitly_wait(10)
    if d(resourceId="com.facebook.katana:id/(name removed)", className="android.widget.ImageView").exists():
        d(resourceId="com.facebook.katana:id/(name removed)", className="android.widget.ImageView").click()
        time.sleep(1)
        d.implicitly_wait(10)
        d(resourceId="com.facebook.katana:id/(name removed)", text=u"SHARE").click()

    d.implicitly_wait(10)
    d(className="android.view.ViewGroup", instance=8).click()
    d(description=u"SHARE NOW").click()
    time.sleep(1)
    d.implicitly_wait(10)
    d(resourceId="com.autel.explorer:id/tv_list_back").click()
    time.sleep(1)

#3-6.2 facebook 分享多个短视频：
def share_facebook_multivideo():
    test.test_into_Album_List()
    time.sleep(0.5)
    d.implicitly_wait(5)
    d(resourceId="com.autel.explorer:id/tv_album_select").click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    d(resourceId="com.autel.explorer:id/vf_list_selected").click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    d(className="android.widget.ImageView", instance=10).click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    d(resourceId="com.autel.explorer:id/iv_list_share").click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    # 下载
    if d(resourceId="com.autel.explorer:id/tv_ok").exists():
        d(resourceId="com.autel.explorer:id/tv_ok").click()
        print('start dowloading File!')
        time.sleep(30)
        d.implicitly_wait(60)
    # 弹出分享菜单，上划
    if d(resourceId="android:id/sem_title_default").exists():
        # d.implicitly_wait(5)
        d.swipe(0.5, 0.49, 0.5, 0.14)
        time.sleep(2)
    d.implicitly_wait(5)
    if d(resourceId="android:id/text1", text=u"Facebook").exists():
        d(resourceId="android:id/text1", text=u"Facebook").click()
        print('Click Facebook share link!')

    time.sleep(5)  # facebook 的share 按钮在进入facebook 1~5秒内会可以点击
    d.implicitly_wait(10)
    d(resourceId="com.facebook.katana:id/(name removed)", text=u"SHARE").click()
    print('click share button.')
    time.sleep(1)
    d.implicitly_wait(10)
    if d(resourceId="com.facebook.katana:id/(name removed)", className="android.widget.ImageView").exists():
        d(resourceId="com.facebook.katana:id/(name removed)", className="android.widget.ImageView").click()
        time.sleep(1)
        d.implicitly_wait(10)
        d(resourceId="com.facebook.katana:id/(name removed)", text=u"SHARE").click()
    time.sleep(1)
    d.implicitly_wait(10)
    d(className="android.view.ViewGroup", instance=8).click()
    d(description=u"SHARE NOW").click()
    time.sleep(1)
    d.implicitly_wait(10)
    d(resourceId="com.autel.explorer:id/tv_list_back").click()
    time.sleep(1)

    '''
    test.test_into_Album()
    test.test_into_Album_List()
    d.implicitly_wait(10)
    d(resourceId="com.autel.explorer:id/tv_album_select").click()
    d.implicitly_wait(10)
    d(className="android.widget.LinearLayout", instance=4).click()
    time.sleep(0.5)
    d(className="android.widget.LinearLayout", instance=5).click()

    time.sleep(0.5)
    d(resourceId="com.autel.explorer:id/iv_list_share").click()
    time.sleep(2)
    if d(resourceId="com.autel.explorer:id/tv_ok").exists():
        d(resourceId="com.autel.explorer:id/tv_ok").click()
    d.implicitly_wait(300)
    d(resourceId="android:id/text1", text=u"Facebook").click()

    d.implicitly_wait(10)
    d(resourceId="com.facebook.katana:id/(name removed)", text=u"SHARE",enabled=True).click()
    d.implicitly_wait(10)
    # d(description=u"Selected:News Feed").click()
    d(description=u"SHARE NOW").click()
    '''

#3-7.1 youtube分享单个短视频    #不循环执行
def share_youtube_onevideo():
    d.set_fastinput_ime('True')
    #拍摄视频

    # test.record()
    # time.sleep(0.5)
    # test.record()
    # time.sleep(1)
    #
    # # 录第二个短视频
    # test.record()
    # time.sleep(0.5)
    # test.record()
    # time.sleep(1)

    test.test_into_Album_List()
    time.sleep(0.5)
    d.implicitly_wait(5)
    d(resourceId="com.autel.explorer:id/tv_album_select").click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    d(resourceId="com.autel.explorer:id/vf_list_selected").click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    d(resourceId="com.autel.explorer:id/iv_list_share").click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    if d(resourceId="com.autel.explorer:id/tv_ok").exists():
        d(resourceId="com.autel.explorer:id/tv_ok").click()
        print('start dowloading File!')
        time.sleep(60)
        d.implicitly_wait(90)

    if d(resourceId="android:id/sem_title_default").exists():
    # d.implicitly_wait(5)
        d.swipe(0.5, 0.49, 0.5, 0.14)
        time.sleep(1)
    d.implicitly_wait(5)
    d(resourceId="android:id/text1", text=u"YouTube").click()
    print('Click Youtube share link!')
    time.sleep(5)  # facebook 的share 按钮在进入facebook 1~5秒内会可以点击
    title = 'AutelShareyoutube'+time.strftime('%H_%M_%S')
    d(resourceId="com.google.android.youtube:id/title_edit").set_text(title)
    time.sleep(0.5)
    d(resourceId="com.google.android.youtube:id/description_edit").set_text('A sample for testing share function.')
    time.sleep(0.5)
    d(resourceId="com.google.android.youtube:id/menu_upload_activity_done").click()
    time.sleep(40)
    d.implicitly_wait(60)
    if d(resourceId="com.google.android.youtube:id/upload_status_detailed_message").exists():
        d(resourceId="com.google.android.youtube:id/upload_status_detailed_message",
          text=u"This video is ready to be watched.", className="android.widget.TextView", instance=1).exists()
        print('share completed!,ready to back to Autel Explorer')
        d.press('back')
        time.sleep(0.5)
        d.press('back')
        time.sleep(0.5)
        d.press('back')

#3-7.2 youtube分享多个短视频
def share_youtube_multivideo():
    d.set_fastinput_ime('True')
    #拍摄视频

    # test.record()
    # time.sleep(0.5)
    # test.record()
    # time.sleep(1)
    #
    # # 录第二个短视频
    # test.record()
    # time.sleep(0.5)
    # test.record()
    # time.sleep(1)

    test.test_into_Album_List()
    time.sleep(0.5)
    d.implicitly_wait(5)
    d(resourceId="com.autel.explorer:id/tv_album_select").click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    d(resourceId="com.autel.explorer:id/vf_list_selected").click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    d(className="android.widget.ImageView", instance=10).click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    d(resourceId="com.autel.explorer:id/iv_list_share").click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    if d(resourceId="com.autel.explorer:id/tv_ok").exists():
        d(resourceId="com.autel.explorer:id/tv_ok").click()
        print('start dowloading File!')
        time.sleep(60)
        d.implicitly_wait(90)

    if d(resourceId="android:id/sem_title_default").exists():
    # d.implicitly_wait(5)
        d.swipe(0.5, 0.49, 0.5, 0.14)
        time.sleep(1)
    d.implicitly_wait(5)
    d(resourceId="android:id/text1", text=u"YouTube").click()
    print('Click Youtube share link!')
    time.sleep(5)  # facebook 的share 按钮在进入facebook 1~5秒内会可以点击
    title = 'AutelShareyoutube'+time.strftime('%H_%M_%S')
    d(resourceId="com.google.android.youtube:id/title_edit").set_text(title)
    time.sleep(0.5)
    d(resourceId="com.google.android.youtube:id/description_edit").set_text('A sample for testing share function.')
    time.sleep(0.5)
    d(resourceId="com.google.android.youtube:id/menu_upload_activity_done").click()
    time.sleep(60)
    d.implicitly_wait(60)
    # if d(resourceId="com.google.android.youtube:id/upload_status_detailed_message").exists():
    #     d(resourceId="com.google.android.youtube:id/upload_status_detailed_message",
    #       text=u"This video is ready to be watched.", className="android.widget.TextView", instance=1).exists()
    print('share completed!,ready to back to Autel Explorer')
    d.press('back')
    time.sleep(0.5)
    d.press('back')
    time.sleep(0.5)
    d.press('back')

#3-8 推特分享单个短视频：
def share_twitter_onevideo():
    d.set_fastinput_ime('True')
    # # 录第一个短视频
    # test.record()
    # time.sleep(0.5)
    # test.record()
    # time.sleep(1)
    test.test_into_Album_List()
    time.sleep(0.5)
    d.implicitly_wait(5)
    d(resourceId="com.autel.explorer:id/tv_album_select").click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    #选择第一个视频
    d(resourceId="com.autel.explorer:id/vf_list_selected").click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    #点分享按钮
    d(resourceId="com.autel.explorer:id/iv_list_share").click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    #下载
    if d(resourceId="com.autel.explorer:id/tv_ok").exists():
        d(resourceId="com.autel.explorer:id/tv_ok").click()
        print('start dowloading File!')
        time.sleep(30)
        d.implicitly_wait(60)
    #弹出分享菜单，上划
    if d(resourceId="android:id/sem_title_default").exists():
        # d.implicitly_wait(5)
        d.swipe(0.5, 0.49, 0.5, 0.14)
        time.sleep(1)
    # 选择要分享的app 如 twitter
    d.implicitly_wait(5)
    d(resourceId="android:id/text1", text=u"Tweet").click()
    print('Click twitter share link!')
    time.sleep(3)
    d.implicitly_wait(5)
    #进入分享的app，点击按钮 自动返回autel explorer
    d(resourceId="com.twitter.android:id/button_tweet").click()
    time.sleep(0.5)
    #返回到相册列表，点击返回图传界面
    d(resourceId="com.autel.explorer:id/tv_list_back").click()

#3-9 微信分享单个短视频
def share_wechat_onevideo():
    d.set_fastinput_ime('True')
    # # 录第一个短视频
    # test.record()
    # time.sleep(0.5)
    # test.record()
    # time.sleep(1)
    test.test_into_Album_List()
    time.sleep(0.5)
    d.implicitly_wait(5)
    d(resourceId="com.autel.explorer:id/tv_album_select").click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    # 选择第一个视频
    d(resourceId="com.autel.explorer:id/vf_list_selected").click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    # 点分享按钮
    d(resourceId="com.autel.explorer:id/iv_list_share").click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    # 下载
    if d(resourceId="com.autel.explorer:id/tv_ok").exists():
        d(resourceId="com.autel.explorer:id/tv_ok").click()
        print('start dowloading File!')
        time.sleep(30)
        d.implicitly_wait(60)
    # 弹出分享菜单，上划
    if d(resourceId="android:id/sem_title_default").exists():
        # d.implicitly_wait(5)
        d.swipe(0.5, 0.49, 0.5, 0.14)
        time.sleep(1)
    # 选择要分享的app 如 twitter
    d.implicitly_wait(5)
    d(resourceId="android:id/text1", text=u"WeChat").click()
    print('Click WeChat share link!')
    time.sleep(5)
    d.implicitly_wait(5)

    d(resourceId="com.tencent.mm:id/b8a").set_text('dydx')
    time.sleep(1)
    d.implicitly_wait(10)
    d(resourceId="com.tencent.mm:id/py").click()
    time.sleep(1)
    d.implicitly_wait(10)
    d(resourceId="com.tencent.mm:id/az_").click()
    time.sleep(5)
    d.press('back')
    time.sleep(1)
    d.press('back')
    time.sleep(1)
    d.press('back')



    # 进入分享的app，点击按钮 自动返回autel explorer

#3-10 instagram 分享单个视频：
def share_instagram_onevedio():
    d.set_fastinput_ime('True')
    # 录第一个短视频
    # test.record()
    # time.sleep(0.5)
    # test.record()
    # time.sleep(1)
    test.test_into_Album_List()
    time.sleep(0.5)
    d.implicitly_wait(5)
    d(resourceId="com.autel.explorer:id/tv_album_select").click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    # 选择第一个视频
    d(resourceId="com.autel.explorer:id/vf_list_selected").click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    # 点分享按钮
    d(resourceId="com.autel.explorer:id/iv_list_share").click()
    time.sleep(0.5)
    d.implicitly_wait(5)
    # 下载
    if d(resourceId="com.autel.explorer:id/tv_ok").exists():
        d(resourceId="com.autel.explorer:id/tv_ok").click()
        print('start dowloading File!')
        time.sleep(30)
        d.implicitly_wait(60)
    # 弹出分享菜单，上划
    if d(resourceId="android:id/sem_title_default").exists():
        # d.implicitly_wait(5)
        d.swipe(0.5, 0.49, 0.5, 0.14)
        time.sleep(1)
    # 选择要分享的app 如 twitter
    d.implicitly_wait(5)
    d(resourceId="android:id/text1", text=u"Feed").click()
    print('Click instragram share link!')
    time.sleep(5)
    d.implicitly_wait(5)
    #在instagram点击下一步。
    d(resourceId="com.instagram.android:id/button_next").click()
    time.sleep(1)
    d.implicitly_wait(5)
    d(resourceId="com.instagram.android:id/next_button_textview").click()
    time.sleep(1)
    d.implicitly_wait(5)
    d(resourceId="com.instagram.android:id/next_button_textview").click()
    time.sleep(10)
    d.press('back')
    time.sleep(1)
    d(resourceId="com.autel.explorer:id/tv_list_back").click()


#4-3 单张照片下载
def singlephoto_download():
    test.shot()
    test.test_into_Album()
    d(resourceId="com.autel.explorer:id/iv_preview_download").click()
    time.sleep(1)
    if d(resourceId="com.autel.explorer:id/edit_dg_content",text='Only JPEG images and videos 1080p resolution or less can be downloaded. Others should be copied using the USB cable or SD card.').exists():
        d(resourceId="com.autel.explorer:id/tv_ok").click()
    time.sleep(10)
    d.implicitly_wait(10)
    d(resourceId="com.autel.explorer:id/tv_preview_back").click()



#4-4单张照片删除
def singlephoto_del():
    # test.shot()
    test.test_into_Album()
    d(resourceId="com.autel.explorer:id/iv_preview_delete").click()
    time.sleep(0.5)
    d(resourceId="com.autel.explorer:id/tv_ok").click()
    time.sleep(5)
    d.implicitly_wait(10)
    d(resourceId="com.autel.explorer:id/tv_preview_back").click()


#4-5 单个视频预览
def singlevedio_preview():
    test.record()
    time.sleep(5)
    test.record()
    test.test_into_Album()
    time.sleep(1)
    d(resourceId="com.autel.explorer:id/iv_video_play").click()
    time.sleep(5)
    d.press('back')
    d(resourceId="com.autel.explorer:id/tv_preview_back").click()



#4-7 单个视频下载
def singvedio_download():
    test.record()
    time.sleep(0.5)
    test.record()
    test.test_into_Album()
    d(resourceId="com.autel.explorer:id/vf_preview_bottom_selected").click()
    time.sleep(0.5)
    d(resourceId="com.autel.explorer:id/iv_preview_download").click()

    if d(resourceId="com.autel.explorer:id/edit_dg_content").exists():
        d(resourceId="com.autel.explorer:id/tv_ok").click()
    time.sleep(30)

    d.implicitly_wait(30)
    if d(resourceId="com.autel.explorer:id/iv_preview_download").exists():
         d(resourceId="com.autel.explorer:id/tv_preview_back").click()

#4-8 单个视频删除
def singlevdeio_del():
    test.record()
    time.sleep(0.5)
    test.record()
    test.test_into_Album()
    time.sleep(1)
    d(resourceId="com.autel.explorer:id/vf_preview_bottom_selected").click()
    time.sleep(0.5)
    d(resourceId="com.autel.explorer:id/iv_preview_delete").click()
    print('click delete btn')
    time.sleep(0.5)
    d(resourceId="com.autel.explorer:id/tv_ok").click()
    print('confirm delete')

    time.sleep(2)

    d.toast.show('hello world')
    d(resourceId="com.autel.explorer:id/tv_preview_back").click()


#4-9 单个文件浏览切换
def singlemediaswitch():

    test.test_into_Album()
    d.swipe(0.8,0.3,0.15,0.3)
    time.sleep(1)
    d.swipe(0.8,0.3,0.15,0.3)
    time.sleep(2)
    d.swipe(0.15,0.3,0.8,0.3)
    time.sleep(1)
    d.swipe(0.15, 0.3, 0.8, 0.3)
    time.sleep(0.5)
    d(resourceId="com.autel.explorer:id/tv_preview_back").click()


#4-10 返回多张预览界面
def backtoMultipreview():
    test.test_into_Album_List()
    d(resourceId="com.autel.explorer:id/tv_list_back").click()


#5-1 视频播放
def vedioPlayback():
    # test.record()
    # time.sleep(3)
    # test.record()
    test.test_into_Album()
    time.sleep(0.5)
    d(resourceId="com.autel.explorer:id/iv_video_play").click()
    time.sleep(3)
    d.press('back')
    d(resourceId="com.autel.explorer:id/tv_preview_back").click()



#5-2 暂停和播放
def vdeioPlayandPause():
    # test.record()
    # time.sleep(10)
    # test.record()
    test.test_into_Album()
    time.sleep(0.5)
    d(resourceId="com.autel.explorer:id/iv_video_play").click()
    time.sleep(0.5)
    d(resourceId="com.autel.explorer:id/start").click()
    time.sleep(1)
    d(resourceId="com.autel.explorer:id/start").click()
    d.press('back')
    d(resourceId="com.autel.explorer:id/tv_preview_back").click()



#5-3播放时快进后退
def vedioBackForward():
    # test.record()
    # time.sleep(10)
    # test.record()
    test.test_into_Album()
    time.sleep(0.5)
    # d(resourceId="com.autel.explorer:id/iv_preview_download").click()
    # d.implicitly_wait(30)
    # if d(resourceId="com.autel.explorer:id/iv_preview_download").exists():
    d(resourceId="com.autel.explorer:id/iv_video_play").click()
    time.sleep(2)
    d.drag(0.251,0.946,0.45, 0.946)
    print('拖动')
    time.sleep(2)
    if d(resourceId="com.autel.explorer:id/progress").exists():
        d.drag(0.7, 0.946, 0.251, 0.946)
        print('拖动')
    else:
        d.click(0.5,0.5)
        d.drag(0.7,0.946,0.251,0.946)
        print("drag again")
    time.sleep(2)
    d.press('back')
    print('back')
    time.sleep(1)
    d(resourceId="com.autel.explorer:id/tv_preview_back").click()



#5-4暂停时快进后退
def vedioPausebackForward():
    # test.record()
    # time.sleep(10)
    # test.record()
    test.test_into_Album()
    time.sleep(0.5)
    # d(resourceId="com.autel.explorer:id/iv_preview_download").click()
    # d.implicitly_wait(30)
    # if d(resourceId="com.autel.explorer:id/iv_preview_download").exists():
    d(resourceId="com.autel.explorer:id/iv_video_play").click()
    time.sleep(6)
    d.click(0.3,0.3)
    time.sleep(0.5)
    d(resourceId="com.autel.explorer:id/start").click()
    d.drag(0.251, 0.946, 0.45, 0.946)
    time.sleep(3)
    if d(resourceId="com.autel.explorer:id/progress").exists():
        d.drag(0.7, 0.946, 0.251, 0.946)
    else:
        d.click(0.5, 0.5)
        d.drag(0.7, 0.946, 0.251, 0.946)
    d.press('back')
    d(resourceId="com.autel.explorer:id/tv_preview_back").click()

#6-1 APP上退出相册
def Album_backtoCamera():
    test.test_into_Album()
    time.sleep(1)
    d(resourceId="com.autel.explorer:id/tv_preview_back").click()









#-------------------------------------------------------------------------------

# share_facebook_onephoto()
# share_facebook_multiphoto()
# share_twitter_onephoto()
# share_twitter_multiphoto()
# share_instagram_onephoto()
# share_wechat_onephoto()
# share_wechat_multiphoto()
# share_facebook_onephoto()
# share_facebook_multivideo()
# share_youtube_onevideo()
# share_youtube_multivideo()
# share_twitter_onevideo()
# share_facebook_multivideo()
# share_wechat_onevideo()
# share_instagram_onevedio()
# singlephoto_download()
# singlephoto_del()
# singlevedio_preview()
# singvedio_download()
# singlephoto_del()
# singlemediaswitch()
# vedioPlayback()
# vdeioPlayandPause()
# vedioBackForward()
# vedioPausebackForward()
# Album_backtoCamera()
i = 0
while True:
    i = i+1
    print("\n第", i , '次运行开始\n--------------------------------------------------------------------------')
    print(datetime.datetime.now())


    #
    # print('\n2-1正在录像，不能进入相册')
    # test_Album_Video()
    # time.sleep(2)
    #
    # print('\n2-1.2正在拍照不能进入相册')
    # test_Album_Pict()
    # time.sleep(2)
    #
    # print('\n2-3 .1下载文件')   #not recycle
    # test_Album_Downing()
    # time.sleep(2)


    print('\n2-3相册列表界面单张下载')
    test_Album_Down()
    time.sleep(2)

    print('\n2-3.3相册列表多张下载')    #暂时不循环用，单独测
    test_Album_List_multipleDown()
    time.sleep(2)

    print('\n2-5  多张删除')
    test_Album_List_Dele()
    time.sleep(2)

    # time.sleep(60)

    print('\n准备照片素材')
    preparePhoto2()


    '''

    print('\n3-1 .1分享facebook 单张')
    share_facebook_onephoto()
    time.sleep(2)

    print('\n3-1 .2分享facebook 多张')
    share_facebook_multiphoto()
    time.sleep(2)



    print('\n3-3.1分享twitter 单张')
    share_twitter_onephoto()
    time.sleep(2)

   

    print('\n3-4.1，微信单张分享')
    share_wechat_onephoto()
    time.sleep(2)

    print('\n3-4.2，微信多张分享')
    share_wechat_multiphoto()
    time.sleep(2)


    print('\n-5.1 instagram 分享单张')
    share_instagram_onephoto()
    time.sleep(2)


    print('\n准备视频素材！')
    prepareVideos3()


    print('\n3-6.1 facebook 分享单个短视频')
    share_facebook_onevideo()
    time.sleep(2)

    print('\n3-6.2 facebook 分享多个短视频')  #可运行，太费时间，
    share_facebook_multivideo()
    time.sleep(2)


    # print('\n3-7.1 youtube分享单个短视频')   #不循环
    # share_youtube_onevideo()
    # time.sleep(2)

    # print('\n3-7.2youtube分享多个短视频') #上传有问题
    # share_youtube_multivideo()
    # time.sleep(2)
    


    print('\n3-8 推特分享单个短视频')
    share_twitter_onevideo()
    time.sleep(2)

    print('\n3-9 微信分享单个短视频')
    share_wechat_onevideo()
    time.sleep(2)

    print('\n3-10 instagram 分享单个视频')
    share_instagram_onevedio()
    time.sleep(2)


    print('\n4-3 单张照片下载')
    singlephoto_download()
    time.sleep(2)

    print('\n4-4单张照片删除')
    singlephoto_del()
    time.sleep(2)

    print('\n4-5 单个视频预览')
    singlevedio_preview()
    time.sleep(2)

    print('\n4-7 单个视频下载')
    singvedio_download()
    time.sleep(2)

    print('\n4-8 单个视频删除  ')
    singlevdeio_del()
    time.sleep(2)

    print('\n 4-9 单个文件浏览切换 ')
    singlemediaswitch()
    time.sleep(2)

    print('\n4-10 返回多张预览界面  ')
    backtoMultipreview()
    time.sleep(2)

    print("准备视频素材")

    test.record()
    time.sleep(10)
    test.record()


    print('\n 5-1 视频播放 ')
    vedioPlayback()
    time.sleep(2)

    print('\n 5-2 暂停和播放 ')
    vdeioPlayandPause()
    time.sleep(2)

    print('\n 5-3播放时快进后退 ')
    vedioBackForward()
    time.sleep(2)

    print('\n5-4暂停时快进后退  ')
    vedioPausebackForward()
    time.sleep(2)

    print('\n 6-1 APP上退出相册 ')
    Album_backtoCamera()
    time.sleep(2)
    '''

    print("\n第", i, '次运行结束\n--------------------------------------------------------------------------')
    print(datetime.datetime.now())