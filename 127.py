"""from calendar import c
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("chromedriver.exe")
url = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
driver.get(url)

content = driver.page_source
soup = BeautifulSoup(content)
x = []

for ul_tag in soup.find_all("ul", attrs = {"class","exoplanet"}):
    li_tags = ul_tag.find_all("li")
    x.append(li_tags)
print(x)
"""
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("chromedriver.exe")
browser.get(START_URL)
time.sleep(10)
def scrape():
    headers = ["Magnitude","Name","Designation", "Distance","Spectral Class", "Mass", "Radius","Luminosity",]
    soup = BeautifulSoup(browser.page_source, "html.parser")
    data = soup.find('table')
    row_data = data.find_all('tr')
    temp_list = []
    names = []
    for tr in row_data:
        x = tr.find_all('td')
        row = [i.text.rstrip()for i in x]
        temp_list.append(row)
        print(temp_list)
    """"
    for i in range(0,len(temp_list)):
        names.append(temp_list[i][1])
    print(temp)
    """
    with open("scrapper_3.csv", "w",encoding = "utf-8") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(temp_list)
scrape()