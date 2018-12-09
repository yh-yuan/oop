#!usr/bin/python  
#-*- coding:utf-8 _*-

import time
import datetime

print(time.timezone)
#localtime,得到当前时间的时间结构，可以通过点好操作符得到相应的属性元素的内容
t=time.localtime()
print(t.tm_hour)
tt=time.asctime(t)
print(tt)
#ctime
t1=time.ctime()
print(t1)
#mktime()使用时间元素获取对应的时间戳
#格式time.mktime(时间元祖)
#clock获取cpu时间
#sleep:是程序进入睡眠，n秒后继续
t2=time.localtime()
ft=time.strftime('%Y{y}%m{m}%d{d}',t2).format(y='年',m='月',d='日')
print(ft)
#datetime
#datetime.date
dt=datetime.date(2018,3,26)
print(dt)
print(dt.day)
print(dt.year)
print(dt.month)
