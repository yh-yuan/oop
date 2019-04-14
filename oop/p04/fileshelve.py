#!usr/bin/python  
#-*- coding:utf-8 _*-
import  shelve
shv=shelve.open(r'shv.db')
shv['one']=1
shv['two']=2
shv['three']=3
shv.close()

shv=shelve.open(r'shv.db',flag='r')
try:
    print(shv['one'])
except Exception as e:
    print("异常")
finally:
    shv.close()