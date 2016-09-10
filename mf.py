import pandas as pd
from bs4 import BeautifulSoup
import requests
import re

# mutual fund class
class MutualFund():
    def __init__(self, code):
        self.schemecode = code # integer
        self.name = 'untitled'
        self.rating = 0
        self.amc = 'unknown'
        self.growth_nav = 0.0
        self.dividend_nav = 0.0
        self.navhistory = pd.DataFrame()  # time series df
        self.category = ''
        self.asset_value = 0
        self.expense_ratio = 0

    def get_values(self):
        url = self.get_snapshot_url()
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "lxml")

        self.name = soup.findAll("span", {"class": "fundname_rating_sep"})[0].string
        self.rating = int(soup.findAll("span", {"itemprop": "rating"})[0].string)
        self.category = soup.find_all("td", string=re.compile("Category:"))[0].parent.find_all('td')[1].string
        self.amc = soup.find_all("td", string=re.compile("Fund House:"))[0].parent.find_all('td')[1].a.string
        self.growth_nav = float(soup.find_all(string=re.compile("Growth:"))[0].parent.text.split()[-1])
        self.dividend_nav = float(soup.find_all(string=re.compile("Dividend:"))[0].parent.text.split()[-1])
        self.asset_value = float(re.sub(",", "", soup.find_all("td", string=re.compile("Assets:"))[0].parent.find_all('td')[1].text.split()[1]))
        self.expense_ratio = float(soup.find_all("td", string=re.compile("Expense:"))[0].parent.find_all("td")[1].string.split()[0][:-1])


    def get_snapshot_url(self):
        return '''https://www.valueresearchonline.com/funds/newsnapshot.asp?schemecode=''' + int(self.schemecode)

