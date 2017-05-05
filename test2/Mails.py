# -*-coding:UTF-8-*-
__author__ = 'CuiCan'

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 发件人
AUTO_MAIL = "monitor@evergrande.com"
# 收件人列表
MAIL_LIST = ["zhaopeng@evergrande.com", "cuican@evergrande.com"]

def SendStatMail(aSub, aHtml):
    re = False
    msg = MIMEMultipart('alternative', _charset='utf-8')
    msg['Subject'] = aSub.decode('utf-8')
    msg['From'] = AUTO_MAIL
    msg['To'] = ";".join(MAIL_LIST)
    part = MIMEText(aHtml, 'html', _charset='utf-8')
    msg.attach(part)

    # 设置服务器，用户名、口令以及邮箱后缀
    mail_host = "smtp.qiye.163.com"
    mail_user = "monitor@evergrande.com"
    mail_pass = "rJv772L2HaUQ"
    # mail_postfix = "evergrande.com"
    s = smtplib.SMTP()
    try:
        s.connect(mail_host, 25)
        s.login(mail_user, mail_pass)
        s.sendmail(AUTO_MAIL, MAIL_LIST, msg.as_string())
        re = True
    except Exception, e:
        print str(e)
    finally:
        s.close()
    return re
