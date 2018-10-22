import urllib
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

import ssl

def daily_thought():
    url = 'https://www.brainyquote.com/quote_of_the_day'

    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)  # ssl ceritificate verification
    # page = urlopen(req, context=gcontext)
    page = urlopen(req)
    # page = urlopen(req).read()
    # webpage = page.decode('utf-8')
    soup = BeautifulSoup(page, 'html.parser')
    quoted_image = soup.find('img', attrs={'id': 'qimage_129207'})

    quote = soup.find('img', attrs={'class': 'p-qotd'})
    quote_text = quote['alt']
    quote_img = quote['data-img-url']

    fw = open('template.txt', 'w')
    fw.write(quote_text)
    fw.close


    req1 = Request('https://www.brainyquote.com' + quote_img, headers={'User-Agent': 'Mozilla/5.0'})
    resource = urlopen(req1)
    output = open("quote-of-the-day.jpg","wb")
    output.write(resource.read())
    output.close()

    print(quote_text)
    print(quote_img)
    print('today\'s thought captured')


# alternate script for scraping
# import requests
# URL = "https://www.geeksforgeeks.org/data-structures/"
# r = requests.get(URL)
# print(r.content)
if __name__=='__main__':
    daily_thought()
