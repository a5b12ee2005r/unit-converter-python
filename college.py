import college
print(college.student)
print(len(college.student))

# Task 2

student=["Hamna","Hafsa","Zainab","Horria","Maryam"]
print(student)
# add
student.append("Hajra")
print(student)
# remove
student.remove("Hafsa")
print(student)
# update
student[2]="Ayesha"
print(student)
# total student
print(len(student))


# Task 3

student=("23","Computer science","4th")
print(student)
# indexing
print(student[0])
print(student[1])
print(student[2])
# Error
# student[1]="cybersecuirty"
# note
# Tuples are immutable,so their value cannot be changed.

# Task 4
club={"computer science society","Arts","media","community","caligraphy"}
print(club)
# add
club.add("science")
print(club)
# remove
club.remove("computer science society")
print(club)

if "Arts" in club:
    print("Arts club exits")
else:
    print("Arts does not club")









    