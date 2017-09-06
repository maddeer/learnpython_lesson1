#!/usr/bin/python3

def entersting(first_str,second_str): 
    if first_str==second_str :
        return 1
    elif len(first_str) > len(second_str) and first_str != second_str :
        return 2 
    elif first_str != second_str and second_str == 'learn':
        return 3 
    else:
        return 4

first_input=input('enter first: ')
second_input=input('enter second: ')
e=entersting(first_input,second_input)
print('{}'.format(e))

