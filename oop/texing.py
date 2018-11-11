#!usr/bin/python  
#-*- coding:utf-8 _*-

class Person():
    name='damao'

    __age=24
p=Person()

print(p.name)
#访问是错误的，无法访问到私有属性
print(p.__age)





