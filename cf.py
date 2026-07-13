# Assingment
# Part A
import math
print(math.sqrt(144))
# power
print(math.pow(7,4))
# pi
print(math.pi)
# area
radius=10
print(math.pi*10**2)

# PART B
# Random
import random
dice=random.randint(50,100)
print(dice)
# otp code
otp=random.randint(100000,999999)
print(otp)
# Choice
f=["Apple","Banana","Mango","Peach","Grapes"]
print(random.choice(f))

# Part C

# Date Time
from datetime import datetime
print(datetime.now())
# Date 
from datetime import date
print(date.today())
# sleep
import time
print("Program start")
time.sleep(3)
print("program finish")


# Part D
# 1.food file
# 1. filter
import csv
file=open("food-price-index-september-2023-index-numbers.csv","r")
data=csv.reader(file)
next(data)
for row in data:
    if row[3]=="FINAL":
        print(row)
file.close()
# 2.filter
import csv
file=open("food-price-index-september-2023-index-numbers.csv","r")
data=csv.reader(file)
next(data)
for row in data:
    if row[4]=="Index":
        print(row)
file.close()
# 3.filter  
file=open("food-price-index-september-2023-index-numbers.csv","r")
data=csv.reader(file)
next(data)
for row in data:
    if row[5]=="Consumer":
        print(row)
file.close() 
# 4.filter  
file=open("food-price-index-september-2023-index-numbers.csv","r")
data=csv.reader(file)
next(data)
for row in data:
    if row[6]=="Food Price":
        print(row)
file.close()

# 2.Buisness
# 1.filter
import csv
file=open("buisenes.csv","r")
data=csv.reader(file)
next(data)
for row in data:
    if row[1]=="total":
        print(row)
file.close() 
# 2.filter 
file=open("buisenes.csv","r")
data=csv.reader(file)
next(data)
for row in data:
    if row[2]=="1":
        print(row)
file.close() 
# 3.filter
file=open("buisenes.csv","r")
data=csv.reader(file)
next(data)
for row in data:
    if row[3]=="total":
        print(row)
file.close()
# 4.filter
file=open("buisenes.csv","r")
data=csv.reader(file)
next(data)
for row in data:
    if len (row) > 6:
        if int(row[6])>10000:
             print(row)
file.close()
# 3.Anual income
# 1.filter
import csv
file=open("Annual.csv","r")
data=csv.reader(file)
next(data)
for row in data:
    if row[0]=="2007.03":
        print(row)
file.close()        
# 2.filter
file=open("Annual.csv","r")
data=csv.reader(file)
next(data)
for row in data:
    if row[1]=="Non-corporate business enterprises":
        print(row)
file.close()
# 3.filter
file=open("Annual.csv","r")
data=csv.reader(file)
next(data)
for row in data:
    if row [5]=="6":
         print(row)
    

file.close()
# 4.filter
file=open("Annual.csv","r")
data=csv.reader(file)
next(data)
for row in data:
    if row[5] == "AFA0000":
        print(row)
file.close()
# 4.National
# 1.filter
import csv
file=open("national.csv","r")
data=csv.reader(file)
for row in data:
    if row[3]=="Final":
        print(row)
file.close() 
# 2.filter 
file=open("national.csv","r")
data=csv.reader(file)
next(data)
for row in data:
    
    if row[4]=="Dollars":
        print(row)
file.close()     
# 3.filter 
file=open("national.csv","r")
data=csv.reader(file)
next(data)
for row in data:
    if row[5]=="6":
        print(row)
file.close() 
# 4.filter
file=open("national.csv","r")
data=csv.reader(file)
next(data)
for row in data:
    if float(row[2])> 60000:
        print(row)
file.close()