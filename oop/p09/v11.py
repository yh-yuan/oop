#!usr/bin/python  
#-*- coding:utf-8 _*-

import tkinter

baseFrame=tkinter.Tk()

cvs=tkinter.Canvas(baseFrame,width=300,height=200)
cvs.pack()

# 一条线需要两个点指明起始
# 参数数字的单位是px

cvs.create_line(23,23,190,234)
cvs.create_text(56,57,text="i love maolu")

baseFrame.mainloop()