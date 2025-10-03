# tuples are immutable
# it can contain duplicate value
#
# tuple_ex=(1,2,3,0,0,00)
# print(tuple_ex)
# print(tuple_ex[0])
# tuple_ex2=tuple([1,2,3,4,5])
# print(tuple_ex2)
# tuple_ex3=tuple(["hello"])
# print(tuple_ex3)
# print(tuple_ex3[:4])
#
# weeks_tuples=("Mon", "Tue", "Wed", "Thu", "Fri")
# print(weeks_tuples[::2])
#
# for week in weeks_tuples:
#     print(week)

# count to count the number of times values exist
number_tuples=(0,1,1,(6,6,6),2,3,4,5,5,6)
print(number_tuples.count(10))
print(number_tuples[3][2])

try:
    print(number_tuples[3][12])
except Exception as e:  # Catch all other exceptions
    print(f"An unexpected error occurred: {e}")