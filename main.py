import smtplib

from django.dispatch import receiver
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
email="jameswanjala1998@gmail.com"
password="jemo1999"
server.login(email,password)
sender_email=email
receiver_email="jamesbengi21@gmail.com"
message="whats up big boy"
server.sendmail(sender_email,receiver_email,message)