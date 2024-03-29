import requests
from bs4 import BeautifulSoup
import json


def keysearch(key):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)  AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}

    url = 'https://kith.com/sitemap_products_1.xml?from=135297231&to=2057600008261'

    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, 'html.parser')

    mylist = []
    global mylists
    mylists = mylist
    for items in soup.find_all("url"):
        item = items.find("image:title")
        if item is not None:
            title = item.text
            url = items.find("loc").text
            time = items.find("lastmod").text
            if keyword.lower() in title.lower():
                print(title, url)
                mylist.append(title)
                purl = ('{}.json'.format(url))
                r2 = requests.get(url=purl, headers=headers)
                data = json.loads(r2.content)
                for proditems in data['product']['variants']:
                    variant = proditems['id']
                    size = proditems['title']
                    link = 'https://www.kith.com/cart/{}:1'.format(variant)
                    print('     ',size,'ATC:',link)
                print()
            else:
                if keyword.lower() in url.lower():
                    mylist.append(url)
                    print('Not in Item Name, but Found {}'.format(url))
        if item is None:
            url2 = items.find("loc").text
            if keyword.lower() in url2.lower():
                    mylist.append(url2)
                    print('Not in Item Name, but Found {}'.format(url2))


while True:
    keyword = input('Enter Keyword, Then Please press Enter:').lower()
    if keyword == "":
        print('END')
        break
    keysearch(keyword)
    if len(mylists) == 0:
        print('No Keywords {}'.format(keyword).title())
        print()
