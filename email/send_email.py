from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import smtplib

from setting.connect_setting import get_email_setting

email_setting = get_email_setting()

#建立MIMEMultipart物件
email_content = MIMEMultipart()  

#郵件標題
email_content["subject"] = "Learn Code With Mike"  

#寄件者
email_content["from"] = email_setting['sender']

#收件者
email_content["to"] = email_setting['receiver']

#郵件內容
email_content.attach(MIMEText("Demo python send email"))

#設定SMTP伺服器
with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  
    try:
        #驗證SMTP伺服器
        smtp.ehlo()  

        #建立加密傳輸
        smtp.starttls()

        #登入寄件者gmail
        smtp.login(email_setting['sender'], email_setting['sender_password'])  

        #寄送郵件
        smtp.send_message(email_content) 
        print("Send email Complete!")

    except Exception as e:
        print("Error message: ", e)