import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import config


def send_mail(text="Email Body", subject="Hello World", from_email="Helal <getdailyrewards@gmail.com>", to_mails=None, html=None):
    assert isinstance(to_mails, list)  # Instance of list if not show error
    msg = MIMEMultipart('alternative')
    msg['from'] = from_email
    msg['to'] = ", ".join(to_mails)
    msg["subject"] = subject

    txt_part = MIMEText(text, "plain")
    msg.attach(txt_part)

    if html != None:
        html_part = MIMEText("<h1>This is working<h1>", "html")
        msg.attach(html_part)

    msg_str = msg.as_string()

# mylist = ["Helal", "123", "456"]
# lists = ", abc".join(mylist)
# print(lists)
# my_list = lists.split(',')
# print(my_list)

    # Login to my smtp server
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login(config.username, config.password)
    server.sendmail(from_email, to_mails, msg_str)
    server.quit()
    print("Message Sent")

    # with smtplib.SMTP(host="smtp.gmail.com", port=587) as server:
    #     pass
