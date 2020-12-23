from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import requests
import time

#driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get('https://geo.craigslist.org/iso/us/CA')
cityPage = requests.get('https://geo.craigslist.org/iso/us/CA').text


def pull_links():
    # made new soup obj
    soup = BeautifulSoup(cityPage, 'lxml')
    # obj for the class containing our list items
    cities = soup.find('ul', class_="height6 geo-site-list")

    city_hyperlink = cities.find_all('li')
    for city in city_hyperlink:
        print(city.a['href'])

    print(city_hyperlink)

if __name__ == '__main__':
    pull_links()
