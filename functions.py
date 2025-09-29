# #learning Functions
# print("This\nis\nan\nexample")
# # Passing a single parameter
# def add_number_to_two(number1):
#     return number1 + 2
#
# print('Sum of two numbers are : '+str(add_number_to_two(10)))
#
# #Passing two parameters
# def multiply_numbers(number1, number2):
#     return number1 * number2
#
# print('Multiplication of two numbers is : '+str(multiply_numbers(10, 2)))
#
# # Default value for the parameters
# def divide_numbers(number1=10, number2=2):
#     return number1 / number2
#
# print('Division of two numbers is : '+str(divide_numbers(40,3)))

# Print the string Hello World
# def hello_world_printer():
#     print("Hello World")
#
#
# hello_world_printer()

first_name=input("Enter a first name: ")


def name_printer(name):
    print('Your first name is '+first_name+'.')

name_printer(first_name)