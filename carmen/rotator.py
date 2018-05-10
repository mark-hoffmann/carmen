from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import random


class ProxyRotator:

    def __init__(self):
        self.proxies = []


    def get_proxies(self):

        ua = UserAgent() # From here we generate a random user agent
        proxies = [] # Will contain proxies [ip, port]

        # Retrieve latest proxies
        proxies_req = Request('https://www.sslproxies.org/')
        proxies_req.add_header('User-Agent', ua.random)
        proxies_doc = urlopen(proxies_req).read().decode('utf8')

        soup = BeautifulSoup(proxies_doc, 'html.parser')
        proxies_table = soup.find(id='proxylisttable')

        # Save proxies in the array
        for row in proxies_table.tbody.find_all('tr'):
            proxies.append({
            'ip':   row.find_all('td')[0].string,
            'port': row.find_all('td')[1].string
            })

        self.proxies = proxies
        return


    def _get_random_proxy(self):
        idx = random.randint(0, len(self.proxies) - 1)
        return(self.proxies[idx])

    def make_request(self, url, max_retry=5):
        req = Request(url)
        n=0
        while True and n < max_retry:
            proxy = self._get_random_proxy()
            req.set_proxy(proxy['ip'] + ':' + proxy['port'], 'http')
            try:
                r = urlopen(req)
                return(r)
            except:
                self.proxies.remove(proxy)
            n += 1

        raise Exception(f"Could not find proxy or problem with url: {url}")
        return
