import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import requests
import time

# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get('https://geo.craigslist.org/iso/us/CA')


def get_cities():
    cityPage = requests.get('https://geo.craigslist.org/iso/us').text
    soup = BeautifulSoup(cityPage, 'lxml')
    locations = soup.find('ul', class_="height6 geo-site-list")
    locations = locations.find_all('li')
    for location in locations:
        print(location.a['href'])


if __name__ == '__main__':
    get_cities()






 carforsale = requests.get(city.a['href'])
        souptwo = BeautifulSoup(carforsale, 'lxml')
        print(souptwo.find('li', class_="cta"))
