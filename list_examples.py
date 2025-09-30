# understand some basic functions and list

list_one=[True,2,2.34,"true",[1,2,3,4]]
list_two=list("this is a sample.")
print(list_one)
print(list_two)
print('a' in list_two)
print('a' not in list_two)

# del removes an item based on index
# remove method removes an item based on the given value in the arguments

pets=['cow','horse','elephant','dog','cat','dog']
print(pets)
del pets[4]
print(pets)
pets.remove("dog")
print(pets)

# append add an item at the end of the list
pets.append("pigeon")
print(pets)

# insert allows you to add an item anywhere in the list.
# first argument is the index where we need to add.
# second argument is the item
pets.insert(0,"fish")
print(pets)

