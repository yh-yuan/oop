#!usr/bin/python  
#-*- coding:utf-8 _*-

import tkinter

baseFrame=tkinter.Tk()
menubar=tkinter.Menu(baseFrame)

for item in ['file','edit','view','about']:
    menubar.add_command(label=item)

baseFrame['menu']=menubar

baseFrame.mainloop()