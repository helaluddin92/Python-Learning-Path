from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import config
import smtplib


message = MIMEMultipart()
message["from"] = "Md. Helal Uddin"
message["to"] = 'contact.helaluddin@gmail.com'
message["subject"] = "Test Message"


template = Template(Path('sendemail/html/index.html').read_text())
body = template.substitute({"name": "John", "user": "Helal"})

message.attach(MIMEText(body, "html"))
message.attach(MIMEImage(Path('sendemail/me.jpg').read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(config.userlogin, config.userpassword)
    smtp.send_message(message)
    print("Sent..")
