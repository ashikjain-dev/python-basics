# Take a string by using input function
# use for loop and reverse the given string.

user_string = input("Enter a string: ")
print(user_string)
user_reverse_string = ''
str_length=len(user_string)
for char in range(str_length-1,-1,-1):
    user_reverse_string += user_string[char]

print(user_reverse_string)