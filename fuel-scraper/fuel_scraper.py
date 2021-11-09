from bs4 import BeautifulSoup
import urllib.request
import re
import requests


def get_price_details():
    fp = requests.get(
        "https://www.arboe.at/leistungen/spritpreis-und-e-tankstellenfinder/spritpreise-oesterreich/?")

    # https://www.arboe.at/leistungen/spritpreis-und-e-tankstellenfinder/spritpreise-oesterreich/?
    # https://sprit.club/de/l/Graz?type=DIE
    soup = BeautifulSoup(fp.content, 'html.parser')
    soupString = str(soup)

    # test print
    with open("soup.txt", 'w') as f:
        f.writelines(soupString)

    gasstation = re.findall(r'"name": "(.*?)"', soupString)
    price = re.findall(r'"D": "(.*?)"', soupString)
    address = re.findall(r'"strasse": "(.*?)"', soupString)
    city = re.findall(r'"city": "(.*?)"', soupString)

    # print(gasstation)
    # print(price)
    # print(address)
    # print(city)

    for i in range(len(city)):
        if city[i] == "Graz" and price[i] != "0":
            print(gasstation[i], ",", price[i],
                  ",", city[i], ",", address[i], ",", city[i])


get_price_details()
