import imaplib
import email
import config

host = "imap.gmail.com"
username = config.username
password = config.password

mail = imaplib.IMAP4_SSL(host)
mail.login(username, password)
mail.select("inbox")

_, search_data = mail.search(None, "ALL")

for num in search_data[0].split():
    # print(num, end=",")
    _, data = mail.fetch(num, '(RFC822)')
    # print(data[0])
    _, b = data[0]
    email_message = email.message_from_bytes(b)
    # raw_email = b.decode('utf-8')
    # email_message = email.message_from_string(raw_email)
    # print(email_message)
    for header in ["subject", "to", "from", "date"]:
        print(f"{header}: {email_message[header]}")
    for part in email_message.walk():
        if part.get_content_type() == "text/plain":
            body = part.get_payload(decode=True)
            print(body)

