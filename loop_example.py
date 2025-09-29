# # # Understand while loop by printing a number from 10 to 1
# #
# # # counter=10
# # # while counter>0:
# # #     print(counter)
# # #     counter-=1
# #
# #
# # # Get a number from a user and add the number  till 1
# #
# # user_number=int(input("Please enter the user number: "))
# # result=0
# #
# # while user_number>0:
# #     result=result+user_number
# #     user_number-=1
# # print("The result is",result)
#
# # For loop
# word='hello world'
# for letter in word:
#     print(letter)
#
#
# # get a string and count the characters in it.
# user_string=input("Please enter a string: ")
# count_chars=0
# for letter in user_string:
#     count_chars+=1
#
# print("The user string is : "+user_string)
# print("The count of characters is: "+str(count_chars))


# range example
num_input=range(17,19)
print(num_input)
print(type(num_input))
for num in num_input:
    print(num)