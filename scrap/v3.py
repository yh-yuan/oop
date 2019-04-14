#!usr/bin/python  
#-*- coding:utf-8 _*-

from urllib import request,parse

if __name__=="__main__":
    url = 'http://www.baidu.com/s?'
    wd = input("Input your keyword:")
    qs={
        "wd":wd
    }

    qs=parse.urlencode(qs)
    print(qs)

    fullurl=url+qs
    print(fullurl)

    rsp=request.urlopen(fullurl)

    html=rsp.read()

    html=html.decode()
    print(html)
