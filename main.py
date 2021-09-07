# scraper.py
import requests
from bs4 import BeautifulSoup

url = 'https://www.omskinform.ru/all'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

thead = soup.find_all('a', class_='n_cap_lnk')
tbody = soup.find_all('a', class_='n_text_lnk2')
for i in range(0, len(thead)):
    print(thead[i].text, end='')
    print(tbody[i].text)

def link_finder():
    global b
    soup.append('td')
    for a in soup.find_all('a', href=True):
        b = a['href']
        if 'https://www.omskinform.ru/all' in b:
            print(b)
    return b
