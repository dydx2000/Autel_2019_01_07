#conding：utf-8
import time
from PIL import Image
import logging
import os
# file = 'CamShots_' + time.strftime("%Y-%m-%d_%H_%M_%S") + ".log"
# fp = os.open(file,w)
logging.basicConfig(level=logging.INFO,
                    format="\n%(asctime)s %(filename)s   line:%(lineno)d  %(levelname)s  %(funcName)s %(message)s",
                    datefmt='%Y %m %d %H:%M:%S',
                    # filename='CamShots.log',
                    # filename='CamShots_' + time.strftime("%Y-%m-%d_%H_%M_%S") + ".log",
                    filename='CamShots.log',

                    filemode='a')

# logging.basicConfig(level=logging.ERROR,
#                     format='\n\r%(asctime)s %(filename)s   line:%(lineno)d  %(levelname)s  %(funcName)s %(message)s',
#                     datefmt='%a,%d %b %Y %H:%M:%S',
#                     filename='CamShots.log',
#                     filemode='a')
logger = logging.getLogger(__name__)
import random

import uiautomator2 as u2


pkg_name='com.autel.explorer'
# d=u2.connect_wifi('192.168.1.17') #samsung s7
d=u2.connect_wifi('192.168.1.13') #google nexus
# d=u2.connect_wifi('10.250.16.69') #google nexus

# d.wait_activity(30)
# d.wait_timeout = 20.0


class ParaError(Exception):
    pass
    # print("Parameter input error")

class SwitchError(Exception):
    pass
    # print("Switch windows Error!")

class Camera:

    def __init__(self):
        pass

    #拍照
    def shot(self):
        d.implicitly_wait(5.0)
        #在拍照画面
        try:
            if  d(resourceId="com.autel.explorer:id/rel_camera_takephoto_controller").exists():
                try:
                    d(resourceId="com.autel.explorer:id/rel_camera_takephoto_controller").click()
                    print("shot()")
                except:
                    self.catchError()

                if d(resourceId="com.autel.explorer:id/toast_msg_tv",text='SD card is full').exists():
                    self.camSetFormatsdcard('yes')
                    time.sleep(8)
                    print("reshot()")
                    try:
                        d.implicitly_wait(10.0)
                        d(resourceId="com.autel.explorer:id/rel_camera_takephoto_controller").click()
                    except:
                        self.catchError()

            # 在录相界面
            else:
                if d(resourceId="com.autel.explorer:id/iv_camera_record_controller").exists():
                    try:
                        d(resourceId="com.autel.explorer:id/iv_mode_switcher").click()
                        time.sleep(0.5)
                        d.implicitly_wait(5.0)
                        if d(resourceId="com.autel.explorer:id/rel_camera_takephoto_controller").exists():
                            d(resourceId="com.autel.explorer:id/rel_camera_takephoto_controller").click()
                            print('switched to photo caputure windows.')

                    except:
                        self.catchError()

                    if d(resourceId="com.autel.explorer:id/toast_msg_tv", text='SD card is full').exists():
                        self.camSetFormatsdcard('yes')
                        time.sleep(8)
                        print("reshot()")
                        try:
                            d.implicitly_wait(10.0)
                            d(resourceId="com.autel.explorer:id/rel_camera_takephoto_controller").click()
                        except:
                            self.catchError()
        except:
            pass

    #快拍
    def fast_shot(self):
        try:
            d(resourceId="com.autel.explorer:id/rel_camera_takephoto_controller").click()
        except:
            logger.info("can't find shot button!")

        if d(resourceId="com.autel.explorer:id/toast_msg_tv", text='SD card is full').exists():
            self.camSetFormatsdcard('yes')
            time.sleep(8)
            print("reshot()")
            try:
                d.implicitly_wait(10.0)
                d(resourceId="com.autel.explorer:id/rel_camera_takephoto_controller").click()
            except:
                self.catchError()

    #捕获异常
    def catchError(self):

        logger.exception('error caught')
        timestamp = time.strftime('%Y-%m-%d_%H-%M-%S')
        errpath ='./errorshots/'
        errpic = errpath +  timestamp + '_Error.jpg'
        d.screenshot(errpic)
    def starlog(self):
        logging.info("function start")

    def endlog(self):
        logging.info("fundtion end")
    # 确认在主画面
    def mainWindowConfirm(self):  # 确认在相机主画面
        # time.sleep(1)
        # 如果有拍照按钮,则确认是照相模式啥都不做了
        if d(resourceId="com.autel.explorer:id/rel_camera_controller").exists():
        # if d(resourceId="com.autel.explorer:id/iv_camera_outer").exists():
            print('Is in shotting or recording window')

        # ("指南针按钮 "): 说明在地图模式,点击小图切换到相机
        elif d(resourceId="com.autel.explorer:id/compass_iv").exists():
            print('Now is in the map window.')
            d.click(0.14, 0.268)
            time.sleep(3)

            # 切换成功的情况
            if d(resourceId="com.autel.explorer:id/rel_camera_controller").exists():  # 切换成功的情况
                print('Is in shotting or recording window.')

            # 切换不成功的情况
            else:
                d(resourceId="com.autel.explorer:id/intercept_img_shrink").click()  # 把小图展开,再点小图中央切换到拍摄画面,
                time.sleep(2)
                d.click(0.14, 0.268)
                time.sleep(1)
                d.implicitly_wait(5.0)
                if d(resourceId="com.autel.explorer:id/rel_camera_controller").exists():
                    print('Is in shotting or recording window.')

        # 在相册画面
        elif d(resourceId="com.autel.explorer:id/tv_enter_album_list").exists():
            d(resourceId="com.autel.explorer:id/tv_preview_back").click()
            time.sleep(0.5)
            d.implicitly_wait(5.0)
            if d(resourceId="com.autel.explorer:id/rel_camera_controller").exists():
                print('Is in shotting or recording window.')
        # 在相册列表画面
        elif d(resourceId="com.autel.explorer:id/tv_album_select").exists():
            d(resourceId="com.autel.explorer:id/tv_list_back").click()
            time.sleep(0.5)
            d.implicitly_wait(5.0)
            if d(resourceId="com.autel.explorer:id/rel_camera_controller").exists():
                print('Is in shotting or recording window.')
        # 在开始界面
        elif d(resourceId="com.autel.explorer:id/tv_autel_home_start").exists():
            d(resourceId="com.autel.explorer:id/tv_autel_home_start").click()
            time.sleep(8)
            time.sleep(0.5)
            d.implicitly_wait(5.0)
            if d(resourceId="com.autel.explorer:id/rel_camera_controller").exists():
                print('Is in shotting or recording window.')
        # 在智能飞行界面
        elif d(text=u"Intelligent Flight").exists():
            # 点击相机按钮
            d(resourceId="com.autel.explorer:id/model_choice_bg").click()
            time.sleep(0.5)
            d.implicitly_wait(5.0)
            if d(resourceId="com.autel.explorer:id/rel_camera_controller").exists():
                print('Is in shotting or recording window.')
        # 在通用设置界面
        elif d(resourceId="com.autel.explorer:id/tv_setting_title").exists():
            # 点击关闭
            d(resourceId="com.autel.explorer:id/iv_setting_close").click()

            time.sleep(0.5)
            d.implicitly_wait(5.0)
            if d(resourceId="com.autel.explorer:id/rel_camera_controller").exists():
                print('Is in shotting or recording window.')
        # 在相机设置界面
        elif d(resourceId="com.autel.explorer:id/camera_general_setting_title").exists():
            d.click(0.5, 0.5)  # 画面中央点一下跳出
            time.sleep(0.5)
            d.implicitly_wait(5.0)
            if d(resourceId="com.autel.explorer:id/rel_camera_controller").exists():
                print('Is in shotting or recording window.')

        elif d(resourceId="com.autel.explorer:id/warn_history_title_tv").exists():  # 在飞机状态画面
            d.click(0.5, 0.5)  # 画面中央点一下
            time.sleep(0.5)
            d.implicitly_wait(5.0)
            if d(resourceId="com.autel.explorer:id/rel_camera_controller").exists():
                print('Is in shotting or recording window.')

        #在各智能飞行内部
        elif d(resourceId="com.autel.explorer:id/rl_mode").exists() and\
                (not d(resourceId="com.autel.explorer:id/tv_mode",text='Standby').exists()):
            d(resourceId="com.autel.explorer:id/rl_mode").click()
            time.sleep(1.5)
            d.implicitly_wait(5.0)
            d(resourceId="com.autel.explorer:id/model_choice_txt").click()
            time.sleep(0.5)

        else:
            pass
        time.sleep(2)

    #前往设置
    def GotoSettingsWindow(self):
        # 已经在设置界面
        if d(resourceId="com.autel.explorer:id/tv_setting_title").exists():
            print('is  in settings!')
        # 在开始界面
        elif d(resourceId="com.autel.explorer:id/tv_autel_home_start").exists():
            d(resourceId="com.autel.explorer:id/tv_autel_home_start").click()
            time.sleep(5)
            d(resourceId="com.autel.explorer:id/rl_setting").click()
            time.sleep(0.5)
        # 在地图界面
        elif d(resourceId="com.autel.explorer:id/compass_iv").exists():
            d(resourceId="com.autel.explorer:id/rl_setting").click()
            time.sleep(0.5)
        # 在媒体拍摄界面
        elif d(resourceId="com.autel.explorer:id/iv_camera_outer").exists():
            d(resourceId="com.autel.explorer:id/rl_setting").click()
            time.sleep(0.5)
        # 在各智能飞行界面
        elif d(resourceId="com.autel.explorer:id/rl_left").exists():
            d(resourceId="com.autel.explorer:id/rl_setting").click()
            time.sleep(0.5)
        #  在智能飞行界面
        elif d(text=u"Intelligent Flight").exists():
            d(resourceId="com.autel.explorer:id/layout_cancel").click()
            time.sleep(0.5)
            d(resourceId="com.autel.explorer:id/rl_setting").click()
        else:
            pass



    #切换到拍照画面
    def SwitchtoCaptureMode(self):
            self.mainWindowConfirm()

            if d(resourceId="com.autel.explorer:id/rel_camera_takephoto_controller"):
                print('Now in Shotting Window')

            elif d(resourceId="com.autel.explorer:id/iv_camera_record_controller"):

                print('Now is at Recording Mode.')
                try:
                    if d(resourceId="com.autel.explorer:id/iv_recording_point"):
                        print('Now is recording,try to stop!')
                        self.stop_record()
                        time.sleep(2)
                    time.sleep(1.5)
                    d(resourceId="com.autel.explorer:id/iv_mode_switcher").click()
                    time.sleep(2)
                    d.implicitly_wait(5.0)
                    if d(resourceId="com.autel.explorer:id/rel_camera_takephoto_controller"):
                        print('Is in the Shotting Window')
                except:
                    self.catchError()
                    logging.info('切换到拍照失败')
                    print('切换到拍照失败')


            else:
                print('Switch to capture mode error!')

            time.sleep(1)


    #功能选择
    def FunctionSelect(self,func,listAll):
        seq = 0
        if func in listAll:
            for i in range(0, len(listAll)):
                if func == listAll[i]:
                    seq = i
                    if d(resourceId="com.autel.explorer:id/tv_ui_first_para", text=func).exists():
                        print("is in function %s" % func)

                    else:
                        try:
                            i = 0
                            while i <= len(listAll):  # 通过参数指定模式的参数编号 seq 与 当前滑块 最左边的 所见元素的编号比较, seq比较大,就左移,否则右移
                                flag = False
                                if d(resourceId="com.autel.explorer:id/tv_ui_first_para", text=listAll[i]).exists():

                                    if i > seq:
                                        j = 0
                                        while j <= 10:
                                            d.swipe(0.32, 0.94, 0.68, 0.94)  # 往左边滑
                                            time.sleep(0.5)

                                            if d(resourceId="com.autel.explorer:id/tv_ui_first_para",
                                                 text=func).exists():
                                                # d(resourceId="com.autel.explorer:id/tv_ui_first_para", text=func).click()
                                                print('find %s' % func)
                                                flag = True
                                                break
                                            else:
                                                pass
                                            j += 1

                                    else:
                                        j = 0
                                        while j <= 10:
                                            d.swipe(0.68, 0.94, 0.32, 0.94)  # 往右边滑
                                            time.sleep(0.5)
                                            if d(resourceId="com.autel.explorer:id/tv_ui_first_para",
                                                 text=func).exists():
                                                print('find %s' % func)
                                                flag = True
                                                break
                                            else:
                                                pass
                                        j += 1

                                if flag:
                                    break
                                i += 1
                        except:
                            self.catchError()
                    break
        else:
            logger.info("You have iput a wrong Shotting Function.")
            print("You have iput a wrong Shotting Function.")
            logging.exception(ParaError)

        time.sleep(1.5)

    #滑动选择相机属性
    def scrollToFunc(self,func):
        try:
            self.SwitchtoCaptureMode()
        except:
            self.catchError()
            logger.info("switch to CaputreMode error!")

        listAll = ['SIZE', 'FORMAT', 'MODE', 'EXPOSURE MODE', 'ISO', 'SHUTTER', 'EV', 'WB', 'COLOR', 'STYLE',
                   'DIGITAL ZOOM']

        try:
            self.FunctionSelect(func,listAll)
        except:
            self.catchError()
            logger.info('Function selecting error!')
        # time.sleep(0.5)

    #设置照片大小
    def SetPictureSize(self,num):
        logging.info("function start")
        self.scrollToFunc('SIZE')
        listPara = ["4000x3000","4000x2250"]
        func = 'SIZE'
        time.sleep(2)
        logging.info("function ends")
        logging.info("function starts.")
        self.outsidecircle(num,listPara,func)
        logging.info("function ends")

    #设置照片格式
    def SetPictureFomat(self,num):
        logging.info("function start")
        self.scrollToFunc('FORMAT')
        listPara = ['JPG','RAW',"RAW+JPG"]
        func = 'FORMAT'
        self.outsidecircle(num,listPara,func)
        logging.info("function ends")

    #通用第二层参数选择方法
    def insideListCircleCommon(self,num,listPara,func):
        time.sleep(1.5)

        if num in listPara:

            for i in range(0, len(listPara)):
                if num == listPara[i]:
                    seq = i
                    break
            time.sleep(0.5)
            d.implicitly_wait(5.0)
            if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                try:
                    d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                    print ("%s %s selected" %(func,num))
                    time.sleep(0.5)
                except:
                    self.catchError()

                if func not in ['CONTRAST','SHARP','SATURATION']:
                    d.click(0.5, 0.5)

            else:

                for i in range(0, len(listPara)):
                    if num == listPara[i]:
                        seq = i
                        break
                try:
                    i = 0
                    while i <= len(listPara):  # 通过参数指定模式的参数编号 seq 与 当前滑块 最左边的 所见元素的编号比较, seq比较大,就左移,否则右移
                        flag = False
                        time.sleep(0.5)
                        d.implicitly_wait(5.0)
                        if d(resourceId="com.autel.explorer:id/tv_second_para", text=listPara[i]):


                            if i > seq:
                                j = 0
                                while j <= 30:
                                    d.swipe(0.32, 0.82, 0.68, 0.82)  # 滚动条
                                    time.sleep(0.8)
                                    if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                                        d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                                        print("%s %s selected" %(func,num))
                                        time.sleep(0.5)
                                        if func not in ['CONTRAST', 'SHARP', 'SATURATION']:
                                            d.click (0.5, 0.5)
                                        flag = True
                                    else:
                                        print("not found,continue...,%s Time" % (j + 1))
                                    if flag:
                                        break
                                    j += 1

                            else:
                                j = 0
                                while j <= 30:
                                    d.swipe(0.68, 0.82, 0.32, 0.82)  # 往右边滑
                                    time.sleep(0.8)

                                    if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                                        time.sleep(0.5)
                                        d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                                        print ("%s %s selected" % (func, num))
                                        if func not in ['CONTRAST', 'SHARP', 'SATURATION']:
                                            d.click (0.5, 0.5)
                                        flag = True
                                    else:
                                        print("not found,continue...,%s Time" % (j + 1))

                                    if flag:
                                        break
                                    j += 1

                        else:
                            pass

                        if flag:
                            break
                        i += 1
                except:
                    self.catchError()


            time.sleep(0.5)

        else:
            print ("输入的%s参数有错误!"%func)
            logging.exception (ParaError)
            time.sleep (0.5)
            if func not in ['CONTRAST', 'SHARP', 'SATURATION']:
                d.click (0.5, 0.5)

    # 选择BURST 二级参数方法
    def insideCircleBurst(self,num):

        listPara = ["3", "5", "7", "10", "14"]
        func = 'BURST'
        self.insideListCircleCommon (num, listPara, func)

    # 选择Timelapse 二级参数方法
    def insideCircleTimelapse(self,num):

        listPara = ["2s", "5s", "7s", "10s", "20s","30s","60s"  ]
        func ='Timelapse'
        self.insideListCircleCommon(num,listPara,func)

    #选择AEB二级参数方法
    def insideCircleAeb(self, num):

        listPara = ["3", "5"]
        func = "AEB"
        self.insideListCircleCommon(num,listPara,func)

    #相机 mode　子项选择
    def SetPictureMode(self,mode,num=None):
        logging.info("function start")
        self.scrollToFunc('MODE')
        time.sleep(0.5)
        try:
            d(resourceId="com.autel.explorer:id/tv_ui_first_para", text='MODE').click()
        except:
            self.catchError()
        time.sleep(1)

        if  d(resourceId="com.autel.explorer:id/tv_second_para", text=mode):         #没有的话就往左或者往右翻找找吧
            if mode == "SINGLE":
                try:
                    d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).click()
                except:
                    self.catchError()
                print("SINGEL selected")
                time.sleep(1)
                d.click(0.5, 0.5)

            else:
                try:
                    d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).click()
                    time.sleep(1.5)
                except:
                    self.catchError()

                try:
                    if d(resourceId="com.autel.explorer:id/iv_second_next"):
                        d(resourceId="com.autel.explorer:id/iv_second_next").click()
                        time.sleep(1.5)
                        if mode == "BURST":
                            self.insideCircleBurst(num)
                        elif mode == "TIMELAPSE":
                            self.insideCircleTimelapse(num)
                        else:
                            self.insideCircleAeb(num)

                    else:
                        if mode == "BURST":
                            self.insideCircleBurst(num)
                        elif mode == "TIMELAPSE":
                            self.insideCircleTimelapse(num)
                        else:
                            self.insideCircleAeb(num)

                except:
                    self.catchError()

        else:
                if mode=='SINGLE':      #给每个选项编号
                    seq=0
                elif mode=='BURST':
                    seq=1
                elif mode=='TIMELAPSE':
                    seq=2
                elif mode=='AEB':
                    seq=3
                else:
                    print("MODE 参数有误")
                    logging.exception(ParaError)
                    d.click(0.5, 0.5)
                time.sleep(1.5)
                listMode = ['SINGLE', 'BURST', 'TIMELAPSE', 'AEB']  # 把参放进列表里头:
                if mode in listMode:

                    try:
                        i = 0
                        while i <= len(listMode):  # 通过参数指定模式的参数编号 seq 与 当前滑块 最左边的 所见元素的编号比较, seq比较大,就左移,否则右移
                            flag = False
                            time.sleep(1)
                            d.implicitly_wait(5)
                            if d(resourceId="com.autel.explorer:id/tv_second_para", text=listMode[i]):

                                if i > seq:
                                    j = 0
                                    while j <= 10:
                                        d.swipe(0.32, 0.82, 0.68, 0.82)  # 往左边滑
                                        time.sleep(0.8)

                                        if d(resourceId="com.autel.explorer:id/tv_second_para", text=mode):

                                            if mode == "SINGLE":
                                                try:
                                                    d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).click()
                                                    print("SINGEL selected")
                                                except:
                                                    self.catchError()
                                                finally:
                                                    flag=True
                                                time.sleep(1)
                                                d.click(0.5, 0.5)
                                        # if d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).exists():
                                            else:
                                                try:
                                                    d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).click()
                                                    time.sleep(1.5)
                                                except:
                                                    self.catchError()

                                                if d(resourceId="com.autel.explorer:id/iv_second_next"):
                                                    try:
                                                        d(resourceId="com.autel.explorer:id/iv_second_next").click()
                                                        time.sleep(1.5)
                                                    except:
                                                        self.catchError()

                                                    if mode=="BURST":
                                                        self.insideCircleBurst(num)
                                                    elif mode=="TIMELAPSE":
                                                        self.insideCircleTimelapse(num)
                                                    else:
                                                        self.insideCircleAeb(num)

                                                    flag= True
                                                else:
                                                    if mode=="BURST":
                                                        self.insideCircleBurst(num)
                                                    elif mode=="TIMELAPSE":
                                                        self.insideCircleTimelapse(num)
                                                    else:
                                                        self.insideCircleAeb(num)
                                                    flag=True
                                        else:
                                            print("not found,continue...")

                                        if flag:
                                               break
                                        j += 1

                                else:
                                    j = 0
                                    while j <= 10:
                                        d.swipe(0.68, 0.82, 0.32, 0.82)  # 往右边滑
                                        time.sleep(0.8)


                                        if d(resourceId="com.autel.explorer:id/tv_second_para", text=mode):
                                            if mode == "SINGLE":
                                                try:
                                                    d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).click()
                                                    print("SINGEL selected")
                                                    time.sleep(0.5)
                                                except:
                                                    self.catchError()
                                                finally:
                                                    flag=True

                                                time.sleep(0.5)
                                                d.click (0.5, 0.5)

                                            else:

                                                d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).click()
                                                time.sleep(1.5)
                                                if d(resourceId="com.autel.explorer:id/iv_second_next"):
                                                    try:
                                                        d(resourceId="com.autel.explorer:id/iv_second_next").click()
                                                        time.sleep(1.5)

                                                    except:
                                                        self.catchError()
                                                    if mode=="BURST":
                                                        self.insideCircleBurst(num)
                                                    elif mode=="TIMELAPSE":
                                                        self.insideCircleTimelapse(num)
                                                    else:
                                                        self.insideCircleAeb(num)

                                                    flag= True
                                                else:
                                                    if mode=="BURST":
                                                        self.insideCircleBurst(num)
                                                    elif mode=="TIMELAPSE":
                                                        self.insideCircleTimelapse(num)
                                                    else:
                                                        self.insideCircleAeb(num)
                                                    flag=True
                                        else:
                                            print("Mode,not found,continue...")


                                        if flag:
                                            break
                                        j += 1

                            else:
                                pass

                            if flag:
                                break
                            i += 1  # #
                    except:
                        self.catchError()
                # d.click(0.5,0.5)
        logging.info("function ends")

    #通用第一层参数选择方法
    def outsidecircle(self,num,listPara,func):
        time.sleep(1.5)

        try:
            #先判断输入参数是否有效!
            if num not in listPara:
                print("You have inputed a wrong parameter")

            #输入参数有效的情况下:
            else:
                #参数在主画面显示的情况下
                if d(resourceId="com.autel.explorer:id/tv_first_para",text=num).exists():
                    print("%s setted" % num)

                # 参数未在主画面显示的情况下
                else:
                    try:
                        #点击该功能项
                        d(resourceId="com.autel.explorer:id/tv_ui_first_para", text=func).click()
                        print("%s tapped" %func)
                        time.sleep(1)
                    except:
                        self.catchError()

                    #找到转入参数在参数更表中的序列号
                    seq=0
                    for i in range(0, len(listPara)):
                        if num == listPara[i]:
                            seq = i
                            break

                    time.sleep(1.5)
                    d.implicitly_wait(5)
                    if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():

                        try:
                            #在点开的一级列表中存在传入的参数对应的选项
                            d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                            print("%s setted" % num)
                            time.sleep (1)
                        except:
                            self.catchError()

                    else:
                        i = 0
                        while i <= len(listPara):  # 通过参数指定模式的参数编号 seq 与 当前滑块 最左边的 所见元素的编号比较, seq比较大,就左移,否则右移

                            flag = False
                            if d(resourceId="com.autel.explorer:id/tv_second_para", text=listPara[i]):

                                if i > seq:
                                    j = 0
                                    while j <= 30:
                                        d.swipe(0.32, 0.82, 0.68, 0.82)  # 往左边滑
                                        time.sleep(0.8)
                                        if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                                            try:
                                                d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                                                print("%s setted" % num)
                                                time.sleep(1.5)
                                            except:
                                                self.catchError()
                                            finally:
                                                flag = True
                                        else:
                                            print("Para,not found,continue...")
                                        if flag:
                                            break
                                        j += 1

                                else:
                                    j = 0
                                    while j <= 30:
                                        d.swipe(0.68, 0.82, 0.32, 0.82)  # 往右边滑
                                        time.sleep(0.8)

                                        if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():

                                            try:
                                                d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                                                print("%s setted" % num)
                                                time.sleep(1.5)
                                            except:
                                                self.catchError()
                                            finally:
                                                flag = True
                                        else:
                                            print("not found,continue...")

                                        if flag:
                                            break
                                        j += 1

                            else:
                                pass

                            if flag:
                                break
                            i += 1
                    time.sleep(1)

                    d.long_click(0.5, 0.5)
                    time.sleep(1)
        except:
            self.catchError()
            print('Into function error!')

    #选择照片曝光模式
    def SetPictureExpo(self,num):
        logging.info("function start")
        self.scrollToFunc("EXPOSURE MODE")

        listPara = ['AUTO','MANUAL']
        func = 'EXPOSURE MODE'
        time.sleep(1.5)

        self.outsidecircle(num,listPara,func)
        logging.info("fundtion ends")

    #设置照片iso
    def SetPictureIso(self,num):
        logging.info("function start")
        self.SetPictureExpo("MANUAL")
        self.scrollToFunc("ISO")

        listPara = ["100", "200", "400", "800", "1600", "3200"]
        func = 'ISO'
        self.outsidecircle(num,listPara,func)
        logging.info("function ends")

    #设置照片快门
    def SetPictureShutter(self,num):
        logging.info("function start")
        self.SetPictureExpo("MANUAL")
        time.sleep(0.5)
        self.scrollToFunc("SHUTTER")
        func = 'SHUTTER'

        listPara = ["1/8000", "1/6000", "1/5000", "1/4000", "1/3200", "1/2500", "1/2000", "1/1600", "1/1250", "1/1000",
                       "1/800", "1/640", "1/500",
                       "1/400", "1/320", "1/240", "1/200", "1/160", "1/120", "1/100", "1/80", "1/60", "1/50", "1/40",
                       "1/30", "1/25", "1/20", "1/15", "1/12.5",
                       "1/10", "1/8", "1/6.25", "1/5", "1/4", "1/3", "1/2.5", "1/2", "1/1.67", "1/1.25", "1\"", "1.3\"",
                       "1.6\"", "2\"", "2.5\"", "3\"", "3.2\"",
                       "4\"", "5\"", "6\"", "8\""]

        self.outsidecircle(num,listPara,func)
        logging.info("function ends")

    # 设置照片快门 --优化方案
    def SetPictureShutterOP(self, num):
            logging.info("function start")
            self.SetPictureExpo("MANUAL")
            time.sleep(2)
            self.scrollToFunc("SHUTTER")
            time.sleep(1.5)

            listPara = ["1/8000", "1/6000", "1/5000", "1/4000", "1/3200", "1/2500", "1/2000", "1/1600", "1/1250",
                        "1/1000",
                        "1/800", "1/640", "1/500",
                        "1/400", "1/320", "1/240", "1/200", "1/160", "1/120", "1/100", "1/80", "1/60", "1/50", "1/40",
                        "1/30", "1/25", "1/20", "1/15", "1/12.5",
                        "1/10", "1/8", "1/6.25", "1/5", "1/4", "1/3", "1/2.5", "1/2", "1/1.67", "1/1.25", "1\"",
                        "1.3\"",
                        "1.6\"", "2\"", "2.5\"", "3\"", "3.2\"",
                        "4\"", "5\"", "6\"", "8\""]
            if num not in listPara:
                print("You have inputed a wrong parameter")

            else:
                d.implicitly_wait(5.0)
                if d(resourceId="com.autel.explorer:id/tv_first_para", text=num).exists():
                    print("%s setted" % num)

                else:
                    try:
                        # 点击SHUTTER进入模块
                        d(resourceId="com.autel.explorer:id/tv_ui_first_para", text="SHUTTER").click()
                        time.sleep(1.5)
                    except:
                        self.catchError()
                    # time.sleep(0.5)
                    # 判断所选参数是否可见 ,可见情况
                    d.implicitly_wait(5.0)
                    if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                        # time.sleep(0.5)
                        try:
                            d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                            time.sleep(1.5)
                        except:
                            self.catchError()

                    # 判断所选参数是否可见 ,不可见情况
                    else:
                        try:
                            num2 = num
                            if num2.endswith('"'):
                                num2 = float(num2[:-1])
                                print('Given parameter is %d' % (num2))
                            else:
                                num3 = num2.split("/")
                                # print(num3)
                                num2a = float(num3[0])
                                num2b = float(num3[1])
                                num2 = num2a / num2b
                                print('Given parameter is %d/%d' % (num2a, num2b))

                            time.sleep(1.5)
                            d.implicitly_wait(5.0)
                        except:
                            self.catchError()

                        try:
                            elenum = d(resourceId="com.autel.explorer:id/tv_second_para").get_text()

                            if elenum.endswith('"'):
                                elenum = float(elenum[:-1])
                                print('current left parameteris %s' % elenum)
                            else:
                                elenum = elenum.split("/")

                                elenuma = float(elenum[0])
                                elenumb = float(elenum[1])
                                elenum = elenuma / elenumb
                                print('current left parameter is %d/%d' % (elenuma, elenumb))
                            time.sleep(1)
                            self.insideCircleCommonOP(num,elenum,num2)
                        except:
                            self.catchError()
                            logging.info("can't set shutter")
            logging.info("function ends")

    #设置照片EV
    def SetpictureEv(self,num):
        logging.info("function start")
        self.SetPictureExpo("AUTO")
        time.sleep(2)
        self.scrollToFunc("EV")

        listPara = ["-3.0", "-2.7", "-2.3", "-2.0", "-1.7", "-1.3", "-1.0", "-0.7", "-0.3", "0","+0.3","+0.7","+1.0","+1.3","+1.7","+2.0","+2.3","+2.7","+3.0"]
        func = 'EV'
        time.sleep(1.5)

        self.outsidecircle(num,listPara,func)
        logging.info("function ends")

    #自定义白平衡二层循环
    def insideCircleWB(self,num):

        listPara = ["2000K", "2100K", "2200K", "2300K", "2400K", "2500K", "2600K", "2700K", "2800K", "2900K",
                  "3000K", "3100K", "3200K", "3300K", "3400K", "3500K", "3600K", "3700K", "3800K", "3900K",
                  "4000K", "4100K", "4200K", "4300K", "4400K", "4500K", "4600K", "4700K", "4800K", "4900K",
                  "5000K", "5100K", "5200K", "5300K", "5400K", "5500K", "5600K", "5700K", "5800K", "5900K",
                  "6000K", "6100K", "6200K", "6300K", "6400K", "6500K", "6600K", "6700K", "6800K", "6900K",
                  "7000K", "7100K", "7200K", "7300K", "7400K", "7500K", "7600K", "7700K", "7800K", "7900K",
                  "8000K", "8100K", "8200K", "8300K", "8400K", "8500K", "8600K", "8700K", "8800K", "8900K",
                  "9000K", "9100K", "9200K", "9300K", "9400K", "9500K", "9600K", "9700K", "9800K", "9900K",
                  "10000K"]
        func = 'WB'
        self.insideListCircleCommon(num,listPara,func)

    # 自定论文二层循环 --通用优化方案
    def insideCircleCommonOP(self,num,elenum, num2):
        time.sleep(0.5)
        if elenum > num2:
            j = 0

            while j <= 30:
                flag = False
                d.swipe(0.32, 0.82, 0.68, 0.82)  # 滚动条
                time.sleep(0.8)
                if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():

                    try:
                        d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                        time.sleep(1)
                    except:
                        self.catchError()
                    finally:
                        flag = True
                else:
                    print("not found,continue...,%s Time" % (j + 1))
                if flag:
                    break
                j += 1

        else:
            j = 0
            while j <= 30:
                flag = False
                d.swipe(0.68, 0.82, 0.32, 0.82)  # 往右边滑
                time.sleep(0.8)

                if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                    try:
                        d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                        time.sleep(1)
                    except:
                        self.catchError()
                    finally:
                        flag = True
                else:
                    print("not found,continue...,%sTime" % (j + 1))

                if flag:
                    break
                j += 1

        d.click(0.5, 0.5)

    #自定义白平衡 --优化速度
    def insideCircleWBOP(self,num):
        if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
            try:
                d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                time.sleep(1)
            except:
                self.catchError()
        else:
            try:
                num2= int(num[0:-1])
                print('num2: ',num2)
                elenum=d(resourceId="com.autel.explorer:id/tv_second_para").get_text()
                elenum=int(elenum[0:-1])
                print('elenum: ',elenum)

                self.insideCircleCommonOP(num,elenum,num2)
            except:
                self.catchError()

    #设置白平衡
    def SetPictureWB(self,num):
        logging.info("function start")

        self.scrollToFunc("WB")
        time.sleep(1.5)

        if num in ["AUTO", "SUNNY", "CLOUDY", "INCAN", "NEON"]:  # 预设的情况:
            listPara = ["AUTO", "SUNNY", "CLOUDY", "INCAN", "NEON"]
            func = 'WB'
            self.outsidecircle(num,listPara,func)

        elif num not in ["AUTO", "SUNNY", "CLOUDY", "INCAN", "NEON"]:  # WB ==  'x000K' 的情况:

            if d(resourceId="com.autel.explorer:id/tv_first_para", text=num).exists():
                print("%s setted" % num)
            
            else:
                try:
                    d(resourceId="com.autel.explorer:id/tv_ui_first_para", text=u"WB").click()
                    time.sleep(1.5)
                except:
                    self.catchError()
                # (...) 存在的情况
                if d(resourceId="com.autel.explorer:id/iv_second_next").exists():
                    if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():# xxxxK 和 (...)均存在的情况
                        pass   #己经存在该选择项
                     #(...)存在, xxxxK不存在的情况,点(...)进入下一层循环
                    elif not  d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                        try:
                            d(resourceId="com.autel.explorer:id/iv_second_next").click()
                            time.sleep(1.5)
                            self.insideCircleWBOP(num)
                        except:
                            d.click(0.5,0.5)
                            self.catchError()
                        time.sleep(1)

                        # d.click(0.5, 0.5)

                # (...)不存在的情况
                else:
                    i=0
                    while i<=2:
                        d.swipe(0.68, 0.82, 0.32, 0.82)  # 滑向滚动条右侧
                        time.sleep(0.8)
                        if d(resourceId="com.autel.explorer:id/iv_second_next").exists():
                            if d(resourceId="com.autel.explorer:id/tv_second_para",text=num):  # xxxxK 和 (...)均存在的情况
                                break  # 己经存在该选择项
                            # (...)存在, xxxxK不存在的情况,点(...)进入下一层循环
                            elif not d(resourceId="com.autel.explorer:id/tv_second_para", text=num):
                                try:
                                    d(resourceId="com.autel.explorer:id/iv_second_next").click()
                                    time.sleep(1.5)
                                    self.insideCircleWBOP(num)
                                    break
                                except:
                                    self.catchError()
                        i+=1
        else:
              pass

        logging.info("function ends")

    #设置照片色彩
    def SetPictureColor(self,num):
        logging.info("function start")
        self.scrollToFunc("COLOR")

        listPara = ["NONE", "LOG", "VIVID", "B&W", "ART", "FILM","BEACH","DREAM","CLASSIC","NOSTALGIC"]
        func = 'COLOR'

        self.outsidecircle(num,listPara,func)
        logging.info("function ends")

    #对比度三级菜单
    def insideCircleContrast(self,num):

        listPara = ["-3", "-2", "-1", "±0", "+1", "+2", "+3" ]
        print(num[3:5])
        num=num[3:5]
        func = 'CONTRAST'

        self.insideListCircleCommon(num,listPara,func)

    #锐度三级菜单
    def insideCircleSharp(self,num):

        listPara = ["-3", "-2", "-1", "±0", "+1", "+2", "+3" ]
        print(num[0:2])
        num=num[0:2]
        func = 'SHARP'

        self.insideListCircleCommon(num,listPara,func)

    #饱和度三级菜单
    def insideCircleSaturation(self,num):

        listPara = ["-3", "-2", "-1", "±0", "+1", "+2", "+3"]
        print(num[6:8])
        num=num[6:8]
        func = 'SATURATION'

        self.insideListCircleCommon(num,listPara,func)

    #自定义风格二级菜单
    def insideCircleStyle(self,num):
        try:
            d(resourceId="com.autel.explorer:id/iv_second_next").click()
            time.sleep(0.5)
        except:
            self.catchError()
        try:
            self.insideCircleContrast(num)
        except:
            self.catchError()

        try:
            d(resourceId="com.autel.explorer:id/tv_back").click()
            time.sleep(0.5)
        except:
            self.catchError()


        try:
            d(resourceId="com.autel.explorer:id/tv_ui_second_para").click()
            time.sleep(0.5)
            d(resourceId="com.autel.explorer:id/iv_second_next").click()
            time.sleep(0.5)
        except:
            self.catchError()
        self.insideCircleSharp(num)

        try:
            d(resourceId="com.autel.explorer:id/tv_back").click()
            time.sleep(0.5)
        except:
            self.catchError()

        try:
            d(resourceId="com.autel.explorer:id/tv_ui_second_para", text=u"SATURATION").click()
            time.sleep(0.5)
        except:
            self.catchError()
        try:
            d(resourceId="com.autel.explorer:id/iv_second_next").click()
            time.sleep(0.5)
        except:
            self.catchError()
        try:
            self.insideCircleSaturation(num)
        except:
            self.catchError()
        try:
            d(resourceId="com.autel.explorer:id/tv_back").click()
            time.sleep(0.5)
        except:
            self.catchError()
        time.sleep(1)

        print("Style %s is Setted" % num)
        d.click(0.5,0.5)

    #照片风格一级菜单
    def SetPitureStyle(self,num):
        logging.info("function start")
        # self.scrollToFunc("STYLE")
        self.scrollToFunc("STYLE")
        listPara = ["STD.", "NEUT.", "LAND.",'%s']

        # == 自定义的情况:
        if num not in ["STD.", "NEUT.", "LAND."]:

            # (...) 存在的情况

            if d(resourceId="com.autel.explorer:id/tv_first_para", text=num):
                print("Style %s is Setted"%num)

            else:

                try:
                    d(resourceId="com.autel.explorer:id/tv_ui_first_para", text=u"STYLE").click()
                    time.sleep(0.5)
                    if d(resourceId="com.autel.explorer:id/iv_second_next").exists():
                        if d(resourceId="com.autel.explorer:id/tv_second_para",
                             text=num).exists():  # "指定参数" 和 (...)均存在的情况
                            pass  # 己经存在该选择项

                        # (...)存在, "xx xx xx"不存在的情况,点(...)进入下一层循环
                        elif not d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                            try:
                                d(resourceId="com.autel.explorer:id/iv_second_next").click()
                                time.sleep(0.5)
                            except:
                                self.catchError()
                            self.insideCircleStyle(num)

                    else:
                        j = 0
                        while j <= 3:
                            d.swipe(0.68, 0.82, 0.32, 0.82)  # 滑向滚动条右侧
                            if d(resourceId="com.autel.explorer:id/iv_second_next").exists():
                                if d(resourceId="com.autel.explorer:id/tv_second_para",
                                     text=num).exists():  # "指定参数" 和 (...)均存在的情况
                                    d.click(0.5, 0.5)
                                    break  # 己经存在该选择项

                                elif not d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                                    try:
                                        d(resourceId="com.autel.explorer:id/iv_second_next").click()
                                        time.sleep(0.5)
                                    except:
                                        self.catchError()

                                    self.insideCircleStyle(num)
                                    break
                except:
                    self.catchError()


        # 是预设前三项情况
        else:

            listPara = ["STD.", "NEUT.", "LAND."]
            func = 'STYLE'

            self.outsidecircle(num, listPara, func)
        logging.info("function ends")
    #照片数码变焦
    def SetPictureDigizoom(self,num):
        logging.info("function start")

        self.scrollToFunc("DIGITAL ZOOM")
        time.sleep(3)
        listPara = ["1.0X", "2.0X", "3.0X", "4.0X","5.0X","6.0X","7.0X","8.0X"]
        func = 'DIGITAL ZOOM'

        if d(resourceId="com.autel.explorer:id/tv_ui_first_para", text=u"DIGITAL ZOOM"):
            pass
        else:
            time.sleep(2)
        self.outsidecircle(num,listPara,func)
        logging.info("function ends")

    #  云台角度 '0°'
    def GimbalAngle(self,num):
        logging.info("function start")
        self.SwitchtoCaptureMode()
        time.sleep(2)
        try:
            angle=d(resourceId="com.autel.explorer:id/tv_arch_indicator").get_text()
            if num == angle:
                print("Needed Gimbal angle was set.")
            else:
                d(resourceId="com.autel.explorer:id/rl_gimbal_angle").click()
                time.sleep(1.5)

                try:
                    d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                except:
                    self.catchError()
                time.sleep(0.5)
                d.click(0.5,0.5)
        except:
            self.catchError()
        logging.info("function ends")

    ##---------------------------- Recoding Module ------------------------------------##
        # 在主界面判断是否在录相状态


    #切换到录相模式
    def SwitchtoRecordMode(self):
            self.mainWindowConfirm()

            d.implicitly_wait(5.0)
            if d(resourceId="com.autel.explorer:id/iv_camera_record_controller"):
                print('Is in the Recording Window')

            elif d(resourceId="com.autel.explorer:id/rel_camera_takephoto_controller"):
                print("Now is at Shoting Mode!")


                try:
                    i = 0
                    while i <= 9:
                        d(resourceId="com.autel.explorer:id/iv_mode_switcher").click()
                        time.sleep(1.5)
                        # d.implicitly_wait(5.0)

                        if d(resourceId="com.autel.explorer:id/iv_camera_record_controller"):
                            print('Is in the Recording Window')
                            break
                        else:
                            print('switch error,try again')

                        i += 1
                except:
                    self.catchError()
                    print('切换到录相失败！')


            else:
                print("Switch to recording mdoe error!")


            time.sleep(1)



    #在录相状态选择功能模式
    def scrollToAVFunc(self,func):
        self.SwitchtoRecordMode()

        listAll = ['PIV', 'STANDARD', 'FORMAT', 'RESOLUTION', 'FRAME RATE', 'EXPOSURE MODE', 'ISO', 'SHUTTER', 'EV', 'WB',
                  'COLOR', 'STYLE','DIGITAL ZOOM']

        self.FunctionSelect(func,listAll)


    #PIV设置
    def setVideoPIV(self,num):
        logging.info("function start")
        self.scrollToAVFunc("PIV")
        listPara = ["MANUAL", "5S", "10S", "30S", "60S"]
        func = 'PIV'

        self.outsidecircle(num,listPara,func)
        logging.info("function ends")

    #选择视频制式
    def setVedioStandard(self,num):
        logging.info("function start")
        self.scrollToAVFunc('STANDARD')
        listPara = ['NTSC','PAL']
        func = 'STANDARD'

        self.outsidecircle(num,listPara,func)
        logging.info("function ends")
    #选择视频格式
    def setVedioFormat(self,num):
        logging.info("function start")
        self.scrollToAVFunc('FORMAT')
        listPara = ['MOV','MP4']
        func = 'FORMAT'

        self.outsidecircle(num,listPara,func)
        logging.info("function ends")

    #视频分辨率
    def setVideoReso(self,num):
        logging.info("function start")
        self.scrollToAVFunc("RESOLUTION")

        if num == "4K+":
            num = "4K+(4096x2160)"
        elif num == "4K":
            num = "4K(3840x2160)"
        elif num == "2.7K":
            num = "2.7K(2720x1530)"
        elif num == "1080P":
            num == "1080P(1920x1080)"

        listPara = ["4K+(4096x2160)", "4K(3840x2160)", "2.7K(2720x1530)", "1080P(1920x1080)"]
        func = 'RESOLUTION'

        self.outsidecircle(num,listPara,func)
        logging.info("function ends")
    #视频帧率
    def setVideoFramerate(self,num):
        logging.info("function start")
        self.scrollToAVFunc("FRAME RATE")

        try:
            if d(resourceId="com.autel.explorer:id/tv_first_para",text=num).exists():
                print("%s already setted"%num)

            else:
                self.scrollToAVFunc("RESOLUTION")

                if d(resourceId="com.autel.explorer:id/tv_first_para", text=u"4K+").exists():
                     ratetext=d(resourceId="com.autel.explorer:id/tv_first_para", text=u"4K+").get_text()
                elif d(resourceId="com.autel.explorer:id/tv_first_para", text=u"4K").exists():
                     ratetext = d(resourceId="com.autel.explorer:id/tv_first_para", text=u"4K").get_text()
                elif d(resourceId="com.autel.explorer:id/tv_first_para", text=u"2.7K").exists():
                     ratetext = d(resourceId="com.autel.explorer:id/tv_first_para", text=u"2.7K").get_text()
                elif d(resourceId="com.autel.explorer:id/tv_first_para", text=u"1080P").exists():
                     ratetext = d(resourceId="com.autel.explorer:id/tv_first_para", text=u"1080P").get_text()
                elif d(resourceId="com.autel.explorer:id/tv_first_para", text=u"720P").exists():
                     ratetext = d(resourceId="com.autel.explorer:id/tv_first_para", text=u"720P").get_text()


                if ratetext == "4K+":
                    listPara = ["30FPS","24FPS"]
                elif ratetext == "4K" or ratetext == "2.7K":
                    listPara = ["60FPS","48FPS","30FPS","24FPS"]
                elif ratetext == "1080P":
                    listPara =["120FPS","60FPS","48FPS","30FPS","24FPS"]
                elif ratetext == "720P":
                    listPara = ["240FPS","60FPS","48FPS","30FPS","24FPS"]
                else:
                    logging.exception(ParaError)

                func = 'FRAME RATE'


                self.outsidecircle(num,listPara,func)
        except:
            self.catchError()
        logging.info("function ends")

    #视频曝光模式
    def setVedioExpo(self,num):
        logging.info("function start")
        self.scrollToAVFunc("EXPOSURE MODE")
        listPara = ['AUTO', 'MANUAL']
        func = 'EXPOSURE MODE'

        self.outsidecircle (num, listPara, func)
        logging.info("function ends")

    #视频ISO
    def setVedioIso(self,num):
        logging.info("function start")
        self.setVedioExpo("MANUAL")
        self.scrollToAVFunc("ISO")
        listPara = ["100", "200", "400", "800", "1600", "3200"]
        func = 'ISO'

        self.outsidecircle(num,listPara,func)
        logging.info("function ends")


    def setVedioShutter(self,num):
        self.setVedioExpo("MANUAL")
        self.scrollToAVFunc("SHUTTER")
        listPara = ["1/8000", "1/6000", "1/5000", "1/4000", "1/3200", "1/2500", "1/2000", "1/1600", "1/1250", "1/1000",
                       "1/800", "1/640", "1/500",
                       "1/400", "1/320", "1/240", "1/200", "1/160", "1/120", "1/100", "1/80", "1/60"]
        func = 'SHUTTER'

        self.outsidecircle(num,listPara,func)



    def setVedioEv(self,num):
        self.setVedioExpo("AUTO")
        self.scrollToAVFunc("EV")
        listPara = ["-3.0", "-2.7", "-2.3", "-2.0", "-1.7", "-1.3", "-1.0", "-0.7", "-0.3", "0","+0.3","+0.7","+1.0","+1.3","+1.7","+2.0","+2.3","+2.7","+3.0"]
        func = 'EV'

        self.outsidecircle(num,listPara,func)


    #设置视频白平衡
    def setVedioWB(self,num):
        self.scrollToAVFunc("WB")

        if num in ["AUTO", "SUNNY", "CLOUDY", "INCAN", "NEON"]:  # 预设的情况:
            listPara = ["AUTO", "SUNNY", "CLOUDY", "INCAN", "NEON"]
            func = 'WB'
            self.outsidecircle(num, listPara, func)

        elif num not in ["AUTO", "SUNNY", "CLOUDY", "INCAN", "NEON"]:  # WB ==  'x000K' 的情况:

            if d(resourceId="com.autel.explorer:id/tv_first_para", text=num).exists():
                print("%s setted" % num)

            else:
                try:
                    d(resourceId="com.autel.explorer:id/tv_ui_first_para", text=u"WB").click()
                    time.sleep(1.5)
                except:
                    self.catchError()
                # (...) 存在的情况
                if d(resourceId="com.autel.explorer:id/iv_second_next").exists():
                    if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():  # xxxxK 和 (...)均存在的情况
                        pass  # 己经存在该选择项
                    # (...)存在, xxxxK不存在的情况,点(...)进入下一层循环
                    elif not d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                        try:
                            d(resourceId="com.autel.explorer:id/iv_second_next").click()
                            time.sleep(1.5)
                        except:
                            self.catchError()
                        self.insideCircleWBOP(num)

                        time.sleep(0.5)

                # (...)不存在的情况
                else:
                    i = 0
                    while i <= 2:
                        d.swipe(0.68, 0.82, 0.32, 0.82)  # 滑向滚动条右侧
                        time.sleep(0.8)
                        if d(resourceId="com.autel.explorer:id/iv_second_next").exists():
                            if d(resourceId="com.autel.explorer:id/tv_second_para",
                                 text=num).exists():  # xxxxK 和 (...)均存在的情况
                                break  # 己经存在该选择项
                            # (...)存在, xxxxK不存在的情况,点(...)进入下一层循环
                            elif not d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                                try:
                                    d(resourceId="com.autel.explorer:id/iv_second_next").click()
                                    time.sleep(1.5)
                                except:
                                    self.catchError()
                                self.insideCircleWBOP(num)
                                break
                        i += 1
        else:
            pass


    #设置视频色彩
    def setVedioColor(self,num):
        self.scrollToAVFunc("COLOR")
        listPara = ["NONE", "LOG", "VIVID", "B&W", "ART", "FILM","BEACH","DREAM","CLASSIC","NOSTALGIC"]
        func = 'color'

        self.outsidecircle(num,listPara,func)

    #设置视频风格 -- 待优化
    def setVedioStyle_debuging(self,num):
        self.scrollToAVFunc("STYLE")

        listPara = ["STD.", "NEUT.", "LAND.","%s"]

        # == 自定义的情况:
        if num not in ["STD.", "NEUT.", "LAND."]:

            # (...) 存在的情况

            if d (resourceId="com.autel.explorer:id/tv_first_para", text=num).exists ():
                print ("Style %s is Setted" % num)

            else:

                try:
                    d (resourceId="com.autel.explorer:id/tv_ui_first_para", text=u"STYLE").click ()
                except:
                    logging.exception ('------------Exceptions Caught--------')
                if d (resourceId="com.autel.explorer:id/iv_second_next").exists ():
                    if d (resourceId="com.autel.explorer:id/tv_second_para",
                          text=num).exists ():  # "指定参数" 和 (...)均存在的情况
                        pass  # 己经存在该选择项

                    # (...)存在, "xx xx xx"不存在的情况,点(...)进入下一层循环
                    elif not d (resourceId="com.autel.explorer:id/tv_second_para", text=num).exists ():
                        try:
                            d (resourceId="com.autel.explorer:id/iv_second_next").click ()
                        except:
                            logging.exception ('------------Exceptions Caught--------')
                        time.sleep (0.5)
                        self.insideCircleStyle (num)

                else:
                    j = 0
                    while j <= 3:
                        d.swipe (0.68, 0.82, 0.32, 0.82)  # 滑向滚动条右侧
                        if d (resourceId="com.autel.explorer:id/iv_second_next").exists ():
                            if d (resourceId="com.autel.explorer:id/tv_second_para",
                                  text=num).exists ():  # "指定参数" 和 (...)均存在的情况
                                d.click (0.5, 0.5)
                                break  # 己经存在该选择项

                            # (...)存在, xxxxK不存在的情况,点(...)进入下一层循环
                            elif not d (resourceId="com.autel.explorer:id/tv_second_para", text=num).exists ():
                                try:
                                    d (resourceId="com.autel.explorer:id/iv_second_next").click ()
                                except:
                                    logging.exception ('------------Exceptions Caught--------')
                                time.sleep (0.5)

                                self.insideCircleStyle (num)
                                break




        # 是预设前三项情况
        else:

            listPara = ["STD.", "NEUT.", "LAND.","%S"]
            func = 'STYLE'

            self.outsidecircle (num, listPara, func)

    #设置视频风格
    def setVedioStyle(self,num):
        self.scrollToAVFunc("STYLE")
        time.sleep(1)
        # listPara = ["STD.", "NEUT.", "LAND.",'%s']
        listPara = ["STD.", "NEUT.", "LAND."]

        # == 自定义的情况:
        if num not in ["STD.", "NEUT.", "LAND."]:

            # (...) 存在的情况

            if d(resourceId="com.autel.explorer:id/tv_first_para", text=num).exists():
                print("Style %s is Setted"%num)

            else:

                try:
                    d(resourceId="com.autel.explorer:id/tv_ui_first_para", text=u"STYLE").click()
                    time.sleep(0.5)
                    if d(resourceId="com.autel.explorer:id/iv_second_next"):
                        if d(resourceId="com.autel.explorer:id/tv_second_para", text=num):  # "指定参数" 和 (...)均存在的情况
                            pass  # 己经存在该选择项

                        # (...)存在, "xx xx xx"不存在的情况,点(...)进入下一层循环
                        elif not d(resourceId="com.autel.explorer:id/tv_second_para", text=num):
                            # time.sleep(2)
                            try:
                                d(resourceId="com.autel.explorer:id/iv_second_next").click()
                                time.sleep(0.5)
                            except:
                                self.catchError()
                            # time.sleep(2)
                            self.insideCircleStyle(num)


                    else:
                        j = 0
                        while j <= 3:
                            d.swipe(0.68, 0.82, 0.32, 0.82)  # 滑向滚动条右侧
                            if d(resourceId="com.autel.explorer:id/iv_second_next").exists():
                                if d(resourceId="com.autel.explorer:id/tv_second_para",
                                     text=num).exists():  # "指定参数" 和 (...)均存在的情况
                                    d.click(0.5, 0.5)
                                    print("Style %s  Set" % num)
                                    break  # 己经存在该选择项

                                # (...)存在, xxxxK不存在的情况,点(...)进入下一层循环
                                elif not d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                                    time.sleep(0.5)
                                    try:
                                        d(resourceId="com.autel.explorer:id/iv_second_next").click()
                                        time.sleep(0.5)

                                    except:
                                        logging.exception('------------Exceptions Caught--------')
                                        timestamp = time.strftime('%H_%M_%S')
                                        errpic = timestamp + '_Error.jpg'
                                        d.screenshot(errpic)
                                    time.sleep(0.5)

                                    self.insideCircleStyle(num)
                                    break
                except:
                    self.catchError()



        # 是预设前三项情况
        else:
            try:
                time.sleep(0.5)
                d.implicitly_wait(5.0)
                d(resourceId="com.autel.explorer:id/tv_ui_first_para", text=u"STYLE").click()
                time.sleep(0.5)

                for i in range(0, len(listPara)-1):
                    if num == listPara[i]:
                        seq = i
                        time.sleep(1)
                        break

                if d(resourceId="com.autel.explorer:id/tv_ui_second_para", text=num).exists():

                    try:
                        d(resourceId="com.autel.explorer:id/tv_ui_second_para", text=num).click()
                        time.sleep(0.5)
                        print("Style %s  Set"%num)

                    except:
                        logging.exception('------------Exceptions Caught--------')
                        timestamp = time.strftime('%H_%M_%S')
                        errpic = timestamp + '_Error.jpg'
                        d.screenshot(errpic)

                else:
                    i = 0
                    while i <= len(listPara):  # 通过参数指定模式的参数编号 seq 与 当前滑块 最左边的 所见元素的编号比较, seq比较大,就左移,否则右移
                        flag = False
                        if d(resourceId="com.autel.explorer:id/tv_ui_second_para", text=listPara[i]):
                            # driver.find_element_by_android_uiautomator('new UiSelector().text(listMode[i])'):

                            if i > seq:
                                j = 0
                                while j <= 20:
                                    d.swipe(0.32, 0.82, 0.68, 0.82)  # 往左边滑
                                    time.sleep(0.8)
                                    if d(resourceId="com.autel.explorer:id/tv_ui_second_para", text=num).exists():
                                        # if d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).exists():
                                        try:
                                            d(resourceId="com.autel.explorer:id/tv_ui_second_para", text=num).click()
                                            time.sleep(0.5)
                                            print("Style %s  Set" % num)
                                        except:
                                            logging.exception('------------Exceptions Caught--------')
                                            timestamp = time.strftime('%H_%M_%S')
                                            errpic = timestamp + '_Error.jpg'
                                            d.screenshot(errpic)
                                        finally:
                                            flag = True
                                    else:
                                        print("Para,not found,continue...")
                                    if flag:
                                        break
                                    j += 1


                            else:
                                j = 0
                                while j <= 20:
                                    d.swipe(0.68, 0.82, 0.32, 0.82)  # 滑向滚动条右侧
                                    time.sleep(0.8)

                                    if d(resourceId="com.autel.explorer:id/tv_ui_second_para", text=num).exists():
                                        # time.sleep(0.5)
                                        try:
                                            d(resourceId="com.autel.explorer:id/tv_ui_second_para", text=num).click()
                                            time.sleep(0.5)
                                            print("Style %s  Set" % num)
                                        except:
                                            logging.exception('------------Exceptions Caught--------')
                                            timestamp = time.strftime('%H_%M_%S')
                                            errpic = timestamp + '_Error.jpg'
                                            d.screenshot(errpic)
                                        finally:
                                            flag = True
                                    else:
                                        print("not found,continue...")

                                    if flag:
                                        break
                                    j += 1

                        else:
                            pass

                        if flag:
                            break
                        i += 1
            except:
                self.catchError()
            # time.sleep(2)
            d.click(0.5, 0.5)

    #设置视频数码变焦
    def setVedioDigizoom(self,num):

            self.scrollToAVFunc("DIGITAL ZOOM")
            listPara = ["1.0X", "2.0X", "3.0X", "4.0X","5.0X","6.0X","7.0X","8.0X"]
            func = 'DIGITAL ZOOM'

            self.outsidecircle(num,listPara,func)

    #录相设置
    def record(self):
        # 录相按钮存在
        d.implicitly_wait(5.0)
        if d(resourceId="com.autel.explorer:id/iv_camera_record_controller"):
            try:
                d(resourceId="com.autel.explorer:id/iv_camera_record_controller").click()
                print("record()")
            except:
                self.catchError()

            #sd卡满
            # d.implicitly_wait(5.0)
            if d(resourceId="com.autel.explorer:id/toast_msg_tv",text='SD card is full').exists():
                self.camSetFormatsdcard('yes')
                time.sleep(8)
                try:
                    d.implicitly_wait(10.0)
                    d(resourceId="com.autel.explorer:id/iv_camera_record_controller").click()
                    print("rerecord()")
                    # time.sleep(0.5)
                except:
                    self.catchError()

        # 录相按钮不存在
        else:
            # d.implicitly_wait(10.0)
            try:
                d(resourceId="com.autel.explorer:id/iv_mode_switcher").click()
                time.sleep(1.5)
                d.implicitly_wait(5.0)
                d(resourceId="com.autel.explorer:id/iv_camera_record_controller").click()
                print("record()")
            except:
                self.catchError()
                logging.info('切换到录相模式失败！')
             #sd 卡满
            if d(resourceId="com.autel.explorer:id/toast_msg_tv",text='SD card is full').exists():
                self.camSetFormatsdcard('yes')
                time.sleep(8)
                try:
                    d.implicitly_wait(10.0)
                    d(resourceId="com.autel.explorer:id/iv_camera_record_controller").click()
                    print("rerecord()")
                    # time.sleep(0.5)
                except:
                    self.catchError()
                    logging.info('录相失败！')

            '''
            try:
                d.implicitly_wait(10.0)
                if  d(resourceId="com.autel.explorer:id/iv_camera_record_controller").exists():
                    d(resourceId="com.autel.explorer:id/iv_camera_record_controller").click()
                    print("record()")
            except:
                self.catchError()
                logging.info('录相按钮点击失败！')

            time.sleep(0.5)
            if d(resourceId="com.autel.explorer:id/toast_msg_tv",text='SD card is full').exists():
                self.camSetFormatsdcard('yes')
                time.sleep(8)

                try:
                    d.implicitly_wait(10.0)
                    d(resourceId="com.autel.explorer:id/iv_camera_record_controller").click()
                    print("rerecord()")
                    # time.sleep(0.5)
                    # print('record()')
                    # time.sleep(2)
                except:
                    self.catchError()
                    logging.info('录相按钮点击失败！')
            '''

    #快录
    def fast_record(self):
        try:
            if d(resourceId="com.autel.explorer:id/tv_recording_left_time").wait(3):
                try:
                    d(resourceId="com.autel.explorer:id/iv_camera_record_controller").click()
                except:
                    pass
                print('Existing recording!')
                time.sleep(2)
                try:
                    d(resourceId="com.autel.explorer:id/iv_camera_record_controller").click()
                except:
                    pass
                print('restart recording')


            else:
                time.sleep(2)

                d.implicitly_wait(3.0)

                d(resourceId="com.autel.explorer:id/iv_camera_record_controller").click()

                print('start recording!')
                time.sleep(1)
                d.implicitly_wait(3.0)
                if d(resourceId="com.autel.explorer:id/toast_msg_tv", text='SD card is full'):
                    self.camSetFormatsdcard('yes')
                    time.sleep(8)
                    try:
                        d.implicitly_wait(10.0)
                        d(resourceId="com.autel.explorer:id/iv_camera_record_controller").click()
                        print("rerecord()")
                        # time.sleep(0.5)
                    except:
                        self.catchError()
        except:
            pass

    def stop_record(self):
            try:
                if d(resourceId="com.autel.explorer:id/tv_recording_left_time").exists(3):
                    try:
                        d(resourceId="com.autel.explorer:id/iv_camera_record_controller").click()
                    except:
                        pass
                    time.sleep(1)
                    print('stop recording!')
                    time.sleep(1)
                # d.implicitly_wait(2)
                    i =0
                    while i <=10:
                        if d(resourceId="com.autel.explorer:id/tv_recording_left_time").exists(3):
                            d(resourceId="com.autel.explorer:id/iv_camera_record_controller").click()
                            print('not stopped! restop!')
                            time.sleep(2)
                        else:
                            break
                        i += 1
                else:
                    print('recording is stopped')
            except:
                pass

            time.sleep(2)

    ##---------------------------- Camera Settings ------------------------------------##
    #网格设置
    def camSetGrid(self,num):

        try:
            if d(resourceId="com.autel.explorer:id/iv_camera_setting"):
                d(resourceId="com.autel.explorer:id/iv_camera_setting").click()
            else:
                d(resourceId="com.autel.explorer:id/rl_camera_setting").click()
            time.sleep(1)

            if d(resourceId="com.autel.explorer:id/view_chart"):
                d(resourceId="com.autel.explorer:id/layout_histogram_cancel").click()
                time.sleep(0.5)
            time.sleep(0.5)
            d(resourceId="com.autel.explorer:id/rl_general_setting_item").click()
            time.sleep(1)

            if num == 'None':
                time.sleep(0.5)
                d.implicitly_wait(5.0)
                d(resourceId="com.autel.explorer:id/general_setting_image_item_value_text").click()
            elif num == 'Grid':
                time.sleep(0.5)
                d.implicitly_wait(5.0)
                d(resourceId="com.autel.explorer:id/general_setting_image_item_value_text", text=u"Grid").click()
            elif num == 'Grid + Line':
                time.sleep(0.5)
                d.implicitly_wait(5.0)
                d(resourceId="com.autel.explorer:id/general_setting_image_item_value_text", text=u"Grid + Line").click()
            else:
                pass
            time.sleep(2)

            d.long_click(0.3, 0.5)
        except:
            self.catchError()
            d.long_click(0.3,0.5)

    #中心点设置
    def camSetCenterPoint(self,num):

        try:
            d(resourceId="com.autel.explorer:id/iv_camera_setting").click()
            time.sleep(0.5)
            d(resourceId="com.autel.explorer:id/item_general_setting_key_tv", text=u"Center Point").click()
            time.sleep(0.5)
        except:
            self.catchError()
            logging.info('进入相册设置失败')

        if num == 'None':
            d.implicitly_wait(5.0)
            d(resourceId="com.autel.explorer:id/general_setting_image_item_value_text").click()
        elif num == 'SquareWithout':
            d.implicitly_wait(5.0)
            d(resourceId="com.autel.explorer:id/general_setting_image_item_value_text",
              text=u"Square(Without Center Point)").click()
        elif num == 'SquareWith':
            d.implicitly_wait(5.0)
            d(resourceId="com.autel.explorer:id/general_setting_image_item_value_text",
              text=u"Square(With Center Point)").click()
        elif num == 'Cross':
            d(resourceId="com.autel.explorer:id/general_setting_image_item_value_text", text=u"Cross").click()
        elif num == 'CircleWith':
            d.implicitly_wait(5.0)
            d(resourceId="com.autel.explorer:id/general_setting_image_item_value_text",
              text=u"Circle(With Center Point)").click()
        elif  num == 'CircleWithout':
            d.implicitly_wait(5.0)
            d(resourceId="com.autel.explorer:id/general_setting_image_item_value_text",
              text=u"Circle(Without Center Point)").click()
        else:
            pass
        time.sleep(0.5)
        d.click(0.3,0.5)

    #直方图 参数为 'on' , 'off'
    def camSetHis(self,num):
        # d(resourceId="com.autel.explorer:id/iv_camera_setting").click()
        try:
            d(resourceId="com.autel.explorer:id/rl_camera_setting").click()
            time.sleep(2)
        except:
            self.catchError()
        d.screenshot('screen.jpg')
        im = Image.open("screen.jpg")
        r,g,b =im.split()
        color =b.getpixel((1766, 591)) #oneplus 3
        # color =b.getpixel((1363,391))

        print(color)
        time.sleep(2)
        status =''
        if color == 223:
            status='on'
        elif color != 223:
            status = 'off'
        else:
            pass

        if num == status:
            time.sleep(0.5)
            d.long_click(0.3,0.5)
        elif num != status:

            try:
                d(resourceId="com.autel.explorer:id/item_general_setting_autel_ss").click()
                time.sleep(1)
            except:
                self.catchError()

            if status =='off':
                d.drag(0.78, 0.206, 0.411, 0.271,0.12)

            time.sleep(2)
            d.click(0.3, 0.5)
        else:
            pass

    # 过曝警告 参数为 'on' , 'off'
    def camSetOverExp(self,num):

        try:
            d(resourceId="com.autel.explorer:id/iv_camera_setting").click()
            time.sleep(2)
        except:
            self.catchError()
        try:
            d.screenshot('screen.jpg')
            im = Image.open("screen.jpg")
            r,g,b =im.split()
            color =b.getpixel((1766, 767))

            print(color)
            time.sleep(1)
            status =''
            if color == 223:
                status='on'
            elif color != 223:
                status = 'off'
            else:
                pass

            if num == status:
                time.sleep(0.5)
                d.click(0.3,0.5)
            elif num != status:
                try:
                    d(resourceId="com.autel.explorer:id/item_general_setting_autel_ss", className="android.view.View",
                      instance=1).click()
                except:
                    self.catchError()
                    logging.info('没点到！')
                time.sleep(0.5)
                d.click(0.3, 0.5)
            else:
                pass
        except:
            self.catchError()

    # subtitle.ass file 参数为 'on' , 'off' 录相模式下使用.
    def camSetSubtitle(self, num):
        try:
            d(resourceId="com.autel.explorer:id/iv_camera_setting").click()
            time.sleep(2)
        except:
            self.catchError()
            logging.info('没点到相机设置按钮！')

        d.screenshot('screen.jpg')
        im = Image.open("screen.jpg")
        print('mode:',im.mode)
        print('size:',im.size)
        r, g, b = im.split()
        color = b.getpixel((1766, 947))

        try:
            print(color)
            time.sleep(1)
            status = ''
            if color == 223:
                status = 'on'
            elif color != 223:
                status = 'off'
            else:
                pass

            if num == status:
                time.sleep(2)
                d.click(0.3, 0.5)
            elif num != status:
                try:
                    d(resourceId="com.autel.explorer:id/item_general_setting_autel_ss", className="android.view.View",
                      instance=2).click()
                except:
                    self.catchError()
                time.sleep(0.5)
                d.click(0.3, 0.5)
            else:
                pass
        except:
            self.catchError()
        # im = Image.new("RGB", (128, 128), "#FF0000")
        # im.save("test1.png")  # 图像im为128x128大小的红色图像。
        # im = Image.new("RGB", (128, 128))  # 图像im为128x128大小的黑色图像，因为变量color不赋值的话，图像内容被设置为0，即黑色。
        # im.save("test2.png")
        # im = Image.new("RGB", (128, 128), "red")  # 图像im为128x128大小的红色图像。
        # im.save("test3.png")
        # im2 = Image.new('RGB',(200,200),"blue")
        # im2.save('blue.png')

    # AntiFlicker 参数为： 'Auto','60HZ' ,'50HZ'
    def camSetAntiFlicker(self,num):
        logging.info("function start.")
        self.setVedioExpo('AUTO')
        logging.info('start  into av fucntion rate')
        self.scrollToAVFunc('FRAME RATE')
        logging.info('ends into av fucntion rate')
        time.sleep(2)
        try:
            # text =d(resourceId="com.autel.explorer:id/tv_first_para", textContains="FPS").get_text()
            if d(resourceId="com.autel.explorer:id/tv_ui_first_para", text=u"FRAME RATE"):
                text = d(resourceId="com.autel.explorer:id/tv_ui_first_para", text=u"FRAME RATE").up(resourceId="com.autel.explorer:id/tv_first_para").get_text()
                print(int(text[:-3]))
            else:
                print("get frame rate test again.")
                text = d(resourceId="com.autel.explorer:id/tv_ui_first_para", text=u"FRAME RATE").up(
                    resourceId="com.autel.explorer:id/tv_first_para").get_text()
                print(int(text[:-3]))
                time.sleep(2)
            if int(text[:-3]) < 100:

                try:
                    d(resourceId="com.autel.explorer:id/iv_camera_setting").click()
                    time.sleep(3)
                    d.swipe(0.58, 0.77, 0.58, 0.2)
                    # self.swipe_right_up()
                    time.sleep(3)
                    text = d(resourceId="com.autel.explorer:id/item_general_setting_key_tv",
                             text=u"Anti-Flicker").right(
                        resourceId="com.autel.explorer:id/item_general_setting_value_tv").get_text()
                    print('anti-flicker now is :%s' % text)
                    time.sleep(0.5)
                    if text == num:
                        print("Already set to %s" % num)
                        time.sleep(2)
                        d.click(0.3, 0.5)
                        time.sleep(5)
                    else:
                        try:
                            d(resourceId="com.autel.explorer:id/item_general_setting_key_tv",
                              text=u"Anti-Flicker").click()
                            time.sleep(1.5)
                            d.implicitly_wait(3)
                            if num == 'Auto':
                                d(resourceId="com.autel.explorer:id/general_setting_tv_item_value").click()
                            elif num == '50Hz':
                                d(resourceId="com.autel.explorer:id/general_setting_tv_item_value",
                                  text=u"50Hz").click()
                            elif num == '60Hz':
                                d(resourceId="com.autel.explorer:id/general_setting_tv_item_value",
                                  text=u"60Hz").click()
                            else:
                                pass

                            time.sleep(1)
                            d.click(0.3, 0.5)
                            time.sleep(5)
                        except:
                            self.catchError()
                            d.long_click(0.3, 0.5)
                            time.sleep(1)

                except:
                    d.click(0.3, 0.5)
                    self.catchError()
                    time.sleep(1)
            else:
                print('frame rate is bigger than 100FPS.')
                time.sleep(1)

        except:
            self.catchError()
            logger.error("maybe can't get FPS")
        time.sleep(3)
        logging.info("fucntion ends.")


     # Vedeo Encoding Format : 'H.265','H.264'  Optimized
    def camSetVideoEncoding(self,num):

        try:
            d.implicitly_wait(5.0)
            d(resourceId="com.autel.explorer:id/iv_camera_setting").click()
            time.sleep(2)
            d.swipe(0.58, 0.77, 0.58, 0.12)
            time.sleep(1.5)
            if d(resourceId="com.autel.explorer:id/item_general_setting_value_tv", text=num):
                text = num
                print("Already set to %s!" % num)
                time.sleep(2)
                d.click(0.3, 0.5)
                time.sleep(3)
            else:
                d(resourceId="com.autel.explorer:id/item_general_setting_key_tv",
                  text=u"Video Encoding Format").click()
                time.sleep(1.5)
                d.implicitly_wait(3.0)

                if num == 'H.264':
                    try:
                        d(resourceId="com.autel.explorer:id/general_setting_tv_item_value").click()
                    except:
                        self.catchError()
                else:
                    try:
                        d(resourceId="com.autel.explorer:id/general_setting_tv_item_value", text=u"H.265").click()
                    except:
                        self.catchError()

                time.sleep(2)
                d.long_click(0.3, 0.5)
                time.sleep(3)

        except:
            self.catchError()
            time.sleep(0.5)
            d.long_click(0.3, 0.5)
            time.sleep(3)

        '''
        try:
            d.implicitly_wait(5.0)
            d(resourceId="com.autel.explorer:id/iv_camera_setting").click()
            time.sleep(2)
            d.swipe(0.58, 0.77, 0.58, 0.12)
            time.sleep(1.5)
            if d(resourceId="com.autel.explorer:id/item_general_setting_value_tv", text=u"H.265"):
                text = "H.265"
            else:
                text = "H.264"
            if text == num:
                print("Already set to %s!" % num)
                time.sleep(2)
                d.click(0.3, 0.5)
                time.sleep(1.5)

            else:
                if num == 'H.264':
                    d(resourceId="com.autel.explorer:id/item_general_setting_key_tv",
                      text=u"Video Encoding Format").click()
                    time.sleep(1.5)
                    d.implicitly_wait(3.0)
                    d(resourceId="com.autel.explorer:id/general_setting_tv_item_value").click()
                    time.sleep(2)
                    d.long_click(0.3, 0.5)
                    time.sleep(3)
                elif num == 'H.265':
                    d(resourceId="com.autel.explorer:id/item_general_setting_key_tv",
                      text=u"Video Encoding Format").click()
                    time.sleep(1.5)
                    d.implicitly_wait(3.0)
                    d(resourceId="com.autel.explorer:id/general_setting_tv_item_value", text=u"H.265").click()
                    time.sleep(2)
                    d.long_click(0.3, 0.5)
                    time.sleep(3)

                else:
                    pass

        except:
            self.catchError()
            time.sleep(0.5)
            d.long_click(0.3, 0.5)
            time.sleep(3)

        '''



    #格式化sd卡， 'yes' 'no'
    def camSetFormatsdcard(self,num):

        try:
            d(resourceId="com.autel.explorer:id/rl_camera_setting").click()
            # d(resourceId="com.autel.explorer:id/iv_camera_setting").click()
            time.sleep(1)
            d.swipe(0.77, 0.77, 0.77, 0.12)
            time.sleep(2)
            d(resourceId="com.autel.explorer:id/item_general_setting_key_tv", text=u"Format SD Card").click()
            time.sleep(2)
            if num == 'yes':
                d(resourceId="com.autel.explorer:id/tv_ok").click()
                time.sleep(30)
            else:
                d(resourceId="com.autel.explorer:id/tv_cancel").click()
        except:
            print('格式化失败，请重新尝试')
            self.catchError()
            logging.info('格式化失败！')
            d.long_click(0.3,0.5)
            time.sleep(2)

    # 重置相机 Reset Camera : 'yes' , 'no'
    def  camReset(self,num):

        time.sleep(1)
        d.swipe(0.77, 0.77, 0.77, 0.12)
        time.sleep(5)

        try:
            d(resourceId="com.autel.explorer:id/item_general_setting_key_tv", text=u"Reset Camera").click()
            time.sleep(2)

        except:
            print('Could not find "Reset Camera button ",try again')
            d.swipe(0.77, 0.77, 0.77, 0.12)
            try:
                d(resourceId="com.autel.explorer:id/item_general_setting_key_tv", text=u"Reset Camera").click()
                time.sleep(3)
                if num == 'yes':
                    try:
                        d(resourceId="com.autel.explorer:id/tv_ok").click()

                        time.sleep(2)
                    except:
                        self.catchError()
                else:

                    try:
                        d(resourceId="com.autel.explorer:id/tv_cancel").click()
                        time.sleep(2)
                    except:
                        self.catchError()
            except:
                self.catchError()


    def swipe_right_up(self):
        d.swipe(0.78,0.84,0.78,0.23)

    def camSettingsReset(self):
        # time.sleep(1)

        try:
            d(resourceId="com.autel.explorer:id/rl_camera_setting").click()
            time.sleep(1.5)
            d.implicitly_wait(5.0)

            if d(resourceId="com.autel.explorer:id/camera_general_setting_title").exists():
                self.swipe_right_up()
                time.sleep(0.8)
                if d(resourceId="com.autel.explorer:id/item_general_setting_key_tv", text=u"Reset Camera").exists():
                    d(resourceId="com.autel.explorer:id/item_general_setting_key_tv", text=u"Reset Camera").click()
                    time.sleep(1.5)
                    d.implicitly_wait(5.0)
                    d(resourceId="com.autel.explorer:id/tv_ok").click()
                    time.sleep(10)

                else:
                    self.swipe_right_up()
                    d(resourceId="com.autel.explorer:id/item_general_setting_key_tv", text=u"Reset Camera").click()
                    time.sleep(1.5)
                    d.implicitly_wait(5.0)
                    d(resourceId="com.autel.explorer:id/tv_ok").click()
                    time.sleep(10)
        except:
            self.catchError()
            logging.info('reset failed.')

    ##--------------------------- Ablum  ------------------------------------##

    #进入相册预览界面
    def test_into_Album(self):
        if d(resourceId="com.autel.explorer:id/tv_autel_home_start").exists():
            d(resourceId="com.autel.explorer:id/tv_autel_home_start").click()
            time.sleep(5)
            d(resourceId="com.autel.explorer:id/civ_album_playback").click()
            time.sleep(0.5)
        elif  d(resourceId="com.autel.explorer:id/civ_album_playback").exists():
            d(resourceId="com.autel.explorer:id/civ_album_playback").click()
            time.sleep(0.5)
        elif d(resourceId="com.autel.explorer:id/iv_setting_close").exists():
            d(resourceId="com.autel.explorer:id/iv_setting_close").click()
            time.sleep(0.1)
            d(resourceId="com.autel.explorer:id/civ_album_playback").click()
            time.sleep(0.5)
        elif d(resourceId="com.autel.explorer:id/camera_general_setting_title").exists():
            d.click(0.3, 0.3)
            time.sleep(0.5)
            d(resourceId="com.autel.explorer:id/civ_album_playback").click()
            time.sleep(0.5)
        elif d(text=u"Intelligent Flight").exists():
            d(resourceId="com.autel.explorer:id/layout_cancel").click()
            time.sleep(0.2)
            d(resourceId="com.autel.explorer:id/civ_album_playback").click()
            time.sleep(0.5)
        elif  d(resourceId="com.autel.explorer:id/iv_mode_switcher").exists():
            d(resourceId="com.autel.explorer:id/civ_album_playback").click()
            time.sleep(0.5)
        elif d(resourceId="com.autel.explorer:id/tv_enter_album_list").exists():
            pass
        else:
            pass

    #进入相册列表界面
    def test_into_Album_List(self):
        #在首页
        if d(resourceId="com.autel.explorer:id/tv_autel_home_start").exists():
            d(resourceId="com.autel.explorer:id/tv_autel_home_start").click()
            time.sleep(5)
            d(resourceId="com.autel.explorer:id/civ_album_playback").click()
            time.sleep(0.5)
            d(resourceId="com.autel.explorer:id/tv_enter_album_list").click()
            time.sleep(1)
            d.implicitly_wait(5)
         #在相册预览界面
        elif  d(resourceId="com.autel.explorer:id/civ_album_playback").exists():
            d(resourceId="com.autel.explorer:id/civ_album_playback").click()
            time.sleep(1.5)
            d.implicitly_wait(5)
            d(resourceId="com.autel.explorer:id/tv_enter_album_list").click()
            time.sleep(1)
            d.implicitly_wait(5)
        #在设置界面
        elif d(resourceId="com.autel.explorer:id/iv_setting_close").exists():
            d(resourceId="com.autel.explorer:id/iv_setting_close").click()
            time.sleep(0.5)
            d.implicitly_wait(5)
            d(resourceId="com.autel.explorer:id/civ_album_playback").click()
            time.sleep(0.5)
            d.implicitly_wait(5)
            d(resourceId="com.autel.explorer:id/tv_enter_album_list").click()
            time.sleep(1)
            d.implicitly_wait(5)
        #在相机设置界面
        elif d(resourceId="com.autel.explorer:id/camera_general_setting_title").exists():
            d.click(0.3, 0.3)
            time.sleep(0.5)
            d(resourceId="com.autel.explorer:id/civ_album_playback").click()
            time.sleep(0.5)
            d(resourceId="com.autel.explorer:id/tv_enter_album_list").click()
            time.sleep(1)
            d.implicitly_wait(5)
        #在智能飞行界面
        elif d(text=u"Intelligent Flight").exists():
            d(resourceId="com.autel.explorer:id/layout_cancel").click()
            time.sleep(0.2)
            d(resourceId="com.autel.explorer:id/civ_album_playback").click()
            time.sleep(0.5)
            d(resourceId="com.autel.explorer:id/tv_enter_album_list").click()
            time.sleep(1)
            d.implicitly_wait(5)
         #在媒体捕获画面（拍照，录相）
        elif  d(resourceId="com.autel.explorer:id/iv_mode_switcher").exists():
            d(resourceId="com.autel.explorer:id/civ_album_playback").click()
            time.sleep(0.5)
            d(resourceId="com.autel.explorer:id/tv_enter_album_list").click()
            time.sleep(1)
            d.implicitly_wait(5)
        #在相册预览界面
        elif d(resourceId="com.autel.explorer:id/tv_enter_album_list").exists():
            d(resourceId="com.autel.explorer:id/tv_enter_album_list").click()
            time.sleep(1)
        #已在相册列表界面
        elif d(resourceId="com.autel.explorer:id/tv_album_select").exists():
            pass
        else:
            pass

#-------------------------------其他接口-----------------------------------------#
    #回到首页
    def goStart(self):
        #在首页
        if  d(resourceId="com.autel.explorer:id/tv_autel_home_start", text=u"GO FLY",
          className="android.widget.TextView").exists():
           print('is in start page')
           time.sleep(1)
        # 在已登录界面
        elif d(resourceId="com.autel.explorer:id/tv_logout", text=u"Logout", className="android.widget.TextView").exists():
            print('is in login interface!')
            d(resourceId="com.autel.explorer:id/iv_common_back", className="android.widget.ImageView").click()
            time.sleep(5)

        #在登录界面
        elif d(resourceId="com.autel.explorer:id/btn_login", text=u"Login", className="android.widget.Button").exists():
            d(resourceId="com.autel.explorer:id/iv_back", className="android.widget.ImageView").click()
            time.sleep(5)

        #在注册界面
        elif d(resourceId="com.autel.explorer:id/btn_login", text=u"Register", className="android.widget.Button").exists():
            d(resourceId="com.autel.explorer:id/iv_back", className="android.widget.ImageView").click()
            d.implicitly_wait(10)
            d(resourceId="com.autel.explorer:id/iv_back", className="android.widget.ImageView").click()
            time.sleep(5)




            # 在功能界面

        #在个人信息中心
        elif d(resourceId="com.autel.explorer:id/tv_common_title", text=u"Personal Information", className="android.widget.TextView").exists():
            d(resourceId="com.autel.explorer:id/iv_back", className="android.widget.ImageView").click()
            time.sleep(5)

         #在功能界面
        elif d(resourceId="com.autel.explorer:id/rl_left").exists():
            d(resourceId="com.autel.explorer:id/rl_left").click()
            time.sleep(5)

        # 在设置界面
        elif d(resourceId="com.autel.explorer:id/tv_setting_title", text=u"Settings",className="android.widget.TextView").exists():
            d(resourceId="com.autel.explorer:id/iv_setting_close", className="android.widget.ImageView").click()
            d.implicitly_wait(15)
            d(resourceId="com.autel.explorer:id/rl_left", className="android.widget.RelativeLayout").click()
            d.implicitly_wait(15)
            d(resourceId="com.autel.explorer:id/iv_user_icon_default", className="android.widget.ImageView").click()
            time.sleep(8)

        # 在相机设置界面
        elif d(resourceId="com.autel.explorer:id/camera_general_setting_title", text=u"Camera Settings",className="android.widget.TextView").exists():
            d.click(0.5, 0.5)
            time.sleep(0.5)
            d(resourceId="com.autel.explorer:id/rl_left", className="android.widget.RelativeLayout").click()
            time.sleep(8)

        #在飞行方录界面
        elif d(resourceId="com.autel.explorer:id/flight_record_device_sn_tv").exists():
            d(resourceId="com.autel.explorer:id/flight_record_back").click()
            time.sleep(0.5)
            d.click(0.3,0.5)

        else:
            pass

    #进入智能飞行界面
    def flyControlSet(self):
        # 已经在设置界面
        if d(resourceId="com.autel.explorer:id/tv_setting_title").exists():
            print('is  in settings!')
        # 在开始界面
        elif d(resourceId="com.autel.explorer:id/tv_autel_home_start").exists():
            d(resourceId="com.autel.explorer:id/tv_autel_home_start").click()
            time.sleep(5)
            d(resourceId="com.autel.explorer:id/rl_setting").click()
            time.sleep(0.5)
        # 在地图界面
        elif d(resourceId="com.autel.explorer:id/compass_iv").exists():
            d(resourceId="com.autel.explorer:id/rl_setting").click()
            time.sleep(0.5)
        # 在媒体拍摄界面
        elif d(resourceId="com.autel.explorer:id/iv_camera_outer").exists():
            d(resourceId="com.autel.explorer:id/rl_setting").click()
            time.sleep(0.5)
        # 在各智能飞行界面
        elif d(resourceId="com.autel.explorer:id/rl_left").exists():
            d(resourceId="com.autel.explorer:id/rl_setting").click()
            time.sleep(0.5)
        # 在智能飞行选择界面
        elif d(text=u"Intelligent Flight").exists():
            d(resourceId="com.autel.explorer:id/layout_cancel").click()
            time.sleep(0.5)
            d(resourceId="com.autel.explorer:id/rl_setting").click()
        # 在VR模式界面
        elif d(resourceId="com.autel.explorer:id/iv_vr_settings").exists():
            d(resourceId="com.autel.explorer:id/iv_back").click()
            time.sleep(2)
            d(resourceId="com.autel.explorer:id/tv_autel_home_start").click()
            time.sleep(5)
            d(resourceId="com.autel.explorer:id/rl_setting").click()
        else:
            pass

    # 登录
    def login(self,mail, passwd):
        self.goStart()
        d.set_fastinput_ime(True)
        if d(resourceId="com.autel.explorer:id/iv_user_icon_default"):
            d(resourceId="com.autel.explorer:id/iv_user_icon_default").click()
        else:
            d(resourceId="com.autel.explorer:id/iv_user_icon").click()
        # 已登录情况下
        if d(resourceId="com.autel.explorer:id/iv_user_setting", className="android.widget.ImageView").exists():
            d(resourceId="com.autel.explorer:id/iv_user_photo", className="android.widget.ImageView").click()
            d.implicitly_wait(10)
            d(resourceId="com.autel.explorer:id/tv_logout", text=u"Logout", className="android.widget.TextView").click()
            time.sleep(0.5)
            d(resourceId="com.autel.explorer:id/tv_ok", text=u"OK", className="android.widget.TextView").click()
            time.sleep(6)
            d(resourceId="com.autel.explorer:id/iv_user_icon_default", className="android.widget.ImageView").click()
            d.implicitly_wait(10)
            d(resourceId="com.autel.explorer:id/ed_email").set_text(mail)
            d(resourceId="com.autel.explorer:id/ed_pwd").set_text(passwd)
            d(resourceId="com.autel.explorer:id/btn_login").click()
            time.sleep(2)
            d.click(0.3, 0.5)

        else:

            d(resourceId="com.autel.explorer:id/ed_email").set_text(mail)
            time.sleep(0.5)
            d(resourceId="com.autel.explorer:id/ed_pwd").set_text(passwd)
            time.sleep(0.5)
            d.implicitly_wait(5.0)
            d(resourceId="com.autel.explorer:id/btn_login").click()
            time.sleep(5)
            d.click(0.3, 0.5)

    # 进入个人中心
    def intoPerCenter(self):
        self.goStart()
        time.sleep(0.5)
        if d(resourceId="com.autel.explorer:id/iv_user_icon").exists(3):
            d(resourceId="com.autel.explorer:id/iv_user_icon").click_exists(5)
            time.sleep(0.5)
        else:
            d(resourceId="com.autel.explorer:id/iv_user_icon_default", className="android.widget.ImageView").click_exists(5)
            time.sleep(0.5)

def main():
    test = Camera()
    time.sleep(0.5)
    # print('\n白平衡预设')   #debuging
    # WBPreSet3_5()
    # time.sleep(3)


    # test.setVideoPIV('60S')
    # test.setVideoPIV('30S')
    # test.setVideoPIV('5S')
    # test.setVideoPIV('10S')
    # test.setVideoPIV('MANUAL')
    # test.GimbalAngle("50°")  #0°'

    # test.SetPictureSize("4000x3000") # pass

    # test.SetPictureFomat("JPG") #PASS
    # SetPictureMode_pre("TIMELAPSE")
    # insideCercle("5s")


    # test.SetPictureMode("TIMELAPSE","5s")  # 输入时间注意大小写
    # test.insideCircleBurst("2")
    # test.insideCircleTimelapse("5s")
    # test.insideCircleAeb("5")

    # test.SetPictureExpo('AUTO')  #PASS

    # test.SetPictureIso("800")     #PASS
    # test.SetPictureShutter("1\"")    #PASS                   # 整数时间后才加 "
    # test.SetpictureEv("+0.93")    #PASS
    # test.SetPictureWB("SUNNY")      #PASS

    # test.SetPictureColor("NONE")
    # test.SetPictureDigizoom("2.0X")


    # test.SetPictureWB("2100K")  #注意大小写
    # test.scrollToFunc("STYLE")
    # test.SetPitureStyle("-3 +2 ±0") #注意 "." 不要忘了.
    # test.SetPitureStyle("NEUT.") #注意 "." 不要忘了.
    # test.SetPitureStyle("-1 -1 -1") #注意 "." 不要忘了.

    #2-8 设置相机拍照格式为 JPG+RAW 拍照
    # test.SetPictureFomat("JPG")
    # test.SetPictureMode_pre('AEB', "3")
    # test.shot()
    # time.sleep(5)

    ##2-9 大小设为 4000x3000, 各种组合拍照
    # test.SetPictureSize("4000x3000")
    # test.SetPictureFomat("RAW")
    # test.SetPictureMode_pre('AEB',"3")
    # test.shot()
    # time.sleep(5)

    ##2-10 照片大小：16：9 4000x2250
    # test.SetPictureSize("4000x2250")
    # test.SetPictureFomat("JPG")
    # test.SetPictureMode_pre('AEB',"5")
    # test.shot()
    # time.sleep(5)

    # ##3-1 风格 标准
    # test.SetPitureStyle("STD.")
    # test.shot()

    # ##3-2 风格 柔和
    # test.SetPitureStyle("NEUT.")
    # test.SetPictureMode_pre('SINGLE')
    # test.shot()

    # ##3-2 风格 风光
    # test.SetPitureStyle("LAND.")
    # test.SetPictureMode_pre('SINGLE')
    # test.shot()
    #
    # ##3-5 白平衡：自动
    # test.SetPictureWB("AUTO")
    # test.shot()
    #time.sleep(5)


    # ### 3-6 白平衡 晴天
    # test.SetPictureWB("SUNNY")
    # test.shot()
    # time.sleep(5)

    # ### 3-7 白平衡 阴天
    # test.SetPictureWB("CLOUDY")
    # test.shot()
    # time.sleep(5)

    # ## 3-8 白平衡：白炽灯
    # test.SetPictureWB("INCAN")
    # test.shot()
    # time.sleep(5)
    #
    # # ## 3-9 白平衡：荧光灯
    # test.SetPictureWB("NEON")
    # test.shot()
    # time.sleep(5)
    #
    #
    # # ## 3-10 白平衡：自定义
    # test.SetPictureWB("8000K")
    # test.shot()
    # time.sleep(5)

    # 3-11 颜色
    # test.SetPictureColor("BEACH")
    # test.shot()
    # time.sleep(5)

    # # 3-14 EV
    # test.SetpictureEv("+2.3")
    # test.shot()
    # time.sleep(5)

    # 3 - 15 ISO
    # test.SetPictureIso("400")
    # test.shot()
    # time.sleep(5)
    #
    # ##3-16 SHUTTER 快门
    # test.SetPictureShutter("1/2")
    # test.shot()
    # time.sleep(5)
    # test.recordStatusConfirm()

    # test.captureStatusConfirm()
    # test.recordStatusConfirm()
    # test.scrollToAVFunc('PIV')
    # test.scrollToAVFunc('WB')
    # test.scrollToAVFunc('STANDARD')
    # test.scrollToAVFunc('DIGITAL ZOOM')
    # test.scrollToAVFunc('PIV')
    # test.scrollToAVFunc('WB')
    # test.scrollToAVFunc('FORMAT')
    # test.scrollToAVFunc('STYLE')
    # test.setVedioStandard('NTSC')
    # test.setVedioFormat('MOV')
    # test.setVideoReso("4K+")
    # test.setVideoFramerate("240FPS")
    # test.setVideoPIV('MANUAL')
    # test.setVideoPIV('5S')
    # test.setVideoPIV('60S')
    # test.setVideoPIV('MANUAL')
    # test.setVideoPIV('30S')
    # test.setVedioExpo('MANUAL')
    # test.setVedioExpo('AUTO')
    # if d(resourceId="com.autel.explorer:id/tv_ui_first_para", text=u"PIV", className="android.widget.TextView").up\
    #     (resourceId="com.autel.explorer:id/tv_first_para", text=u"MANUAL", className="android.widget.TextView"):
    #     print("Yes,It exists!")
    # else:
    #     print("Not exist!")
    # # test.setVedioExpo("AUTO")
    # # test.setVedioIso('1600')
    # # test.setVedioShutter('1/80')
    # # test.setVedioEv('+1.3')
    # test.setVedioWB('2000K')
    # test.SetPictureWB('2000K')
    # test.setVedioColor("ART")
    # test.setVedioStyle('STD.')
    # test.setVedioDigizoom('2.0X')
    # ifchecked=d(resourceId="com.autel.explorer:id/view_chart",clickable=False).exists()
    # print(ifchecked)
    # test.scrollToFunc('SIZE')
    # test.scrollToFunc('DIGITAL ZOOM')
    # test.scrollToFunc('FORMAT')
    # test.scrollToFunc('STYLE')
    # test.scrollToFunc('MODE')
    # # test.scrollToFunc('COLOR')
    # # test.scrollToFunc('EXPOSURE MODE')
    # # test.scrollToFunc('WB')
    # # test.scrollToFunc('ISO')
    #
    #
    while True:
        test.camSetAntiFlicker('50Hz')
        time.sleep(3)
        test.camSetAntiFlicker('60Hz')
        time.sleep(3)

        test.camSetAntiFlicker('Auto')
        time.sleep(3)





if __name__ == '__main__':
    main()

# cam=Camera()
# cam.GimbalAngle("50°")


# SetPitureShutter("1/12.5")
# SetPitureWB("%sK")  #待解决
# SetPictureExpo("MANUAL")


#scrollToFunc("COLOR")
#SetPictureSize("4000x2250")
# SetPictureFomat('RAW+JPG')
# testPhoneBasic()


# insideCercle("5s")
# SetPictureMode("BURST","3")  #有小问题要调试
# SetPictureExpo("AUTO")
# SetPictureIso("800")


# d.app_stop()

