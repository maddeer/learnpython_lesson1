#!/usr/bin/env python3 

from bs4 import BeautifulSoup
from requests_yandex import get_html

#html = ''' 
#<html>
#    <head>
#        <title>My page</title>
#    </head>
#    <body>
#        <h1>Title</h1>
#        <p> text1 in abzce</p>
#        <p> text2 in abzce</p>
#        <p> text3 in abzce</p>
#        <p> text4 in abzce</p>
#    </body>
#</html>
#'''

html = get_html('https://yandex.ru/search/?text=python')

bs = BeautifulSoup(html, 'html.parser')

print(bs.title.text)
for item in bs.find_all('li', class_='serp-item'):
    print(item.text)

print(bs.prettify())
