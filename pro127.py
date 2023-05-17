from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

SU = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("\Users\91939\Python\projects")
browser.get(SU)
time.sleep(10)

def scrape():
    headers = ["Name", "Distance", "Mass", "Radius"]
    star_data = []
    for i in range(0,15):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for ul_tag in soup.find_all("th", attrs={"Name","Mass"}):
            li_tags = ul_tag.find_all("tr")
            temp_list = []
            for index, li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tags.contents[0])
                    except:
                        temp_list.append("")
            star_data.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("scraper_127.csv","w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(star_data)

scrape()