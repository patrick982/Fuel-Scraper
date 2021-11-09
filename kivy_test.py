from types import CoroutineType
from kivy.app import App
from kivy.uix.label import Label
from bs4 import BeautifulSoup
import urllib.request
import re
import requests


def get_price_details():
    fp = requests.get(
        "https://www.arboe.at/leistungen/spritpreis-und-e-tankstellenfinder/spritpreise-oesterreich/?")

    # sources
    # https://www.arboe.at/leistungen/spritpreis-und-e-tankstellenfinder/spritpreise-oesterreich/?
    # https://sprit.club/de/l/Graz?type=DIE

    soup = BeautifulSoup(fp.content, 'html.parser')
    soupString = str(soup)

    # test print
    # with open("soup.txt", 'w') as f:
    #    f.writelines(soupString)

    gasstation = re.findall(r'"name": "(.*?)"', soupString)
    price = re.findall(r'"D": "(.*?)"', soupString)
    address = re.findall(r'"strasse": "(.*?)"', soupString)
    city = re.findall(r'"city": "(.*?)"', soupString)

    # print(gasstation)
    # print(price)
    # print(address)
    # print(city)

    """
    for i in range(len(city)):
        if city[i] == "Graz" and price[i] != "0":
            print(gasstation[i], ",", price[i],
                  ",", city[i], ",", address[i], ",", city[i])
    """

    return gasstation, price, address, city


class MainApp(App):
    def build(self):

        gasstation, price, address, city = get_price_details()

        label1 = Label(text=gasstation[1] + " " + price[1] + " " + " " + address[1] + " " + city[1],
                       size_hint=(.5, .5),
                       pos_hint={'center_x': .5, 'center_y': .5})
        label2 = Label(text=str(price[1]),
                       size_hint=(.5, .5),
                       pos_hint={'center_x': .5, 'center_y': .5})
        label3 = Label(text=address[1],
                       size_hint=(.5, .5),
                       pos_hint={'center_x': .5, 'center_y': .5})
        label4 = Label(text=city[1],
                       size_hint=(.5, .5),
                       pos_hint={'center_x': .5, 'center_y': .5})

        return label1


if __name__ == '__main__':
    app = MainApp()
    app.run()
