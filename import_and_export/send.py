import sys
import requests
from formatting import format_msg


def send(my_name, my_website=None, verbose=False):
    if my_website != None:
        msg = format_msg(my_name=my_name, my_website=my_website)
    else:
        msg = format_msg(my_name=my_name)
    return msg
    if verbose:
        print(my_name, my_website)
    response = requests.get("http://httpbin.org/json")
    if response.status_code == 200:
        return response.json()
    else:
        return "There is an error"


if __name__ == "__main__":
    print(sys.argv)
    name = "Unknown"
    if len(sys.argv) > 1:
        name = sys.argv[1]
        r = send(name, verbose=True)
        print(r)
