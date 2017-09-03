#!/usr/bin/python3 

def get_count(myval,percent=18):
    try:
        val_count=float(myval)
        counted=val_count*percent/100 
        return counted
    except (ValueError,TypeError): 
        print('Error')

value=get_count('a100')
print('counted: {}'.format(value))
value=get_count('100')
print('counted: {}'.format(value))
value=get_count('63',33)
print('counted: {:.2f}'.format(value))
