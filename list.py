# #complete module
# import calculation

# print(calculation.add(1,2))
# print(calculation.sub(5,3))
# print(calculation.mutiply(3,6))
# print(calculation.divide(10,2))

# # specific fucntion

# from calculation import add,sub

# print(add(4,6))
# print(sub(7,2))

# # alias
# import calculation as cal
# print(cal.add(2,3))

# from calculation import *
# print(add(4,8))


# Data structures in python
# lists, tuples, sets, dictionary

name=["xzyz","abc","hig"]
# print
print(name)
# indexing
print(name[1])
# replace
name[2]="hdshdf"
print(name)
# add
name.append("vcvcvcv")
print(name)
# remove
name.remove("xzyz")
print(name)
# length
print(len(name))

# tuples
# fruits=("apple","mango","banana","apple")
# print(fruits)
# print(fruits[1])


# sets
fruits={"apple","mango","banana","apple"}
print(fruits)
fruits.add("cherry")
print(fruits)
fruits.remove("apple")
print(fruits)