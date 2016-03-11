# -*- coding: utf-8 -*-

import random
from urllib2 import urlopen
from lxml.html import parse
from pandas.io.parsers import TextParser

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
urlGOT = random_url()
print url

handle_var = urllib.urlopen(url)
download_html = handle_var.read()



def _unpack(row, kind ='td'):
    elts = row.findall('.//%s' % kind)
    return [val.text for val in elts]

def parse_options_data(table):
    rows = table.findall('.//tr')
    header = _unpack(rows[0], kind='th')
    data = [_unpack(r) for r in rows[1:]]
    return TextParser(data, names=header).get_chunk()

if __name__ == '__main__':

    url = urlGOT
    parsed = parse(url)

    doc = parsed.getroot()

    links = doc.findall('.//a')

    links_sub_list = links[15:20]
    lnk = links_sub_list[0]

    sample_url = lnk.get('href')

    sample_display_text = lnk.text_content()

    tables = doc.findall('.//table')

    dt = tables [0]

    rows = dr.findall('//tr/')

    headers = _unpack(rows[0], kind='th')

    row_vals = _unpack(rows[1], kind='td')

    tide_data = parse_options_data(dt)

    print tide_data[:10]
