#!/usr/bin/python3

weather={'city':'moscow','temperature':20,'wind':'East'}
weather2={'date':'26.06.2017','city':'moscow','temperture':20,'wind':'East'}
weather3={'date':'26.06.2017','city':'leningrad','temperture':22,'wind':'East'}

weatherlist=[weather,weather2,weather3,weather.copy()]
print(weatherlist)
weather['temperature']=22
print(weatherlist)

