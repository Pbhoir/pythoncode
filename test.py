# Student Result Program

name = "Siddhesh"
age = 20
marks = [85, 78, 92, 88, 76]

print("===== STUDENT RESULT =====")
print("Name:", name)
print("Age:", age)

print("\nSubject Marks:")
for i, mark in enumerate(marks, 1):
    print("Subject", i, ":", mark)

total = sum(marks)
average = total / len(marks)

print("\nTotal Marks:", total)
print("Average:", average)

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)

if average >= 40:
    print("Result: PASS")
else:
    print("Result: FAIL")

print("\nPython program executed successfully!")
