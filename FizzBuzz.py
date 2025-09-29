# write a function which iterates through 1 to 50
# if number multiples of both 3 and 5 then print "FizzBuzz"
# if number multiples of only 3 then print "Fizz"
# if number multiples of only 5 then print "Buzz"
# for other number just print the number.

def fizzbuzz():
    nums= range(1, 51)
    for num in nums:
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)



fizzbuzz()