import os
import math

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_dir = os.path.join(BASE_DIR, 'textfile.txt')


class FileObj:
    def __init__(self, filepath):
        self.file = open(filepath, 'r+')

    def read_file(self):
        print(self.file.read().format(name="Helal", user="Myuser"))

    def __del__(self):
        self.file.close()
        del self.file


# myfile = FileObj(file_dir)
# print(myfile.__del__())
print(divmod(5, 2))

x = math.ceil(5.5)
print(x)
x = math.floor(5.5)
print(x)
