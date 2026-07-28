# print("Welcome")
# for i in range(10):
#     print("Welcome",i)
# for i in range(1,11):
#     print("Welcome",i)   
#  
# for variable in sequence(start,end, steps)
# for variable in sequence(even,end, 2)
# for variable in sequence(odd,end, 2)
# even
for i in range(4,100,2):
    print(i)
# odd
for i in range(7,156,2):
    print("odd numbers:",i)
for i in range(2,20,2):
    print(i**2)    

for i in range(1,9):
    if i==6:
        break
    print(i)
    print("loop ended")

for i in range(1,9):
    if i==2:
        continue
    print(i)

# table
num=int(input("enter any number : "))
for i in range(1,11):
    print(num,"x",i,"=",num*i)

for i in range(5,0,-1):
    print("*"*i)