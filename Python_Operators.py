#Task 1 — Arithmetic Operators
a=25
b=4
# Find and print:
print(a,b)
# Addition
print("Addition",a+b)
# Subtraction
print("Subtraction",a-b)
# Multiplication
print("Multiplication",a*b)
# Division
print("Division",a/b)
# Floor division
print("Floor Division",a//b)
# Modulus
print("Modulus",a%b)
# Power
print("Power",a**b)
#Task 2 — Assignment Operators
x = 10
# Using assignment operators, perform:
# Add 5
x+=5
print("Addition",x)
x = 10
x-=3
print("Subtraction",x)
x = 10
x*=2
print("Multiply",x)
x = 10
x/=4
print("Divide",x)
x = 10
x%=3
print("Modulus",x)
#Task 3 — Comparison Operators
a = 15
b = 10
# Write expressions using:
# >
print("a is greater than b",a>b)
# <
print("A is lesser than b",a<b)
# >=
print("a is greater than or equal to b",a>=b)
# <=
print("A is lesser than or equal to b",a<=b)
# ==
print("A is equal to b",a==b)
# !=
print("A is not equal to b",a!=b)
#Task 4 — Logical Operators
age = 25
salary = 50000
# Write expressions using:
# and
print("Value by using AND operator",age<salary and salary>age)
# or
print("Value by using OR operator",age<salary or salary<age)
# not
print("Value by using NOT operator",not age)
#Task 5 — Identity Operators
a = [10, 20]
b = a
c = [10, 20]
# Check:
print(a is b)
print(a is c)
print(b is c)
print(a == b)
print(a == c)
# Question:
# Why are a is c and a == c different?
#Here in a is c it was checking the objects address or location while a==c is checking or comparing the values in the objects
#Task 6 — Membership Operators
numbers = [10, 20, 30, 40, 50]
# Check whether:
# 20 exists in the list
print(20 in numbers)
# 60 exists in the list
print(60 in numbers)
# 30 does not exist
print(30 not in numbers)
# 100 does not exist
print(100 not in numbers)
#Task 7 — Bitwise Operators
a = 10
b = 6
# Find:
print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a << 1)
print(a >> 1)
print(bin(a))
print(bin(b))
#Task 8 — Predict the Output
a = 10
b = 20
print(a + b)
print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a < b and b > 15)
print(a > b or b > 15)
print(not(a > b))

#Task 9 — Mixed Operators
a = 10
b = 5
c = 10
print(a + b * 2)#Compund Assignment Operator
print(a > b and c == a)#Logical Operator
print(a == c or b > c)#Logical Operator
print(a is c)#Identical Operator
print(a in [5, 10, 15])#Membership
print(a & b)#Bitwise Operator
#Task 10 — Real Challenge
a = 20
b = 10
numbers = [10, 20, 30]
x = a
# Write a program containing at least one example of:
# Arithmetic operator
print("Arithmetic Operator",a+b)
# Assignment operator
b*=2
print("Assignment Operator",b)
# Comparison operator
print("Comparison operator",a>b)
# Logical operator
print("Logical Operator",a>b and a<b)
# Identity operator
print("Identity Operator",a is b)
# Membership operator
print("Membership Operator",20 in numbers)
# Bitwise operator
print("Bitwise Operator",a|b)






