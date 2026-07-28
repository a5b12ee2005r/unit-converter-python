student={
    "name" : "xyz",
    "age":23,
    "cgpa":3.5,
}
print(student)

# access the value
print(student["name"])
print(student["age"])

# get methood
print(student.get("hello"))

# add new item
student["uni"]="umt"
print(student)

# update the exsiting values not keys
student["age",]=25
print(student)

# update the  whole block
student.update({
    "name":"abc",
    "age":27,
    "cgpa":3.7
})
print(student)

# remove items
student.pop("name")
print(student)

# last item
student.popitem()
print(student)

# length
print(len(student))

#keys
print(student.keys())

# values
print(student.values())

for key in student:
    print(key)

for key in student.values():
    print(key)

for key,value in student.items():
    print(key, ":" , value)

student2=student.copy()
print(student2)

# del student2
# print(student2)

# del student
print(student)



















