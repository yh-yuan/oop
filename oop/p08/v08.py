#!usr/bin/python  
#-*- coding:utf-8 _*-

from email.mime.text import  MIMEText
mail_content="""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>大毛宝贝</title>
    </head>
    <body>
        <h1>这是袁海武给你使用html格式发的第一封python邮件，发给我的宝贝的</h1>
    </body>
    </html>
"""
msg = MIMEText(mail_content, "html", "utf-8")

from_addr="769270245@qq.com"
from_pwd='anhmawsovnuvbfae'

to_addr='1640494798@qq.com'
smtp_srv="smtp.qq.com"

try:
    import smtplib

    srv = smtplib.SMTP_SSL(smtp_srv.encode(), 465)

    srv.login(from_addr, from_pwd)
    srv.sendmail(from_addr, [to_addr], msg.as_string())
    srv.quit()

except Exception as e:
    print(e)