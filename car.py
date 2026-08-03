class car:
    pass

s1=car()
s2=car()
print(s1)
print(s2)

#constructor

class car:
    def __init__(self):
        print("constructor is called")
s1=car()
print(s1)

class car:
    def __init__(self):
        self.name="Alto"
        self.model=2023

car1=car()
print(car1.name)
print(car1.model)

class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

student1=student("abc",12)
student2=student("xyz",13)

print(student1.name,student1.age)

print(student2.name,student2.age)