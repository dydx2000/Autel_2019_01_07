'''from tkinter import *

root = Tk()

text = Text(root, width=30, height=3)  # 30的意思是30个平均字符的宽度，height设置为两行
text.pack()

text.insert(INSERT, 'I Love\n')  # INSERT表示输入光标所在的位置，初始化后的输入光标默认在左上角
text.insert(END, 'Study!')
text.insert(END,'\nI love study too')

mainloop()
# 生成好的Text组件可以进行编辑（并不是只读形式的）

'''
'''
from tkinter import *

root = Tk()

text = Text(root, width=30, height=5)
text.pack()

text.insert(INSERT, 'I Love')
text.insert(END, 'Study!')


def show():
    print('呦西，我被点了一下')


b1 = Button(text, text='点我', command=show)  # 注意放入的是Text而不是root了
text.window_create(INSERT, window=b1)

mainloop()
'''

'''
from tkinter import *

root = Tk()

text = Text(root, width=50, height=40)
text.pack()

photo = PhotoImage(file=u"c:/tuzidead.gif")  # 只支持GIF格式的


def show():
    text.image_create(END, image=photo)


b1 = Button(text, text='点我', command=show)  # 注意放入的是Text而不是root了
text.window_create(INSERT, window=b1)

mainloop()
'''

from tkinter import *
import webbrowser

root = Tk()

text = Text(root, width=30, height=5)
text.pack()

text.insert(INSERT, 'Baidu.com的创始人是李彦宏')

text.tag_add('link', '1.0', '1.8')
text.tag_config('link', foreground='blue', underline=True)


def show_arrow_cursor(event):
    text.config(cursor='arrow')


def show_xterm_cursor(event):
    text.config(cursor='xterm')


def click(event):
    webbrowser.open('http://www.baidu.com')


text.tag_bind('link', '<Enter>', show_arrow_cursor)  # <Enter>指的是当鼠标进入的时候调用show_hand_cursor函数
text.tag_bind('link', '<Leave>', show_xterm_cursor)
text.tag_bind('link', '<Button-1>', click)

mainloop()
