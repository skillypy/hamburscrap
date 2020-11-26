import requests
from bs4 import BeautifulSoup
import csv

key = 'hotel'
location = 'london'
url = 'https://www.yell.com/ucs/UcsSearchAction.do?scrambleSeed=1662503310&keywords={}&location={}&pageNum='.format(key, location)

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
}

req = requests.get(url, headers=headers)
soup = BeautifulSoup(req.text, 'html5lib')
items = soup.find_all('div', 'row businessCapsule--mainRow')
for itm in items:
    name = itm.find('span', 'businessCapsule--name').text  # class bs lgsung di tulis 'businessCapsule--name'
    address = ''.join(itm.find('span', {'itemprop': 'address'}).text.strip().split('\n'))  # selain class hrs di tulis {'itemprop' : 'address'}
    try: web = itm.find('a', {'rel': 'nofollow noopener'})['href'].replace('http://', '').replace('https://', '').replace('www.', '').split('/')[0]
    except: web = ''
    print(web)
