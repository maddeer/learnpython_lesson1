#!/usr/bin/python3

try: 
    age=int(input('Enter your age: ').strip())
    if age < 18 :
        print ('you are from school')
    elif age>18 and age<23:
        print ('you are from institute')
    elif age>23:
        print('go to the work') 

except (TypeError,ValueError):
    print ('Enter the numbers')
