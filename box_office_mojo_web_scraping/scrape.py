import os
import sys
import requests
from requests_html import HTML
import pandas as pd
import datetime

BASE_DIR = os.path.dirname(__file__)


def url_to_text(url, filepath="box_office_mojo_web_scraping/word.html", save=False):
    r = requests.get(url)
    if r.status_code == 200:
        html_txt = r.text
        if save:
            with open(filepath, 'w') as f:
                f.write(html_txt)
        return html_txt
    return None


def parse_and_extract(url, name="2017"):
    r_url = url_to_text(url)
    if r_url == None:
        return False
    r_html = HTML(html=r_url)
    # print(r_html)
    table_class = '.imdb-scroll-table'
    r_table = r_html.find(table_class)
    table_data = []
    if len(r_table) == 0:
        return False
    parsed_table = r_table[0]
    rows = parsed_table.find("tr")
    header_rows = rows[0]
    header_cols = header_rows.find("th")
    header_name = [x.text for x in header_cols]
    for row in rows[1:]:
        cols = row.find("td")
        col_data = []
        for i, col in enumerate(cols):
            col_data.append(col.text)
            table_data.append(col_data)

    path = os.path.join(BASE_DIR, 'data')
    os.makedirs(path, exist_ok=True)
    file_path = os.path.join(path, f"{name}.csv")
    df = pd.DataFrame(table_data, columns=header_name)
    # Index use for serial no. Here already have serial no so index=False.
    df.to_csv(file_path, index=False)
    return True


def run(start_year=None, years_ago=0):
    if start_year == None:
        now = datetime.datetime.now()
        start_year = now.year
    assert isinstance(start_year, int)
    assert isinstance(years_ago, int)
    assert len(f"{start_year}") == 4
    for i in range(0, years_ago+1):
        url = f"https://www.boxofficemojo.com/year/world/{start_year}/"
        finished = parse_and_extract(url, name=start_year)
        if finished:
            print(f"Finished{start_year}")
        else:
            print(f"Not finished {start_year}")
        start_year -= 1


if __name__ == "__main__":
    try:
        start = int(sys.argv[1])
    except:
        start = None
    try:
        count = int(sys.argv[2])
    except:
        count = 0
    run(start_year=start, years_ago=count)
