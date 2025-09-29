# Understanding flow  for if condition

# veg=input("Type the name of a vegetable : ")
# if veg.lower()=="corn":
#     print("The vegetable name is corn.")
# else:
#     print("The vegetable name is not corn.")


# example for if else logic
# get a number from the use
# check if it is even number
# if it is even number and again check if it is divided by 4

# user_number=int(input("enter your number"))
#
# if user_number%2==0:
#     if user_number%4==0:
#         print("The number is divisible by 4.")
#     else:
#         print("The number is divisible by 4.")
# else:
#     print("The number is not an even number.")

# Get GPA of a student
# Check if it is greater than 3.7
# Check he is from approved institution
# Print approved loan.

gpa=float(input('What is the applicant\'s grade point average?'))

if gpa>=3.7:
    insta_app = input('Is the student going to be educated at an approved institution? (Y/N)')
    if insta_app== 'Y':
        print('The applicant is qualified for the loan.')
    else:
        print('The applicant is not qualified for the loan.')
else:
    print('The applicant did not have enough grade to qualify for the loan.')