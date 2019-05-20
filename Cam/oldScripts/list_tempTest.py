listMode=['SINGLE','BURST','TIMELAPSE','AEB']
# for i in range(0,len(listMode)):
# for i in range(len(listMode)):
#     print (listMode[i])
#     # print(type(listMode[i]))
#
# print("\n\r----------------------\n")
#
# for j in listMode:
#     print(j)
#
# def funx(x):
#     def funy(y):
#         return x * y
#     return funy
#
# print(funx(2)(5))
#
import tkinter as tk

# root = tk.Tk()
# root.title('My first python window')
# root.geometry('200x50')
# thelabel =tk.Label(root,text ='这里放的是一个标签.')
# thelabel.pack()
# root.mainloop()


# class APP:
#     def __init__(self,master):
#         frame = tk.Frame(master)
#         frame.pack(side=tk.LEFT,padx =10,pady =10)
#         self.hi_there = tk.Button(frame,text ='打招呼',bg='black',fg='white',command =self.say_hi)
#         self.hi_there.pack()
#
#     def say_hi(self):
#         print('朋友们,这是我的第二个gui程序.')
#
#
# root = tk.Tk()
# app =APP(root)
# root.mainloop()

from tkinter import *
root =Tk()

textLabel = Label(root,text ='豆比\n兔子',justify =LEFT,pady =10 )
textLabel.pack(side = TOP)

photo = PhotoImage(file =r"c:\tuzi.gif")
imgLabel = Label(root,image=photo,pady = 20)
imgLabel.pack(side=BOTTOM)

mainloop()

