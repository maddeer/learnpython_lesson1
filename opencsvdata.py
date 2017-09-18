#!/usr/bin/env python3

import csv
from collections import Counter

streets = [] 
with open('data.csv', 'r', encoding='utf-8') as f:
    fields = [
                "ID","Name","Longitude_WGS84","Latitude_WGS84","Street","AdmArea","District","RouteNumbers",
                "StationName", "Direction","Pavilion","OperatingOrgName","EntryState","global_id","geoData",
             ]
    csvdata = csv.DictReader(f, fields, delimiter=';')
    streetcout = {}
    for row in csvdata:
        streets.append(row['Street'])

streetcout = Counter(streets)
   
maxstreet = streetcout.most_common()[0][0]
maxcount_street = streetcout.most_common()[0][1]
print('Максимальное колличество остановок: {} \nНаходятся на остановке "{}"'.format(maxcount_street, maxstreet))
