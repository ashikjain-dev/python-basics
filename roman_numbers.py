# Give a Roman number equivalent to English number
from win32comext.taskscheduler.taskscheduler import IID_ITask
from random import randint
english_number=int(input("Please enter the english number: "))
print(english_number)

def get_roman_number(number):
    if number ==0:
        return 0
    elif number==1:
        return 'I'
    elif number==2:
        return 'II'
    elif number==3:
        return 'III'
    elif number==4:
        return 'IV'
    elif number==5:
        return 'V'
    elif number==6:
        return 'VI'
    elif number==7:
        return 'VII'
    elif number==8:
        return 'VIII'
    elif number==9:
        return 'IX'
    elif number==10:
        return 'X'
    else:
        return 'The number should be less than or equal to 10.'


generate_number=randint(1,10)
print('The number is '+str(generate_number)+'and it\' equivalent roman number is :'+str(get_roman_number(generate_number)))
print('The number is '+str(english_number)+'and it\' equivalent roman number is :'+str(get_roman_number(english_number)))
