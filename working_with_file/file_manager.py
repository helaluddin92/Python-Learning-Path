import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

file_dir = os.path.join(BASE_DIR, 'template', 'textfile')
os.makedirs(file_dir, exist_ok=True)
for i in range(0, 12):
    fname = f"{i}.txt"
    file_path = os.path.join(file_dir, fname)
    if os.path.exists(file_path):
        print(f"Skipped{fname}")
        continue
    with open(file_path, 'w') as file:
        write_file = file.write("Hello World")
        print(write_file)
