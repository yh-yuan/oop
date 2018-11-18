#!usr/bin/python  
#-*- coding:utf-8 _*-
class Person():
    def __init__(self):
        pass
    def __setattr__(self,name,value):
        print("设置属性：{0}".format(name))
        #会导致问题,会一直重复调用__setattr__
        #self.name=value
        #为避免死循环，统一调用父类的魔法函数
        super().__setattr__(name,value)

        # 实例方法
    def eat(self):
        print(self)
        print("Eating.....")

        # 类方法
        # 类方法的第一个参数，一般命名为cls，区别于self
    @classmethod
    def play(cls):
        print(cls)
        print("Playing.....")

        # 静态方法
        # 不需要用第一个参数表示自身或者类
    @staticmethod
    def say():
        print("Saying....")

yueyue = Person()

# 实例方法
yueyue.eat()
# 类方法
Person.play()
yueyue.play()
#静态方法
Person.say()
yueyue.say()
p=Person()
p.age=18


