# 安装：pip install zmail

import zmail
# subject 标题
# Content_text：邮件文本内容
# Content_html:发送html格式内容
# Attachments:附件

# 发送人
sender={'username':'2804555260@qq.com','password':'hhrotgwljdmqdfhh'}
# 登录邮箱
server=zmail.server(sender['username'],sender['password'])

# 邮件内容
mail_content={
    'subject':'我是标题',
    'Content_text':'我是邮件内容http://www.baidu.com',
    # 'Content_html':'<a href="http://www.baidu.com">嗨，你好</a>',
    'Attachments':'./files/a.docx'
}

# 收件人
receive=['1418404585@qq.com','7845684@qq.com','2804555260@qq.com']
# 发送邮件
server.send_mail(receive,mail_content,cc=['964197460@qq.com'])

# 注意：
# Content_text和Content_html只能选择一个使用