#!/usr/bin/python3

weather={'city':'moscow','temperature':20,'wind':'East'}
weather2={'date':'26.06.2017','city':'moscow','temperture':20,'wind':'East'}
weather3={'date':'26.06.2017','city':'leningrad','temperture':22,'wind':'East'}

weatherlist=[weather,weather2,weather3,weather.copy()]
print(weatherlist)
weather['temperature']=22
print(weatherlist)
# age,test=23,2.3333
# print('your {1} test {0:_^4} {1:=+010.2f} {2:=+5}'.format(age,test,-23))
# print ("test {d[key]} {d[sad]} asaa {d2[key2]}".format(d=data,d2=data2) ) 
# 
# from datetime import datetime
#'{:%Y-%m-%d %H:%M}'.format(datetime(2001, 2, 3, 4, 5))

# try: 
#    del dict['key']
# except KeyError: 
#    print('error')
# 
