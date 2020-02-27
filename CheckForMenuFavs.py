import urllib
from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
from datetime import datetime
import os
from os.path import isfile, join
import csv
import shutil
import sqlite3

#test on school computer

def get_menu_items():
    menu_url = "https://dining.humboldt.edu/j-menu"
    response = urllib.request.urlopen(menu_url)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")

    name_box = soup.find('div', attrs={'class' : 'food-menu-dropdown'})
    name = name_box.text.strip()


favorites = ["Belgian Waffles", "Pasta Bar", "Baklava", "Cheesy Potatoes", "Veggie Omelet", "Beef Barbocoa"]

def favorite_alert():
    print("Favorites available today: ")
    for fav in favorites:
        if fav in name:
            print(fav)
    

if __name__ == '__main__':
    get_menu_items()
    favorite_alert()