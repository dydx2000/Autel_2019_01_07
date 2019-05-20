

'''
root =Tk()

phooto = PhotoImage(file =r"c:\tuzi.gif")
theLabel =Label(root,
                text ="good good study,\n day day up",
                justify =LEFT,
                image = phooto,
                compound =CENTER,
                font =('宋体',15),
                bg ="yellow")

theLabel.pack()
mainloop()

'''



from tkinter import *
root =Tk()


def callback():
    var.set('豆比小狗')


frame1 = Frame(root)
frame2 = Frame(root)


var = StringVar()
var.set('可爱小猫')

textLabel = Label(frame1,
                  textvariable =var,
                  justify = LEFT)

textLabel.pack(side=LEFT)

photo = PhotoImage(file =r'c:\tuzi.gif')
imgLabel = Label(root,image = photo)
imgLabel.pack(side = RIGHT)



theButton = Button(frame2,text ='点击改变Label的文字',command =callback)
theButton.pack()


frame1.pack(padx =10,pady = 10 )
frame2.pack(padx =10,pady = 10 )


mainloop()

