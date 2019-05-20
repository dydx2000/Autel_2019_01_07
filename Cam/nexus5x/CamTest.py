import datetime
import time
import logging
# logging.basicConfig(level=logging.ERROR,
#                     format='\r\n%(asctime)s %(filename)s [line:%(lineno)d]  %(levelname)s  %(funcName)s %(message)s',
#                     datefmt='%a,%d %b %Y %H:%M:%S',
#                     filename='CamShots.log',
#                     filemode='a')
import random
# import Autel_Explorer.Camera.uiautomator2_cam_shots as uiauto
# import Autel_Explorer.Camera.uiautomator2_cam_shots_filter as uiauto
import Cam.nexus5x.uiautomator2_cam_shots_filter as uiauto
# import Autel_Explorer.Camera.uiautomator2_cam_shots_test as uiauto
import uiautomator2 as u2

d = uiauto.d
# d.implicitly_wait(60)
# d.wait_timeout = 60
test=uiauto.Camera()
# time.sleep(1)


# 1-1 app断开连接时相机功能是否可用 "1.app未连接飞行器时，点击首页“GO FLY”按钮，进入模块选择界面
# 2.点击相机模块 ，进入相机界面"
def camtohometocam():
    d(resourceId="com.autel.explorer:id/rl_left").click()
    time.sleep(1)
    d(resourceId="com.autel.explorer:id/tv_autel_home_start").click()

'''1-1, 1-2 app连上或断开飞行器，首页 --> 相机界面 '''
def homeTocam():
    d(resourceId="com.autel.explorer:id/tv_autel_home_start").click()

''' 1-3退出相机功能界面 '''
def home():
    time.sleep(1)
    d(resourceId="com.autel.explorer:id/rl_left").click()


'''2-1 拍照模式：单拍（默认拍照模式是单拍）'''
def singleShot2_1():
    test.SetPictureMode('SINGLE')
    test.shot()
    time.sleep(3)


''' 2-2 拍照模式：Burst连拍  3,5,7,10,14,'''
def burstShot2_2():
    listPara = ["3", "5", "7", "10", "14"]
    random.shuffle(listPara)
    for num in listPara:

        test.SetPictureMode('BURST',num)
        # num=int(num)+5
        test.shot()
        time.sleep(5)
        # time.sleep(num)

    test.SetPictureMode('SINGLE')
    time.sleep(3)

'''2-3 拍照模式：AEB连拍 3,5 '''
def AEBshot2_3():
    test.SetPictureMode('AEB','3')
    test.shot()
    time.sleep(5)

    test.SetPictureMode('AEB','5')
    test.shot()
    time.sleep(5)

    test.SetPictureMode('SINGLE')
    time.sleep(3)


'''2-4 拍照模式：定时拍 Auto'''

def auto_timmelapse2_4():
    test.SetPictureExpo('AUTO')
    test.scrollToFunc('FORMAT')
    listPara = ["5s", "7s", "10s", "20s", "30s", "60s"]
    # if d(resourceId="com.autel.explorer:id/tv_first_para", text=u"RAW+JPG").exists() or  d(resourceId=
    #      "com.autel.explorer:id/tv_first_para", text=u"RAW").exists():
    #
    #     listPara = ["5s", "7s", "10s", "20s","30s","60s"]
    # a =random.randint(len(listPara))
    # random.shuffle(listPara)        #打乱列表顺序
    print(listPara)
    for num in listPara:
        test.SetPictureMode('TIMELAPSE',num)
        print('timelapse',num)
        delay = int(num[:-1])
        # d(resourceId="com.autel.explorer:id/iv_camera_outer").click()
        # if d(resourceId="com.autel.explorer:id/toast_msg_tv", text='SD card is full').exists():
        #     test.camSetFormatsdcard('yes')
        #     time.sleep(8)
        #     print("reshot()")
        test.shot()
        time.sleep(delay+3)
        # d(resourceId="com.autel.explorer:id/iv_camera_outer").click()
        test.shot()
        time.sleep(5)

        # time.sleep(delay+2)
        # test.shot()
        # time.sleep(5)

    test.SetPictureMode('SINGLE')
    time.sleep(5)

'''2-5 拍照模式：定时拍 MANUAL'''
def manual_Timelapse2_5():
    test.SetPictureExpo('MANUAL')
    test.scrollToFunc('FORMAT')
    listPara = ["2s", "5s", "7s", "10s", "20s", "30s", "60s"]
    # if d(resourceId="com.autel.explorer:id/tv_first_para", text=u"RAW+JPG").exists() or d(resourceId=
    #                                                                                       "com.autel.explorer:id/tv_first_para",
    #                                                                                       text=u"RAW").exists():
    #     listPara = ["5s", "7s", "10s", "20s", "30s", "60s"]
    listPara = ["5s", "7s", "10s", "20s", "30s", "60s"]
    random.shuffle(listPara)  #打乱列表顺序
    for num in listPara:
        test.SetPictureMode('TIMELAPSE', num)
        print('timelapse', num)
        delay = int(num[:-1])
        test.shot()
        time.sleep(delay + 3)
        test.shot()
        time.sleep(5)


'''2-6 照片格式：JPG '''
def JPG2_6():
    #jpg 单拍
    test.SetPictureFomat('JPG')
    test.SetPictureMode('SINGLE')
    test.shot()

    '''
    time.sleep(2)

    #jpg BURST 连拍
    test.SetPictureFomat('JPG')

    for num in ['3','5','7','10','14',]:
        test.SetPictureMode('BURST',num)
        test.shot()
        time.sleep(5)

    #jpg TIMELAPSE 延时拍
    test.SetPictureFomat('JPG')
    for num in ['5s','7s','10s','20s','30s','60s']:
        test.SetPictureMode('TIMELAPSE',num)
        test.shot()
        time.sleep(61)
        test.shot()

    #jpg AEB
    test.SetPictureFomat('JPG')
    for num in ['3','5']:
        test.SetPictureMode('AEB',num)
        test.shot()
        time.sleep(5)
        test.shot()

    test.SetPictureFomat('JPG')
    test.SetPictureMode('SINGLE')
    test.shot()
    time.sleep(3)
    '''


'''2-7 照片格式：RAW '''
def RAW2_7():
    #RAW 单拍
    test.SetPictureFomat('RAW')
    test.SetPictureMode('SINGLE')
    test.shot()

    time.sleep(2)
    '''

    #RAW BURST
    test.SetPictureFomat('RAW')

    for num in ['3','5','7','10','14',]:
        test.SetPictureMode('BURST',num)
        test.shot()
        time.sleep(2)

    #RAW TIMELAPSE
    test.SetPictureFomat('RAW')
    for num in ['5s','7s','10s','20s','30s','60s']:
        test.SetPictureMode('TIMELAPSE',num)
        test.shot()
        time.sleep(61)
        test.shot()

    #RAW AEB
    test.SetPictureFomat('RAW')
    for num in ['3','5']:
        test.SetPictureMode('AEB',num)
        test.shot()
        time.sleep(5)
        test.shot()

    test.SetPictureFomat('JPG')
    test.SetPictureMode('SINGLE')
    test.shot()
    time.sleep(3)
    '''

'''2-8 照片格式：JPG+RAW  '''
def RAWJPG2_8():
    # RAW 单拍
    test.SetPictureFomat('RAW')
    test.SetPictureMode('SINGLE')
    test.shot()
    time.sleep(2)

    '''
    # RAW+JPG BURST
    test.SetPictureFomat('RAW+JPG')

    for num in ['3','5','7','10','14']:
        test.SetPictureMode('BURST',num)
        test.shot()
        time.sleep(2)

    #RAW+jpg TIMELAPSE

    test.SetPictureFomat('RAW+JPG')
    for num in ['5s','7s','10s','20s','30s','60s']:
        test.SetPictureMode('TIMELAPSE',num)
        test.shot()
        time.sleep(61)
        test.shot()

    #RAW+JPG AEB
    test.SetPictureFomat('RAW+JPG')
    for num in ['3','5']:
        test.SetPictureMode('AEB',num)
        test.shot()
        time.sleep(5)

    test.SetPictureFomat('JPG')
    test.SetPictureMode('SINGLE')
    test.shot()
    time.sleep(3)
    '''

'''2-9 照片大小：4：3（4000x3000）'''
def size43_2_9():
    test.SetPictureSize('4000x3000')
    test.shot()

    '''
    for i in [JPG2_6(),RAWJPG2_8()]:
        i
    print('\napp重置')
    camSetFormatReset3_24()
    '''

    time.sleep(2)

'''2-10 照片大小：16：9（4000x2250）'''
def size169_2_10():
    test.SetPictureSize('4000x2250')
    '''
    for i in [RAW2_7(),RAWJPG2_8()]:
        i
    '''
    test.shot()
    time.sleep(2)

##------------------------录相--------------------------###

# 2-1 NTSC:视频尺寸
''' 2-1 NTSC:视频尺寸

"1.点击NTSC/PAL，选择NTSC(默认值)
2.点击视频大小，选择4K+（4096x2160）
或选择4K（3840x2160）
或选择2.7K（2704x1520）
或选择1080P（1920x1080）
或选择720P（1280x720）
3.其他参数为默认参数
4.点击录像按钮，进行录像"
'''
''' 2-1 NTSC:视频尺寸'''
def NTSC2_1():
    test.setVedioStandard('NTSC')
    for res in ['4K+',"4K",'2.7K','1080P','720P']:
        test.setVideoReso(res)
        test.fast_record() #开始录
        time.sleep(5)
        #录相中返回首页,再返回,还在继续录相
        try:
            d(resourceId="com.autel.explorer:id/rl_left").click()
            time.sleep(1)
            d(resourceId="com.autel.explorer:id/tv_autel_home_start").click()
        except:
            pass
        time.sleep(10)
        test.stop_record() #停止录
    time.sleep(2)
    test.setVideoReso('4K')

# '''2-2 PAL:视频尺寸 '''
def PAL2_2():
    test.setVedioStandard('PAL')
    for res in ["4K+","4K","2.7K","1080P",'720P']:
        test.setVideoReso(res)
        time.sleep(3)
        test.fast_record() #开始录
        time.sleep(5)
        # 录相中返回首页,再返回,还在继续录相
        d(resourceId="com.autel.explorer:id/rl_left").click()
        time.sleep(1)
        d(resourceId="com.autel.explorer:id/tv_autel_home_start").click()
        time.sleep(5)
        test.stop_record()#停止录
        time.sleep(2)
    time.sleep(2)
    test.setVideoReso('4K')

'''2-3 视频格式：MOV'''
def mov2_3():
    test.setVedioFormat('MOV')
    time.sleep(3)
    test.fast_record()
    time.sleep(5)
    test.stop_record()

''' 2-4 视频格式：MP4'''
def mp4_2_4():
    test.setVedioFormat('MP4')
    time.sleep(3)
    test.fast_record()
    time.sleep(5)
    test.stop_record()
    time.sleep(2)

''' 2-6 视频编码格式'''
def H264_2_6():
    test.camSetVideoEncoding('H.264')
    time.sleep(3)
    test.fast_record()
    time.sleep(5)
    test.stop_record()
    time.sleep(5)

''' 2-7 视频编码格式'''
def H265_2_7():
    test.camSetVideoEncoding('H.265')
    time.sleep(3)
    test.fast_record()
    time.sleep(5)
    test.stop_record()
    time.sleep(5)

''' 2-8 PIV功能 '''
def PIV2_8():
    # for num in ['5S','10S','30S','60S','MANUAL']:
    for num in ['5S','10S','30S','MANUAL']:

        test.setVideoPIV(num)
        if num =='MANUAL':
            print('PIV MANUAL set.')
            time.sleep(3)
            test.fast_record()
            time.sleep(5)
            test.stop_record()
            time.sleep(5)
        else:
            num =int(num[:-1])+2
            print(num)
            time.sleep(3)

            test.fast_record()
            time.sleep(num)
            test.stop_record()
            time.sleep(5)

    time.sleep(2)

'''3-1 3-2 3-3风格：标准 风格：柔和 风格：风光 '''
def stytlePreset3_1():
    for num in  ['STD.','NEUT.','LAND.']:
        test.setVedioStyle(num)
        time.sleep(3)
        test.fast_record()
        time.sleep(5)
        test.stop_record()
        time.sleep(2)

'''3-4 风格：自定义 '''
def styleSelfDef3_4():

    for num in ["-3 ±0 ±0","-2 ±0 ±0","±0 +1 ±0","±0 +2 ±0",'±0 ±0 +2']:
        test.setVedioStyle(num) #注意 "." 不要忘了.
        time.sleep(3)
        test.record()
        time.sleep(5)
        test.stop_record()
        time.sleep(2)

''' 3-5 白平衡：自动  3-6 白平衡：晴天 3-7 白平衡：阴天 3-8 白平衡：白炽灯 '''
def WBPreSet3_5():
    test.SetPictureMode('SINGLE')
    for num in ['AUTO','SUNNY','CLOUDY','INCAN','NEON']:
        test.SetPictureWB(num)
        test.shot()
        time.sleep(2)

'''3-10 白平衡：自定义'''
def WBSelfDef3_10():
    test.SetPictureMode('SINGLE')
    for num in ['2000K','3000K','2900K','4200K','10000K','8000K','2100K','5600K','2300K']:
        test.SetPictureWB(num)
        test.shot()
        time.sleep(2)


'''3-11 色彩 '''
def color3_11():
    listPara = ["NONE", "LOG", "VIVID", "B&W", "ART", "FILM","BEACH","DREAM","CLASSIC","NOSTALGIC"]
    random.shuffle(listPara)
    for num in  listPara:
        test.SetPictureColor(num)
        test.shot()
        time.sleep(2)


'''3-12 拍摄模式：自动模式（A档）'''
def expoatuoshot3_12():
    test.SetPictureExpo('AUTO')
    test.shot()
    time.sleep(3)


''' 3-13  拍摄模式：手动模式（M档）'''
def expomanualshot():
    test.SetPictureExpo('MANUAL')
    test.shot()
    time.sleep(3)


'''3-14 A档：EV '''
def autoEV3_14():
    listPara = ["-3.0", "-2.7", "-2.3", "-2.0",
                                               # "-1.7", "-1.3", "-1.0",
                #"-0.7", "-0.3", "0","+0.3","+0.7",
                        "+1.0","+1.3","+1.7","+2.0","+2.3","+2.7","+3.0"]
    random.shuffle(listPara)
    print(listPara)
    for num in listPara:
        test.SetpictureEv(num)
        # test.shot()
        test.fast_shot()
        time.sleep(2)


    time.sleep(2)

'''3-15 M档：ISO '''
def manualISO3_15():

    listPara = ["100","200", "400", "800", "1600", "3200"]
    random.shuffle(listPara)
    print(listPara)
    for num in listPara:
        test.SetPictureIso(num)
        test.shot()
        time.sleep(2)


'''3-16 M档：快门 '''
def manualShutter3_16():
    listPara = ["1/8000", "1/6000", "1/5000",
                "1/4000", "1/3200", "1/2500", "1/2000", "1/1600", "1/1250", "1/1000",
                           "1/800", "1/640", "1/500",
                           "1/400", "1/320", "1/240", "1/200", "1/160", "1/120", "1/100", "1/80", "1/60", "1/50", "1/40",
                           "1/30", "1/25", "1/20", "1/15", "1/12.5",
                            "1/10", "1/8", "1/6.25", "1/5", "1/4", "1/3", "1/2.5", "1/2", "1/1.67", "1/1.25",
                            "1\"", "1.3\"",
                           "1.6\"", "2\"", "2.5\"", "3\"", "3.2\"",
                            "4\"", "5\"", "6\"", "8\""
                            ]
    random.shuffle(listPara)
    print(listPara)
    for num in listPara:
        print(num)
        test.SetPictureShutterOP(num)
        test.shot()
        if num.endswith("\""):
            num = int(float(num[0:-1]))
            time.sleep(num+5)
        else:
            time.sleep(5)

'''3-17 AE点测光模式 '''
def AE3_17():

    test.SetPictureExpo("AUTO")
    time.sleep(2)
    d.click(0.5, 0.5)
    time.sleep(5)
    d.click(0.6,0.3)

    test.SetPictureExpo("MANUAL") #manual 模式下不不能AE测光
    time.sleep(2)
    d.click(0.6,0.6)
    time.sleep(2)

'''3-18 数码变焦 '''
def digitalzoomshot3_18():

    listPara = ["1.0X", "2.0X", "3.0X", "4.0X","5.0X","6.0X","7.0X","8.0X"]
    random.shuffle(listPara)
    print(listPara)
    for num in listPara:
        test.SetPictureDigizoom(num)
        time.sleep(1)
        test.shot()
        time.sleep(5)
        try:
            d(resourceId="com.autel.explorer:id/rl_left").click()
            time.sleep(3)
            d(resourceId="com.autel.explorer:id/tv_autel_home_start").click()
            time.sleep(8)
        except:
            pass

    test.SetPictureDigizoom('1.0X')

'''3-19 云台角度调节 '''

def gimbal3_19():

    listPara = ['0°','30°','45°','50°','60°','90°']
    for num in listPara:
        test.GimbalAngle(num)
        time.sleep(2)
    test.GimbalAngle('0°')

''' 3-20  直方图 '''
def camsetHis3_20():
    test.camSetHis('on')
    try:
        d(resourceId="com.autel.explorer:id/rl_left").click()
    except:
        print('could not find the button for back to start page!')
    time.sleep(5)

    try:
        d(resourceId="com.autel.explorer:id/tv_autel_home_start").click()
    except:
        print('Could not find start button')
    time.sleep(8)
    test.fast_record()
    time.sleep(5)
    test.stop_record()
    time.sleep(2)
    test.camSetHis('off')


''' 3-21  过曝警告 '''
def camsetOverExp3_21():
    test.camSetOverExp('on')
    time.sleep(1)
    try:
        d(resourceId="com.autel.explorer:id/rl_left").click()
    except:
        pass
    time.sleep(3)
    try:
        d(resourceId="com.autel.explorer:id/tv_autel_home_start").click()
    except:
        pass
    time.sleep(3)
    test.camSetOverExp('off')
    time.sleep(1)
    d.click(0.47, 0.47)
    time.sleep(2)

''' 3-22  抗闪烁  '''
def camSetAntiFlicker3_22():
    listPara = ['Auto','50Hz','60Hz']
    for num in listPara:
        test.camSetAntiFlicker(num)
        time.sleep(2)
        # d.click(0.47, 0.47)
        test.fast_record()
        time.sleep(5)
        test.stop_record()
        time.sleep(2)

    time.sleep(2)

''' 3-23  网格  '''
def camSetGrid3_23():
    listPara = ['None','Grid','Grid + Line']
    for num in listPara:
        test.camSetGrid(num)
        # time.sleep(1)
        # test.shot() #  有问题，拍照后，录相延时不会停。
        time.sleep(5)
        test.fast_record()
        time.sleep(5)
        test.stop_record()
        time.sleep(5)
    test.camSetGrid('None')
    # d.click(0.47, 0.47)
    time.sleep(2)

''' 3-24  重置  '''
def camSetFormatReset3_24():

        test.camSettingsReset()
        time.sleep(20)

''' 3-25  格式化SD卡  '''
def camSetFormatsdcard3_25():
    for num in ['yes','no']:
        test.camSetFormatsdcard(num)
        time.sleep(5)

''' 3-26  相机版本号  '''
def camSetVersion3_26():

        try:
            d.implicitly_wait(5.0)
            d(resourceId="com.autel.explorer:id/rl_camera_setting").click()
        except:
            print('进入相机通用设置失败！')
            test.catchError()
        time.sleep(1)
        d.swipe(0.77, 0.8, 0.77, 0.4)
        time.sleep(1)
        d.swipe(0.77, 0.8, 0.77, 0.35)
        time.sleep(1)

        try:
            d.implicitly_wait(5.0)
            i=d(resourceId="com.autel.explorer:id/item_general_setting_value_tv", textStartsWith='V').get_text()
            print(i)
            d.click(0.3,0.5)

        except:
            print('获取相机版本失败!')
            d.click(0.3,0.5)


''' 3-27  全屏/退出全屏  '''
def camSetFullScreen3_27():
    d.swipe(0.475, 0.241,0.472, 0.696)
    time.sleep(1)
    d.click(0.47, 0.47)
    time.sleep(1)


timestamp = datetime.datetime.now()
i=0

while True:
    i+=1

    print('___________________________第 %d 轮开始____________________________'%i)
    print(datetime.datetime.now())


    singleShot2_1()
    time.sleep(3)


    print('\nBURST 延时拍照')
    burstShot2_2()
    time.sleep(3)

    print('\nAEB拍照')
    AEBshot2_3()
    time.sleep(3)

    print('\nTimelapse')
    auto_timmelapse2_4()
    time.sleep(3)

    print("\nJPG格式拍照")
    JPG2_6()
    time.sleep(3)

    print("\nRAW格式拍照")
    RAW2_7()
    time.sleep(3)

    print("\nRAW + JPG格式拍照")
    RAWJPG2_8()
    time.sleep(3)

    print('\照片大小4:3拍照')
    size43_2_9()
    time.sleep(3)

    print('\照片大小16:9拍照')
    size169_2_10()
    time.sleep(3)

    print('\n视频格式mov录相')
    mov2_3()
    time.sleep(3)

    print("\n视频格式mp4 录相")
    mp4_2_4()
    time.sleep(3)



    print('\n预设风格')
    stytlePreset3_1()
    time.sleep(5)

    '''
    print('\n自定义风格')
    styleSelfDef3_4()
    time.sleep(5)  #  停在这里！
    '''

    print('\n白平衡预设')
    WBPreSet3_5()
    time.sleep(5)   #pass


    print('\n自定义白平衡')
    WBSelfDef3_10()
    time.sleep(5)     #pass

    print('\n色彩')
    color3_11()
    time.sleep(5)  #pass

    print('\n自动曝光')
    expoatuoshot3_12()
    time.sleep(5)

    print('\n手动曝光')
    expomanualshot()
    time.sleep(5) #pass

    print('\nEV')
    autoEV3_14()
    time.sleep(5)  #pass


    print('\nISO')
    manualISO3_15()
    time.sleep(5) #pass


    print('\n快门')
    manualShutter3_16()
    time.sleep(3)   #pass

    print('\nAE')
    AE3_17()
    time.sleep(3)  #pass

    print('\n数码变焦')
    digitalzoomshot3_18()
    time.sleep(3)  #pass

    print('\n云台角度')
    gimbal3_19()
    time.sleep(10)  #pass


    print('\n抗闪烁')
    camSetAntiFlicker3_22()
    time.sleep(5)  #pass

    print('\nH264')
    H264_2_6()
    time.sleep(5)   #pass

    print('\nH265')
    H265_2_7()
    time.sleep(5)   #pass

    print('\napp重置')
    camSetFormatReset3_24()
    time.sleep(120)


    print('\nPIV视频录制')
    PIV2_8()
    time.sleep(5)  #pass



    print('\n显示柱状图')
    camsetHis3_20()
    time.sleep(5)   #pass


    print('\n网格设置')
    camSetGrid3_23()
    time.sleep(5)   #pass

    print('\n过曝')
    camsetOverExp3_21()
    time.sleep(5)     #pass

    print('\n相机版本')
    camSetVersion3_26()
    time.sleep(5)    #pass

    print('\n格式化sd卡')
    camSetFormatsdcard3_25()
    time.sleep(20)

    # print('\napp重置')
    # camSetFormatReset3_24()
    # time.sleep(120)

    time.sleep(30)
    print('___________________________第 %d 轮结束____________________________' % i)
    print(datetime.datetime.now())


