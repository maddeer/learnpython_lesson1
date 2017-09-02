#!/usr/bin/python3 
def get_summ(one,two,delimeter=' '):
    return_string=str(one)+ str(delimeter) + str(two)
    return return_string.upper()

print(get_summ('Hello',2,'\t'))
print(get_summ('Hello',2,' '))
print(get_summ('Hello',2,' & '))
print(get_summ('Hello',2))
print(get_summ('Hello',2,' + '))
