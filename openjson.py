#!/usr/bin/env python3

import json
import csv 
import math

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
        #metro_geo_longt = round(float(metro_station['geoData']['coordinates'][0]),3)
        #metro_geo_latit = round(float(metro_station['geoData']['coordinates'][1]),3)
        metro_geo_longt = float(metro_station['geoData']['coordinates'][0])
        metro_geo_latit = float(metro_station['geoData']['coordinates'][1])

        for bus_station in bus_stations:
            try:
                #bus_longt = round(float(bus_station['Longitude_WGS84']),3)
                bus_longt = float(bus_station['Longitude_WGS84'])
                #bus_latit = round(float(bus_station['Latitude_WGS84']),3)
                bus_latit = float(bus_station['Latitude_WGS84'])

                if math.sqrt((metro_geo_longt - bus_longt)**2 + (metro_geo_latit - bus_latit)**2) < 0.0005:
                    metro_stats.append(metro_station['NameOfStation'])
            except ValueError:
                pass

    counter = Counter(metro_stats)
    maxstation = counter.most_common()[0][0]
    maxcount_street = counter.most_common()[0][1]
    print('Максимальное колличество остановок: {} \nНаходятся на станции "{}"'.format(maxcount_street, maxstation))


if __name__ == '__main__':
    main()
