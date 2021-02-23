import rpa as r
import pyautogui as p
import smtplib
import pandas as pd
import psutil
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

process_tee = "tee.exe"

for proc in psutil.process_iter():
    if proc.name() == process_tee:
        proc.kill()


r.init()
r.url('https://www.melhorcambio.com/dolar-hoje')
p.sleep(3)
window = p.getActiveWindow().maximize()
commercial_dollar = r.read('//*[@id="comercial"]')
p.sleep(3)
p.hotkey('ALT', 'F4')

email_text = 'Hello, \n     Today, ' + str(pd.Timestamp('today')) + '...the value of the commercial dollar is R$: {}'.format(commercial_dollar)

by_me = '' ##who will send the email
password = '' #password
to = '' #who will receive the email

message = MIMEMultipart()
message['From'] = by_me
message['To'] = to
message['Subject'] = 'Dollar quote'
message.attach(MIMEText(email_text, 'plain'))

session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login(by_me, password)
email_text = message.as_string()
session.sendmail(by_me, to, email_text)
session.quit()




