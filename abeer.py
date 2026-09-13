# #


# print("hello world")
# #string
# name="abeer"

# #integer
# batch=3

# #float
# course=3.0

# #boolean
# istrue=True

# print(name)
# print(batch)
# print(course)

# hello=input("Your Name:")
# print(hello)




# calculatir practice
# num1=20
# num2=20
# num1=float(input("Enter first name"))
# num2=float(input("Enter second name"))
# print(num1 + num2)
# print(num1 - num2)
# print(num1 * num2)
# print(num1 / num2)





# calculator task
# num1=float(input("Enter first num :"))
# operator=input("enter any sign(+, -, *, /) :")
# num2=float(input("Enter second num :"))
# if operator=="+":
#     print("Result", num1+num2)
# elif operator=="-":
#     print("Result", num1-num2)
# elif operator=="*":
#     print("Result", num1*num2)
# elif operator=="/":
#     if num2 !=0:
#         print("Result", num1/num2)
#     else:
#         print("numer is not disvalid")
# else:
    # print("invalid character")






# bill = int(input("Enter the product's price: "))

# if bill >= 3000:
#     discount = 20
#     final_bill = bill - (bill * discount / 100)
#     print("Discount:", discount, "%")
#     print("Final Bill:", final_bill)

# elif bill >= 2000:
#     discount = 10
#     final_bill = bill - (bill * discount / 100)
#     print("Discount:", discount, "%")
#     print("Final Bill:", final_bill)

# else:
#     print("Offer is over")
#     print("Final Bill:", bill)



# x=float(input("enter any number"))

# print("your answer in Meter:", x*1000)
# print("your answer in Kilometer:", x/1000)
# print("your answer in Centimeter:", x*2.54)
# print("your answer in Inche :", x/2.54)
# print("your answer in Meter:", x*0.3048)
# print("your answer in Feet:", x/0.3048)
# print("your answer in Kiilometer:", x*1.60934)
# print("your answer in Miles:", x/1.60934)






# f =float(input("enter temperature:"))
# celcius =(f-32) *  5/9
# print("Fahrenheit :", {f})
# c = float(input("enter temperature:"))
# Fahrenheit = (c *9/5) + 532
# print("Celcius:", {c})
# if Celcius=="c":
#     print("Result", Fahrenheit)
# elif Fahrenheit=="f":
#     print("Result",Celcius )


# if else
# conditional rendering
# a=20
# if a>=20:
#     print("you are eligible")
# else:
#     print("you are not eligible")
    


# even odd
# a=int(input("enter any number"))
# if a%2==0:
#     print("even number")
# else:
#     print("odd number")
# negative and postive number
# a=-12
# if a>0:
#     print("positive number")
# elif a<0:
#     print("negative number")
# else:
#     print("you number is zero")



# grading system
# marks=int(input("enter your marks in the range of 1-100"));
# if marks>=90:
#     print("you grade is A")
# elif marks>=80:
#     print("your grade is B")
# elif marks>=70:
#     print("Youar grade is C")
# elif marks>=60:
#     print("your grade is E")
# else:
#     print("you are fail")

# largets value
# num1 =90
# num2= 75
# num3=87

# if num1>num2 and num1>num3:
#     print(num1)
# elif num2>num1 and num2>num3:
#     print(num2)
# else:
#     print(num3)






# age=20
# id=False

# if age>18:
#     if id:
#         print("welcome t0 the school")
#     else:
#         print("bring your id")
# else:
#     print("you are not eligible")
# pasword managment system
# password=str(input("Enter you pasword"))
# id=int(input("Enter your id"))

# if password=="123" and  id==345:
#     print("you are login")
# else:
#     print("login failed")





# amount=int(input("enter any final bill"))
# if amount>2000:
#     discount=amount*0.10
#     print("your discount is", discount)
#     print("your new bill is : ", amount-discount)
# else:
#     print("you are not eligible for discount")







# LOOPS
# print("WELCOME")


# for loop
# for variable in sequence
# for i in range(10):
#     print("welcome",i)


# for i in range(1,11):
#     print("welcome",i)



# for variable in sequence(start,end, steps)
# for variable in sequence(even,end, 2)
# for variable in sequence(odd,end, 2)



# # even
# for i in range(4,100,2):
#     print(i)
# # odd
# for i in range(7,156,2):
#     print("odd numbers:", i)





# for i in range(2,20,2):
#     print(i**2)





# for i in range(4,19,2):
#     print(i**2)












# students=["web dev","cyber","graphic","python"]
# for i in students:
#     print(i)

# for i in range(1,9):
#     if i==6:
#         break
#     print(i)
#     print("loop ended")

# for i in range(1,9):
#     if i==2:
#         continue
#     print(i)

# table
# num=int(input("enter any number : "))
# for i in range(1,11):
#     print(num,"x",i,"=",num*i)

# for i in range(5,0,-1):
#     print("*"*i)






# array=[-76,48,-64,76,4,86,-54,100,-56,-45,76,-42]
# print=("valid marks")
# for i in array:
#     if i<0:
#         nagValue = i
#         continue
#     print(i)

# print("invalid marks")
# for i in array:
#     if i>0:
#        positiveValue = i
#        continue
#     print(i)

# print("perfect marks")
# for i in array:
#     if i == 100:
#         print(i)
#         break




# count=1
# while count<=5:
#     print(count)
#     count+=1

# count=1
# while count<5:
#     print(count)
#     count+=1
  
# def xyz(name):
#     print("hello",name)
# xyz("abeer")

# def xyz(name):
#     print("hello",name)
# xyz(input("Enter your name:"))

# def xyz(name,age):
#     print("hello{name},your age is{age}")
# xyz(input("Enter your name:"),input("Enter your age:"))



# def evenOdd(num):
#     if num%2==0:
#         print("even")
#     else:
#         print("Odd")
# evenOdd (int(input("Enter num:")))



# def grade(marks):
#     if marks>=90:
#         return"A"
#     elif marks>=80:
#         return "B"
#     elif marks>=70:
#         return "C"
#     elif marks>=60:
#         return "D"
#     elif marks<60:
#         return "Fail"
    
# print(grade(int(input("Enter any marks:"))))



# import math
# # square root
# print(math.sqrt(81))
# print(math.sqrt(25))
# # power
# print(math.pow(2,4))
# print(math.pow(5,5))
# # pi
# print(math.pi)
#  # area
# area=pi*r^2
# radius=6
# print(math.pi*6**2)

# # random
# import random
# dice=random.randint(1,6)
# print(dice)
# otp=random.randint(1000,9999)
# print(otp)
# # random choice
# a=["ali","faizan","salman"]
# print(random.choice(a))

# # date time
# from datetime import datetime
# print(datetime.now())
# # date
# from datetime import date
# print(date.today())
# # sleep
# # import time
# # print("start")
# # time.sleep(4)
# # print("finish")

# import csv
# file=open("practice.csv","r")
# data=csv.reader(file)
# for row in data:
#     print(row)

# file.close()
# # applying filter
# import csv
# file=open("practice.csv","r")
# data=csv.reader(file)
# for row in data:
#     if "B" in row[1] and "f_50-99" in row[3]:
#         print(row)

# file.close()



#                                                       Assingment# 
# # Part A
# import math
# print(math.sqrt(144))
# # power
# print(math.pow(7,4))
# # pi
# print(math.pi)
# # area
# radius=10
# print(math.pi*10**2)

# # PART B
# # Random
# import random
# dice=random.randint(50,100)
# print(dice)
# # otp code
# otp=random.randint(100000,999999)
# print(otp)
# # Choice
# f=["Apple","Banana","Mango","Peach","Grapes"]
# print(random.choice(f))

# # Part C

# # Date Time
# from datetime import datetime
# print(datetime.now())
# # Date 
# from datetime import date
# print(date.today())
# # sleep
# import time
# print("Program start")
# time.sleep(3)
# print("program finish")


# # Part D
# # 1.food file
# # 1. filter
# import csv
# file=open("food-price-index-september-2023-index-numbers.csv","r")
# data=csv.reader(file)
# next(data)
# for row in data:
#     if row[3]=="FINAL":
#         print(row)
# file.close()
# # 2.filter
# import csv
# file=open("food-price-index-september-2023-index-numbers.csv","r")
# data=csv.reader(file)
# next(data)
# for row in data:
#     if row[4]=="Index":
#         print(row)
# file.close()
# # 3.filter  
# file=open("food-price-index-september-2023-index-numbers.csv","r")
# data=csv.reader(file)
# next(data)
# for row in data:
#     if row[5]=="Consumer":
#         print(row)
# file.close() 
# # 4.filter  
# file=open("food-price-index-september-2023-index-numbers.csv","r")
# data=csv.reader(file)
# next(data)
# for row in data:
#     if row[6]=="Food Price":
#         print(row)
# file.close()

# # 2.Buisness
# # 1.filter
# import csv
# file=open("buisenes.csv","r")
# data=csv.reader(file)
# next(data)
# for row in data:
#     if row[1]=="total":
#         print(row)
# file.close() 
# # 2.filter 
# file=open("buisenes.csv","r")
# data=csv.reader(file)
# next(data)
# for row in data:
#     if row[2]=="1":
#         print(row)
# file.close() 
# # 3.filter
# file=open("buisenes.csv","r")
# data=csv.reader(file)
# next(data)
# for row in data:
#     if row[3]=="total":
#         print(row)
# file.close()
# # 4.filter
# file=open("buisenes.csv","r")
# data=csv.reader(file)
# next(data)
# for row in data:
#     if len (row) > 6:
#         if int(row[6])>10000:
#              print(row)
# file.close()
# # 3.Anual income
# # 1.filter
# import csv
# file=open("Annual.csv","r")
# data=csv.reader(file)
# next(data)
# for row in data:
#     if row[0]=="2007.03":
#         print(row)
# file.close()        
# # 2.filter
# file=open("Annual.csv","r")
# data=csv.reader(file)
# next(data)
# for row in data:
#     if row[1]=="Non-corporate business enterprises":
#         print(row)
# file.close()
# # 3.filter
# file=open("Annual.csv","r")
# data=csv.reader(file)
# next(data)
# for row in data:
#     if row [5]=="6":
#          print(row)
    

# file.close()
# # 4.filter
# file=open("Annual.csv","r")
# data=csv.reader(file)
# next(data)
# for row in data:
#     if row[5] == "AFA0000":
#         print(row)
# file.close()
# # 4.National
# # 1.filter
# import csv
# file=open("national.csv","r")
# data=csv.reader(file)
# for row in data:
#     if row[3]=="Final":
#         print(row)
# file.close() 
# # 2.filter 
# file=open("national.csv","r")
# data=csv.reader(file)
# next(data)
# for row in data:
    
#     if row[4]=="Dollars":
#         print(row)
# file.close()     
# # 3.filter 
# file=open("national.csv","r")
# data=csv.reader(file)
# next(data)
# for row in data:
#     if row[5]=="6":
#         print(row)
# file.close() 
# # 4.filter
# file=open("national.csv","r")
# data=csv.reader(file)
# next(data)
# for row in data:
#     if float(row[2])> 60000:
#         print(row)
# file.close()


#                                                 DICTIONARY #                                          

# student={
#     "name" : "xyz",
#     "age":23,
#     "cgpa":3.5,
# }
# print(student)

# # access the value
# print(student["name"])
# print(student["age"])

# # get methood
# print(student.get("hello"))

# # add new item
# student["uni"]="umt"
# print(student)

# # update the exsiting values not keys
# student["age",]=25
# print(student)

# # update the  whole block
# student.update({
#     "name":"abc",
#     "age":27,
#     "cgpa":3.7
# })
# print(student)

# # remove items
# student.pop("name")
# print(student)

# # last item
# student.popitem()
# print(student)

# # length
# print(len(student))

# #keys
# print(student.keys())

# # values
# print(student.values())

# for key in student:
#     print(key)

# for key in student.values():
#     print(key)

# for key,value in student.items():
#     print(key, ":" , value)

# student2=student.copy()
# print(student2)

# # del student2
# # print(student2)

# # del student
# print(student)



 
#                                           FILE HANDLING AND EXCESS#                                            



# with open("example.txt","r") as file:
# print(file.read())

# with open("example.txt","r") as file:
# print(file.readline())


# # with open("example.txt","r") as file:
# # print(file.readlines())

# with open("example.txt","w") as file:
# file.write("hello world")

# with open("example.txt","a") as file:
# file.write("\nhello world 2")

# with open("example.txt","w") as file:
# file.write("deleted")

# with open("example.txt","a") as file:

# file.write("\ndeleted2")

# import csv
# with open("practice.csv","r") as file:
# reader=csv.reader(file)
# for row in reader:
# print(row)

# exception handling
# try:
# num=10
# print(num/0)
# except:
# print("you number is not divisble by zero")

# try:
# num=int(input("enter any number"))
# print(100/num)
# except:
# print("an error occured")

# try:
# num=int(input("enter any number"))
# print(100/num)
# except (ZeroDivisionError,ValueError,IndexError):
# print("you input is not valid")

# else handling
# try:
# age=int(input("enter your age"))
# except ValueError:
# print("inavlid age")
# else:
# print("age is",age)

# finally

# try:
# num=int(input("enter any number"))
# print(100/num)
# except:
# print("error")
# finally:
# print("program finished...")

# FileNotFoundError -> jb file available ni thi
# ZeroDivisionError: division by zero
# TypeError->type invalid
# valueError->value is invalid
# indexError->when we acces the invalid index


#                                                      LIST #                                                   

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

# name=["xzyz","abc","hig"]
# # print
# print(name)
# # indexing
# print(name[1])
# # replace
# name[2]="hdshdf"
# print(name)
# # add
# name.append("vcvcvcv")
# print(name)
# # remove
# name.remove("xzyz")
# print(name)
# # length
# print(len(name))

# # tuples
# # fruits=("apple","mango","banana","apple")
# # print(fruits)
# # print(fruits[1])


# # sets
# fruits={"apple","mango","banana","apple"}
# print(fruits)
# fruits.add("cherry")
# print(fruits)
# fruits.remove("apple")
# print(fruits)


#                                                        LOOPS#                                                         


# print("Welcome")
# for i in range(10):
#     print("Welcome",i)
# for i in range(1,11):
#     print("Welcome",i)   
 
# for variable in sequence(start,end, steps)
# for variable in sequence(even,end, 2)
# for variable in sequence(odd,end, 2)
# # even
# for i in range(4,100,2):
#     print(i)
# # odd
# for i in range(7,156,2):
#     print("odd numbers:",i)
# for i in range(2,20,2):
#     print(i**2)    

# for i in range(1,9):
#     if i==6:
#         break
#     print(i)
#     print("loop ended")

# for i in range(1,9):
#     if i==2:
#         continue
#     print(i)

# table
# num=int(input("enter any number : "))
# for i in range(1,11):
#     print(num,"x",i,"=",num*i)

# for i in range(5,0,-1):
#     print("*"*i)

#                                                         OBJECT#                                                       

# class student:
#    def __init__(self,name,age,cgpa,uni):
#         self.name=name
#         self.age=age
#         self.cgpa=cgpa
#         self.uni=uni

# student1=student("Fatima",19,3.5,"oxford")        
# student2=student("Huda",20,3.2,"LUMS")
# student3=student("Hafsa",18,3.1,"umt")

# print(student1.name, student1.age, student1.cgpa, student1.uni)       
# print(student2.name, student2.age, student2.cgpa, student2.uni)       
# print(student3.name, student3.age, student3.cgpa, student3.uni)


#                                                         OOPCAR#                                                  


# class car:
#     pass

# s1=car()
# s2=car()
# print(s1)
# print(s2)

# #constructor

# class car:
#     def __init__(self):
#         print("constructor is called")
# s1=car()
# print(s1)

# class car:
#     def __init__(self):
#         self.name="Alto"
#         self.model=2023

# car1=car()
# print(car1.name)
# print(car1.model)

# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

# student1=student("abc",12)
# student2=student("xyz",13)

# print(student1.name,student1.age)

# print(student2.name,student2.age)






# # inheritence
# class student:
#     def study(self):
#         print("hi my name is abeer")



# class teacher(student):
#     pass
# s1=teacher()
# s1.study()



# # example1
# class student:
#     def __init__(self,name):
#         self.name=name
#     def study(self):
#         print(self.name,"is studying")



# class teacher:
#     def __init__(self,name):
#         self.name=name
#     def teach(self):d
#         print(self.name,"is teaching")


# s=teacher("abeer")
# s1=student("aqsa")
# s.teach()
# s1.study()


# class teacher:
#     def __init__(self,name):
#         self.name=name
#     def teach(self):
#         print(self.name,"is teaching")




# class student(teacher):
#     def study(self):
#         print(self.name,"is studying")



# class admin(student):
#     def manage(self):
#         print(self.name,"is managing")

# t=teacher("aqsa")
# s=student("abeer")
# a=admin("javeria")
# a.study()
# a.teach()
# a.manage()







                        #   activity portion  








# choice = input("Enter C to convert Celsius to Fahrenheit or F to convert Fahrenheit to Celsius: ").lower()

# if choice == "c":
#     celsius = float(input("Enter temperature in Celsius: "))
#     fahrenheit = (celsius * 9/5) + 32
#     print("Result:", fahrenheit, "°F")

# elif choice == "f":
#     fahrenheit = float(input("Enter temperature in Fahrenheit: "))
#     celsius = (fahrenheit - 32) * 5/9
#     print("Result:", celsius, "°C")
    
# else:
#     print("Invalid choice!")






# f =float(input("enter temperature:"))
# celcius =(f-32) *  5/9
# print("Fahrenheit:", f)
# c = float(input("enter temperature:"))
# # Fahrenheit =(c * 9/5) + 32
# # print("Celsius:", c)
# # if celcius=="c":
# #     print("Result", Fahrenheit)
# # elif Fahrenheit=="f":
# #   print("Fahrenheit:", f)










# marks=int(input("enter your marks in the range of 1-100="))

# if marks>=80:
#     print("your grade is A")
# elif marks>=70:
#     print("Youar grade is B")
# elif marks>=60:
#     print("Youar grade is C")
# else:
#     print("you are fail")



# for i in range (1,10):
#     print(i)

# for i in range(1,10):
#     if i==9:
#         break
#     if i==5:
#         continue
#     print(i)



# for i in range(1,10):
#     if i==5:
#         continue
#     print(i)



# def calculate(price,quantity):
#     return(price*quantity)

# result=(50*4)
# print(result)


# calculate(50,4)



# def greet():
#     print("Hello, Welcome to Python!")

# greet()



# def welcome():
#     print("Welcome to Python!")

# welcome()
# welcome()
# welcome()




# def greet(name):
#     print("Hello,", name)

# greet("Abeer")
# greet("Ali")


# def add(a, b):
#     return a + b

# result = add(10, 20)
# print(result)



# class Student:
#     def __init__(self, name, age, marks):
#         self.name = name
#         self.age = age
#         self.marks = marks

#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("Marks:", self.marks)


# student1 = Student("Abeer", 20, 85)
# student2 = Student("Ali", 21, 90)
# student3 = Student("Sara", 19, 88)

# student1.display()
# student2.display()
# student3.display()


























