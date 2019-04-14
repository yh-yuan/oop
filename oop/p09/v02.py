#!usr/bin/python  
#-*- coding:utf-8 _*-

import tkinter

def showLabel():
    global baseFrame
    #在函数中定义了一个label
    #label的父组件是baseFrame
    lb=tkinter.Label(baseFrame,text="显示Label")
    lb.pack()

baseFrame=tkinter.Tk()
#生成一个按钮
#command参数指示，当按钮被按下的时候，执行哪个函数
btn=tkinter.Button(baseFrame,text="show label",command=showLabel)
btn.pack()
baseFrame.mainloop()

'''
Button的属性：

anchor 				设置按钮中文字的对其方式，相对于按钮的中心位置
background(bg) 		设置按钮的背景颜色
foreground(fg)		设置按钮的前景色（文字的颜色）
borderwidth(bd)		设置按钮边框宽度
cursor				设置鼠标在按钮上的样式
command				设定按钮点击时触发的函数
bitmap				设置按钮上显示的位图
font				设置按钮上文本的字体
width				设置按钮的宽度  (字符个数)
height				设置按钮的高度  (字符个数)
state				设置按钮的状态
text				设置按钮上的文字
image				设置按钮上的图片
'''