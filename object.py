class student:
   def __init__(self,name,age,cgpa,uni):
        self.name=name
        self.age=age
        self.cgpa=cgpa
        self.uni=uni

student1=student("Fatima",19,3.5,"oxford")        
student2=student("Huda",20,3.2,"LUMS")
student3=student("Hafsa",18,3.1,"umt")

print(student1.name, student1.age, student1.cgpa, student1.uni)       
print(student2.name, student2.age, student2.cgpa, student2.uni)       
print(student3.name, student3.age, student3.cgpa, student3.uni)