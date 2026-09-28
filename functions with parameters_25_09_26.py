#Beginner Practice Tasks
#1. Add Two Numbers
#Create a function add(a, b) that takes two numbers and returns their sum. Example: 10, 20 → 30.
def add(a,b):
    return a+b
print(add(10,20))
#2. Subtract Two Numbers
#Create subtract(a, b) that returns the difference between two numbers. Example: 20, 5 → 15.
def subtract(a,b):
    return a-b
print(subtract(20,5))
#3. Multiply Two Numbers
#Create multiply(a, b) that returns the multiplication result. Example: 5, 4 → 20.
def multiply(a,b):
    return a*b
print(multiply(20,5))
#4. Divide Two Numbers
#Create divide(a, b) that returns the division result. Example: 20, 5 → 4.0.
def divide(a,b):
    return a/b
print(divide(20,5))
#5. Square of a Number
#Create square(n) that returns the square of a number. Example: 5 → 25.
def square(n):
    return n*n
print(square(5))
#6. Cube of a Number
#Create cube(n) that returns the cube of a number. Example: 3 → 27.
def cube(n):
    return n**3
print(cube(3))
#7. Double a Number
#Create double(n) that returns twice the given number. Example: 10 → 20.
def double(n):
    return n+n
print(double(5))
#8. Half of a Number
#Create half(n) that returns half of the given number. Example: 20 → 10.0.
def half(n):
    return n/2
print(half(10))
#9. Check Even or Odd
#Create check_even_odd(n). Return "Even" if the number is even; otherwise return "Odd".
def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(check_even_odd(10))
#10. Check Positive or Negative
#Create check_number(n). Return "Positive" for a positive number and "Negative" for a negative number.
def check_number(n):
    if n>0:
        return "Positive Number"
    elif n<0:
        return "Negative Number"
    else:
        return "Zero"
print(check_number(0))
#11. Check Positive, Negative or Zero
#Create a function that returns "Positive", "Negative", or "Zero" based on the given number.
def check_number(n):
    if n>0:
        return "Positive Number"
    elif n<0:
        return "Negative Number"
    else:
        return "Zero"
print(check_number(0))
#12. Check Pass or Fail
#Create check_result(marks). Return "Pass" when marks are 40 or above; otherwise return "Fail".
def check_result(marks):
    if marks>=40:
        return "Pass"
    else:
        return "Fail"
print(check_result(20))
#13. Check Adult or Minor
#Create check_age(age). Return "Adult" when age is 18 or above; otherwise return "Minor".
def check_age(age):
    if age>=18:
        return "Adult"
    else:
        return "Minor"
print(check_age(10))
#14. Find the Bigger Number
#Create greater(a, b) that returns the bigger of two numbers. Example: 10, 25 → 25.
def greater(a, b):
    if a>b:
        return "A is bigger than B"
    else:
        return "B is bigger than A"
print(greater(25,20))
#15. Find the Smaller Number
#Create smaller(a, b) that returns the smaller of two numbers. Example: 10, 25 → 10.
def smaller(a, b):
    if a<b:
        return "A is smaller than B"
    else:
        return "B is smaller than A"
print(smaller(25,20))
#16. Rectangle Area
#Create rectangle_area(length, width) and return length × width.
def rectangle_area(length, width):
    return length*width
print(rectangle_area(25,12))
#17. Rectangle Perimeter
#Create rectangle_perimeter(length, width) and return 2 × (length + width).
def rectangle_perimeter(length, width):
    return 2 * (length + width)
print(rectangle_perimeter(15,20))
#18. Simple Interest
#Create simple_interest(principal, rate, time). Return (P × R × T) / 100.
def simple_interest(p,r,t):
    return ((p*r*t)/100)
print(simple_interest(200,5000,3))
#19. Total Marks
#Create total_marks(m1, m2, m3) and return the total of three subject marks.
def total_marks(m1, m2, m3):
    return m1+m2+m3
print(total_marks(15,20,30))
#20. Average Marks
#Create average(m1, m2, m3) and return the average of three marks.
def average(m1, m2, m3):
    return (m1+m2+m3)/3
print(average(43,25,30))
#21. Store the Returned Value
#Create add(a, b) using return. Call it with 10 and 20 and store the returned value in a variable called result.
#Print result.
def add(a, b):
    return a+b
result=add(10,20)
print(result)
#22. Use a Returned Value in Another Calculation
#Create add(a, b) using return. Call it with 10 and 20, then multiply the returned value by 5. Expected result:
#150.
def add(a, b):
    return a+b
result=add(10,20)
print(result*5)
#23. Return a Name
#Create get_name() that returns a name. Call it using print(get_name()).
def get_name():
    return "John"
print(get_name())
#24. Return Pass/Fail and Print the Result
#Create a function that returns "Pass" or "Fail". Store the returned value in result and print result.
def func(n):
    if n>=40:
        return "Pass"
    else:
        return "Fail"
res=func(10)
print(res)
#25. Largest of Three Numbers
#Create largest(a, b, c) that returns the largest of three numbers. Example: 10, 25, 15 → 25.
def largest(a, b, c):
    if a>=b and a>=c:
        return "A is bigger"
    elif b>=a and b>=c:
        return "B is bigger"
    else:
        return "C is bigger"
print(largest(10,52,30))
    
        
        
