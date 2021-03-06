#enconding：utf-8
import datetime
from PIL import Image
import logging
logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a,%d %b %Y %H:%M:%S',
                    filename='CamShots.log',
                    filemode='a')

import random
import uiautomator2 as u2
import time
pkg_name='com.autel.explorer'
# pkg_name='com.taobao.taobao'
# d=u2.connect_wifi('192.168.1.12')  # LG
# d=u2.connect_wifi('192.168.15.31')
d=u2.connect_usb('7cc8c0d9')  # One Plus 3
# d=u2.connect_wifi('192.168.1.11') #One Plus 3
# d=u2.connect_usb('50a72b24260b') #华为
# d=u2.connect_usb('12dd6e53') # OnePlus 6
# d=u2.connect_wifi('192.168.1.17') # OnePlus 6
# d=u2.connect_usb('12dd6e53') # OnePlus 6
# d=u2.connect_usb('7cc8c0d9') # OnePlus 3
# d.wait_activity(30)
# bootstrap
# d.app_start(pkg_name)
d.wait_timeout = 30.0
time.sleep(1)
d.implicitly_wait(10.0)

class ParaError(Exception):
    pass
    # print("Parameter input error")

class SwitchError(Exception):
    pass
    # print("Switch windows Error!")

class Camera:

    def shot(self):
        # d(resourceId="com.autel.explorer:id/iv_camera_outer").click()
        d(resourceId="com.autel.explorer:id/rel_camera_takephoto_controller").click()
        print("shot")
    listPara=[]
    def __init__(self):
        pass
        # self.listPara=[]
    #基本测试
    def testPhoneBasic(self):
        for i in range(1,11):
            time.sleep(1.5)

            d(resourceId="com.autel.explorer:id/tv_autel_home_start").click_exists(timeout=5000)
            # d(resourceId="com.autel.explorer:id/tv_autel_home_start").click(timeout=5000)
            time.sleep(3)
            # d(resourceId="com.autel.explorer:id/tv_mode").exists(timeout=5000)
            # d(resourceId="com.autel.explorer:id/tv_mode").click_exists(timeout=5000)
            # # d(resourceId="com.autel.explorer:id/tv_mode").click(timeout=5000)
            # time.sleep(1)
            #
            # d(resourceId="com.autel.explorer:id/model_choice_bg").click()
            # time.sleep(0.5)

            d.swipe(0.32, 0.94, 0.68, 0.94)
            time.sleep(1.5)
            d(text="FORMAT").click()
            f=random.randint(1,3)
            print(f)
            if f==1:
                d(text="JPG").click()

            if f==2:
                d(text="RAW").click()
            else:
                d(text="RAW+JPG").click()


            time.sleep(0.5)
            d.click(0.5,0.5)
            # inst=random.randint(1,11)
            d(resourceId="com.autel.explorer:id/rel_camera_takephoto_controller").click()
            time.sleep(1)
            d(resourceId="com.autel.explorer:id/rl_left").click()
            print('Ran for %s times' % i)
            time.sleep(1.5)

    #在主界面判断是否在拍照状态
    def captureStatusConfirm(self):
        time.sleep(0.5)


        if d(resourceId="com.autel.explorer:id/rel_camera_takephoto_controller").exists(): #如果有拍照按钮,则确认是照相模式啥都不做了
            pass

        elif d(resourceId="com.autel.explorer:id/iv_camera_record_controller").exists(): #("录相按钮"): 点切换按钮
             d(resourceId="com.autel.explorer:id/iv_mode_switcher").click() # ("照片录相切换按钮 ").click()



        elif d(resourceId="com.autel.explorer:id/compass_iv").exists():    # ("指南针按钮 "): 说明在地图模式,点击小图切换到相机
            print('Now is in the map window.')
            d.click(0.14, 0.268)
            time.sleep(3)

            # 切换成功的情况
            if  d(resourceId="com.autel.explorer:id/rel_camera_takephoto_controller").exists() or d(resourceId="com.autel.explorer:id/iv_camera_record_controller").exists():  #切换成功的情况
                    if d(resourceId="com.autel.explorer:id/rel_camera_takephoto_controller").exists():  # 如果有拍照按钮,则确认是照相模式
                        print('Is in the Shotting Window')

                    elif d(resourceId="com.autel.explorer:id/iv_camera_record_controller").exists():  # ("录相按钮"): 点切换按钮
                        print('Switching to Shotting Window')
                        d(resourceId="com.autel.explorer:id/iv_mode_switcher").click()  # ("照片录相切换按钮 ").click()
                    else:
                        pass

            # 切换不成功的情况
            else:
                d(resourceId="com.autel.explorer:id/intercept_img_shrink").click()  #把小图展开,再点小图中央切换到拍摄画面,
                time.sleep(1)
                d.click(0.14, 0.268)
                time.sleep(1)
                if d(resourceId="com.autel.explorer:id/rel_camera_takephoto_controller").exists():  # 如果有拍照按钮,则确认是照相模式
                    pass

                elif d(resourceId="com.autel.explorer:id/iv_camera_record_controller").exists():  # ("录相按钮"): 点切换按钮
                    d(resourceId="com.autel.explorer:id/iv_mode_switcher").click()  # ("照片录相切换按钮 ").click()

    #切换到拍照画面
    def SwitchtoCaptureMode(self):

            if  d(resourceId="com.autel.explorer:id/tv_autel_home_start").exists():  #在开始界面
                d(resourceId="com.autel.explorer:id/tv_autel_home_start").click()
                time.sleep(3)
                if d(resourceId="com.autel.explorer:id/rel_camera_takephoto_controller").exists():

                    print('Is in the Shotting Window')
                else:
                    d(resourceId="com.autel.explorer:id/iv_mode_switcher").click()

            if d(resourceId="com.autel.explorer:id/iv_camera_outer").exists():
                if d(resourceId="com.autel.explorer:id/rel_camera_takephoto_controller").exists():

                    print('Is in the Shotting Window')
                else:
                    d(resourceId="com.autel.explorer:id/iv_mode_switcher").click()


            elif  d(text=u"Intelligent Flight").exists():            #在智能飞行界面
                    d(resourceId="com.autel.explorer:id/model_choice_bg").click() #点击相机按钮
                    self.captureStatusConfirm()

            elif  d(resourceId="com.autel.explorer:id/tv_setting_title").exists():     #在设置界面

                # d(resourceId="com.autel.explorer:id/iv_setting_close").click()                      #点击关闭
                    d(resourceId="com.autel.explorer:id/iv_setting_close").click()
                    self.captureStatusConfirm()


            elif  d(resourceId="com.autel.explorer:id/camera_general_setting_title").exists(): #在相机设置界面
                    d.click(0.5,0.5)                                 #画面中央点一下跳出

                    self.captureStatusConfirm()

            elif d(resourceId="com.autel.explorer:id/warn_history_title_tv").exists(): #在飞机状态画面
                    d.click(0.5,0.5)                                                       #画面中央点一下
                    self.captureStatusConfirm()
                # captureStatusConfirm()
            # elif driver.find_element_by_id("图片预览界面"):              #在图片预览画面
            #     pass

            # elif     driver.find_element_by_id("在用户中心"):            #在用户中心,登 录
            #         driver.back()
            # elif    driver.find_element_by_id("在注册中心"):
            #     pass
            else:
               logging.exception(SwitchError)
               print("Switching to Shotting widow failed")

    #滑动选择相机属性
    def scrollToFunc(self,func):
        self.SwitchtoCaptureMode()
        time.sleep(2)      #如果不稳定,建议设成3秒以上


        listAll = ['SIZE', 'FORMAT', 'MODE', 'EXPOSURE MODE', 'ISO', 'SHUTTER', 'EV', 'WB', 'COLOR', 'STYLE',
                   'DIGITAL ZOOM']
        seq=0
        if func in listAll:
            for i in range (0,len(listAll)):
                if func == listAll[i]:
                    seq=i
        else:
            print("You have iput a wrong Shotting Function.")
            logging.exception(ParaError)

        if   d(resourceId="com.autel.explorer:id/tv_ui_first_para", text=func).exists():
            print("is in function %s"%func)

        else:
            try:
                i = 0
                while i <= len (listAll):  # 通过参数指定模式的参数编号 seq 与 当前滑块 最左边的 所见元素的编号比较, seq比较大,就左移,否则右移
                    flag=False
                    if  d(resourceId="com.autel.explorer:id/tv_ui_first_para", text=listAll[i]).exists():

                        if i > seq:
                            j = 0
                            while j <= 10:
                                d.swipe(0.32, 0.94, 0.68, 0.94)  # 往左边滑
                                time.sleep(0.5)
                                if  d(resourceId="com.autel.explorer:id/tv_ui_first_para", text=func).exists():
                                    # d(resourceId="com.autel.explorer:id/tv_ui_first_para", text=func).click()
                                    print('find %s' %func)
                                    flag=True
                                    break

                                else:
                                    pass


                                j += 1

                        else:
                            j = 0
                            while j <= 10:
                                d.swipe (0.68, 0.94, 0.32, 0.94)  # 往右边滑
                                time.sleep(0.5)
                                if  d(resourceId="com.autel.explorer:id/tv_ui_first_para", text=func).exists():
                                    print('find %s' %func)
                                    flag=True
                                    break

                                else:
                                    pass
                            j += 1

                    if flag:
                        break
                    i += 1

            except:
                logging.exception('------------Exceptions Caught--------')
    #设置照片大小
    def SetPictureSize(self,Size):
        self.scrollToFunc('SIZE')

        time.sleep(0.5)

        #检查输入参数

        if d(resourceId="com.autel.explorer:id/tv_first_para",text=Size).exists():
            print("is %s setted"%Size)

        else:

            d(resourceId="com.autel.explorer:id/tv_ui_first_para",text='SIZE').click()

            if Size == "4000x3000":
                    # time.sleep(2)

                    try:
                        d(resourceId="com.autel.explorer:id/tv_second_para", text=u"4000x3000(4:3)").click()
                    except:
                        logging.exception('------------Exceptions Caught--------')

            else:
                    try:
                        d(resourceId="com.autel.explorer:id/tv_second_para").click()
                    except:
                        logging.exception('------------Exceptions Caught--------')

            #设置完成点击屏幕中央
            time.sleep(1)
            d.click(0.5,0.5)

    #设置照片格式
    def SetPictureFomat(self,format):
        self.scrollToFunc('FORMAT')
        time.sleep(0.5)

        if d(resourceId="com.autel.explorer:id/tv_first_para",text=format).exists():
            print("%s setted"%format)

        else:
            d(resourceId="com.autel.explorer:id/tv_ui_first_para", text='FORMAT').click()
        # 检查输入参数
            try:
                if format == "JPG":
                    d(resourceId="com.autel.explorer:id/tv_second_para").click()

                elif format == "RAW":
                    d(resourceId="com.autel.explorer:id/tv_second_para", text="RAW").click()

                else:
                    d(resourceId="com.autel.explorer:id/tv_second_para", text="RAW+JPG").click()
            except:
                logging.exception('------------Exceptions Caught--------')

            # 设置完成点击屏幕中央
            time.sleep(1)

            d.click(0.5, 0.5)

    def insideListCircleCommon(self,num):

        if num in self.listPara:

            for i in range(0, len(self.listPara)):
                if num == self.listPara[i]:
                    seq = i

            if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                time.sleep(0.5)
                d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                d.click(0.5, 0.5)

            else:

                for i in range(0, len(self.listPara)):
                    if num == self.listPara[i]:
                        seq = i
                try:
                    i = 0
                    while i <= len(self.listPara):  # 通过参数指定模式的参数编号 seq 与 当前滑块 最左边的 所见元素的编号比较, seq比较大,就左移,否则右移
                        flag = False
                        if d(resourceId="com.autel.explorer:id/tv_second_para", text=self.listPara[i]):
                            # driver.find_element_by_android_uiautomator('new UiSelector().text(listMode[i])'):

                            if i > seq:
                                j = 0
                                while j <= 30:
                                    d.swipe(0.32, 0.82, 0.68, 0.82)  # 滚动条
                                    time.sleep(0.8)
                                    if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                                        # if d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).exists():
                                        d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                                        d.click(0.5, 0.5)
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
                                        time.sleep(0.5)
                                        d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                                        d.click(0.5, 0.5)
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
                    logging.exception('------------Exceptions Caught--------')

            time.sleep(1)

    def insideCircleBurst(self,num):

        listPara = ["3", "5", "7", "10", "14"]
        # self.insideListCircleCommon(num)

        if num in listPara:

            for i in range(0, len(listPara)):
                if num == listPara[i]:
                    seq = i
                    break

            if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                time.sleep(0.5)
                d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                print("BURST %s selected" % num)
                time.sleep(1)
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
                        if d(resourceId="com.autel.explorer:id/tv_second_para", text=listPara[i]):
                            # driver.find_element_by_android_uiautomator('new UiSelector().text(listMode[i])'):

                            if i > seq:
                                j = 0
                                while j <= 30:
                                    d.swipe(0.32, 0.82, 0.68, 0.82)  # 滚动条
                                    time.sleep(0.8)
                                    if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                                        # if d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).exists():
                                        d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                                        print("BURST %s selected"%num)
                                        d.click(0.5, 0.5)
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
                                        time.sleep(0.5)
                                        d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                                        print("BURST %s selected" % num)
                                        d.click(0.5, 0.5)
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
                    logging.exception('------------Exceptions Caught--------')

            time.sleep(1)



        else:
            print("输入 BURST 的参数有错误!")
            logging.exception(ParaError)
            time.sleep(1)

            d.click(0.5, 0.5)

    def insideCircleTimelapse(self,num):

        listPara = ["2s", "5s", "7s", "10s", "20s","30s","60s"  ]

        if num in listPara:

            for i in range(0, len(listPara)):
                if num == listPara[i]:
                    seq = i
                    break

            if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                time.sleep(0.5)
                try:
                    d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                    print("TIMELAPSE %s selected" % num)
                except:
                    logging.exception('------------Exceptions Caught--------')
                time.sleep(1)
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
                        if d(resourceId="com.autel.explorer:id/tv_second_para", text=listPara[i]):
                            # driver.find_element_by_android_uiautomator('new UiSelector().text(listMode[i])'):

                            if i > seq:
                                j = 0
                                while j <= 30:
                                    d.swipe(0.32, 0.82, 0.68, 0.82)  # 滚动条
                                    time.sleep(0.8)
                                    if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                                        # if d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).exists():
                                        d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                                        print("TIMELAPSE %s selected" % num)
                                        time.sleep(0.5)
                                        d.click(0.5, 0.5)
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
                                        time.sleep(0.5)
                                        d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                                        print("TIMELAPSE %s selected" % num)
                                        time.sleep(0.5)
                                        d.click(0.5, 0.5)
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
                    logging.exception('------------Exceptions Caught--------')

            time.sleep(1)

        else:
            print("输入的参数有错误!")
            logging.exception(ParaError)
            time.sleep(1)
            d.click(0.5, 0.5)

    def insideCircleAeb(self, num):

        listPara = ["3", "5"]

        if num in listPara:
            seq = 0
            for i in range(0, len(listPara)):
                if num == listPara[i]:
                    seq = i

            if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                time.sleep(0.5)
                try:
                    d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                    print("AEB %s selected" % num)
                except:
                    logging.exception('------------Exceptions Caught--------')

                time.sleep(0.5)
                d.click(0.5, 0.5)

            else:
                seq=0
                for i in range(0, len(listPara)):
                    if num == listPara[i]:
                        seq = i
                try:
                    i = 0
                    while i <= len(listPara):  # 通过参数指定模式的参数编号 seq 与 当前滑块 最左边的 所见元素的编号比较, seq比较大,就左移,否则右移
                        flag = False
                        if d(resourceId="com.autel.explorer:id/tv_second_para", text=listPara[i]):
                            # driver.find_element_by_android_uiautomator('new UiSelector().text(listMode[i])'):

                            if i > seq:
                                j = 0
                                while j <= 30:
                                    d.swipe(0.32, 0.82, 0.68, 0.82)  # 滚动条
                                    time.sleep(0.8)
                                    if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                                        # if d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).exists():
                                        d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                                        print("AEB %s selected" % num)
                                        time.sleep(0.5)
                                        d.click(0.5, 0.5)
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
                                        time.sleep(0.5)
                                        d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                                        print("AEB %s selected" % num)
                                        time.sleep(0.5)
                                        d.click(0.5, 0.5)
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
                    logging.exception('------------Exceptions Caught--------')

            time.sleep(1)

        else:
            print("输入 AEB 的参数有错误!")
            logging.exception(ParaError)
            time.sleep(1)
            d.click(0.5, 0.5)

    #相机 mode　子项选择
    def SetPictureMode(self,mode,num=None):

        self.scrollToFunc('MODE')
        try:
            d(resourceId="com.autel.explorer:id/tv_ui_first_para", text='MODE').click()
        except:
            logging.exception('------------Exceptions Caught--------')

        time.sleep(1)
        if  d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).exists:         #没有的话就往左或者往右翻找找吧
            if mode == "SINGLE":
                try:
                    d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).click()
                except:
                    logging.exception('------------Exceptions Caught--------')
                print("SINGEL selected")
                time.sleep(1)
                d.click(0.5, 0.5)

            else:
                try:
                    d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).click()
                except:
                    logging.exception('------------Exceptions Caught--------')
                time.sleep(0.5)

                try:
                    if d(resourceId="com.autel.explorer:id/iv_second_next").exists():
                        d(resourceId="com.autel.explorer:id/iv_second_next").click()
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
                    logging.exception('------------Exceptions Caught--------')


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

                #  当mode选择为"SINGLE "的时候
                # if seq == 0:
                #     listMode=['SINGLE','BURST','TIMELAPSE','AEB']  #把参放进列表里头:
                #     i=0
                #     while i<=len(listMode) :   #通过参数指定模式的参数编号 seq 与 当前滑块 最左边的 所见元素的编号比较, seq比较大,就左移,否则右移
                #         flag= False
                #         if d(resourceId="com.autel.explorer:id/tv_second_para", text=listMode[i]):
                #          # driver.find_element_by_android_uiautomator('new UiSelector().text(listMode[i])'):
                #
                #               if i>seq:
                #                   j=0
                #
                #                   while j<=10:
                #                       d.swipe(0.32, 0.82, 0.68, 0.82) #往左边滑
                #                       try:
                #                           d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).click()
                #                           flag=True
                #
                #                       except:
                #                           print("not found,continue...")
                #                       finally:
                #                          if flag:
                #                            break
                #                   j+=1
                #
                #
                #               else:
                #                   j = 0
                #                   while j <= 10:
                #                       d.swipe(0.68, 0.82, 0.32, 0.82)  # 往右边滑
                #                       try:
                #                           d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).click().click()
                #                           # driver.find_element_by_android_uiautomator('new UiSelector().text(mode)').click()
                #                           flag = True
                #
                #                       except:
                #                           print("not found,continue...")
                #
                #                       finally:
                #                          if flag:
                #                            break
                #                   j += 1
                #
                #         if flag:
                #              break
                #         i+=1    #   #



                #  当mode参数为其他时,定位的需要的mode 中,

                listMode = ['SINGLE', 'BURST', 'TIMELAPSE', 'AEB']  # 把参放进列表里头:
                try:
                    i = 0
                    while i <= len(listMode):  # 通过参数指定模式的参数编号 seq 与 当前滑块 最左边的 所见元素的编号比较, seq比较大,就左移,否则右移
                        flag = False
                        if d(resourceId="com.autel.explorer:id/tv_second_para", text=listMode[i]):
                            # driver.find_element_by_android_uiautomator('new UiSelector().text(listMode[i])'):

                            if i > seq:
                                j = 0
                                while j <= 10:
                                    d.swipe(0.32, 0.82, 0.68, 0.82)  # 往左边滑
                                    time.sleep(1.5)
                                    if d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).exists():

                                        if mode == "SINGLE":
                                            try:
                                                d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).click()
                                                print("SINGEL selected")
                                            except:
                                                logging.exception('------------Exceptions Caught--------')
                                            finally:
                                                flag=True
                                            time.sleep(1)
                                            d.click(0.5, 0.5)
                                    # if d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).exists():
                                        else:
                                            try:
                                                d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).click()
                                            except:
                                                logging.exception('------------Exceptions Caught--------')
                                            if d(resourceId="com.autel.explorer:id/iv_second_next").exists():
                                                try:
                                                    d(resourceId="com.autel.explorer:id/iv_second_next").click()
                                                except:
                                                    logging.exception('------------Exceptions Caught--------')
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
                                    time.sleep(1)


                                    if d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).exists():
                                        if mode == "SINGLE":
                                            try:
                                                d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).click()
                                            except:
                                                logging.exception('------------Exceptions Caught--------')
                                            print("SINGEL selected")
                                            flag=True
                                            time.sleep(1)
                                            d.click(0.5, 0.5)

                                        else:

                                            d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).click()
                                            if d(resourceId="com.autel.explorer:id/iv_second_next").exists():
                                                try:
                                                    d(resourceId="com.autel.explorer:id/iv_second_next").click()
                                                except:
                                                    logging.exception('------------Exceptions Caught--------')
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
                    logging.exception('------------Exceptions Caught--------')
                d.click(0.5,0.5)
    #相机各选项 二级菜单参数选择
    # def insideCercle(num):
    #     # 内层循环----按第二个参数选择.
    #     time.sleep(1)
    #     if d(resourceId="com.autel.explorer:id/iv_second_next").exists():  #参数可见
    #         d.click(0.496, 0.817)
    #         # d(resourceId="com.autel.explorer:id/iv_second_next").click()
    #     else:
    #                                                                     #参数不可见
    #         # listBurst = ["3", "5", "7","10","14"]
    #         # if num == "3":
    #         #     seq = 0
    #         # elif num == "5":
    #         #     seq = 1
    #         # elif num == "7":
    #         #     seq = 2
    #         # elif num == "10":
    #         #     seq = 3
    #         # elif num == "14":
    #         #     seq = 4
    #         # else:
    #         #     print("输入的参数有误")
    #
    #         if num == "5s":
    #             seq = 0
    #         elif num == "7s":
    #             seq = 1
    #         elif num == "10s":
    #             seq = 2
    #         elif num == "20s":
    #             seq = 3
    #         elif num == "30s":
    #             seq = 4
    #         elif num == "60s":
    #             seq = 5
    #         else:
    #             print("INDISE 输入的参数有误")
    #
    #         listPara = ["5s", "7s", "10s", "20s", "30", "60s"]  # 把参放进列表里头:
    #
    #         if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
    #             time.sleep(0.5)
    #             d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
    #
    #         else:
    #             # listPara = ["3","5","7","10","14"]  # 把参放进列表里头:
    #             # listPara = ["5s","7s","10s","20s","30","60s"]  # 把参放进列表里头:
    #             i = 0
    #             while i <= len(listPara):  # 通过参数指定模式的参数编号 seq 与 当前滑块 最左边的 所见元素的编号比较, seq比较大,就左移,否则右移
    #                 flag = False
    #                 if d(resourceId="com.autel.explorer:id/tv_second_para", text=listPara[i]):
    #                     # driver.find_element_by_android_uiautomator('new UiSelector().text(listMode[i])'):
    #
    #                     if i > seq:
    #                         j = 0
    #                         while j <= 10:
    #                             d.swipe(0.32, 0.82, 0.68, 0.82)  # 往左边滑
    #                             time.sleep(1)
    #                             if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
    #                                 # if d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).exists():
    #                                 d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
    #                                 flag = True
    #                             else:
    #                                 print("Para,not found,continue...")
    #                             if flag:
    #                                 break
    #                             j += 1
    #
    #
    #                     else:
    #                         j = 0
    #                         while j <= 10:
    #                             d.swipe(0.68, 0.82, 0.32, 0.82)  # 往右边滑
    #                             time.sleep(1)
    #
    #                             if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
    #                                 time.sleep(0.5)
    #                                 d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
    #                                 flag = True
    #                             else:
    #                                 print("not found,continue...")
    #
    #                             if flag:
    #                                 break
    #                             j += 1
    #
    #                 else:
    #                     pass
    #
    #                 if flag:
    #                     break
    #                 i += 1
    #     time.sleep(1)
    #
    #     d.click(0.5, 0.5)

    def SetPictureMode_old(self,mode,num=None):
        self.SetPictureMode_pre(mode)
        # self.insideCircle(num)

    def SetPictureExpo(self,exp):
        self.scrollToFunc("EXPOSURE MODE")
        time.sleep(0.5)

        if d(resourceId="com.autel.explorer:id/tv_first_para",text=exp).exists():
            print("%s setted"%exp)

        else:
            try:
                d(resourceId="com.autel.explorer:id/tv_ui_first_para", text="EXPOSURE MODE").click()
            except:
                logging.exception('------------Exceptions Caught--------')

            if exp == "AUTO":
                try:
                    d(resourceId="com.autel.explorer:id/tv_second_para").click()
                except:
                    logging.exception('------------Exceptions Caught--------')
            elif exp == "MANUAL":
                try:
                    d(resourceId="com.autel.explorer:id/tv_second_para", text=u"MANUAL").click()
                except:
                    logging.exception('------------Exceptions Caught--------')
            else:
                print("曝光模式输入有误!")
                logging.exception(ParaError)
            time.sleep(1)

            d.click(0.5, 0.5)


    def SetPictureIso(self,num):
        self.SetPictureExpo("MANUAL")
        self.scrollToFunc("ISO")

        if d(resourceId="com.autel.explorer:id/tv_first_para",text=num).exists():
            print("is %s setted"%num)

        else:
            try:
                d(resourceId="com.autel.explorer:id/tv_ui_first_para", text="ISO").click()
            except:
                logging.exception('------------Exceptions Caught--------')

            if num == "100":
                seq = 0
            elif num == "200":
                seq = 1
            elif num == "400":
                seq = 2
            elif num == "800":
                seq = 3
            elif num == "1600":
                seq = 4
            elif num == "3200":
                seq = 5
            else:
                print("输入的参数有误")
                logging.exception(ParaError)

            listPara = ["100","200", "400", "800", "1600", "3200"]
            if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                time.sleep(0.5)
                try:
                    d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                except:
                    logging.exception('------------Exceptions Caught--------')

            else:
                try:
                    i = 0
                    while i <= len(listPara):  # 通过参数指定模式的参数编号 seq 与 当前滑块 最左边的 所见元素的编号比较, seq比较大,就左移,否则右移
                        flag = False
                        if d(resourceId="com.autel.explorer:id/tv_second_para", text=listPara[i]):
                            # driver.find_element_by_android_uiautomator('new UiSelector().text(listMode[i])'):

                            if i > seq:
                                j = 0
                                while j <= 10:
                                    d.swipe(0.32, 0.82, 0.68, 0.82)  # 往左边滑
                                    time.sleep(1)
                                    if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                                        # if d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).exists():
                                        try:
                                            d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                                        except:
                                            logging.exception('------------Exceptions Caught--------')
                                        finally:
                                            flag = True
                                    else:
                                        print("Para,not found,continue left swipe")
                                    if flag:
                                        break
                                    j += 1


                            else:
                                j = 0
                                while j <= 10:
                                    d.swipe(0.68, 0.82, 0.32, 0.82)  # 往右边滑
                                    time.sleep(1)
                                    if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                                        time.sleep(0.5)
                                        try:
                                            d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                                        except:
                                            logging.exception('------------Exceptions Caught--------')
                                        finally:
                                            flag = True
                                    else:
                                        print("Para,not found,continue right swipe")

                                    if flag:
                                        break
                                    j += 1

                        else:
                            pass

                        if flag:
                            break
                        i += 1
                except:
                    logging.exception('------------Exceptions Caught--------')

            time.sleep(1)

            d.click(0.5, 0.5)


    def SetPictureShutter(self,num):
        self.SetPictureExpo("MANUAL")
        self.scrollToFunc("SHUTTER")

        listPara = ["1/8000", "1/6000", "1/5000", "1/4000", "1/3200", "1/2500", "1/2000", "1/1600", "1/1250", "1/1000",
                       "1/800", "1/640", "1/500",
                       "1/400", "1/320", "1/240", "1/200", "1/160", "1/120", "1/100", "1/80", "1/60", "1/50", "1/40",
                       "1/30", "1/25", "1/20", "1/15", "1/12.5",
                       "1/10", "1/8", "1/6.25", "1/5", "1/4", "1/3", "1/2.5", "1/2", "1/1.67", "1/1.25", "1\"", "1.3\"",
                       "1.6\"", "2\"", "2.5\"", "3\"", "3.2\"",
                       "4\"", "5\"", "6\"", "8\""]
        if num not in listPara:
            print("You have inputed a wrong parameter")

        else:
            if d(resourceId="com.autel.explorer:id/tv_first_para",text=num).exists():
                print("%s setted"%num)

            else:
                try:
                    d(resourceId="com.autel.explorer:id/tv_ui_first_para", text="SHUTTER").click()
                except:
                    logging.exception('------------Exceptions Caught--------')
                ##########################
                seq=0
                for i in range(0, len(listPara)):
                    if num == listPara[i]:
                        seq = i
                        break

                if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                    time.sleep(0.5)
                    try:
                        d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                    except:
                        logging.exception('------------Exceptions Caught--------')

                else:
                    i = 0
                    while i <= len(listPara):  # 通过参数指定模式的参数编号 seq 与 当前滑块 最左边的 所见元素的编号比较, seq比较大,就左移,否则右移

                        flag = False
                        if d(resourceId="com.autel.explorer:id/tv_second_para", text=listPara[i]):
                            # driver.find_element_by_android_uiautomator('new UiSelector().text(listMode[i])'):

                            if i > seq:
                                j = 0
                                while j <= 20:
                                    d.swipe(0.32, 0.82, 0.68, 0.82)  # 往左边滑
                                    time.sleep(0.8)
                                    if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                                        # if d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).exists():
                                        try:
                                            d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                                        except:
                                            logging.exception('------------Exceptions Caught--------')
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
                                    d.swipe(0.68, 0.82, 0.32, 0.82)  # 往右边滑
                                    time.sleep(0.8)

                                    if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                                        time.sleep(0.5)
                                        try:
                                            d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                                        except:
                                            logging.exception('------------Exceptions Caught--------')
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

                d.click(0.5, 0.5)

    def SetpictureEv(self,num):
        self.SetPictureExpo("AUTO")
        self.scrollToFunc("EV")


        listPara = ["-3.0", "-2.7", "-2.3", "-2.0", "-1.7", "-1.3", "-1.0", "-0.7", "-0.3", "0","+0.3","+0.7","+1.0","+1.3","+1.7","+2.0","+2.3","+2.7","+3.0"]

        if num not in listPara:
            print("You have inputed a wrong parameter")

        else:
            if d(resourceId="com.autel.explorer:id/tv_first_para",text=num).exists():
                print("%s setted"%num)

            else:
                try:
                    d(resourceId="com.autel.explorer:id/tv_ui_first_para", text="EV").click()
                except:
                    logging.exception('------------Exceptions Caught--------')
                ##########################

                for i in range(0, len(listPara)):
                    if num == listPara[i]:
                        seq = i
                        break
                if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                    time.sleep(0.5)
                    try:
                        d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                    except:
                        logging.exception('------------Exceptions Caught--------')

                else:
                    i = 0
                    while i <= len(listPara):  # 通过参数指定模式的参数编号 seq 与 当前滑块 最左边的 所见元素的编号比较, seq比较大,就左移,否则右移
                        flag = False
                        if d(resourceId="com.autel.explorer:id/tv_second_para", text=listPara[i]):
                            # driver.find_element_by_android_uiautomator('new UiSelector().text(listMode[i])'):

                            if i > seq:
                                j = 0
                                while j <= 20:
                                    d.swipe(0.32, 0.82, 0.68, 0.82)  # 往左边滑
                                    time.sleep(0.8)
                                    if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                                        # if d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).exists():
                                        try:
                                            d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                                        except:
                                            logging.exception('------------Exceptions Caught--------')
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
                                    d.swipe(0.68, 0.82, 0.32, 0.82)  # 往右边滑
                                    time.sleep(0.8)

                                    if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                                        time.sleep(0.5)
                                        try:
                                            d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                                        except:
                                            logging.exception('------------Exceptions Caught--------')
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

                d.click(0.5, 0.5)

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
        if num in listPara:
            for i in range(0, len(listPara)):
                if num == listPara[i]:
                    seq = i
                    break

            if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                time.sleep(0.5)
                try:
                    d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                except:
                    logging.exception('------------Exceptions Caught--------')

            else:
                i = 0
                while i <= len(listPara):  # 通过参数指定模式的参数编号 seq 与 当前滑块 最左边的 所见元素的编号比较, seq比较大,就左移,否则右移
                    flag = False
                    if d(resourceId="com.autel.explorer:id/tv_second_para", text=listPara[i]):
                        if i > seq:
                            j = 0
                            while j <= 30:
                                d.swipe(0.32, 0.82, 0.68, 0.82)  # 滚动条
                                time.sleep(0.5)
                                if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                                    # if d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).exists():
                                    try:
                                        d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                                    except:
                                        logging.exception('------------Exceptions Caught--------')
                                    finally:
                                        flag = True
                                else:
                                    # print("Para,not found,continue...")
                                    print("not found,continue...,%sTime" % (j + 1))
                                if flag:
                                    break
                                j += 1


                        else:
                            j = 0
                            while j <= 30:
                                d.swipe(0.68, 0.82, 0.32, 0.82)  # 往右边滑
                                time.sleep(0.5)

                                if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                                    # time.sleep(0.5)
                                    try:
                                        d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                                    except:
                                        pass
                                    finally:
                                        flag= True
                                else:
                                    print("not found,continue...,%sTime"%(j+1))

                                if flag:
                                    break
                                j += 1

                    else:
                        pass

                    if flag:
                        break
                    i += 1

            time.sleep(1)

            d.click(0.5, 0.5)
        else:
            print("输入 xxxxK 的参数有错误!")
            logging.exception(ParaError)
            time.sleep(1)

            d.click(0.5, 0.5)

    def SetPictureWB(self,num):
        self.scrollToFunc("WB")

        if d(resourceId="com.autel.explorer:id/tv_first_para", text=num).exists():
            print("%s setted" % num)


        else:
            try:
                d(resourceId="com.autel.explorer:id/tv_ui_first_para", text=u"WB").click()
            except:
                logging.exception('------------Exceptions Caught--------')

            listPara = ["AUTO", "SUNNY", "CLOUDY", "INCAN", "NEON", "%sK"]



            if num not in ["AUTO", "SUNNY", "CLOUDY", "INCAN", "NEON"]:  # == x000K的情况:
                # (...) 存在的情况
                if d(resourceId="com.autel.explorer:id/iv_second_next").exists():
                    if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():# xxxxK 和 (...)均存在的情况
                        pass   #己经存在该选择项
                     #(...)存在, xxxxK不存在的情况,点(...)进入下一层循环
                    elif not  d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                        try:
                            d(resourceId="com.autel.explorer:id/iv_second_next").click()
                        except:
                            pass
                        time.sleep(0.5)

                        try:
                            self.insideCircleWB(num)
                        except:
                            logging.exception('------------Exceptions Caught--------')

                        # else:
                        #     self.insideCercle(num)


                        time.sleep(1)

                        d.click(0.5, 0.5)

                # (...)不存在的情况
                else:
                    i=0
                    while i<=2:
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
                                except:
                                    logging.exception('------------Exceptions Caught--------')
                                time.sleep(0.5)

                                try:
                                    self.insideCircleWB(num)
                                except:
                                    logging.exception('------------Exceptions Caught--------')
                                break

                        i+=1

                    # while True:



            #   num not in ["AUTO", "SUNNY", "CLOUDY", "INCAN", "NEON"]:  # == x000K的情况:
            else:

                for i in range(0, len(listPara)-1):
                    if num == listPara[i]:
                        seq = i
                        break

                if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                    time.sleep(0.5)
                    try:
                        d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                    except:
                        logging.exception('------------Exceptions Caught--------')

                else:
                    i = 0
                    while i <= len(listPara):  # 通过参数指定模式的参数编号 seq 与 当前滑块 最左边的 所见元素的编号比较, seq比较大,就左移,否则右移
                        flag = False
                        if d(resourceId="com.autel.explorer:id/tv_second_para", text=listPara[i]):
                            # driver.find_element_by_android_uiautomator('new UiSelector().text(listMode[i])'):

                            if i > seq:
                                j = 0
                                while j <= 20:
                                    d.swipe(0.32, 0.82, 0.68, 0.82)  # 往左边滑
                                    time.sleep(0.8)
                                    if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                                        # if d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).exists():
                                        try:
                                            d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                                        except:
                                            logging.exception('------------Exceptions Caught--------')
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

                                    if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                                        time.sleep(0.5)
                                        try:
                                            d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                                        except:
                                            logging.exception('------------Exceptions Caught--------')
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
                d.click(0.5, 0.5)

    def SetPictureColor(self,num):
        self.scrollToFunc("COLOR")

        listPara = ["NONE", "LOG", "VIVID", "B&W", "ART", "FILM","BEACH","DREAM","CLASSIC","NOSTALGIC"]

        if num not in listPara:
            print("You have inputed a wrong parameter")

        else:

            if d(resourceId="com.autel.explorer:id/tv_first_para",text=num).exists():
                print("%s setted"%num)


            else:
                try:
                    d(resourceId="com.autel.explorer:id/tv_ui_first_para", text="COLOR").click()
                except:
                    logging.exception('------------Exceptions Caught--------')
                for i in range(0, len(listPara)):
                    if num == listPara[i]:
                        seq = i
                        break

                if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                    time.sleep(0.5)
                    try:
                        d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                    except:
                        logging.exception('------------Exceptions Caught--------')



                else:
                    i = 0
                    while i <= len(listPara):  # 通过参数指定模式的参数编号 seq 与 当前滑块 最左边的 所见元素的编号比较, seq比较大,就左移,否则右移
                        flag = False
                        if d(resourceId="com.autel.explorer:id/tv_second_para", text=listPara[i]):
                            # driver.find_element_by_android_uiautomator('new UiSelector().text(listMode[i])'):

                            if i > seq:
                                j = 0
                                while j <= 20:
                                    d.swipe(0.32, 0.82, 0.68, 0.82)  # 往左边滑
                                    time.sleep(0.8)
                                    if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                                        # if d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).exists():
                                        try:
                                            d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                                        except:
                                            logging.exception('------------Exceptions Caught--------')
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
                                    d.swipe(0.68, 0.82, 0.32, 0.82)  # 往右边滑
                                    time.sleep(0.8)

                                    if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                                        time.sleep(0.5)
                                        try:
                                            d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                                        except:
                                            logging.exception('------------Exceptions Caught--------')
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

                d.click(0.5, 0.5)


    def insideCircleContrast(self,num):

        listPara = ["-3", "-2", "-1", "±0", "+1", "+2", "+3" ]
        print(num[3:5])
        num=num[3:5]
        if num in listPara:

            for i in range(0, len(listPara)):
                if num == listPara[i]:
                    seq = i
                    break
            if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                time.sleep(0.5)
                try:
                    d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                except:
                    logging.exception('------------Exceptions Caught--------')

            else:

                for i in range(0, len(listPara)):
                    if num == listPara[i]:
                        seq = i
                        break
                i = 0
                while i <= len(listPara):  # 通过参数指定模式的参数编号 seq 与 当前滑块 最左边的 所见元素的编号比较, seq比较大,就左移,否则右移
                    flag = False
                    if d(resourceId="com.autel.explorer:id/tv_second_para", text=listPara[i]):
                        # driver.find_element_by_android_uiautomator('new UiSelector().text(listMode[i])'):

                        if i > seq:
                            j = 0
                            while j <= 30:
                                d.swipe(0.32, 0.82, 0.68, 0.82)  # 滚动条
                                time.sleep(0.8)
                                if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                                    # if d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).exists():
                                    try:
                                        d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                                    except:
                                        logging.exception('------------Exceptions Caught--------')
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
                                    time.sleep(0.5)
                                    try:
                                        d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                                    except:
                                        logging.exception('------------Exceptions Caught--------')
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



        else:
            print("输入 contrast 的参数有错误!")
            logging.exception(ParaError)
            time.sleep(1)

            d.click(0.5, 0.5)

    def insideCircleSharp(self,num):

        listPara = ["-3", "-2", "-1", "±0", "+1", "+2", "+3" ]
        print(num[0:2])
        num=num[0:2]
        if num in listPara:
            for i in range(0, len(listPara)):
                if num == listPara[i]:
                    seq = i
                    break

            if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                time.sleep(0.5)
                try:
                    d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                except:
                    logging.exception('------------Exceptions Caught--------')

            else:
                i = 0
                while i <= len(listPara):  # 通过参数指定模式的参数编号 seq 与 当前滑块 最左边的 所见元素的编号比较, seq比较大,就左移,否则右移
                    flag = False
                    if d(resourceId="com.autel.explorer:id/tv_second_para", text=listPara[i]):
                        # driver.find_element_by_android_uiautomator('new UiSelector().text(listMode[i])'):

                        if i > seq:
                            j = 0
                            while j <= 30:
                                d.swipe(0.32, 0.82, 0.68, 0.82)  # 滚动条
                                time.sleep(0.8)
                                if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                                    # if d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).exists():
                                    try:
                                        d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                                    except:
                                        logging.exception('------------Exceptions Caught--------')
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
                                    time.sleep(0.5)
                                    try:
                                        d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                                    except:
                                        logging.exception('------------Exceptions Caught--------')
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



        else:
            print("输入 Sharp 的参数有错误!")
            logging.exception(ParaError)
            time.sleep(1)

            d.click(0.5, 0.5)

    def insideCircleSaturation(self,num):

        listPara = ["-3", "-2", "-1", "±0", "+1", "+2", "+3"]
        print(num[6:8])
        num=num[6:8]
        if num in listPara:
            for i in range(0, len(listPara)):
                if num == listPara[i]:
                    seq = i
                    break

            if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                time.sleep(0.5)
                d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()

            else:
                i = 0
                while i <= len(listPara):  # 通过参数指定模式的参数编号 seq 与 当前滑块 最左边的 所见元素的编号比较, seq比较大,就左移,否则右移
                    flag = False
                    if d(resourceId="com.autel.explorer:id/tv_second_para", text=listPara[i]):
                        # driver.find_element_by_android_uiautomator('new UiSelector().text(listMode[i])'):

                        if i > seq:
                            j = 0
                            while j <= 30:
                                d.swipe(0.32, 0.82, 0.68, 0.82)  # 滚动条
                                time.sleep(0.8)
                                if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                                    # if d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).exists():
                                    try:
                                        d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                                    except:
                                        logging.exception('------------Exceptions Caught--------')
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
                                    time.sleep(0.5)
                                    try:
                                        d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                                    except:
                                        logging.exception('------------Exceptions Caught--------')
                                    finally:
                                        flag = True
                                else:
                                    print("not found,continue...",j+1)

                                if flag:
                                    break
                                j += 1

                    else:
                        pass

                    if flag:
                        break
                    i += 1

            time.sleep(1)



        else:
            print("输入 saturation 的参数有错误!")
            time.sleep(1)

            # d.click(0.5, 0.5)


    def insideCircleStyle(self,num):
        time.sleep(0.5)
        try:
            d(resourceId="com.autel.explorer:id/iv_second_next").click()
        except:
            logging.exception('------------Exceptions Caught--------')
        self.insideCircleContrast(num)
        try:
            d(resourceId="com.autel.explorer:id/tv_back").click()
        except:
            logging.exception('------------Exceptions Caught--------')
        time.sleep(1)

        try:
            d(resourceId="com.autel.explorer:id/tv_ui_second_para").click()
            d(resourceId="com.autel.explorer:id/iv_second_next").click()
        except:
            logging.exception('------------Exceptions Caught--------')
        self.insideCircleSharp(num)
        try:
            d(resourceId="com.autel.explorer:id/tv_back").click()
        except:
            logging.exception('------------Exceptions Caught--------')
        time.sleep(1)

        d(resourceId="com.autel.explorer:id/tv_ui_second_para", text=u"SATURATION").click()
        try:
            d(resourceId="com.autel.explorer:id/iv_second_next").click()
        except:
            logging.exception('------------Exceptions Caught--------')
        self.insideCircleSaturation(num)
        try:
            d(resourceId="com.autel.explorer:id/tv_back").click()
        except:
            logging.exception('------------Exceptions Caught--------')
        time.sleep(1)

        print("Style %s is Setted" % num)
        d.click(0.5,0.5)


    def SetPitureStyle(self,num):
        # self.scrollToFunc("STYLE")
        self.scrollToFunc("STYLE")
        listPara = ["STD.", "NEUT.", "LAND.",'%s']

        # == 自定义的情况:
        if num not in ["STD.", "NEUT.", "LAND."]:

            # (...) 存在的情况

            if d(resourceId="com.autel.explorer:id/tv_first_para", text=num).exists():
                print("Style %s is Setted"%num)

            else:

                try:
                    d(resourceId="com.autel.explorer:id/tv_ui_first_para", text=u"STYLE").click()
                except:
                    logging.exception('------------Exceptions Caught--------')
                if d(resourceId="com.autel.explorer:id/iv_second_next").exists():
                    if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():# "指定参数" 和 (...)均存在的情况
                        pass   #己经存在该选择项

                     #(...)存在, "xx xx xx"不存在的情况,点(...)进入下一层循环
                    elif not  d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                        try:
                            d(resourceId="com.autel.explorer:id/iv_second_next").click()
                        except:
                            logging.exception('------------Exceptions Caught--------')
                        time.sleep(0.5)
                        self.insideCircleStyle(num)

                else:
                    j=0
                    while j<=3:
                        d.swipe(0.68, 0.82, 0.32, 0.82)  # 滑向滚动条右侧
                        if d(resourceId="com.autel.explorer:id/iv_second_next").exists():
                            if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():  # "指定参数" 和 (...)均存在的情况
                                d.click(0.5,0.5)
                                break  # 己经存在该选择项

                            # (...)存在, xxxxK不存在的情况,点(...)进入下一层循环
                            elif not d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                                try:
                                    d(resourceId="com.autel.explorer:id/iv_second_next").click()
                                except:
                                    logging.exception('------------Exceptions Caught--------')
                                time.sleep(0.5)

                                self.insideCircleStyle(num)
                                break

        # 是预设前三项情况
        else:

            d(resourceId="com.autel.explorer:id/tv_ui_first_para", text=u"STYLE").click()

            for i in range(0, len(listPara)-1):
                if num == listPara[i]:
                    seq = i
                    break

            if d(resourceId="com.autel.explorer:id/tv_ui_second_para", text=num).exists():
                time.sleep(0.5)
                try:
                    d(resourceId="com.autel.explorer:id/tv_ui_second_para", text=num).click()
                except:
                    logging.exception('------------Exceptions Caught--------')

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
                                    except:
                                        logging.exception('------------Exceptions Caught--------')
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
                                    time.sleep(0.5)
                                    try:
                                        d(resourceId="com.autel.explorer:id/tv_ui_second_para", text=num).click()
                                    except:
                                        logging.exception('------------Exceptions Caught--------')
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
            d.click(0.5, 0.5)


    def SetPictureDigizoom(self,num):

            self.scrollToFunc("DIGITAL ZOOM")
            listPara = ["1.0X", "2.0X", "3.0X", "4.0X","5.0X","6.0X","7.0X","8.0X"]

            if num not in listPara:
                print("You have inputed a wrong parameter")


            else:

                if d(resourceId="com.autel.explorer:id/tv_first_para", text=num).exists():
                    print("%s setted" % num)

                else:
                    try:
                        d(resourceId="com.autel.explorer:id/tv_ui_first_para", text="DIGITAL ZOOM").click()
                    except:
                        logging.exception('------------Exceptions Caught--------')

                    for i in range(0, len(listPara)):
                        if num == listPara[i]:
                            seq = i
                            break

                    if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                        time.sleep(0.5)
                        try:
                            d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                        except:
                            logging.exception('------------Exceptions Caught--------')

                    else:
                        i = 0
                        while i <= len(listPara):  # 通过参数指定模式的参数编号 seq 与 当前滑块 最左边的 所见元素的编号比较, seq比较大,就左移,否则右移
                            flag = False
                            if d(resourceId="com.autel.explorer:id/tv_second_para", text=listPara[i]):
                                # driver.find_element_by_android_uiautomator('new UiSelector().text(listMode[i])'):

                                if i > seq:
                                    j = 0
                                    while j <= 20:
                                        d.swipe(0.32, 0.82, 0.68, 0.82)  # 往左边滑
                                        time.sleep(0.8)
                                        if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                                            # if d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).exists():
                                            try:
                                                d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                                            except:
                                                logging.exception('------------Exceptions Caught--------')
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
                                        d.swipe(0.68, 0.82, 0.32, 0.82)  # 往右边滑
                                        time.sleep(0.8)

                                        if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                                            time.sleep(0.5)
                                            try:
                                                d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                                            except:
                                                logging.exception('------------Exceptions Caught--------')
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

                    d.click(0.5, 0.5)

    #  '0°'
    def GimbalAngle(self,num):
        self.SwitchtoCaptureMode()
        angle=d(resourceId="com.autel.explorer:id/tv_arch_indicator").get_text()
        if num == angle:
            print("Needed Gimbal angle was set.")
        else:
            d(resourceId="com.autel.explorer:id/rl_gimbal_angle").click()

            try:
                d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
            except:
                logging.exception('------------Exceptions Caught--------')
            time.sleep(0.5)
            d.click(0.5,0.5)

##---------------------------- Recoding Module ------------------------------------##
        # 在主界面判断是否在录相状态
    def recordStatusConfirm(self):
            time.sleep(0.5)

            if d(resourceId="com.autel.explorer:id/iv_camera_record_controller").exists():  # 如果有录相按钮,则确认是录相模式
                pass

            elif d(resourceId="com.autel.explorer:id/rel_camera_takephoto_controller").exists():  # ("拍照按钮"): 点切换按钮
                d(resourceId="com.autel.explorer:id/iv_mode_switcher").click()  # ("照片录相切换按钮 ").click()



            elif d(resourceId="com.autel.explorer:id/compass_iv").exists():  # ("指南针按钮 "): 说明在地图模式,点击小图切换到相机
                print('Now is in the map window.')
                d.click(0.14, 0.268)
                time.sleep(2)

                if d(resourceId="com.autel.explorer:id/iv_camera_record_controller").exists() \
                        or d(resourceId="com.autel.explorer:id/rel_camera_takephoto_controller").exists():  # 切换成功的情况
                    if d(resourceId="com.autel.explorer:id/iv_camera_record_controller").exists():  # 如果有录相按钮,则确认是录相模式
                        print('Is in the Recording Window')

                    elif d(
                            resourceId="com.autel.explorer:id/rel_camera_takephoto_controller").exists():  # ("照相按钮"): 点切换按钮
                        print('Switching to recording Window')
                        d(resourceId="com.autel.explorer:id/iv_mode_switcher").click()  # ("照片录相切换按钮 ").click()

                else:  # 切换不成功的情况
                    d(resourceId="com.autel.explorer:id/intercept_img_shrink").click()  # 把小图展开,再点小图中央切换到拍摄画面,
                    time.sleep(1)
                    d.click(0.14, 0.268)
                    time.sleep(1)
                    if d(resourceId="com.autel.explorer:id/iv_camera_record_controller").exists() \
                            or d(
                        resourceId="com.autel.explorer:id/rel_camera_takephoto_controller").exists():  # 切换成功的情况
                        if d(
                                resourceId="com.autel.explorer:id/iv_camera_record_controller").exists():  # 如果有录相按钮,则确认是录相模式
                            print('Is in the Recording Window')

                        elif d(
                                resourceId="com.autel.explorer:id/rel_camera_takephoto_controller").exists():  # ("照相按钮"): 点切换按钮
                            print('Switching to recoding Window')
                            d(resourceId="com.autel.explorer:id/iv_mode_switcher").click()  # ("照片录相切换按钮 ").click()
                        else:
                            pass

    def SwitchtoRecordMode(self):

            if  d(resourceId="com.autel.explorer:id/tv_autel_home_start").exists():  #在开始界面
                d(resourceId="com.autel.explorer:id/tv_autel_home_start").click()
                time.sleep(3)
                if d(resourceId="com.autel.explorer:id/iv_camera_record_controller").exists():

                    print('Is in the Record Window')
                else:
                    d(resourceId="com.autel.explorer:id/iv_mode_switcher").click()

            if d(resourceId="com.autel.explorer:id/iv_camera_record_controller").exists() \
                    or d(resourceId="com.autel.explorer:id/rel_camera_takephoto_controller").exists():    #在拍照或者录相界面
                if d(resourceId="com.autel.explorer:id/iv_camera_record_controller").exists():

                    print('Is in the record Window')
                else:
                    d(resourceId="com.autel.explorer:id/iv_mode_switcher").click()



            elif  d(text=u"Intelligent Flight").exists():            #在智能飞行界面
                    d(resourceId="com.autel.explorer:id/model_choice_bg").click() #点击相机按钮
                    self.recordStatusConfirm()

            elif  d(resourceId="com.autel.explorer:id/tv_setting_title").exists():     #在设置界面

                # d(resourceId="com.autel.explorer:id/iv_setting_close").click()                      #点击关闭
                    d(resourceId="com.autel.explorer:id/iv_setting_close").click()
                    self.recordStatusConfirm()


            elif  d(resourceId="com.autel.explorer:id/camera_general_setting_title").exists(): #在相机设置界面
                    d.click(0.5,0.5)                                 #画面中央点一下跳出

                    self.recordStatusConfirm()

            elif d(resourceId="com.autel.explorer:id/warn_history_title_tv").exists(): #在飞机状态画面
                    d.click(0.5,0.5)                                                       #画面中央点一下
                    self.recordStatusConfirm()
                # captureStatusConfirm()
            # elif driver.find_element_by_id("图片预览界面"):              #在图片预览画面
            #     pass

            # elif     driver.find_element_by_id("在用户中心"):            #在用户中心,登 录
            #         driver.back()
            # elif    driver.find_element_by_id("在注册中心"):
            #     pass
            else:
               logging.exception(SwitchError)
               print("Switching to Shotting widow failed")

    def scrollToAVFunc(self,func):
        self.SwitchtoRecordMode()

        time.sleep(3)      #如果不稳定,建议设成3秒以上


        listAll = ['PIV', 'STANDARD', 'FORMAT', 'RESOLUTION', 'FRAME RATE', 'EXPOSURE MODE', 'ISO', 'SHUTTER', 'EV', 'WB',
                  'COLOR', 'STYLE','DIGITAL ZOOM']
        seq=0
        if func in listAll:
            for i in range (0,len(listAll)):
                if func == listAll[i]:
                    seq=i
                    break
        else:
            print("You have input a wrong Record Function.")
            logging.exception(ParaError)

        if   d(resourceId="com.autel.explorer:id/tv_ui_first_para", text=func).exists():
            print("is in function %s"%func)

        else:
            try:
                i = 0
                while i <= len (listAll):  # 通过参数指定模式的参数编号 seq 与 当前滑块 最左边的 所见元素的编号比较, seq比较大,就左移,否则右移
                    flag=False
                    if  d(resourceId="com.autel.explorer:id/tv_ui_first_para", text=listAll[i]).exists():

                        if i > seq:
                            j = 0
                            while j <= 10:
                                d.swipe(0.33, 0.94, 0.65, 0.94)  # 往左边滑
                                time.sleep(0.5)
                                if  d(resourceId="com.autel.explorer:id/tv_ui_first_para", text=func).exists():
                                    # d(resourceId="com.autel.explorer:id/tv_ui_first_para", text=func).click()
                                    print('find %s' %func)
                                    flag=True
                                    break

                                else:
                                    pass


                                j += 1

                        else:
                            j = 0
                            while j <= 10:
                                d.swipe (0.68, 0.94, 0.32, 0.94)  # 往右边滑
                                time.sleep(0.5)
                                if  d(resourceId="com.autel.explorer:id/tv_ui_first_para", text=func).exists():
                                    print('find %s' %func)
                                    flag=True
                                    break

                                else:
                                    pass
                            j += 1

                    if flag:
                        break
                    i += 1

            except:
                logging.exception('------------Exceptions Caught--------')

    def setVideoPIV(self,num):
        self.scrollToAVFunc("PIV")

        if d(resourceId="com.autel.explorer:id/tv_ui_first_para", text=u"PIV", className="android.widget.TextView").up\
            (resourceId="com.autel.explorer:id/tv_first_para", text=num, className="android.widget.TextView"):
            print('Piv is set to %s'%num)

        else:

            try:
                d(resourceId="com.autel.explorer:id/tv_ui_first_para", text="PIV").click()
            except:
                logging.exception('------------Exceptions Caught--------')

            listPara = ["MANUAL","5s","10S","30S","60S"]
            if num in listPara:
                for i in range(0, len(listPara)):
                    if num == listPara[i]:
                        seq = i
                        break

            if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                time.sleep(0.5)
                try:
                    d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                except:
                    logging.exception('------------Exceptions Caught--------')

            else:
                try:
                    i = 0
                    while i <= len(listPara):  # 通过参数指定模式的参数编号 seq 与 当前滑块 最左边的 所见元素的编号比较, seq比较大,就左移,否则右移
                        flag = False
                        if d(resourceId="com.autel.explorer:id/tv_second_para", text=listPara[i]):
                            # driver.find_element_by_android_uiautomator('new UiSelector().text(listMode[i])'):

                            if i > seq:
                                j = 0
                                while j <= 10:
                                    d.swipe(0.32, 0.82, 0.68, 0.82)  # 往左边滑
                                    time.sleep(1)
                                    if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                                        # if d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).exists():
                                        try:
                                            d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                                        except:
                                            logging.exception('------------Exceptions Caught--------')
                                        finally:
                                            flag = True
                                    else:
                                        print("Para,not found,continue left swipe")
                                    if flag:
                                        break
                                    j += 1


                            else:
                                j = 0
                                while j <= 10:
                                    d.swipe(0.68, 0.82, 0.32, 0.82)  # 往右边滑
                                    time.sleep(1)
                                    if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                                        time.sleep(0.5)
                                        try:
                                            d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                                        except:
                                            logging.exception('------------Exceptions Caught--------')
                                        finally:
                                            flag = True
                                    else:
                                        print("Para,not found,continue right swipe")

                                    if flag:
                                        break
                                    j += 1

                        else:
                            pass

                        if flag:
                            break
                        i += 1
                except:
                    logging.exception('------------Exceptions Caught--------')

            time.sleep(1)

            d.click(0.5, 0.5)

    def setVedioStandard(self,STANDARD):
        self.scrollToAVFunc('STANDARD')
        time.sleep(0.5)

        if d(resourceId="com.autel.explorer:id/tv_first_para",text=STANDARD).exists():
            print("%s already setted"%STANDARD)

        else:
            d(resourceId="com.autel.explorer:id/tv_ui_first_para", text='STANDARD').click()
        # 检查输入参数
            try:
                if STANDARD == "NTSC":
                    d(resourceId="com.autel.explorer:id/tv_second_para",text='NTSC').click()

                elif STANDARD == "PAL":
                    d(resourceId="com.autel.explorer:id/tv_second_para", text="PAL").click()

                else:
                    pass
            except:
                logging.exception('------------Exceptions Caught--------')

            # 设置完成点击屏幕中央
            time.sleep(1)

            d.click(0.5, 0.5)

    def setVedioFormat(self,format):
        self.scrollToAVFunc('FORMAT')
        time.sleep(0.5)

        if d(resourceId="com.autel.explorer:id/tv_first_para",text=format).exists():
            print("%s already setted"%format)

        else:
            d(resourceId="com.autel.explorer:id/tv_ui_first_para", text='FORMAT').click()
        # 检查输入参数
            try:
                if format == "MOV":
                    d(resourceId="com.autel.explorer:id/tv_second_para",text='MOV').click()

                elif format == "MP4":
                    d(resourceId="com.autel.explorer:id/tv_second_para", text="MP4").click()

                else:
                    pass
            except:
                logging.exception('------------Exceptions Caught--------')

            # 设置完成点击屏幕中央
            time.sleep(1)

            d.click(0.5, 0.5)

    def setVideoReso(self,num):
        self.scrollToAVFunc("RESOLUTION")
        if d(resourceId="com.autel.explorer:id/tv_first_para",text=num).exists():
            print("%s already setted"%num)

        else:
            if num=="4K+":
                num="4K+(4096x2160)"
            elif num == "4K":
                num="4K(3840x2160)"
            elif num == "2.7K":
                num = "2.7K(2720x1530)"
            elif  num == "1080P":
                num == "1080P(1920x1080)"
            else:
                print(num)
                logging.exception(ParaError)

            try:
                d(resourceId="com.autel.explorer:id/tv_ui_first_para", text="RESOLUTION").click()
            except:
                logging.exception('------------Exceptions Caught--------')

            listPara = ["4K+(4096x2160)","4K(3840x2160)","2.7K(2720x1530)","1080P(1920x1080)"]
            if num in listPara:
                for i in range(0, len(listPara)):
                    if num == listPara[i]:
                        seq = i
                        break
            else:
                pass

            if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                time.sleep(0.5)
                try:
                    d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                except:
                    logging.exception('------------Exceptions Caught--------')

            else:
                try:
                    i = 0
                    while i <= len(listPara):  # 通过参数指定模式的参数编号 seq 与 当前滑块 最左边的 所见元素的编号比较, seq比较大,就左移,否则右移
                        flag = False
                        if d(resourceId="com.autel.explorer:id/tv_second_para", text=listPara[i]):
                            # driver.find_element_by_android_uiautomator('new UiSelector().text(listMode[i])'):

                            if i > seq:
                                j = 0
                                while j <= 10:
                                    d.swipe(0.32, 0.82, 0.68, 0.82)  # 往左边滑
                                    time.sleep(1)
                                    if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                                        # if d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).exists():
                                        try:
                                            d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                                        except:
                                            logging.exception('------------Exceptions Caught--------')
                                        finally:
                                            flag = True
                                    else:
                                        print("Para,not found,continue left swipe")
                                    if flag:
                                        break
                                    j += 1


                            else:
                                j = 0
                                while j <= 10:
                                    d.swipe(0.68, 0.82, 0.32, 0.82)  # 往右边滑
                                    time.sleep(1)
                                    if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                                        time.sleep(0.5)
                                        try:
                                            d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                                        except:
                                            logging.exception('------------Exceptions Caught--------')
                                        finally:
                                            flag = True
                                    else:
                                        print("Para,not found,continue right swipe")

                                    if flag:
                                        break
                                    j += 1

                        else:
                            pass

                        if flag:
                            break
                        i += 1
                except:
                    logging.exception('------------Exceptions Caught--------')

            time.sleep(1)

            d.click(0.5, 0.5)

    def setVideoFramerate(self,num):
        self.scrollToAVFunc("FRAME RATE")
        if d(resourceId="com.autel.explorer:id/tv_first_para",text=num).exists():
            print("%s already setted"%num)


        else:
            # if num=="4K+":
            #     num="4K+(4096x2160)"
            # elif num == "4K":
            #     num="4K(3840x2160)"
            # elif num == "2.7K":
            #     num = "2.7K(2720x1530)"
            # elif  num == "1080P":
            #     num == "1080P(1920x1080)"
            # else:
            #     print(num)
            #     logging.exception(ParaError)
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

            if num in listPara:
                for i in range(0, len(listPara)):
                    if num == listPara[i]:
                        seq = i
                        break
                        try:
                            d(resourceId="com.autel.explorer:id/tv_ui_first_para", text="FRAME RATE").click()
                        except:
                            logging.exception('------------Exceptions Caught--------')

                        if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                            time.sleep(0.5)
                            try:
                                d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                            except:
                                logging.exception('------------Exceptions Caught--------')

                        else:
                            try:
                                i = 0
                                while i <= len(listPara):  # 通过参数指定模式的参数编号 seq 与 当前滑块 最左边的 所见元素的编号比较, seq比较大,就左移,否则右移
                                    flag = False
                                    if d(resourceId="com.autel.explorer:id/tv_second_para", text=listPara[i]):
                                        # driver.find_element_by_android_uiautomator('new UiSelector().text(listMode[i])'):

                                        if i > seq:
                                            j = 0
                                            while j <= 10:
                                                d.swipe(0.32, 0.82, 0.68, 0.82)  # 往左边滑
                                                time.sleep(1)
                                                if d(resourceId="com.autel.explorer:id/tv_second_para",
                                                     text=num).exists():
                                                    # if d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).exists():
                                                    try:
                                                        d(resourceId="com.autel.explorer:id/tv_second_para",
                                                          text=num).click()
                                                    except:
                                                        logging.exception('------------Exceptions Caught--------')
                                                    finally:
                                                        flag = True
                                                else:
                                                    print("Para,not found,continue left swipe")
                                                if flag:
                                                    break
                                                j += 1


                                        else:
                                            j = 0
                                            while j <= 10:
                                                d.swipe(0.68, 0.82, 0.32, 0.82)  # 往右边滑
                                                time.sleep(1)
                                                if d(resourceId="com.autel.explorer:id/tv_second_para",
                                                     text=num).exists():
                                                    time.sleep(0.5)
                                                    try:
                                                        d(resourceId="com.autel.explorer:id/tv_second_para",
                                                          text=num).click()
                                                    except:
                                                        logging.exception('------------Exceptions Caught--------')
                                                    finally:
                                                        flag = True
                                                else:
                                                    print("Para,not found,continue right swipe")

                                                if flag:
                                                    break
                                                j += 1

                                    else:
                                        pass

                                    if flag:
                                        break
                                    i += 1
                            except:
                                logging.exception('------------Exceptions Caught--------')

                        time.sleep(1)

                        d.click(0.5, 0.5)

                        break



            else:
                logging.exception(ParaError)
                print("The Parameter You've input is not in listPara!")

            # if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
            #     time.sleep(0.5)
            #     try:
            #         d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
            #     except:
            #         logging.exception('------------Exceptions Caught--------')
            #
            # else:
            #     try:
            #         i = 0
            #         while i <= len(listPara):  # 通过参数指定模式的参数编号 seq 与 当前滑块 最左边的 所见元素的编号比较, seq比较大,就左移,否则右移
            #             flag = False
            #             if d(resourceId="com.autel.explorer:id/tv_second_para", text=listPara[i]):
            #                 # driver.find_element_by_android_uiautomator('new UiSelector().text(listMode[i])'):
            #
            #                 if i > seq:
            #                     j = 0
            #                     while j <= 10:
            #                         d.swipe(0.32, 0.82, 0.68, 0.82)  # 往左边滑
            #                         time.sleep(1)
            #                         if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
            #                             # if d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).exists():
            #                             try:
            #                                 d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
            #                             except:
            #                                 logging.exception('------------Exceptions Caught--------')
            #                             finally:
            #                                 flag = True
            #                         else:
            #                             print("Para,not found,continue left swipe")
            #                         if flag:
            #                             break
            #                         j += 1
            #
            #
            #                 else:
            #                     j = 0
            #                     while j <= 10:
            #                         d.swipe(0.68, 0.82, 0.32, 0.82)  # 往右边滑
            #                         time.sleep(1)
            #                         if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
            #                             time.sleep(0.5)
            #                             try:
            #                                 d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
            #                             except:
            #                                 logging.exception('------------Exceptions Caught--------')
            #                             finally:
            #                                 flag = True
            #                         else:
            #                             print("Para,not found,continue right swipe")
            #
            #                         if flag:
            #                             break
            #                         j += 1
            #
            #             else:
            #                 pass
            #
            #             if flag:
            #                 break
            #             i += 1
            #     except:
            #         logging.exception('------------Exceptions Caught--------')

            # time.sleep(1)
            #
            # d.click(0.5, 0.5)

    def setVedioExpo(self,exp):
        self.scrollToAVFunc("EXPOSURE MODE")
        time.sleep(0.5)

        # if d(resourceId="com.autel.explorer:id/tv_first_para",text=exp).exists():
        #     print("%s already set"%exp)

        if d(resourceId="com.autel.explorer:id/tv_ui_first_para", text='EXPOSURE MODE', className="android.widget.TextView").up \
                    (resourceId="com.autel.explorer:id/tv_first_para", text=exp,
                     className="android.widget.TextView"):
            print("%s already set" % exp)

        else:
            try:
                d(resourceId="com.autel.explorer:id/tv_ui_first_para", text="EXPOSURE MODE").click()
            except:
                logging.exception('------------Exceptions Caught--------')

            if exp == "AUTO":
                try:
                    d(resourceId="com.autel.explorer:id/tv_second_para").click()
                except:
                    logging.exception('------------Exceptions Caught--------')
            elif exp == "MANUAL":
                try:
                    d(resourceId="com.autel.explorer:id/tv_second_para", text=u"MANUAL").click()
                except:
                    logging.exception('------------Exceptions Caught--------')
            else:
                print("曝光模式输入有误!")
                logging.exception(ParaError)
            time.sleep(1)

            d.click(0.5, 0.5)

    def setVedioIso(self,num):
        self.setVedioExpo("MANUAL")
        self.scrollToAVFunc("ISO")

        if d(resourceId="com.autel.explorer:id/tv_first_para",text=num).exists():
            print("is %s setted"%num)

        else:
            try:
                d(resourceId="com.autel.explorer:id/tv_ui_first_para", text="ISO").click()
            except:
                logging.exception('------------Exceptions Caught--------')

            if num == "100":
                seq = 0
            elif num == "200":
                seq = 1
            elif num == "400":
                seq = 2
            elif num == "800":
                seq = 3
            elif num == "1600":
                seq = 4
            elif num == "3200":
                seq = 5
            else:
                print("输入的参数有误")
                logging.exception(ParaError)

            listPara = ["100","200", "400", "800", "1600", "3200"]
            if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                time.sleep(0.5)
                try:
                    d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                except:
                    logging.exception('------------Exceptions Caught--------')

            else:
                try:
                    i = 0
                    while i <= len(listPara):  # 通过参数指定模式的参数编号 seq 与 当前滑块 最左边的 所见元素的编号比较, seq比较大,就左移,否则右移
                        flag = False
                        if d(resourceId="com.autel.explorer:id/tv_second_para", text=listPara[i]):
                            # driver.find_element_by_android_uiautomator('new UiSelector().text(listMode[i])'):

                            if i > seq:
                                j = 0
                                while j <= 10:
                                    d.swipe(0.32, 0.82, 0.68, 0.82)  # 往左边滑
                                    time.sleep(1)
                                    if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                                        # if d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).exists():
                                        try:
                                            d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                                        except:
                                            logging.exception('------------Exceptions Caught--------')
                                        finally:
                                            flag = True
                                    else:
                                        print("Para,not found,continue left swipe")
                                    if flag:
                                        break
                                    j += 1


                            else:
                                j = 0
                                while j <= 10:
                                    d.swipe(0.68, 0.82, 0.32, 0.82)  # 往右边滑
                                    time.sleep(1)
                                    if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                                        time.sleep(0.5)
                                        try:
                                            d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                                        except:
                                            logging.exception('------------Exceptions Caught--------')
                                        finally:
                                            flag = True
                                    else:
                                        print("Para,not found,continue right swipe")

                                    if flag:
                                        break
                                    j += 1

                        else:
                            pass

                        if flag:
                            break
                        i += 1
                except:
                    logging.exception('------------Exceptions Caught--------')

            time.sleep(1)

            d.click(0.5, 0.5)

    def setVedioShutter(self,num):
        self.setVedioExpo("MANUAL")
        self.scrollToAVFunc("SHUTTER")

        listPara = ["1/8000", "1/6000", "1/5000", "1/4000", "1/3200", "1/2500", "1/2000", "1/1600", "1/1250", "1/1000",
                       "1/800", "1/640", "1/500",
                       "1/400", "1/320", "1/240", "1/200", "1/160", "1/120", "1/100", "1/80", "1/60"]
        if num not in listPara:
            print("You have inputed a wrong parameter")
            logging.exception(ParaError)

        else:
            if d(resourceId="com.autel.explorer:id/tv_first_para",text=num).exists():
                print("%s setted"%num)

            else:
                try:
                    d(resourceId="com.autel.explorer:id/tv_ui_first_para", text="SHUTTER").click()
                except:
                    logging.exception('------------Exceptions Caught--------')
                ##########################
                seq=0
                for i in range(0, len(listPara)):
                    if num == listPara[i]:
                        seq = i
                        break

                if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                    time.sleep(0.5)
                    try:
                        d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                    except:
                        logging.exception('------------Exceptions Caught--------')

                else:
                    i = 0
                    while i <= len(listPara):  # 通过参数指定模式的参数编号 seq 与 当前滑块 最左边的 所见元素的编号比较, seq比较大,就左移,否则右移

                        flag = False
                        if d(resourceId="com.autel.explorer:id/tv_second_para", text=listPara[i]):
                            # driver.find_element_by_android_uiautomator('new UiSelector().text(listMode[i])'):

                            if i > seq:
                                j = 0
                                while j <= 20:
                                    d.swipe(0.32, 0.82, 0.68, 0.82)  # 往左边滑
                                    time.sleep(0.8)
                                    if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                                        # if d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).exists():
                                        try:
                                            d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                                        except:
                                            logging.exception('------------Exceptions Caught--------')
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
                                    d.swipe(0.68, 0.82, 0.32, 0.82)  # 往右边滑
                                    time.sleep(0.8)

                                    if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                                        time.sleep(0.5)
                                        try:
                                            d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                                        except:
                                            logging.exception('------------Exceptions Caught--------')
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

                d.click(0.5, 0.5)

    def setVedioEv(self,num):
        self.setVedioExpo("AUTO")
        self.scrollToAVFunc("EV")


        listPara = ["-3.0", "-2.7", "-2.3", "-2.0", "-1.7", "-1.3", "-1.0", "-0.7", "-0.3", "0","+0.3","+0.7","+1.0","+1.3","+1.7","+2.0","+2.3","+2.7","+3.0"]

        if num not in listPara:
            print("You have inputed a wrong parameter")
            logging.exception(ParaError)

        else:
            if d(resourceId="com.autel.explorer:id/tv_first_para",text=num).exists():
                print("%s setted"%num)

            else:
                try:
                    d(resourceId="com.autel.explorer:id/tv_ui_first_para", text="EV").click()
                except:
                    logging.exception('------------Exceptions Caught--------')
                ##########################

                for i in range(0, len(listPara)):
                    if num == listPara[i]:
                        seq = i
                        break
                if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                    time.sleep(0.5)
                    try:
                        d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                    except:
                        logging.exception('------------Exceptions Caught--------')

                else:
                    i = 0
                    while i <= len(listPara):  # 通过参数指定模式的参数编号 seq 与 当前滑块 最左边的 所见元素的编号比较, seq比较大,就左移,否则右移
                        flag = False
                        if d(resourceId="com.autel.explorer:id/tv_second_para", text=listPara[i]):
                            # driver.find_element_by_android_uiautomator('new UiSelector().text(listMode[i])'):

                            if i > seq:
                                j = 0
                                while j <= 20:
                                    d.swipe(0.32, 0.82, 0.68, 0.82)  # 往左边滑
                                    time.sleep(0.8)
                                    if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                                        # if d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).exists():
                                        try:
                                            d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                                        except:
                                            logging.exception('------------Exceptions Caught--------')
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
                                    d.swipe(0.68, 0.82, 0.32, 0.82)  # 往右边滑
                                    time.sleep(0.8)

                                    if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                                        time.sleep(0.5)
                                        try:
                                            d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                                        except:
                                            logging.exception('------------Exceptions Caught--------')
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

                d.click(0.5, 0.5)

    def setVedioWB(self,num):
        self.scrollToAVFunc("WB")

        if d(resourceId="com.autel.explorer:id/tv_first_para", text=num).exists():
            print("%s already set" %num)


        else:
            try:
                d(resourceId="com.autel.explorer:id/tv_ui_first_para", text=u"WB").click()
            except:
                logging.exception('------------Exceptions Caught--------')

            listPara = ["AUTO", "SUNNY", "CLOUDY", "INCAN", "NEON", "%sK"]



            if num not in ["AUTO", "SUNNY", "CLOUDY", "INCAN", "NEON"]:  # == x000K的情况:
                # (...) 存在的情况
                if d(resourceId="com.autel.explorer:id/iv_second_next").exists():
                    if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():# xxxxK 和 (...)均存在的情况
                        pass   #己经存在该选择项
                     #(...)存在, xxxxK不存在的情况,点(...)进入下一层循环
                    elif not  d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                        try:
                            d(resourceId="com.autel.explorer:id/iv_second_next").click()
                        except:
                            logging.exception('------------Exceptions Caught--------')
                        time.sleep(0.5)

                        self.insideCircleWB(num)

                        # time.sleep(1)

                        d.click(0.5, 0.5)

                # (...)不存在的情况
                else:
                    i=0
                    while i<=2:
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
                                except:
                                    logging.exception('------------Exceptions Caught--------')
                                time.sleep(0.5)
                                self.insideCircleWB(num)
                                break

                        i+=1

                    # while True:

            #   num not in ["AUTO", "SUNNY", "CLOUDY", "INCAN", "NEON"]:  # == x000K的情况:
            else:

                for i in range(0, len(listPara)-1):
                    if num == listPara[i]:
                        seq = i
                        break

                if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                    time.sleep(0.5)
                    try:
                        d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                    except:
                        logging.exception('------------Exceptions Caught--------')

                else:
                    i = 0
                    while i <= len(listPara):  # 通过参数指定模式的参数编号 seq 与 当前滑块 最左边的 所见元素的编号比较, seq比较大,就左移,否则右移
                        flag = False
                        if d(resourceId="com.autel.explorer:id/tv_second_para", text=listPara[i]):
                            # driver.find_element_by_android_uiautomator('new UiSelector().text(listMode[i])'):

                            if i > seq:
                                j = 0
                                while j <= 20:
                                    d.swipe(0.32, 0.82, 0.68, 0.82)  # 往左边滑
                                    time.sleep(0.5)
                                    if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                                        # if d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).exists():
                                        try:
                                            d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                                        except:
                                            logging.exception('------------Exceptions Caught--------')
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
                                    time.sleep(0.5)

                                    if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                                        time.sleep(0.5)
                                        try:
                                            d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                                        except:
                                            logging.exception('------------Exceptions Caught--------')
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
                d.click(0.5, 0.5)

    def setVedioColor(self,num):
        self.scrollToAVFunc("COLOR")

        listPara = ["NONE", "LOG", "VIVID", "B&W", "ART", "FILM","BEACH","DREAM","CLASSIC","NOSTALGIC"]

        if num not in listPara:
            print("You have inputed a wrong parameter")
            logging.exception(ParaError)

        else:

            if d(resourceId="com.autel.explorer:id/tv_first_para",text=num).exists():
                print("%s setted"%num)


            else:
                try:
                    d(resourceId="com.autel.explorer:id/tv_ui_first_para", text="COLOR").click()
                except:
                    logging.exception('------------Exceptions Caught--------')
                for i in range(0, len(listPara)):
                    if num == listPara[i]:
                        seq = i
                        break

                if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                    time.sleep(0.5)
                    try:
                        d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                    except:
                        logging.exception('------------Exceptions Caught--------')



                else:
                    i = 0
                    while i <= len(listPara):  # 通过参数指定模式的参数编号 seq 与 当前滑块 最左边的 所见元素的编号比较, seq比较大,就左移,否则右移
                        flag = False
                        if d(resourceId="com.autel.explorer:id/tv_second_para", text=listPara[i]):
                            # driver.find_element_by_android_uiautomator('new UiSelector().text(listMode[i])'):

                            if i > seq:
                                j = 0
                                while j <= 20:
                                    d.swipe(0.32, 0.82, 0.68, 0.82)  # 往左边滑
                                    time.sleep(0.8)
                                    if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                                        # if d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).exists():
                                        try:
                                            d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                                        except:
                                            logging.exception('------------Exceptions Caught--------')
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
                                    d.swipe(0.68, 0.82, 0.32, 0.82)  # 往右边滑
                                    time.sleep(0.8)

                                    if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                                        time.sleep(0.5)
                                        try:
                                            d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                                        except:
                                            logging.exception('------------Exceptions Caught--------')
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

                d.click(0.5, 0.5)

    def setVedioStyle(self,num):
        self.scrollToAVFunc("STYLE")
        listPara = ["STD.", "NEUT.", "LAND.",'%s']

        # == 自定义的情况:
        if num not in ["STD.", "NEUT.", "LAND."]:

            # (...) 存在的情况

            if d(resourceId="com.autel.explorer:id/tv_first_para", text=num).exists():
                print("Style %s is Setted"%num)

            else:

                try:
                    d(resourceId="com.autel.explorer:id/tv_ui_first_para", text=u"STYLE").click()
                except:
                    logging.exception('------------Exceptions Caught--------')
                if d(resourceId="com.autel.explorer:id/iv_second_next").exists():
                    if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():# "指定参数" 和 (...)均存在的情况
                        pass   #己经存在该选择项

                     #(...)存在, "xx xx xx"不存在的情况,点(...)进入下一层循环
                    elif not  d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                        try:
                            d(resourceId="com.autel.explorer:id/iv_second_next").click()
                        except:
                            logging.exception('------------Exceptions Caught--------')
                        time.sleep(0.5)
                        self.insideCircleStyle(num)

                else:
                    j=0
                    while j<=3:
                        d.swipe(0.68, 0.82, 0.32, 0.82)  # 滑向滚动条右侧
                        if d(resourceId="com.autel.explorer:id/iv_second_next").exists():
                            if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():  # "指定参数" 和 (...)均存在的情况
                                d.click(0.5,0.5)
                                break  # 己经存在该选择项

                            # (...)存在, xxxxK不存在的情况,点(...)进入下一层循环
                            elif not d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                                try:
                                    d(resourceId="com.autel.explorer:id/iv_second_next").click()
                                except:
                                    logging.exception('------------Exceptions Caught--------')
                                time.sleep(0.5)

                                self.insideCircleStyle(num)
                                break

        # 是预设前三项情况
        else:

            d(resourceId="com.autel.explorer:id/tv_ui_first_para", text=u"STYLE").click()

            for i in range(0, len(listPara)-1):
                if num == listPara[i]:
                    seq = i
                    break

            if d(resourceId="com.autel.explorer:id/tv_ui_second_para", text=num).exists():
                time.sleep(0.5)
                try:
                    d(resourceId="com.autel.explorer:id/tv_ui_second_para", text=num).click()
                except:
                    logging.exception('------------Exceptions Caught--------')

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
                                    except:
                                        logging.exception('------------Exceptions Caught--------')
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
                                    time.sleep(0.5)
                                    try:
                                        d(resourceId="com.autel.explorer:id/tv_ui_second_para", text=num).click()
                                    except:
                                        logging.exception('------------Exceptions Caught--------')
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
            d.click(0.5, 0.5)

    def setVedioDigizoom(self,num):

            self.scrollToAVFunc("DIGITAL ZOOM")
            listPara = ["1.0X", "2.0X", "3.0X", "4.0X","5.0X","6.0X","7.0X","8.0X"]

            if num not in listPara:
                print("You have inputed a wrong parameter")


            else:

                if d(resourceId="com.autel.explorer:id/tv_first_para", text=num).exists():
                    print("%s setted" % num)

                else:
                    try:
                        d(resourceId="com.autel.explorer:id/tv_ui_first_para", text="DIGITAL ZOOM").click()
                    except:
                        logging.exception('------------Exceptions Caught--------')

                    for i in range(0, len(listPara)):
                        if num == listPara[i]:
                            seq = i
                            break

                    if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                        time.sleep(0.5)
                        try:
                            d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                        except:
                            logging.exception('------------Exceptions Caught--------')

                    else:
                        i = 0
                        while i <= len(listPara):  # 通过参数指定模式的参数编号 seq 与 当前滑块 最左边的 所见元素的编号比较, seq比较大,就左移,否则右移
                            flag = False
                            if d(resourceId="com.autel.explorer:id/tv_second_para", text=listPara[i]):
                                # driver.find_element_by_android_uiautomator('new UiSelector().text(listMode[i])'):

                                if i > seq:
                                    j = 0
                                    while j <= 20:
                                        d.swipe(0.32, 0.82, 0.68, 0.82)  # 往左边滑
                                        time.sleep(0.8)
                                        if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                                            # if d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).exists():
                                            try:
                                                d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                                            except:
                                                logging.exception('------------Exceptions Caught--------')
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
                                        d.swipe(0.68, 0.82, 0.32, 0.82)  # 往右边滑
                                        time.sleep(0.8)

                                        if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                                            time.sleep(0.5)
                                            try:
                                                d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                                            except:
                                                logging.exception('------------Exceptions Caught--------')
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

                    d.click(0.5, 0.5)

##---------------------------- Camera Settings ------------------------------------##
    def camSetGrid(self,num):
        d(resourceId="com.autel.explorer:id/iv_camera_setting").click()
        d(resourceId="com.autel.explorer:id/item_general_setting_key_tv").click()
        if num == 'None':
            d(resourceId="com.autel.explorer:id/general_setting_image_item_value_text").click()
        elif num == 'Grid':
            d(resourceId="com.autel.explorer:id/general_setting_image_item_value_text", text=u"Grid").click()
        elif num == 'Grid + Line':
            d(resourceId="com.autel.explorer:id/general_setting_image_item_value_text", text=u"Grid + Line").click()
        else:
            pass

        d.click(0.3, 0.5)

    def camSetCenterPoint(self,num):
        d(resourceId="com.autel.explorer:id/iv_camera_setting").click()
        d(resourceId="com.autel.explorer:id/item_general_setting_key_tv", text=u"Center Point").click()
        if num == 'None':
            d(resourceId="com.autel.explorer:id/general_setting_image_item_value_text").click()
        elif num == 'SquareWithout':
            d(resourceId="com.autel.explorer:id/general_setting_image_item_value_text",
              text=u"Square(Without Center Point)").click()
        elif num == 'SquareWith':
            d(resourceId="com.autel.explorer:id/general_setting_image_item_value_text",
              text=u"Square(With Center Point)").click()
        elif num == 'Cross':
            d(resourceId="com.autel.explorer:id/general_setting_image_item_value_text", text=u"Cross").click()
        elif num == 'CircleWith':
            d(resourceId="com.autel.explorer:id/general_setting_image_item_value_text",
              text=u"Circle(With Center Point)").click()
        elif  num == 'CircleWithout':
            d(resourceId="com.autel.explorer:id/general_setting_image_item_value_text",
              text=u"Circle(Without Center Point)").click()
        else:
            pass
        d.click(0.3,0.5)

    #直方图 参数为 'on' , 'off'
    def camSetHis(self,num):
        d(resourceId="com.autel.explorer:id/iv_camera_setting").click()
        time.sleep(2)
        d.screenshot('screen.jpg')
        im = Image.open("screen.jpg")
        r,g,b =im.split()
        color =b.getpixel((1766, 591))


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
            d(resourceId="com.autel.explorer:id/item_general_setting_autel_ss").click()
            time.sleep(0.5)
            d.click(0.3, 0.5)
        else:
            pass

    # 过曝警告 参数为 'on' , 'off'
    def camSetOverExp(self,num):
        d(resourceId="com.autel.explorer:id/iv_camera_setting").click()
        time.sleep(2)
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
            d(resourceId="com.autel.explorer:id/item_general_setting_autel_ss", className="android.view.View",
              instance=1).click()
            time.sleep(0.5)
            d.click(0.3, 0.5)
        else:
            pass

    # subtitle.ass file 参数为 'on' , 'off' 录相模式下使用.
    def camSetSubtitle(self, num):
        d(resourceId="com.autel.explorer:id/iv_camera_setting").click()
        time.sleep(2)
        d.screenshot('screen.jpg')
        im = Image.open("screen.jpg")
        print('mode:',im.mode)
        print('size:',im.size)
        r, g, b = im.split()
        color = b.getpixel((1766, 947))

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
            time.sleep(0.5)
            d.click(0.3, 0.5)
        elif num != status:
            d(resourceId="com.autel.explorer:id/item_general_setting_autel_ss", className="android.view.View",
              instance=2).click()
            time.sleep(0.5)
            d.click(0.3, 0.5)
        else:
            pass
        # im = Image.new("RGB", (128, 128), "#FF0000")
        # im.save("test1.png")  # 图像im为128x128大小的红色图像。
        # im = Image.new("RGB", (128, 128))  # 图像im为128x128大小的黑色图像，因为变量color不赋值的话，图像内容被设置为0，即黑色。
        # im.save("test2.png")
        # im = Image.new("RGB", (128, 128), "red")  # 图像im为128x128大小的红色图像。
        # im.save("test3.png")
        im2 = Image.new('RGB',(200,200),"blue")
        im2.save('blue.png')



def main():
    '''
    time_stamp = datetime.datetime.now()
    mytime=time_stamp.strftime('%Y.%m.%d-%H:%M:%S')
    print(mytime)
    d.screenshot("test_temp/screen.jpg")
    # time.sleep(2)
    im = Image.open("test_temp/screen.jpg")
    r, g, b = im.split()
    color = b.getpixel((1760,580))
    print(color)
    time_stamp = datetime.datetime.now()
    mytime = time_stamp.strftime('%Y.%m.%d-%H:%M:%S')
    print(mytime)
    '''
    d.screen_on()
    time.sleep(2)

    # d.unlock()
    d.swipe(0.5,0.9,0.5,0.051)
    test = Camera()
    time.sleep(0.5)
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
    # test.SetPictureMode("BURST",'7')


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

    # test.shot()
    # time.sleep(5)

    ##2-9 大小设为 4000x3000, 各种组合拍照
    # test.SetPictureSize("4000x3000")
    # test.SetPictureFomat("RAW")
    # test.SetPictureMode('AEB',"3")
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
    #
    # test.setVedioExpo("AUTO")
    # test.setVedioIso('1600')
    # test.setVedioShutter('1/80')
    # test.setVedioEv('+1.3')
    # # test.setVedioWB('2000K')
    # test.setVedioWB('4000K')
    # test.setVedioColor("ART")
    # test.setVedioStyle('STD.')
    # test.setVedioDigizoom('2.0X')
    #
    # test.scrollToFunc('SIZE')
    # test.scrollToFunc('DIGITAL ZOOM')
    # test.scrollToFunc('FORMAT')
    # test.scrollToFunc('STYLE')
    # test.scrollToFunc('MODE')
    # test.scrollToFunc('COLOR')
    # test.scrollToFunc('EXPOSURE MODE')
    # test.scrollToFunc('WB')
    # test.scrollToFunc('ISO')
    #
    # test.camSetGrid('Grid + Line')
    # test.camSetGrid('None')
    # test.camSetCenterPoint('Cross')
    # test.camSetHis('off')
    # test.camSetOverExp('off')
    test.camSetSubtitle('off')




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