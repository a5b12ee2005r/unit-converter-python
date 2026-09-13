    
# Part 1
import math
print(math.sqrt(144))

print(math.pow(7,4))

print(math.pi)

radius=10,
print(math.pi*10**2)
# part 2
import random
dice=random.randint(50,100)
print(dice)
otp=random.randint(100000,999999)
print(otp)

fruits=["Apple","Banana","Orange","Mango","Pear"]
print(random.choice(fruits))
# part 3
from datetime import datetime
print(datetime.now())

from datetime import date
print(date.today())

import time
print("program started")
time.sleep(3)
print("program finished")

# part 4

# 1. filter
import csv
file=open("business.csv","r")
data=csv.reader(file)
next(data)
for row in data:
    if row[3]=="type":
        print(row)
file.close()
# 2.filter
import csv
file=open("business.csv","r")
data=csv.reader(file)
next(data)
for row in data:
    if row[4]=="CPIQ.SAP0220":
        print(row)
file.close()
# 3.filter  
file=open("business.csv","r")
data=csv.reader(file)
next(data)
for row in data:
    if row[5]=="Consumer":
        print(row)
file.close() 
# 4.filter  
file=open("business.csv","r")
data=csv.reader(file)
next(data)
for row in data:
    if row[6]=="Food Price":
        print(row)
file.close()




# 1.filter
import csv
file=open("consumers-price.csv","r")
data=csv.reader(file)
next(data)
for row in data:
    if row[1]=="total":
        print(row)
file.close() 
# 2.filter 
file=open("consumers-price.csv","r")
data=csv.reader(file)
next(data)
for row in data:
    if row[2]=="1":
        print(row)
file.close() 
# 3.filter
file=open("consumers-price.csv","r")
data=csv.reader(file)
next(data)
for row in data:
    if row[3]=="total":
        print(row)
file.close()
# 4.filter
file=open("consumers-price.csv","r")
data=csv.reader(file)
next(data)
for row in data:
    if len (row) > 6:
        if int(row[6])>10000:
             print(row)
file.close()



# 1.filter
import csv
file=open("selected-price.csv","r")
data=csv.reader(file)
next(data)
for row in data:
    if row[0]=="2007.03":
        print(row)
file.close()        
# 2.filter
file=open("selected-price.csv","r")
data=csv.reader(file)
next(data)
for row in data:
    if row[1]=="Non-corporate business enterprises":
        print(row)
file.close()
# 3.filter
file=open("selected-price.csv","r")
data=csv.reader(file)
next(data)
for row in data:
    if row [5]=="6":
         print(row)
    

file.close()
# 4.filter
file=open("selected-price.csv","r")
data=csv.reader(file)
next(data)
for row in data:
    if row[5] == "AFA0000":
        print(row)
file.close()



# 1.filter
import csv
file=open("water.csv","r")
data=csv.reader(file)
for row in data:
    if row[3]=="Final":
        print(row)
file.close() 
# 2.filter 
file=open("water.csv","r")
data=csv.reader(file)
next(data)
for row in data:
    
    if row[4]=="Dollars":
        print(row)
file.close()     
# 3.filter 
file=open("water.csv","r")
data=csv.reader(file)
next(data)
for row in data:
    if row[5]=="6":
        print(row)
file.close() 
# 4.filter
file=open("water.csv","r")
data=csv.reader(file)
next(data)
for row in data:
    if float(row[2])> 60000:
        print(row)
file.close()
