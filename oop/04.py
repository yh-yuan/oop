#!usr/bin/python  
#-*- coding:utf-8 _*-

class Student():
    name = "dana"
    age = 18

    # 注意say的写法，参数由一个self
    def say(self):
        self.name = "aaaa"
        self.age = 200
        print("My name is {0}".format(self.name))
        print("My age is {0}".format(self.age))

    def sayAgain(s):
        print("My name is {0}".format(s.name))
        print("My age is {0}".format(s.age))

yueyue = Student()
yueyue.say()
yueyue.sayAgain()

class Teacher():
    name='damao'
    age=24
    def say(self):
        self.name='yuanhw'
        self.age=28
        print("My name is {0}".format(self.name))
        print('My age is {0}'.format(self.age))
    def sayAgain():
        print(__class__.name)
        print(__class__.age)
        print('hello damao')
t=Teacher()
t.say()
Teacher.sayAgain()
class A():
    name='damao'
    age=24
    def __init__(self):
        self.name='baobei'
        self.age=23
    def say(self):
        print(self.name)
        print(self.age)
class B():
    name='yuan'
    age=28

a=A()
#此时，系统会默认把a作为第一个参数传入函数
a.say()
#此时，self被a替换
A.say(a)
#同样可以把A作为参数传入
A.say(A)
#此时，传入的是类实例B，因为B具有name和age属性，所以不会报错
A.say(B)

#以上代码，利用了鸭子模型

