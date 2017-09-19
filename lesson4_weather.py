#!/usr/bin/env python3 

import requests 

def get_weather(url): 
    result = requests.get(url)
    if result.status_code == 200: 
        return result.json()
    else:
        print('Что то не то') 

if __name__ == '__main__':
    data = get_weather('http://api.openweathermap.org/data/2.5/weather?q=Moscow&APPID=b5245229ccfc3c3d8afde87c6e114104&units=metric')
    print(data)
