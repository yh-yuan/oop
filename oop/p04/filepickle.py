#!usr/bin/python  
#-*- coding:utf-8 _*-
import  pickle
# age=19
# with open(r'test02.txt','wb') as f:
#     pickle.dump(age,f)
#
# with open(r'test02.txt','rb') as f:
#     age=pickle.load(f)
#     print(age)

a=[19,'yuanhaiwu','i love maolu','wugang',[186,56]]
with open(r'test02.txt','wb') as f:
     pickle.dump(a,f)

with open(r'test02.txt','rb') as f:
     a=pickle.load(f)
     print()

