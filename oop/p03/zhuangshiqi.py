#!usr/bin/python  
#-*- coding:utf-8 _*-
import time
import functools
#现在出新的需求，对hello功能进行扩展，每次打印hello之前打印系统时间
#而实现这个功能不能改变现有代码，使用装饰器
#装饰器（Decrator）
#好处，一定义，则可以装饰任意函数，一旦被其装饰，则把装饰器的功能直接添加到定义函数的功能上
def printTime(f):
    def wrapper(*args,**kwargs):
        print("time: ",time.ctime())
        return f(*args,**kwargs)
    return wrapper
@printTime
def hello():
    print('hello world')
hello()
@printTime
def hello2():
    print("今天很高兴，被夸奖了")
    print("还可以有很多的选择")
hello2()
#上面对函数的装饰使用了系统定义的语法糖
#下面手动执行装饰器
def hello3():
    print('我手动执行')
hello3()
hello3=printTime(hello3)
hello3()
#偏函数
int16=functools.partial(int,base=16)
int16('12345')
