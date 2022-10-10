# 发送图片
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import smtplib
from email.mime.text import MIMEText

con=smtplib.SMTP_SSL('smtp.qq.com',465)
con.login(user='2804555260@qq.com',password='hhrotgwljdmqdfhh')

# 发送者账号
sender='2804555260@qq.com'
# 接受者账号
receive=['2804555260@qq.com']
# 抄送者账号
cs=['1787326464@qq.com','1418404585@qq.com','7845684@qq.com']
# 发送图片
message=MIMEMultipart()
# 图片内容
with open('files/imgae.jpg','rb')as f:
    image1=f.read()
    # 放在纸上，图片
    image_data=MIMEImage(image1)
    image_data['Content-Disposition'] = 'attachment;filename="2.jpg"'
    message.attach(image_data)
    msg=MIMEText('图片','html','utf-8')
    message.attach(msg)

message['Subject'] = '这是一封家书'
# 发送人
message['from'] = sender
# 收件人
message['to'] = ';'.join(receive)
# 抄送
message['Cc']= ';'.join(cs)

con.sendmail(sender, receive+cs, message.as_string())