import requests
from bs4 import BeautifulSoup
from random import choice
from fake_useragent import UserAgent
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
ua=UserAgent();
hdr = {'User-Agent': ua.random,
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
      'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
      'Accept-Encoding': 'none',
      'Accept-Language': 'en-US,en;q=0.8',
      'Connection': 'keep-alive'}

def get_proxy():
    url = "https://www.sslproxies.org"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')
    proxy = {'https' : choice(list(map(lambda x:x[0]+':' + x[1], list(zip(map(lambda x:x.text, soup.find_all('td')[::8]),
                                                                          map(lambda x:x.text, soup.find_all('td')[1::8]))))))}
    return proxy


def proxy_req(req_type, url, **kwargs):
    while True:
        try:
            proxy = get_proxy()
            print('using proxy ', proxy)
            r = requests.request(req_type, url, proxies=proxy, timeout=7,headers=hdr, **kwargs)
            break
        except:
            pass
    return r


r = proxy_req('get', 'https://www.similarweb.com/website/youtube.com')
soup = BeautifulSoup(r.content, 'html5lib')
print(soup)
anchors = soup.find_all('a')
print(anchors)
my_href = ''
for i in anchors:
    print(i)
    if str(i['class']) == 'websiteRanks-nameText':
        my_href = str(i.text)
        break
print(my_href, 'my href')