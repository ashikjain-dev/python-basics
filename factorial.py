# find a factorial of a given number.

def factorial(num):
    # use for loop to go through one number and multiples it to the result
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result

user_number=int(input("Enter a number: "))
print("The factorial of", str(user_number), "is", str(factorial(user_number)))