#!/usr/bin/env python3 

from datetime import datetime 
from flask import Flask, abort, request

from lesson4_weather import get_weather 
from news import all_news 
from getnames import get_names


city = 'Moscow'
apikey = 'b5245229ccfc3c3d8afde87c6e114104'

app = Flask(__name__)


@app.route('/') 
def index():
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&APPID={}&units=metric&lang=ru'.format(city, apikey)
    weather = get_weather(url)
    result = '<p>Температура {}</p>'.format(weather['main']['temp'])
    result += '<p>Город: {}</p>'.format(weather['name'])
    result += '<p>Время: {}</p>'.format(datetime.now().strftime('%Y-%m-%d %H:%M'))
    return result

@app.route('/news')
def all_the_news():
    colors = ['green', 'red', 'blue' ] 
    try: 
        limit = int(request.args.get('limit', 10))
    except ValueError: 
        limit = 10
    color = request.args.get('color', 'black') if request.args.get('color') in colors else 'black'
    return '<h1 slyle="color: {}">News: <small>{}</small><h1>'.format(color, limit)


@app.route('/names')
def all_names():
    all_names_data = get_names()

    current_year = int(datetime.now().strftime('%Y'))
    links = ''
    for link in range(2015,current_year+1):
        links += '<a href="?year={year}">{year}</a> '.format(year=link)

    table_full = '''<table>
    <tr>
        <th>Номер</th>
        <th>Имя</th>
        <th>Год</th>
        <th>Месяц</th>
        <th >Колличество</th>
    </tr>{}
    </table>'''

    data_string = '''<tr>
    <td>{0}</td>
    <td>{Name}</td>
    <td>{Year}</td>
    <td style='width: 80; text-align: center; '>{Month}</td>
    <td style='text-align: center;'>{NumberOfPersons}</td>
    </tr>'''

    result = ''
    try:
        year = int(request.args.get('year', '2017'))
    except ValueError: 
        year = 2017

    for string in all_names_data: 
        if string['Cells']['Year'] == year: 
            result += data_string.format(string['Number'], **string['Cells'])

    result = table_full.format(result)
    return links + '<br>' + result


@app.route('/news/<int:news_id>')
def news_by_id(news_id):
    news_list = [ news for news in all_news if news['id'] == news_id ]
    if len(news_list) == 1:
        result = '<h1>{title}</h1>'
        result += '<p>{text}</p>'
        result += '<p>Дата: {date}</p>'
        result = result.format(**news_list[0])
        return 'Новость: {}'.format(result)
    else: 
        abort(404)


if __name__ == '__main__': 
    app.run(port=5000, debug=True)
