#conding：utf-8
import re
import random
import uiautomator2 as u2
import time
pkg_name='com.autel.explorer'
# pkg_name='com.taobao.taobao'
# d=u2.connect_wifi('192.168.1.12')  # LG
# d=u2.connect_wifi('192.168.15.31')
# d=u2.connect_usb('7cc8c0d9')  # One Plus 3
d=u2.connect_wifi('192.168.1.11') #One Plus 3
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

d(resourceId="com.autel.explorer:id/rel_camera_takephoto_controller").click()