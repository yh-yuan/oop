#!usr/bin/python  
#-*- coding:utf-8 _*-

import tkinter

#tkinter._test()

base=tkinter.Tk()
# base.mainloop()

base.wm_title("Label Test")
# lb=tkinter.Label(base,text="python Label")
# lb.pack()
# base.mainloop()

#支持属性很多background,font,underline等
lb1=tkinter.Label(base,text="python ai")
lb1.pack()
lb2=tkinter.Label(base,text="绿色背景",background="green")
lb2.pack()

lb3=tkinter.Label(base,text="蓝色背景",background="blue")
lb3.pack()

base.mainloop()