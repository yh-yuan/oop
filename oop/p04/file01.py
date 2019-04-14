#!usr/bin/python  
#-*- coding:utf-8 _*-
import time
#打开文件，用写的方式
#r表示无需转义
#f=open(r"test01.txt",'w')
#文件打开后必须关闭
#以写方式打开文件，如果没有文件，则创建
#f.close()
#with语句
with open(r"test01.txt","r",encoding='utf8') as f:
    strline=f.readline()
    #此结构保证能够完整读取文件直到结束
    while strline:
        print(strline)
        strline=f.readline()

with open(r'test01.txt','r',encoding='utf8') as f:
    l=list(f)
    for line in l:
        print(line)
#read是按字符读取文件内容，允许输入参数决定读取几个字符

with open('test01.txt','r',encoding='utf8') as f:
    strChar = f.read()
    print(len(strChar))
    print(strChar)
#seek
#打开文件后，从第五个自己开始读取
with open('test01.txt','r',encoding='utf8') as f:
    f.seek(6,0)
    strChar=f.read()
    print(strChar)
with open('test01.txt','r',encoding='utf8') as f:
    strChar=f.read(3)
    while strChar:
        print(strChar)
        time.sleep(1)
        strChar=f.read(3)
with open('test01.txt','r',encoding='utf8') as f:
    strChar=f.read(3)
    pos=f.tell()
    while strChar:
        print(pos)
        print(strChar)
        strChar = f.read(3)
        pos = f.tell()
#文件的写操作，-write

with open('test01.txt','a',encoding='utf8') as f:
    f.write("生活不仅有眼前的苟且，\n还有远方的苟且")
#直接写入行

with open('test01.txt','a',encoding='utf8') as f:
    f.writelines("生活不仅有眼前的苟且，")
    f.writelines("还有远方的苟且")