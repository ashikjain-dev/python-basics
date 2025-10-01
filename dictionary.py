# understand basic of dictionary
# it contains of key value pair
# dict_ex1={
#     "index":0,
#     "name":"Ashik",
#     "age":22,
#     "married":False,
#     0:"false"
# }
# print(dict_ex1["age"])
# print(dict_ex1[0])
#
# # create another dictionary which contains 5 key value pairs
# dict_ex2={
#     "index":0,
#     "name":"Cow",
#     "breed":"Normal",
#     "color":"Black",
#     "gender":"Female"
# }
# print(dict_ex2["breed"])
# print(0 in dict_ex2)
# print("gender" not in dict_ex2)


# Dictionary methods : keys() , values(), items() and get()
# dict_ex3={
#     "index":0,
#     "name":"Cow",
#     "breed":"Normal",
#     "color":"Black",
#     "gender":"Female"
# }
# print(dict_ex3.keys())
# print(dict_ex3.values())
# for k in dict_ex3.keys():
#     print(k)
#
# for value in dict_ex3.values():
#     print(value)
#
#
# # items to get both key and value from dictionary
# print(dict_ex3.items())
#
# for key,value in dict_ex3.items():
#     print(key,value)
#
# print(len(dict_ex3))

#TEST
# dict_ex5={
#     "Queen": "Bohemian Rhapsody",
#     "Bee Gees": "Stayin' Alive",
#     "U2": "One",
#     "Michael Jackson": "Billie Jean",
#     "The Beatles": "Hey Jude",
#     "Bob Dylan": "Like A Rolling Stone"
# }
# print(len(dict_ex5))
# for key in dict_ex5.keys():
#     print(key)
#
# for value in dict_ex5.values():
#     print(value)
#
# for key,value in dict_ex5.items():
#     print(key,value)
#
# print(dict_ex5.get("Promise of the Real","That is not a key that appears in the dictionary."))

# methods 2 : fromkeys() pop() and popitem()

#
# dict_ex10={}.fromkeys('abcdefghijklmnopqrstuvwxyz','consonant')
# for k,v in dict_ex10.items():
#     print(k,v)
#
# fast_food_items = {"McDonald's": "Big Mac",
#                    "Burger King": "Whopper",
#                    "Chick-fil-A": "Original Chicken Sandwich"}
# fast_food_items.popitem()
# print(fast_food_items)

# Methods 3: Clear, Copy and Update
# ex_20={"index":0,"name":"Cow"}
# update_dict={"age":20}
# ex_20.update(update_dict)
# print(ex_20)
# # ex_20.clear()
# # print(ex_20)
#
# duplicate_dict=ex_20.copy()
# duplicate_dict["name"]="Dog"
# print(duplicate_dict)
# print(ex_20)

# Test :
# internet_celebrities = {"DrDisrespect": "YouTube", "ZLaner": "Facebook", "Ninja": "Mixer"}
# another_one = {"shroud": "Twitch"}
# internet_celebrities.update(another_one)
# print(internet_celebrities)
# duplicate1_dict=internet_celebrities.copy()
# internet_celebrities.clear()
# print(duplicate1_dict)
# print(internet_celebrities)


# setdefault()
#normal method to check whether the key is there or not and assign it to some value
# computers_dict={"Google":"ChromeBook","Apple":"MacBook","Microsoft":"Surface Pro"}
# if "Lenova" not in computers_dict:
#     computers_dict["Lenova"]="ThinkPad"
# print(computers_dict)
#
# computers_dict.setdefault("Dell","Dell")
# print(computers_dict)

# dict keyword to create an empty dictionary
empty_dictionary = dict()
print(empty_dictionary)
some_values_dict=dict(a=1, b=2, v3=5)
print(some_values_dict)