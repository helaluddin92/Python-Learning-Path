import requests
from requests_html import HTML
import os
import pandas as pd
import datetime


today = datetime.date.today()

ABS_FILE = os.path.abspath(__file__)
FILE_DIR = os.path.dirname(ABS_FILE)
FILE_PATH = os.path.join(FILE_DIR, "DataFile")
os.makedirs(FILE_PATH, exist_ok=True)
listdir = os.listdir(FILE_PATH)
count = len(listdir)
file_name = f"{today}-{count+1}"
file_path = os.path.join(FILE_PATH, f"{file_name}.csv")


def covid_19(url, filepath=FILE_PATH, save=False):
    r = requests.get(url)
    if r.status_code == 200:
        html_text = r.text
        if save:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(html_text)
        return html_text
    return ""


def parsed_and_extract(url, filesave=file_path):
    txt_html = covid_19(url)
    r_html = HTML(html=txt_html)
    table_id = "#main_table_countries_today"
    r_table = r_html.find(table_id)
    parsed_table = r_table[0]
    rows = parsed_table.find("tr")
    table_data = []
    head_data = []
    for row in rows:
        cols = row.find("td")
        heads = row.find("th")
        find_cols = []
        for head in heads:
            head_data.append(head.text)
        for col in cols:
            find_cols.append(col.text)
        table_data.append(find_cols)
    # print(table_data)
    # if os.path.exists(file_path):
    df = pd.DataFrame(table_data, columns=head_data)
    df.to_csv(file_path, index=False)


url = "https://www.worldometers.info/coronavirus/"

if __name__ == "__main__":
    finished = parsed_and_extract(url)
    if not finished:
        print(f"{today}.csv file saved")
    else:
        print(f"{today}.csv file not saved")
