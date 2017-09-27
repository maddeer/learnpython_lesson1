#!/usr/bin/python3 
import math 

a=[1,2,3,4,5]
print('trying lists')
for i in a :
    print(i)

b={'a': 'b', 'a1':'b1','a2':'b2'}
print('trying dicts')
for i in b :
    print('{}: {}'.format(i,b[i]))

c='string'
print('trying strings')
for i in c :
    print(i)



school=[
    {'school_class': '4a', 'scores': [3,4,4,5,2]},  
    {'school_class': '4b', 'scores': [3,4,4,5,2]},       
    {'school_class': '4c', 'scores': [3,4,4,5,2]},      
    {'school_class': '5a', 'scores': [3,4,4,5,2]},     
    {'school_class': '5b', 'scores': [3,4,4,5,2]},     
    {'school_class': '5c', 'scores': [3,4,4,5,2]},      
    {'school_class': '6a', 'scores': [3,4,4,5,2]},     
    {'school_class': '6b', 'scores': [3,4,4,5,2]}     
]

school_score_sum=[]
for school_class in school : 
    score=math.fsum(school_class['scores'])
    students=len(school_class['scores'])
    class_score_average=round(score/students,3)
    print('Class {} avarage score {}'.format(school_class['school_class'],class_score_average))
    school_score_sum+=school_class['scores']
classes=len(school)
school_score_averege=round(math.fsum(school_score_sum)/len(school_score_sum),3)
print('Schoole avarage score {}. Classes {}'.format(school_score_averege,classes))


#
#
#from decimal import Decimal
#
#Decimal('3.6') * Decimal('8')  # -> Decimal('28.8')
#(Decimal('3.6') + Decimal('3.6') 
#         + Decimal('3.6') + Decimal('3.6') 
#         + Decimal('3.6') + Decimal('3.6') 
#         + Decimal('3.6') + Decimal('3.6'))  # -> Decimal('28.8')
#
#
#
# from decimal import Decimal
# Decimal('1') / 3 * 3  # -> Decimal('0.9999999999999999999999999999')
# from fraction import Fraction
# Fraction('1') / 3 * 3  # -> Fraction(1, 1) == Fraction('1/1') == Fraction('1')
#





def find_person(name):

    namelist=["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
    while True :
        person_name=namelist.pop()
        if name==person_name:
            print('{} нашелся'.format(name))
            break
        else:
            print('{} не {}'.format(person_name,name))
    return 0

find_person('Вася')

import answers

def ask_user():
    while True: 
        try: 
            ask_him=input('How are you: ')
            if ask_him=='OK': 
                print('Good')
                break
            else:
                print(answers.get_answers(ask_him))
        except KeyboardInterrupt: 
            print('\nBay')
            break

ask_user()




import datetime 
print(datetime.datetime.now())
print(dir())
print(globals())
print(locals())
