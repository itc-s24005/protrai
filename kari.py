# s24005
# 沖縄県の推計人口のページより最新情報をスクレイピングするPythonコード
# https://www.pref.okinawa.jp/toukeika/estimates/estimates_suikei.html

import requests
from bs4 import BeautifulSoup

uri = 'https://www.pref.okinawa.jp/toukeika/estimates/estimates_suikei.html'
html = requests.get(uri)

soup = BeautifulSoup(html.text, 'html.parser')
jinkou = soup.find('table', class_="table1 font2 gyo5")

for element in jinkou.find_all('td'):
    print(element['align'])
