# s24005
# 沖縄県の推計人口のページより最新情報をスクレイピングするPythonコード
# https://www.pref.okinawa.jp/toukeika/estimates/estimates_suikei.html

import requests
from bs4 import BeautifulSoup

uri = 'https://www.pref.okinawa.jp/toukeika/estimates/estimates_suikei.html'
html = requests.get(uri)

# 文字コードをにShift_JISエンコーディング
html.encoding = 'Shift_JIS'

# print(html.text)

soup = BeautifulSoup(html.text, 'html.parser')
print(soup.find("title").stiring)
jinkou = soup.find('td', align_='right')
print(soup.find(jinkou).string)
