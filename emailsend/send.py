import sys
import requests
from formatting import format_msg
from send_mail import send_mail


def send(my_name, my_website=None, verbose=False, to_email=None):
    assert to_email != None
    if my_website != None:
        msg = format_msg(my_name=my_name, my_website=my_website)
    else:
        msg = format_msg(my_name=my_name)
    return msg
    if verbose:
        print(my_name, my_website, to_email, html=None)
    send_mail(text=msg, to_emails=[to_email])


if __name__ == "__main__":
    print(sys.argv)
    name = "Unknown"
    if len(sys.argv) > 1:
        name = sys.argv[1]
    email = None
    if len(sys.argv) > 2:
        email = sys.argv[2]
    r = send(name, to_email=email, verbose=True)
    print(r)
