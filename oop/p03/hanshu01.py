#!usr/bin/python  
#-*- coding:utf-8 _*-
from functools import reduce
stm=lambda x:100*x
print(stm(89))

#高阶函数举例
#funA是普通函数，返回一个传入数字得100倍
def funA(n):
    return n*100
#再写一个函数，把传入参数乘以300被，利用高阶函数
def funB(f,n):
    return f(n)*3
print(funB(funA,3))
#比较普通调用，funB要由于普通调用funA,
#map举例
l1=[i for i in range(10)]
def mulTen(n):
    return n*10
#help(map)
l2=map(mulTen,l1)
l3=[i for i in l2]
print(l3)

def myAdd(x,y):
    return x+y
#d对于列表执行myAddreduce操作
rst=reduce(myAdd,[1,2,3,4,5,6])
print(rst)
#filter
def isEven(a):
    return a%2==0
l=[2,3,4,5,5,43,32]
rstf=filter(isEven,l)
print(rstf)
print([i for i in rstf])
#sorted
a=[1,2,3,4,77,64,9,7]
al=sorted(a,reverse=True)
print(al)
astr=['dada','Daneda','wefdsF','JINGJING','hah']
srt1=sorted(astr)
print(srt1)
str2=sorted(astr,key=str.lower)
print(str2)
#返回函数
def myF(a):
    print("in myf")
    return None
a=myF(8)
print(a)
#函数作为返回值返回，被返回的函数在函数体内定义
def myF2():
    def myF3():
        print("in my F 3")
        return 3
    return myF3
f3=myF2()
print(f3)
f3()
#闭包常见坑
#等三个函数都返回的时候菜统一使用，此时I已经变成了3
#解决方案，再写一个函数，
def count():
    fs=[]
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
cf1,cf2,cf3=count()
print(cf1())
print(cf2())
print(cf3())
def count2():
    def f(j):
        def g():
            return j*j
        return g
    fs=[]
    for i in range(1,4):
        fs.append(f(i))
    return fs