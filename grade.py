# Get a student score
# Check if it is greater than 60
# check if it is greater than 70
# Check if it is greater than 80
# Check if it is greater than 90 then print A
# Else less than 90 and greater than 80 then print B
# Else less than 80 and greater than 70 then print C
# Else less than 70 and greater than 60 then print D
# Else print F

grade=int(input('Enter your grade : '))

if grade>=60:
    if grade>=70:
        if grade>=80:
            if grade>=90:
                print('Your grade is awesome! i.e A')
            else:
                print('B')
        else:
            print('C')
    else:
        print('D')
else:
    print('F')


