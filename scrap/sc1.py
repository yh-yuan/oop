#!usr/bin/python  
#-*- coding:utf-8 _*-

from urllib import  request

if __name__=='__main__':
    url='https://blog.csdn.net/ling_mochen/article/details/79314118'
    #打开相应url并把相应页面作为返回
    rsp=request.urlopen(url)
    #把返回结果读取出来
    html=rsp.read()
    #利用charset自动检测
    #cs=charset.detect(html)
    #cd.get("encoding",'utf-8')
    print(type(html))
    html=html.decode('utf-8')
    print(html)
'''
网页编码问题解决，
'''