import requests
from bs4 import BeautifulSoup

url = 'https://www.valueresearchonline.com/funds/newsnapshot.asp?schemecode=15688'


schemecode='15688'


snapshot_url = 'https://www.valueresearchonline.com/funds/newsnapshot.asp?schemecode='
performance_url = 'https://www.valueresearchonline.com/funds/fundperformance.asp?schemecode='


url = snapshot_url + schemecode

r = requests.get(url)

soup = BeautifulSoup(r.text, 'lxml')

