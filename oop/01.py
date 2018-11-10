#!usr/bin/python
#-*- coding:utf-8 _*-
class Student():

    pass
damao=Student()

class PythonStudent():
    name=None
    age=18
    course='python'

    def doHomeWork(self):
        print('i 在做作业')
        return None
mao=PythonStudent()
print(mao.age)
print(mao.name)
mao.doHomeWork()
