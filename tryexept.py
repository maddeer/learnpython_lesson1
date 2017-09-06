#!/usr/bin/python3

def cut_cake(parts):
    try: 
        return 1/int(parts)
    except (ZeroDivisionError,ValueError,TypeError): 
        return 'Are you crazy ?' 

cake=cut_cake(5)
print(cake)
