#!usr/bin/python  
#-*- coding:utf-8 _*-

#1640494798@qq.com
#769270245@qq.com
#anhmawsovnuvbfae

import  smtplib
from email.mime.text import MIMEText

#mimetext三个主要参数
#1、邮件内容
#2、mime子类型，在此案例我们用plain表示text类型
#3、邮件编码格式
msg=MIMEText("Hello,i am yuanhaiwu ,i love maolu,he is my baby,this is my first python to emial","plain","utf-8")

#发送email地址，此处地址直接使用qq# 的邮箱，密码一般需要临时输入，
from_addr="769270245@qq.com"
#此处密码是经过申请设置后的授权码，不是qq邮箱密码
from_pwd='anhmawsovnuvbfae'

#收件人信息
#此处使用qq邮箱
to_addr='1640494798@qq.com'

#输入smtp服务器地址
#此处根据不同的邮件服务商有不同的值
#现在基本任何一家邮件服务商，如果采用第三方手法邮件，都需要开启授权选项
#腾讯qq邮箱的smtp地址是smtp.qq.com

smtp_srv="smtp.qq.com"

try:
    #两个参数
    #第一个是服务器地址，但一定是bytes格式，所以需要编码
    # 第二个参数是服务器的接受访问端口
    srv = smtplib.SMTP_SSL(smtp_srv.encode(), 465)  # SMTP协议默认端口25
#登录邮箱发送
    srv.login(from_addr, from_pwd)
    # 发送邮件
    # 三个参数
    # 1. 发送地址
    # 2. 接受地址，必须是list形式
    # 3. 发送内容，作为字符串发送
    srv.sendmail(from_addr, [to_addr], msg.as_string())
    srv.quit()
except Exception as e:
    print(e)