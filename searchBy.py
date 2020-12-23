import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import requests
import time


# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get('https://geo.craigslist.org/iso/us/CA')
cityPage = requests.get('https://geo.craigslist.org/iso/us/CA').text

# city hyper link is a collection of all the cities


def city_links():
    soup = BeautifulSoup(cityPage, 'lxml')
    # obj for the class containing our list items
    cities = soup.find('ul', class_="height6 geo-site-list")
    # this is a list of elements, so you have to go thru each item in list and
    # apply a href tag cant apply to whole list
    city_hyperlink = cities.find_all('li')
    search_link(city_hyperlink)


# for each city, we made a new soup obj visiting url
def search_link(city_hyperlink):
    i = 0
    for city in city_hyperlink:
        so = requests.get(city.a['href']).text
        soupy = BeautifulSoup(so, 'lxml')
        car_col_class = soupy.find("ul", id="sss0")
        search = car_col_class.find(attrs={"data-cat": "cta"})
        print(search)
        print()
        print(i)
        i = i + 1


def get_vehichle_info():
    make = raw_input("Vehichle make")
    model = raw_input("Model")
    min_year = raw_input("Min year")
    max_year = raw_input("Max year")
    odo = raw_input("odometer limit")
    get_paint_colors = input("Enter acceptable colors separated by space")
    paint_colors = paint_colors.split()
    color options = ["black, blue, brown, green, grey, "]

    transmission
    while (transmission != "auto" | | transmission != "manual" | | transmission != "both"):
        Print("Choose a transmission")
        transmission = input("auto , manual, or both")


def post_to_form():


def
if __name__ == '__main__':
    get_vehichle_info()
    city_links()
