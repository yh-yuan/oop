#!usr/bin/python  
#-*- coding:utf-8 _*-

import  socket

def serverFunc():
    #socket.AF_INET:使用ipv4
    #socket.SOCK_DGRAM：使用udp协议
    sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #绑定ip和port
    #地址是一个tuple类型
    addr=("127.0.0.1",7852)
    sock.bind(addr)
    #接收对方消息
    #等待方式为死等，没有其他可能性
    #recvfrom接受的返回值是一个tuple，前一项表示数据，后一项表示地址
    # 参数的含义是缓冲区大小
    data, addr = sock.recvfrom(500)
    print(data)
    print(type(data))

    # 发送过来的数据是bytes格式，必须通过解码才能得到str格式内容
    # decode默认参数是utf8
    text = data.decode()
    print(type(text))
    print(text)

    # 给对方返回的消息
    rsp = "Ich hab keine Hunge"
    print(addr)
    # 发送的数据需要编码成bytes格式
    # 默认是utf8
    data = rsp.encode()
    sock.sendto(data, addr)

if __name__ == '__main__':
    print("Starting server.........")
    #while True:
    serverFunc()
    print("Ending server........")