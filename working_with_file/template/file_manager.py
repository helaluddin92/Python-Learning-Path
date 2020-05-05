import os
from download_util import download_files

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_dir = os.path.join(BASE_DIR, 'downloads')


download_file = os.path.join(file_dir)

os.makedirs(file_dir, exist_ok=True)

url = 'https://cdn.pixabay.com/photo/2015/06/19/21/24/the-road-815297__340.jpg'


# file_url = os.path.basename(url)
# new_file_dir = os.path.join(download_file, file_url)
# with requests.get(url, stream=True) as reserve:
#     with open(new_file_dir, 'wb') as myfile:
#         shutil.copyfileobj(reserve.raw, myfile)

download = download_files(url, download_file)
