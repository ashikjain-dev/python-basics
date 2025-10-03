#Sets are similar to Lists, but
# it cannot contain duplicate values
# items are unordered similar to dictionary
#
# set_ex1={1,2,3,4,4,5,5,5,6,6,8,9,10}
# print(set_ex1)
# ex2_set=set()
# print(ex2_set)
# ex3_set=set(range(0,20,2))
# print(ex3_set)
# for x in ex3_set:
#     print(x)

# Methods : add, remove, discard, clear, copy, union, intersection and difference.

#movies={"Kotigobba","Manikya"}
# movies.add("Huccha")
# print(movies)
#
# movies.remove("Huccha")
# print(movies)
#
# print(movies.clear())
#
# set1={1,2,3,4,5}
# set2={5,6,7,8,9,0}
# se3=set1.union(set2)
# print(se3)
# se4=set1|set2
# print(se4)
# se5=set1&set2
# print(se5)
# se6=set1.intersection(set2)
# print(se6)
# se7=set1.difference(set2)
# print(se7)
# se8=set2-set1
# print(se8)

# Set comprehensions
lower_case_letter={char.lower() for char in "ALLCAPSINENGLISH"}
print(lower_case_letter)

even_numbers={num+2 for num in range(0,10,2)}
print(even_numbers)