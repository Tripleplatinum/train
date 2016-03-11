# -*- coding: utf-8 -*-

import urllib
import random
import HTMLParser


# Definiuje funkcje random dla katalogu

def random_url():
    
    url_base = ['http://katalog.interia.pl/', 'http://katalog.onet.pl/', 'http://katalog.wp.pl/',
               'http://www.katalog.bajery.pl/', 'http://www.bazastron.com.pl/', 'http://www.webtree.com.pl/',
               'http://www.dmoz.org/', 'http://katalog.promocje.biz/', 'http://katalog.linuxiarze.pl/',
               'http://polskie-strony.org/', 'http://katalog.gazeta.pl/']
    url_base_random = url_base[random.randint(0, len(url_base)-1)]
    getrandom = url_base_random
    return getrandom


# odpalam funkcje i w zmiennej zapisuje html ze strony

random_url()
url = random_url()
print url

handle_var = urllib.urlopen(url)
download_html = handle_var.read()


urlText = []

# definiuje HTMLParser

class parseText(HTMLParser.HTMLParser):

    def handle_data(self, data):
        if data != '\n':
            urlText.append(data)

# instancja parsera

instaParser = parseText()

# dajemy url do parsera
instaParser.feed(download_html)
instaParser.close()
for item in urlText:
    print item

