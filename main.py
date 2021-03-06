from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
from scraper_functions import *



seasons=[]
for i in range(0,18):
    a=2020-i
    b=2021-i
    c=f"{a}-{b}"
    seasons.append(c)

for season in seasons:
    table=pd.DataFrame()
    for i in range(1,9):
        url=f"https://www.oddsportal.com/soccer/england/premier-league-2020-2021/results/2/#/page/{i}/"
        new_table=scrape_table(url)
        new_table=format_table(new_table,url)
        table=concat_tables(table,new_table)
        print(f"Scraped {season}")
        table.to_csv(f"PL Odds {season}")
        print(f"Finished {season}")

