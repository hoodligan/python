# 发送附件

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

con=smtplib.SMTP_SSL('smtp.qq.com',465)
con.login(user='2804555260@qq.com',password='hhrotgwljdmqdfhh')
# 发送者账号
sender='2804555260@qq.com'
# 接受者账号
receive=['2804555260@qq.com','1106614821@qq.com']

# 发送内容
# 附件实例  盒子
message=MIMEMultipart()
# 拿到内容
with open('./files/2020-11-16 21-15-18test_report.html','rb')as f:
    content=f.read()
    # 内容写在信纸上
    files2=MIMEText(content,'base64','utf-8')
    # 纸取个名字  不要用中文去写  用英文
    files2['Content-Disposition']='attachment;filename="2.html"'
    # 把家书放到盒子中寄出去
    message.attach(files2)

    msg=MIMEText('正文内容','plain','utf-8')
    message.attach(msg)

message['Subject']='这是一封家书'
# 发送人
message['from']=sender
# 收件人
message['to']=';'.join(receive)

con.sendmail(sender,receive,message.as_string())

# 注意：在日常工作中，发送html的测试报告，要压缩成压缩文件之后在发送
# 手动压缩 代码压缩 zipfile

