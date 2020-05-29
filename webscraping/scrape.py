import requests
from requests_html import HTML
import pandas as pd
import datetime

now = datetime.datetime.now()
year = now.year


def url_to_text(url, filepath="webscraping/word.html", save=False):
    r = requests.get(url)
    if r.status_code == 200:
        html_text = r.text
        if save:
            with open(f"webscraping/word-{year}.html", 'w') as f:
                f.write(html_text)
        return html_text
    return ""


url = "https://www.boxofficemojo.com/year/world/"
r_url = url_to_text(url)
r_html = HTML(html=r_url)
table_class = ".imdb-scroll-table"
r_table = r_html.find(table_class)
# print(r_table)
table_data = []
header_name = []
if len(r_table) > 0:
    # print(r_table[0].text)
    parsed_table = r_table[0]
    rows = parsed_table.find("tr")
    header_rows = rows[0]
    header_cols = header_rows.find("th")
    header_names = [x.text for x in header_cols]
    table_data = []
    for row in rows[1:]:
        # print(row.text)
        cols = row.find("td")
        row_data = []
        for i, col in enumerate(cols):
            # print(i, col.text, '\n\n')
            row_data.append(col.text)
        table_data.append(row_data)


print(header_names)
print(table_data)

# df = pd.DataFrame(table_data, columns=header_names)
# df.to_csv('webscraping/movies.csv', index=False)
