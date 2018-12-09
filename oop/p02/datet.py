#!usr/bin/python  
#-*- coding:utf-8 _*-

from datetime import  datetime,timedelta
import timeit
#datetime.time
#datetime.datetime 提供日期喝时间的组合
#datetime.timedelta 提供一个时间差，时间长度
dt1=datetime(2018,3,28)
print(dt1.today())

delt1=datetime.now()
print(delt1)
print(delt1.strftime("%Y-%m-%d %H:%M:%S"))
td=timedelta(hours=1)
print((delt1+td).strftime("%Y-%m-%d %H:%M:%S"))
#timeit 时间测量工具
#利用timeit调用代码，执行10000次，查看运行时间
t1=timeit.timeit(stmt="[i for i in range(1000)]",number=1000)
print(t1)

s='''
def doIt(num):
    for i in range(num):
        print("repeat for {0}".format(i))
'''

t=timeit.timeit("doIt(num)",setup=s+"num=3",number=10)
print(t)