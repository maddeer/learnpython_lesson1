#!/usr/bin/env python3 

import requests 

def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except requests.exceptions.RequestException as e: 
        print(e)
        return False

#html = get_html('https://yandex.ru/search/?lr=213&msid=1506507795.1465.22867.23237&text=python')
#print(html)
