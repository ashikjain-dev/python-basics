# Calculate the volume of a rectangular prism
# given l, w and h
# formula v= l*w*h
#
# def calculate_volume(length,width,height):
#     return length*width*height
#
#
# length1=int(input("Enter a length: "))
# width1=int(input("Enter a width: "))
# height1=int(input("Enter a height: "))
# volume=calculate_volume(length1,width1,height1)
# print('The volume of the rectangular prism is '+str(volume)+'cubic feet.')


# Calculate temperature degree in Fahrenheit by using Celsius value
# formula is : f=1.8*c+32
# Take Celsius value from user input

celsius_value=float(input("Enter an integer value: "))



def fahrenheit(celsius):
    return celsius * 1.8 + 32


#The Fahrenheit equivalent of [user entered integer] degrees Celsius is [number returned by function]

print("The Fahrenheit equivalent of "+str(celsius_value)+" degrees Celsius is "+str(fahrenheit(celsius_value))+"degrees Fahrenheit.")
