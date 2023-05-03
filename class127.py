# https://exoplanets.nasa.gov/exoplanet-catalog/
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
import time
import csv

start_url = 'https://exoplanets.nasa.gov/exoplanet-catalog/'
# browser = webdriver.Chrome("chromedriver.exe")
browser = webdriver.Edge("msedgedriver.exe")
browser.get(start_url)
time.sleep(10)

# print( selenium.__version__ ) 

def scrape():
    headers = ["name", "light_years_from_earth",'planet_mass','stellar_magnitude','discovery_date']
    planet_data = []
    for i in range(214):
        soup = BeautifulSoup(browser.page_source, 'html.parser')
        for ul in soup.find_all('ul', attrs={'class','exoplanet'}):
            li = ul.find_all("li")
            temp_list = []
            for index , li_tag in enumerate(li):
                if index == 0:
                    temp_list.append(li_tag.find_all('a')[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except: 
                        temp_list.append('')
            planet_data.append(temp_list)
        browser.find_element('xpath','//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()  
    with open('class127output.csv','w' ,encoding='utf8') as f:
        data = csv.writer(f)
        data.writerow(headers)
        data.writerows(planet_data)             

scrape()


'''
AttributeError: 'WebDriver' object has no attribute 'find_element_by_xpath'
'''




