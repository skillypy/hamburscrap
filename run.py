import requests
from bs4 import BeautifulSoup
import csv

key = 'hotel'
location = 'london'
url = 'https://www.yell.com/ucs/UcsSearchAction.do?scrambleSeed=1662503310&keywords={}&location={}&pageNum='.format(key, location)

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
}

datas = []
count_page = 0
for page in range(1, 5):
    count_page+=1
    print('scraping page', count_page)
    req = requests.get(url+str(page), headers=headers)
    soup = BeautifulSoup(req.text, 'html5lib')
    items = soup.find_all('div', 'row businessCapsule--mainRow')
    for itm in items:
        name = itm.find('span', 'businessCapsule--name').text  # class bs lgsung di tulis 'businessCapsule--name'
        address = ''.join(itm.find('span', {'itemprop': 'address'}).text.strip().split('\n'))  # selain class hrs di tulis {'itemprop' : 'address'}
        try: web = itm.find('a', {'rel': 'nofollow noopener'})['href'].replace('http://', '').replace('https://', '').replace('www.', '').split('/')[0]
        except: web = ''
        try: telp = itm.find('span', 'business--telephoneNumber').text
        except: telp = ''
        pic = itm.find('div', 'col-sm-4 col-md-4 col-lg-5 businessCapsule--leftSide').find('img')["data-original"]
        if 'http' not in pic :
            pic = 'https://yell.com{}'.format(pic)
        datas.append([name, address, web, telp, pic])


csvheader = ['Name','Address','Website','Phone Number','Image URL']
writer = csv.writer(open('results/{}_{}.csv'.format(key, location), 'w', newline=''))
writer.writerow(csvheader)
for d in datas:
    writer.writerow(d)