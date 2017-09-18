#!/usr/bin/env python3

import json
import csv 

from collections import Counter

def getjson():
    with open('data.json', 'r', encoding='utf-8') as f: 
        metro_json = json.loads(f.read())
    return metro_json


def get_escalators(metro):
    for metro_station in  metro: 
        if metro_station['RepairOfEscalators']: 
            for escalator in metro_station['RepairOfEscalators']: 
                print('На станции {} ремонт эскалатора {}'.format(metro_station['Name'], escalator['RepairOfEscalators']))


def getcsv():
    with open('data.csv', 'r', encoding='utf-8') as f:
        fields = [
                    "ID","Name","Longitude_WGS84","Latitude_WGS84","Street","AdmArea","District","RouteNumbers",
                    "StationName", "Direction","Pavilion","OperatingOrgName","EntryState","global_id","geoData",
                ]
        csvdata = csv.DictReader(f, fields, delimiter=';')
        bus_st = []
        for row in csvdata:
            bus_st.append(row)
    return bus_st


def main():
    metro=getjson()
    #print(metro[1])
    #get_escalators(metro)
    bus_stations = getcsv()
    metro_stats=[]
    
    for metro_station in metro:
        metro_geo_longt = round(metro_station['geoData']['coordinates'][0],3)
        metro_geo_latit = round(metro_station['geoData']['coordinates'][1],3)

        for bus_station in bus_stations:
            bus_longt = round(bus_station['Longitude_WGS84'],3)
            bus_latit = round(bus_station['Latitude_WGS84'],3)

            if bus_longt == metro_geo_longt and bus_latit == metro_geo_latit:
                metro_stats.append(metro_station['NameOfStation'])

    counter = Counter(metro_stats)
    maxstation = counter.most_common()[0][0]
    maxcount_street = counter.most_common()[0][1]
    print('Максимальное колличество остановок: {} \nНаходятся на станции "{}"'.format(maxcount_street, maxstreet))


if __name__ == '__main__':
    main()
