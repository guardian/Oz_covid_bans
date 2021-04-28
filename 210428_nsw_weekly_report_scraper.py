import pandas as pd
import os 
from bs4 import BeautifulSoup as bs 
import requests

data_path = os.path.dirname(__file__) + "/data/210428_nsw_epidemiology_reports/"

## Scrape Recent

link = 'https://www.health.nsw.gov.au/Infectious/covid-19/Pages/weekly-reports.aspx'

chunk_size = 2000

r = requests.get(link)
soup = bs(r.text, 'html.parser')
container = soup.find("div", class_="ms-rtestate-field")
lis = container.find_all("li")
for thing in lis:
    try:
        print("one")
        if ".pdf" in thing.a['href'] and "Epidemiological week" in thing.text:
            linko = 'https://www.health.nsw.gov.au' + thing.a['href']
            pdf_r = requests.get(linko, stream=True)
            split = linko.split("/")[-1]
            with open(f"{data_path}{split}", "wb") as f:
                for chunk in pdf_r.iter_content(chunk_size):
                    f.write(chunk)
    except Exception as e:
        print(e)
        continue



## ARCHIVE SCRAPE

# link = 'https://www.health.nsw.gov.au/Infectious/covid-19/Pages/weekly-reports-archive.aspx'

# chunk_size = 2000

# r = requests.get(link)
# soup = bs(r.text, 'html.parser')
# container = soup.find("div", class_="ms-rtestate-field")
# lis = container.find_all("li")
# for thing in lis:
#     linko = 'https://www.health.nsw.gov.au' + thing.a['href']
#     if ".pdf" in linko:
#         pdf_r = requests.get(linko, stream=True)
#         print(linko)
#         split = linko.split("/")[-1]
#         print(split)
#         with open(f"{data_path}{split}", "wb") as f:
#             # f.write_bytes(r.content)
#             for chunk in pdf_r.iter_content(chunk_size):
#                 f.write(chunk)
    

