import smtplib, ssl
from info import info

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = info.sender_email
receiver_email = info.receiver_email
password = info.password
message = """\
Subject: Indoor|Outdoor: Someone is waiting at your door.

Creature detected! Please check."""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.starttls(context=context)
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
