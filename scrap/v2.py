#!usr/bin/python  
#-*- coding:utf-8 _*-

from urllib import  request

if __name__=='__main__':
    url = 'https://blog.csdn.net/ling_mochen/article/details/79314118'
    # 打开相应url并把相应页面作为返回
    rsp = request.urlopen(url)
    # 把返回结果读取出来
    html = rsp.read()
    print("url:{0}".format(rsp.geturl()))
    print("info:{0}".format(rsp.info()))
    print("Code:{0}".format(rsp.getcode()))