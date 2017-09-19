#!/usr/bin/env python3 

import requests 
import apikey 

def get_names():
    url='http://api.data.mos.ru/v1/datasets/2009/rows?api_key={}'.format(apikey.API_KEY)
    result = requests.get(url)
    if result.status_code == 200: 
        return result.json()
    else:
        print('Что то не то') 

if __name__ == '__main__':
    data = get_names()
    print("{}\n{}".format(data[0],data[1]))
