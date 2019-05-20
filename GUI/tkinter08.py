'''from tkinter import *

root = Tk()

w = Canvas(root, width=200, height=100)  # width和height单位是像素
w.pack()
# 到这里还是看不见Canvas的，不过可以通过设置Canvas的background属性来改变背景颜色

# create后面加上下横线再加上我们要绘制对象的名字
w.create_line(0, 50, 200, 50, fill='yellow')  # 前两个参数描述的是直线的起始位置是水平方向的第0个像素和竖直方向的第50像素。fill设置填充颜色
w.create_line(100, 0, 100, 100, fill='red', dash=(4, 4))  # dash是设置虚线
w.create_rectangle(50, 25, 150, 75, fill='blue')  # 左上角右下角的坐标
# 这三个画布对象没有意外的话会一直保留着，直到你去修改它们，它们就可能会被覆盖。
# 例如说这条黄线本来是从左至右贯穿整个Canvas的，但是被矩形覆盖了，中间被覆盖的位置就看不到了
# 还有一些方法可以对这些画布对象进行修改，如Canvas实例对象的coords() itemconfig() move()方法,删除的话可以用delete()方法。下例将进行演示

mainloop()
'''
'''
import tkinter.messagebox
from tkinter import *
tkinter.messagebox.askokcancel("FishC Demo",'发射导弹？')
tkinter.messagebox.askquestion("FishC Demo","买个优盘？")
tkinter.messagebox.askretrycancel("FishC Demo","启动失败，重试？")
tkinter.messagebox.askyesno("FishC Demo","我帅吗?")
tkinter.messagebox.showerror("FishC Demo","出错啦！")
tkinter.messagebox.showinfo("FishC Demo","2017新年快乐")
tkinter.messagebox.showwarning("FishC Demo","你在偷懒！")
mainloop()
'''

import tkinter.filedialog
from tkinter import *
root = Tk()

def callback():
     fileName = tkinter.filedialog.askopenfilename()
     print(fileName)
Button(root,text='打开文本',command=callback).pack()
mainloop()