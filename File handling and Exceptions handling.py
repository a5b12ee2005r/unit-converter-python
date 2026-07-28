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


