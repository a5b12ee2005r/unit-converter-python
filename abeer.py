
##


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




#calculatir practice
# num1=20
# num2=20
# num1=float(input("Enter first name"))
# num2=float(input("Enter second name"))
# print(num1 + num2)
# print(num1 - num2)
# print(num1 * num2)
# print(num1 / num2)





#calculator task
# num1=float(input("Enter first name :"))
# operator=input("enter any sign(+, -, *, /) :")
# num2=float(input("Enter first name :"))
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
#     print("invalid character")






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
# if celcious=="c":
#     print("Result", Fahrenheit)
# elif Fahrenheit=="f":
#     print("Result",celcious )


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
# marks=int(input("enter your marks in the range of 1-100="))
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


#for loop
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


# 

#count=1
# while count<=5:
#     print(count)
#     count+=1
# 
# count=1
# while count<5:
#     print(count)
#     count+=1
#   
# def xyz(name):
#     print("hello",name)
# xyz("abeer")
# 
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



import math
# square root
print(math.sqrt(81))
print(math.sqrt(25))
# power
print(math.pow(2,4))
print(math.pow(5,5))
# pi
print(math.pi)
# area
# area=pi*r^2
radius=6
print(math.pi*6**2)

# random
import random
dice=random.randint(1,6)
print(dice)
otp=random.randint(1000,9999)
print(otp)
# random choice
a=["ali","faizan","salman"]
print(random.choice(a))

# date time
from datetime import datetime
print(datetime.now())
# date
from datetime import date
print(date.today())
# sleep
# import time
# print("start")
# time.sleep(4)
# print("finish")

import csv
file=open("practice.csv","r")
data=csv.reader(file)
for row in data:
    print(row)

file.close()
# applying filter
import csv
file=open("practice.csv","r")
data=csv.reader(file)
for row in data:
    if "B" in row[1] and "f_50-99" in row[3]:
        print(row)

file.close()





























