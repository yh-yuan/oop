#!usr/bin/python  
#-*- coding:utf-8 _*-

from urllib import  request,error

if __name__=="__main__":
    url= "http://www.baidu.com"
    # 使用代理步骤
    # 1. 设置代理地址
    proxy={'http':'219.139.140.246:9999'}
    #创建proxyhandler
    proxy_handler=request.ProxyHandler(proxy)
    #创建opener
    opener=request.build_opener(proxy_handler)
    #安装opener
    request.install_opener(opener)

    #现在如果访问url，则使用代理服务器
    try:
        rsp=request.urlopen(url)
        html=rsp.read().decode()
        print(html)
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)
