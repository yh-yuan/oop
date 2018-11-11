#!usr/bin/python  
#-*- coding:utf-8 _*-

# class Person():
#     name='damao'
#
#     __age=24
# p=Person()
#
# print(p.name)
# #访问是错误的，无法访问到私有属性
# print(p.__age)
class Person():
    name='damao'
    __score=0
    age=24
    _petname='sec' #小明，是保护的。子类可以用，但不能公用
    def sleep(self):
        print('sleep.......')
    def work(self):
        print('make some money')
class Teacher(Person):
    def make_test(self):
        pass
    def work(self):
        # 扩充父类的功能
        Person.work(self)
        super(Teacher, self).work()
        self.make_test()
    pass

t=Teacher()
print(t.name)
print(t._petname)
t.work()
# 私有的不能访问
# print(t.__score)
class Animal():
    def __init__(self):
        print("animal")
class PaxingAni(Animal):
    def __init__(self,name):
        print("paxing dongwu {0}".format(name))

class Dog(PaxingAni):
#     __init__就是构造函数
# 每次实例化的时候，第一个呗调用
# 因为主要工作是初始化，所以得名，第一个参数一定是self
    def __init__(self):
        print("i an init in dog")
class Cat(PaxingAni):
    pass
kaka=Dog()
tom=Cat('tom')







