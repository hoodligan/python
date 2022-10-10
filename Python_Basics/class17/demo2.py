# 发送html测试报告给到相关测试人员

import smtplib
from email.mime.text import MIMEText

con=smtplib.SMTP_SSL('smtp.qq.com',465)
con.login(user='2804555260@qq.com',password='hhrotgwljdmqdfhh')

# 发送者账号
sender='2804555260@qq.com'
# 接受者账号
receive=['2804555260@qq.com','1106614821@qq.com']


# 发送html文件里面的内容 读取出来
with open(r'./files/2020-11-16 21-15-18test_report.html','rb')as f:
    htmlContent=f.read()
    message=MIMEText(str(htmlContent,encoding='utf-8'),'html','utf-8')

message['Subject']='发送给小幸运的一封信'
# 发送人
message['from']=sender
# 收件人
# message['to']=receive
message['to']=';'.join(receive)

con.sendmail(sender,receive,message.as_string())

# html这个附件怎么发送出去