
#coding=utf-8

# x=None
# y=2
# try:
# 	x=1/y
# 	print('try')
# except NameError:
# 	print('unkown variable')
# else:
# 	print('went well')
# finally:
# 	print('cleaning up')
# 	del x
#

import os
text = os.popen("adb devices").read().split()[4]
print(text)
