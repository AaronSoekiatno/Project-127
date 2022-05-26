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
    headers = ["Name", "Distance", "Mass", "Radius"]
    stars_data = []
    for i in range(0, 1):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for ul_tag in soup.find_all("ul", attrs={"class", "Proper name"}):
            li_tags = ul_tag.find_all("li")
            temp_list = []
            for index, li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
            stars_data.append(temp_list)
        #browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("scrapper.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(stars_data)
scrape()