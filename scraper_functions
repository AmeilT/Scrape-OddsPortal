

#import libraries
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']



def scrape_table(url):
    options = Options()
    options.headless = True
    options.add_argument('window-size=1920x1080')  # Headless = True

    web = url
    path = '/Users/ameil/chromedriver'  # introduce your file's path inside '...'

    # execute chromedriver with edited options
    driver = webdriver.Chrome(path, options=options)
    driver.get(web)

    tbl = driver.find_element_by_xpath("//*[@id='tournamentTable']").get_attribute('outerHTML')
    df_list = pd.read_html(tbl)
    table = df_list[0]
    table = table.stack(level=0).reset_index(level=-1)
    table.rename(columns={"1": "Home", "X": "Draw", "2": "Away"}, inplace=True)

    return table


def fixtures_split_home(x):
    home = x.split("-")[0]
    return home


def fixtures_split_away(x):
    away = x.split("-")[1]
    return away


def convert_fraction_to_decimal_odds(x):
    num = float(x.split("/")[0])
    denom = float(x.split("/")[1])
    decimal = (num + denom) / denom
    return decimal


def format_table(table, url):
    options = Options()
    options.headless = True
    options.add_argument('window-size=1920x1080')  # Headless = True
    path = '/Users/ameil/chromedriver'  # introduce your file's path inside '...'
    driver = webdriver.Chrome(path, options=options)
    driver.get(url)
    dates_xpath = driver.find_elements_by_xpath("//*[contains(@class, 'datet')]")
    dates = [y.text for y in dates_xpath]
    datelist = []

    for i in range(0, len(table)):
        try:
            month = dates[i].split()[1]
            date = dates[i]
        except:
            pass

        if month in months:
            datelist.append(date)
        else:
            datelist.append(date)

    table["Date"] = datelist
    table.drop(["level_1", "B's"], axis=1, inplace=True)
    table.drop(table[table["Draw"] == "X"].index, inplace=True)

    renamed_columns = []

    for x in list(table.columns):
        if any(s in x for s in months):
            renamed_columns.append(x)

    renamed_columns.sort()
    renamed_columns

    table = table.rename(
        columns={renamed_columns[0]: "Time", renamed_columns[1]: "Fixture", renamed_columns[2]: "Score"})

    table["Home Team"] = table["Fixture"].apply(fixtures_split_home)
    table["Away Team"] = table["Fixture"].apply(fixtures_split_away)

    table["Home Odds"] = table["Home"].apply(convert_fraction_to_decimal_odds)
    table["Away Odds"] = table["Away"].apply(convert_fraction_to_decimal_odds)

    return table

def concat_tables(table1,table2):
    table=table1.append(table2)
    return table

