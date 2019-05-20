#checkbutton
from tkinter import  *

# root = Tk()
# v = IntVar()
# c = Checkbutton(root,text='测试一下',variable =v)
# c.pack()
#
# l = Label(root,textvariable =v)
# l.pack()
#
# mainloop()


# root = Tk()
# #
# # GIRLS = ['西施','貂蝉','王昭君','杨玉环']
# #
# # v =[]
# #
# # for girl in GIRLS:
# #     v.append(IntVar())
# #     b = Checkbutton(root,text=girl,variable =v[-1])
# #     b.pack(anchor =W)
# #
# # mainloop()

#radiobutton
'''
from tkinter import *

root =Tk()
v =IntVar()

Radiobutton(root,text='one',variable=v,value =1).pack(anchor =W)
Radiobutton(root,text='tow',variable=v,value =2).pack(anchor =W)
Radiobutton(root,text='three',variable=v,value =3).pack(anchor =W)
mainloop()
'''

# radiobutton 多个按钮,一个变量
'''
from tkinter import *
root =Tk()

v= IntVar()

LANGS = [('python',1),('Perl',2),('Ruby',3),('Lua',4)]

v = IntVar()
v.set(1)

for lang,num in LANGS:
    b = Radiobutton(root,text=lang,variable =v,value =num,indicatoron =False)
    b.pack(fill=X)

mainloop()
'''

#labelframe

from tkinter import *
root =Tk()

group = LabelFrame(root,text ='最好的脚本语言是: ',padx=5,pady=5)
group.pack(side=LEFT)
group2 = LabelFrame(root,text ='最不好的脚本语言是: ',padx=5,pady=5)
group2.pack(side = RIGHT)


LANGS = [('python',1),('Perl',2),('Ruby',3),('Lua',4)]
LANGS2 = [('python',1),('Perl',2),('Ruby',3),('Lua',4)]

v = IntVar()

for lang,num in LANGS:
    b =Radiobutton(group,text=lang,variable =v,value=num)
    b.pack(anchor=W)

v2 = IntVar()
for lang, num in LANGS2:
    c=Radiobutton(group2,text=lang,variable =v2,value=num)
    c.pack(anchor =W)
mainloop()





