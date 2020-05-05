import requests
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_dir = os.path.join(BASE_DIR, "template", "downloads")

os.makedirs(file_dir, exist_ok=True)

download_dir = os.path.join(file_dir, 'image2.jpg')
url = "https://cdn.pixabay.com/photo/2015/12/01/20/28/road-1072823__340.jpg"


reserved = requests.get(url)
reserved.raise_for_status()

with open(download_dir, 'wb') as file:
    write_file = file.write(reserved.content)
    print(write_file)
