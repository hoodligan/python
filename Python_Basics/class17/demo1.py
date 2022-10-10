# 邮件
# 内容：1.用python代码发文本邮件  2.发送html邮件 发送附件  图片

# smtp发送邮件   smtp邮件传输协议  smtplib库 ：进行简单的封装  简单

import smtplib

# 1.连接邮箱服务器  邮局   smtplib.SMTP_SSL(邮箱连接地址,端口号)  smtp.xx.com
# 163邮箱：smtp.163.com  端口号
# qq邮箱：smtp.qq.com  端口号  465或587
from email.mime.text import MIMEText

con=smtplib.SMTP_SSL('smtp.qq.com',465)
print(con)

# 登录邮箱  用户名和密码  密码用授权码  qq邮箱--设置--账户-POP3/SMTP服务开启 授权码
con.login(user='2804555260@qq.com',password='hhrotgwljdmqdfhh')

# 发送者账号
sender='2804555260@qq.com'
# 接受者账号
receive='2804555260@qq.com'

# 发送内容  _text 内容, _subtype='plain' 文本 , _charset=None  字符集
htmlContent="<a href='http://www.baidu.com'>我是html代码</a>  东风风神懂法守法大幅度的首付首付"
message=MIMEText(htmlContent,'html','utf-8')
# message=MIMEText('小幸运你好，我是渣渣秋','plain','utf-8')

# 设置头部内容  标题  发件人 收件人
# 标题
message['Subject']='发送给小幸运的一封信'
# 发送人
message['from']=sender
# 收件人
message['to']=receive

# 邮件有没有发送出去 有没有问题,担心发送的邮件有问题
try:
    # 发送邮件
    con.sendmail(sender,receive,message.as_string())
    print('邮件发送成功')
except Exception as e:
    print('没有办法发送邮件，报错了')

# 发送文本文件
# html格式的邮件

# 发送测试报告，发送html的测试报告  发送给测试相关人员怎么发送呢？