# import time
# import random
# import uiautomator2 as u2
# import time
# pkg_name='com.autel.explorer'
# # pkg_name='com.taobao.taobao'
# # d=u2.connect_wifi('192.168.1.12')  # LG
# # d=u2.connect_wifi('192.168.15.31')
# # d=u2.connect_usb('7cc8c0d9')  # One Plus 3
# d=u2.connect_wifi('192.168.1.11') #One Plus 3
#
# def circler():
#     num=""
#     listPara=[]
#     seq=0
#
#     if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
#         time.sleep(0.5)
#         d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
#
#     else:
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
#                             d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
#                             flag = True
#                         else:
#                             print("Para,not found,continue...")
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
#
#                         if d(resourceId="com.autel.explorer:id/tv_second_para", text=num).exists():
#                             time.sleep(0.5)
#                             d(resourceId="com.autel.explorer:id/tv_second_para", text=num).click()
#                             flag = True
#                         else:
#                             print("not found,continue...")
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
#
#
# listShutter=["1/8000","1/6000","1/5000","1/4000","1/3200","1/2500","1/2000","1/1600","1/1250","1/1000","1/800","1/640","1/500",
#                 "1/400","1/320","1/240","1/200","1/160","1/120","1/100","1/80","1/60","1/50","1/40","1/30","1/25","1/20","1/15","1/12.5",
#                 "1/10","1/8","1/6.25","1/5","1/4","1/3","1/2.5","1/2","1/1.67","1/1.25","1\"","1.3\"","1.6\"","2\"","2.5\"","3\"","3.2\"",
#                 "4\"","5\"","6\"","8\""]
# num=""
# for i in range (0,len(listShutter)):
#     if num == listShutter[i]:
#         seq=i
import traceback
import logging

logging.basicConfig(filename='log.log')


def error_func():
    b = 1 / 0


if __name__ == '__main__':
    try:
       error_func()
    except:
        s = traceback.format_exc()
        logging.error(s)

