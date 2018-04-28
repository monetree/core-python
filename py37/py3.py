'''
host = gmail's smtp server(simple mail transfer server)
port = 587
'''
#https://myaccount.google.com/lesssecureapps
#sending emails using python
import smtplib
from email.mime.text import MIMEText
body = '''This is my message body. I wish you all the best in your
love life. have a nice day.'''
msg = MIMEText(body)
msg['From'] = 'soubhagyakumar666@gmail.com'
msg['To'] = 'linux619ubuntu@gmail.com;dgamemaker@gmail.com'
msg['Subject'] = 'BEST VALENTINE WISHES'
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('soubhagyakumar666@gmail.com',"SOubh@gy@519")
server.send_message(msg)
server.quit()
print('mail sent...')