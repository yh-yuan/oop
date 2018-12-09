#!usr/bin/python  
#-*- coding:utf-8 _*-
import calendar

cal=calendar.calendar(2019)
print(cal)
#isleap;判断某一年是否闰年:
#leapdays:获取指定年份之间的闰年的个数
days=calendar.leapdays(1998,2018)
print(days)
m3=calendar.month(2018,3)
print(m3)
m4=calendar.monthrange(2018,11)
print(m4)
#返回一个月每天的矩阵列表
m1=calendar.monthcalendar(2018,3)
print(m1)