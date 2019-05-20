import datetime
import time
import logging
logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a,%d %b %Y %H:%M:%S',
                    filename='CamShots.log',
                    filemode='a')
import random
# import Autel_Explorer.Camera.uiautomator2_cam_shots as uiauto
import Cam.uiautomator2_cam_shotsbak0131 as uiauto
# import Autel_Explorer.Camera.uiautomator2_cam_shots_test as uiauto
import uiautomator2 as u2

d = uiauto.d
d.implicitly_wait(60)
d.wait_timeout = 60
test=uiauto.Camera()
time.sleep(1)

d(resourceId="com.autel.dragonfish:id/waypoint_mission_image").click()
# d(className="android.widget.ImageView", instance=18).click()
d(className="android.view.View", instance=3).click()
d(className="android.view.View", instance=2).click()
d(className="android.view.View", instance=2).click()