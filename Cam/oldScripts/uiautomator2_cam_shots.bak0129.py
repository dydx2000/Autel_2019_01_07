#conding：utf-8
import re
import random
import uiautomator2 as u2
import time
pkg_name='com.autel.explorer'
# pkg_name='com.taobao.taobao'
# d=u2.connect_wifi('192.168.1.12')  # LG
# d=u2.connect_wifi('192.168.1.17')
# d=u2.connect_usb('7cc8c0d9')  # One Plus 3
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


class Camera:
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

    #在主界面判断是否外在拍照状态
    def captureStatusConfirm(self):
        time.sleep(0.5)


        if d(resourceId="com.autel.explorer:id/rel_camera_takephoto_controller").exists(): #如果有拍照按钮,则确认是照相模式啥都不做了
            pass

        elif d(resourceId="com.autel.explorer:id/iv_camera_record_controller").exists(): #("录相按钮"): 点切换按钮
             d(resourceId="com.autel.explorer:id/iv_mode_switcher").click() # ("照片录相切换按钮 ").click()



        elif d(resourceId="com.autel.explorer:id/compass_iv").exists():    # ("指南针按钮 "): 说明在地图模式,点击小图切换到相机
            print('Now is in the map window.')
            d.click(0.14, 0.268)
            time.sleep(2)

            if  d(resourceId="com.autel.explorer:id/rel_camera_takephoto_controller").exists():  #切换成功的情况
                    if d(resourceId="com.autel.explorer:id/rel_camera_takephoto_controller").exists():  # 如果有拍照按钮,则确认是照相模式
                        print('Is in the Shotting Window')

                    elif d(resourceId="com.autel.explorer:id/iv_camera_record_controller").exists():  # ("录相按钮"): 点切换按钮
                        print('Switching to Shotting Window')
                        d(resourceId="com.autel.explorer:id/iv_mode_switcher").click()  # ("照片录相切换按钮 ").click()

            else:                                                                                  #切换不成功的情况
                d(resourceId="com.autel.explorer:id/intercept_img_shrink").click()  #把小图展开,再点小图中央切换到拍摄画面,
                time.sleep(1)
                d.click(0.14, 0.268)
                time.sleep(1)
                if d(resourceId="com.autel.explorer:id/rel_camera_takephoto_controller").exists():  # 如果有拍照按钮,则确认是照相模式
                    pass

                elif d(resourceId="com.autel.explorer:id/iv_camera_record_controller").exists():  # ("录相按钮"): 点切换按钮
                    d(resourceId="com.autel.explorer:id/iv_mode_switcher").click()  # ("照片录相切换按钮 ").click()

    #切换到拍摄画面
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
                if func == listAll[0]:
                    seq=i
        else:
            print("You have iput a wrong Shotting Function.")

        if   d(resourceId="com.autel.explorer:id/tv_ui_first_para", text=func).exists():
            print("is in function %s"%func)

        else:
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
                    d(resourceId="com.autel.explorer:id/tv_second_para", text=u"4000x3000(4:3)").click()

            else:
                    d(resourceId="com.autel.explorer:id/tv_second_para").click()



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
            if format == "JPG":
                d(resourceId="com.autel.explorer:id/tv_second_para").click()

            elif format == "RAW":
                d(resourceId="com.autel.explorer:id/tv_second_para", text="RAW").click()

            else:
                d(resourceId="com.autel.explorer:id/tv_second_para", text="RAW+JPG").click()

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

            time.sleep(1)



    def insideCircleBurst(self,num):

        listPara = ["3", "5", "7", "10", "14"]
        # self.insideListCircleCommon(num)

        if num in listPara:

            for i in range(0, len(listPara)):
                if num == listPara[i]:
                    seq = i

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

            time.sleep(1)



        else:
            print("输入 contrast 的参数有错误!")
            time.sleep(1)

            d.click(0.5, 0.5)

    def insideCircleTimelapse(self,num):

        listPara = ["2s", "5s", "7s", "10s", "20s","30s","60s"  ]

        if num in listPara:

            for i in range(0, len(listPara)):
                if num == listPara[i]:
                    seq = i

            if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                time.sleep(0.5)
                d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                print("TIMELAPSE %s selected" % num)
                time.sleep(1)
                d.click(0.5, 0.5)

            else:

                for i in range(0, len(listPara)):
                    if num == listPara[i]:
                        seq = i
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

            time.sleep(1)

        else:
            print("输入 contrast 的参数有错误!")
            time.sleep(1)
            d.click(0.5, 0.5)

    def insideCircleAeb(self, num):

        listPara = ["3", "5"]

        if num in listPara:

            for i in range(0, len(listPara)):
                if num == listPara[i]:
                    seq = i

            if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                time.sleep(0.5)
                d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
                print("AEB %s selected" % num)
                time.sleep(0.5)
                d.click(0.5, 0.5)

            else:

                for i in range(0, len(listPara)):
                    if num == listPara[i]:
                        seq = i
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

            time.sleep(1)

        else:
            print("输入 contrast 的参数有错误!")
            time.sleep(1)
            d.click(0.5, 0.5)

    #相机 mode　子项选择
    def SetPictureMode_pre(self,mode,num=None):

        self.scrollToFunc('MODE')
        d(resourceId="com.autel.explorer:id/tv_ui_first_para", text='MODE').click()

        time.sleep(1)
        if  d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).exists:         #没有的话就往左或者往右翻找找吧
            if mode == "SINGLE":
                d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).click()
                print("SINGEL selected")
                time.sleep(1)
                d.click(0.5, 0.5)

            else:
                d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).click()
                time.sleep(0.5)



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


        else:
                if mode=='SINGLE':      #给每个选项编号
                    seq=0
                elif mode=='BURST':
                    seq=1
                elif mode=='TIMELAPSE':
                    seq=2
                elif mode=='AEB':
                    seq=3
                else:       #'AEB'
                    print("MODE 参数有误")

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
                                        d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).click()
                                        print("SINGEL selected")
                                        flag=True
                                        time.sleep(1)
                                        d.click(0.5, 0.5)
                                # if d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).exists():
                                    else:
                                        d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).click()
                                        if d(resourceId="com.autel.explorer:id/iv_second_next").exists():
                                            d(resourceId="com.autel.explorer:id/iv_second_next").click()
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
                                        d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).click()
                                        print("SINGEL selected")
                                        flag=True
                                        time.sleep(1)
                                        d.click(0.5, 0.5)

                                    else:

                                        d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).click()
                                        if d(resourceId="com.autel.explorer:id/iv_second_next").exists():
                                            d(resourceId="com.autel.explorer:id/iv_second_next").click()
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
            d(resourceId="com.autel.explorer:id/tv_ui_first_para", text="EXPOSURE MODE").click()

            if exp == "AUTO":
                d(resourceId="com.autel.explorer:id/tv_second_para").click()
            elif exp == "MANUAL":
                d(resourceId="com.autel.explorer:id/tv_second_para", text=u"MANUAL").click()
            else:
                print("曝光模式输入有误!")
            time.sleep(1)

            d.click(0.5, 0.5)


    def SetPictureIso(self,num):
        self.SetPictureExpo("MANUAL")
        self.scrollToFunc("ISO")

        if d(resourceId="com.autel.explorer:id/tv_first_para",text=num).exists():
            print("is %s setted"%num)

        else:
            d(resourceId="com.autel.explorer:id/tv_ui_first_para", text="ISO").click()

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

            listPara = ["100","200", "400", "800", "1600", "3200"]
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
                            while j <= 10:
                                d.swipe(0.32, 0.82, 0.68, 0.82)  # 往左边滑
                                time.sleep(1)
                                if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                                    # if d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).exists():
                                    d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
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
                                    d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
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
                d(resourceId="com.autel.explorer:id/tv_ui_first_para", text="SHUTTER").click()
            ##########################
                seq=0
                for i in range(0, len(listPara)):
                    if num == listPara[i]:
                        seq = i

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
                                while j <= 20:
                                    d.swipe(0.32, 0.82, 0.68, 0.82)  # 往左边滑
                                    time.sleep(0.8)
                                    if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                                        # if d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).exists():
                                        d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
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
                                        d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
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
                d(resourceId="com.autel.explorer:id/tv_ui_first_para", text="EV").click()
            ##########################

                for i in range(0, len(listPara)):
                    if num == listPara[i]:
                        seq = i
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
                                while j <= 20:
                                    d.swipe(0.32, 0.82, 0.68, 0.82)  # 往左边滑
                                    time.sleep(0.8)
                                    if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                                        # if d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).exists():
                                        d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
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
                                        d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
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
                                    d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
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
        else:
            print("输入 xxxxK 的参数有错误!")
            time.sleep(1)

            d.click(0.5, 0.5)

    def SetPictureWB(self,num):
        self.scrollToFunc("WB")

        if d(resourceId="com.autel.explorer:id/tv_first_para", text=num).exists():
            print("%s setted" % num)


        else:
            d(resourceId="com.autel.explorer:id/tv_ui_first_para", text=u"WB").click()


            listPara = ["AUTO", "SUNNY", "CLOUDY", "INCAN", "NEON", "%sK"]



            if num not in ["AUTO", "SUNNY", "CLOUDY", "INCAN", "NEON"]:  # == x000K的情况:
                # (...) 存在的情况
                if d(resourceId="com.autel.explorer:id/iv_second_next").exists():
                    if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():# xxxxK 和 (...)均存在的情况
                        pass   #己经存在该选择项
                     #(...)存在, xxxxK不存在的情况,点(...)进入下一层循环
                    elif not  d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                        d(resourceId="com.autel.explorer:id/iv_second_next").click()
                        time.sleep(0.5)

                        self.insideCircleWB(num)


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
                                d(resourceId="com.autel.explorer:id/iv_second_next").click()
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
                                while j <= 20:
                                    d.swipe(0.32, 0.82, 0.68, 0.82)  # 往左边滑
                                    time.sleep(0.8)
                                    if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                                        # if d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).exists():
                                        d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
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
                                        d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
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
                d(resourceId="com.autel.explorer:id/tv_ui_first_para", text="COLOR").click()
                for i in range(0, len(listPara)):
                    if num == listPara[i]:
                        seq = i

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
                                while j <= 20:
                                    d.swipe(0.32, 0.82, 0.68, 0.82)  # 往左边滑
                                    time.sleep(0.8)
                                    if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                                        # if d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).exists():
                                        d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
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
                                        d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
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

            if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                time.sleep(0.5)
                d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()

            else:

                for i in range(0, len(listPara)):
                    if num == listPara[i]:
                        seq = i
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
                                    d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
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
                                    d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
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
        d(resourceId="com.autel.explorer:id/iv_second_next").click()
        self.insideCircleContrast(num)
        d(resourceId="com.autel.explorer:id/tv_back").click()

        d(resourceId="com.autel.explorer:id/tv_ui_second_para").click()
        d(resourceId="com.autel.explorer:id/iv_second_next").click()
        self.insideCircleSharp(num)
        d(resourceId="com.autel.explorer:id/tv_back").click()

        d(resourceId="com.autel.explorer:id/tv_ui_second_para", text=u"SATURATION").click()
        d(resourceId="com.autel.explorer:id/iv_second_next").click()
        self.insideCircleSaturation(num)
        d(resourceId="com.autel.explorer:id/tv_back").click()

        d.click(0.5,0.5)


    def SetPitureStyle(self,num):
        # self.scrollToFunc("STYLE")
        self.scrollToFunc("STYLE")
        listPara = ["STD.", "NEUT.", "LAND.",'%s']

        # == 自定义的情况:
        if num not in ["STD.", "NEUT.", "LAND."]:
            # (...) 存在的情况
            if d(resourceId="com.autel.explorer:id/iv_second_next").exists():
                if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():# "指定参数" 和 (...)均存在的情况
                    pass   #己经存在该选择项

                 #(...)存在, "xx xx xx"不存在的情况,点(...)进入下一层循环
                elif not  d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                    d(resourceId="com.autel.explorer:id/iv_second_next").click()
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
                            d(resourceId="com.autel.explorer:id/iv_second_next").click()
                            time.sleep(0.5)

                            self.insideCircleStyle(num)
                            break





                # while True:

        # 是预设前三项情况
        else:

            for i in range(0, len(listPara)-1):
                if num == listPara[i]:
                    seq = i

            if d(resourceId="com.autel.explorer:id/tv_ui_second_para", text=num).exists():
                time.sleep(0.5)
                d(resourceId="com.autel.explorer:id/tv_ui_second_para", text=num).click()

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
                                    d(resourceId="com.autel.explorer:id/tv_ui_second_para", text=num).click()
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
                                    d(resourceId="com.autel.explorer:id/tv_ui_second_para", text=num).click()
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
                    d(resourceId="com.autel.explorer:id/tv_ui_first_para", text="DIGITAL ZOOM").click()

                    for i in range(0, len(listPara)):
                        if num == listPara[i]:
                            seq = i

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
                                    while j <= 20:
                                        d.swipe(0.32, 0.82, 0.68, 0.82)  # 往左边滑
                                        time.sleep(0.8)
                                        if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
                                            # if d(resourceId="com.autel.explorer:id/tv_second_para", text=mode).exists():
                                            d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
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
                                            d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
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


def main():
    test = Camera()
    time.sleep(0.5)
    # test.SetPictureSize("4000x3000") # pass

    # test.SetPictureFomat("JPG") #PASS
    # SetPictureMode_pre("TIMELAPSE")
    # insideCercle("5s")


    test.SetPictureMode_pre("BURST","5")
    # test.insideCircleBurst("2")
    # test.insideCircleTimelapse("2s")
    # test.insideCircleAeb("5")

    # test.SetPictureExpo('AUTO')  #PASS

    # test.SetPictureIso("900")     #PASS
    # test.SetPictureShutter("1/12.5")    #PASS                   # 整数时间后才加 "
    # test.SetpictureEv("+0.93")    #PASS
    # test.SetPictureWB("SUNNY")      #PASS

    # test.SetPictureColor("CLASSIC")
    # test.SetPictureDigizoom("2.0X")


    # test.SetPictureWB("2100K")  #注意大小写
    # test.scrollToFunc("STYLE")
    # test.SetPitureStyle("-3 -2 +3") #注意 "." 不要忘了.
    # test.SetPitureStyle("-1 -1 -1") #注意 "." 不要忘了.

if __name__ == '__main__':
    main()

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