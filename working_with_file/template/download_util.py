import os
import shutil
import requests


def download_files(url, directory, fname=None):
    if fname == None:
        fname = os.path.basename(url)
        new_file_dir = os.path.join(directory, fname)
        with requests.get(url, stream=True) as reserve:
            with open(new_file_dir, 'wb') as myfile:
                shutil.copyfileobj(reserve.raw, myfile)
    return new_file_dir
