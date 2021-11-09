from types import CoroutineType
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from bs4 import BeautifulSoup
from kivy.uix.layout import Layout
import kivy
import urllib.request
import re
import requests


def get_price_details():
    fp = requests.get(
        "https://www.arboe.at/leistungen/spritpreis-und-e-tankstellenfinder/spritpreise-oesterreich/?")

    soup = BeautifulSoup(fp.content, 'html.parser')
    soupString = str(soup)

    gasstation = re.findall(r'"name": "(.*?)"', soupString)
    price = re.findall(r'"D": "(.*?)"', soupString)
    address = re.findall(r'"strasse": "(.*?)"', soupString)
    city = re.findall(r'"city": "(.*?)"', soupString)

    return gasstation, price, address, city


class MainApp(App):
    def build(self):

        gasstation, price, address, city = get_price_details()

        layout = BoxLayout(padding=10)

        for i in range(len(city)):
            if city[i] == "Graz" and price[i] != "0":
                label = Label(text=gasstation[i] + " " + price[i] + " " + " " + address[i] + " " + city[i],
                              size_hint=(.5, .5), pos_hint={'center_x': .5, 'center_y': .5})

        layout.add_widget(label)

        return layout


if __name__ == '__main__':
    app = MainApp()
    app.run()
