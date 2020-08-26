import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class SendMail():
    def __init__(self):
        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.starttls()
        s.login('assignmentupgrad@gmail.com', 'Upgrad@123')

        msg = MIMEMultipart()
        message = '''
Hi, here is the list of the restaurants you searched for:
1. I dont know what to show here
2. I dont know what to show here
3. I dont know what to show here
4. I dont know what to show here
5. I dont know what to show here

Enjoy fooding :)

This is an auto generated email. Please dont reply to this email.
        '''

        msg['From'] = 'assignmentupgrad@gmail.com'
        msg['To'] = 'goyal1992.vibhor@gmail.com'
        msg['Subject'] = "Foodie - Restaurant search"

        msg.attach(MIMEText(message, 'plain'))

        s.send_message(msg)
        print('sent')
        del msg


send_mail = SendMail()
