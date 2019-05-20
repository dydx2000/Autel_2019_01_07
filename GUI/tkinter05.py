'''
from tkinter import *

master = Tk()

theLB =Listbox(master,selectmode =MULTIPLE )

theLB.pack()

for item in ['张三','李四','王五','赵六']:
    theLB.insert(END,item)




theButton = Button(master,text='删除',\
                   command=lambda x=theLB:x.delete(ACTIVE))
theButton.pack()

mainloop()
'''

#scroll bar
'''
from tkinter import *

root = Tk()

sb = Scrollbar(root)
sb.pack(side=RIGHT, fill=Y)  # 把滚动条加到右边去，填充整个y轴

lb = Listbox(root, yscrollcommand=sb.set)
# 在Listbox里滑动鼠标滚轮时调用set方法，同时修改滚动条的位置

for i in range(1000):
    lb.insert(END, i)
lb.pack(side=LEFT, fill=BOTH)

# 要与滚动条互通互连，要设置滚动条的command选项
sb.config(command=lb.yview)  # config方法设置某个选项的值
# yview方法是Listbox里的默认方法，方法已经设置好怎么显示垂直滚动对应的内容变化
# 拖动垂直滚动条时调用yview

mainloop()
'''

#scale

from tkinter import *
'''
# 当我们希望用户输入某个范围内的数字的时候，可能会使用Entry组件，但是Entry组件并不能限制一个范围
root = Tk()

s1 = Scale(root, from_=0, to=42)  # 有两个参数from和to，但是from参数和Python的关键字冲突了，所以加个下横线
s1.pack()

s2 = Scale(root, from_=0, to=200, orient=HORIZONTAL)  # 默认Scale是垂直的，可以修改orient参数成水平的
s2.pack()


# 获取滑块当前位置使用的是get方法
def show():
    print(s1.get(), s2.get())


Button(root, text='获取位置', command=show).pack()

mainloop()

'''

from tkinter import *

root = Tk()

# tickinterval=5每5个步长显示刻度
# resolution设置每次移动多少个长度，等于5的话，每次改变只能改变5
# 设置length长度，不然都堆在一起了
s1 = Scale(root, from_=0, to=42, tickinterval=5, resolution=5, length=200).pack()
s2 = Scale(root, from_=0, to=200, tickinterval=10, orient=HORIZONTAL, length=600).pack()

mainloop()




