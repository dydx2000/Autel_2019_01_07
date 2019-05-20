# -*- coding:utf-8 -*-
import os

from PIL import Image

#定义切割时方式，传入文件名

def cut(name):


    path1 ='./test/'
    name1 = path1+name+'.jpg' #要处理的图片文件名
    path3 ="./cutLeft/"
    name3 = path3+name + "_cutL.jpg" #左图保存路径
    path4 = './cutRight/'
    name4 = path4+name + "_cutR.jpg" #右图保存路径

    im =Image.open(name1) # 打开图片
    size =im.size #获取大小
    # print(size) #打印大小


    x1 = 0
    y1 = 0


    x2 = size[0]/2
    y2 = size[1]

    im2 = im.crop((x1,y1, x2, y2))  #切左图
    im2.save(name3)    #保存左图


    x1 = size[0]/2
    y1 = 0
    x2 = size[0]
    y2 = size[1]
    im4 = im.crop((x1, y1, x2, y2)) #切右图
    im4.save(name4)     #保存右图

#在这里传入要处理图片的路径
listdir = os.listdir('.\\test')
# print(listdir)

#判断左图保存路径是否存在，没有就创建文件夹
if os.path.exists(".\\cutLeft"):
    pass
else:
    os.mkdir(".\\cutLeft")

#判断右图保存路径是否存在，没有就创建文件夹
if os.path.exists(".\\cutRight"):
    pass
else:
    os.mkdir(".\\cutRight")

#批量切割处理图片



count = 0
for name in listdir:
    count += 1
    name =name[:-4]  #去除扩展名
    print("正在处理第 %s 张"%count)
    print(name,"\n")
    cut(name)  #调用切割方法




