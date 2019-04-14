#!usr/bin/python  
#-*- coding:utf-8 _*-

import re

#查找数字
# p=re.compile(r"\d+")
# m=p.match("12342tree342",pos=3,endpos=9)
# print(m)
# print(m[0])
# print(m.start(0))
# print(m.end(0))

p=re.compile(r"([a-z]+) ([a-z]+)",re.I)

m=p.match("i am really love maolu")
print(m)
print(m.group(0))
print(m.group(1))
print(m.start(0))
print(m.end(0))
print(m.groups())

#查找
#search
#search（str,[,pos[,endpos]]）在字符串中查找匹配，
'''findall:查找所有
    finditer：查找，返回一个iter结果
'''
p1=re.compile(r'\d+')

m1=p1.search("onee12312421fdsfewre")
print(m1.group())

p2=re.compile(r'\d+')
rst=p2.findall("onee12312421fdsfewre")
print(type(rst))
print(rst)

#sub 替换
#sub(reps,str[,count])

p3=re.compile(r"(\w+) (\w+)")
s="hello 123 want 354 maolu,i love you"
res1=p3.sub(r"hello word",s)
print(res1)

#匹配中文
title=u"世界 你好，hello world"
p4=re.compile(r"[\u4e00-\u9fa5]+")
rst2=p4.findall(title)
print(rst2)

#贪婪和非贪婪
#贪婪：尽可能多的匹配，（*）表示贪婪匹配
#非贪婪：找到符合条件的最小内容即可，（？）表示非贪婪
#正则默认使用贪婪匹配
