# Understand different in-built functions of string

# Upper function -> return the string in upper case.
all_lower_string="change this sentence to an uppercase string."
print(all_lower_string.upper())

# Lower function -> lower all characters.
all_upper_string="WARNING SENTENCE, BE CARFUL!"
print(all_upper_string.lower())

# isUpper and isLower functions checks whether the string or character is upper case or lower case.
print("Hanuman".isupper())
print("KRISHNA".islower())

# isalpha checks whether a string contains only alphabetic
print("SriKrishna".isalpha())

# isalnum checks both number and character.
print("ram".isalnum())
print("123".isalnum())

#isspace checks for the space
print("".isspace())
print(" ".isspace())
print(" ashik ".isspace())

# isdecimal checks for the number
print("123".isdecimal())


#istitle checks whether the word starts with capital letter.
print("The King Is An Ordinary Man Without His Kingdom!".istitle())

#join and split functions
#join takes a list and gives you the string
print("".join(["ashik","a","jain"]))

# split act on a string and returns a list
print("Milk, Water, Air, Food".split(", "))