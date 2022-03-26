import csv
from http import server
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

email_user = "DummyMail17751@gmail.com"
password = "DummyMail@123"
subject = "Your account is Activated"

recipient = input("Enter email id ")

with open('C:\Study\Internship_Source_Catalyst\Customised Auto Mail Generation\Details.csv','r') as csvfile:
    reader=csv.reader(csvfile)
    for line  in reader:
        text="Hello "+line[1]+" your "+line[2]+" account is now activated."
        email_send=line[0]
        msg = MIMEMultipart()
        msg['FROM'] = email_user
        msg['TO'] = email_send
        email_send = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(text,"plain"))
        text = msg.as_string()

        server=smtplib.SMTP_SSL("smtp.gmail.com",465)
        server.login(email_user,password)
        server.sendmail(email_user,email_send,text)

        server.quit()
