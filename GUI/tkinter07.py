'''from tkinter import *
import hashlib  # 获得md5的值要用该库

root = Tk()

text = Text(root, width=30, height=5)
text.pack()

text.insert(INSERT, 'I love study')
contents = text.get('1.0', END)


def getSig(contents):
    n = hashlib.md5(contents.encode())
    return n.digest()  # 只需要得到md5值n的简单摘要即可


sig = getSig(contents)


def check():  # 点下检查的时候，会重新获得一次contents的内容，将原来的contents进行一个md5的hash，获得它的md5的值；同时也获得之后contents的md5的值，将两者进行对比。由于一个内容只能产生一个唯一的散列，因此若不一样，就说明内容发生了改变。
    contents = text.get('1.0', END)
    if sig != getSig(contents):
        print("内容发生变动")
    else:
        print("内容没有发生变动")


Button(root, text="检查", command=check).pack()

mainloop()
'''

from tkinter import *
import hashlib  # 获得md5的值要用该库

root = Tk()

text = Text(root, width=30, height=5)
text.pack()

text.insert(INSERT, 'I enjoy studying Python')


def getIndex(text, index):  # 要把任何支持的格式转化为默认行列字符串的格式可以使用Text组件的index()方法
    return tuple(map(int, str.split(text.index(index), '.')))  # 将转化好的转化成一个元组的形式返回


start = '1.0'
while True:
    pos = text.search("y", start, stopindex=END)
    if not pos:  # 找不到就跳出循环
        break
    print("找到了，位置是：", getIndex(text, pos))  # 把找到的位置转化为人类能读懂的位置
    start = pos + '+1c'  # 将start的位置指向下一个字符

mainloop()
