#Level 1: Functions Without Parameters
#1. Create a function welcome() that prints "Welcome to Python".
def welcome():
    print("Welcome to Python")
welcome()
#2. Create a function greet() that prints "Hello Students".
def greet():
    print("Hello Students")
greet()
#3. Create a function display_name() that prints your name.
def display_name():
    print("John")
display_name()
#4. Create a function show_course() that prints "Python Full Stack".
def show_course():
    print("Python Full Stack")
show_course()
#5. Create a function institute() that prints your institute name.
def institute():
    print("10000Coders")
institute()
#Level 2: Functions With One Parameter
#6. Create a function greet(name) that prints "Hello" along with the name.
def greet(name):
    print("hello",name)
name="John"
greet(name)
#7. Create a function square(n) that prints the square of a number.
def square(n):
    print(n**2)
square(n=5)
#8. Create a function display_age(age) that prints the age.
def display_age(age):
    print(age)
display_age(age=53)
#9. Create a function student(name) that prints "Student Name:" along with the name.
def student(name):
    print("Student Name:",name)
student(name="Teena")
#10. Create a function double(n) that prints double the given number.
def double(n):
    print(n+n)
double(n=10)
#Level 3: Functions With Two Parameters
#11. Create a function add(a, b) that prints the sum of two numbers.
def add(a,b):
    print(a+b)
a=10
b=20
add(a,b)
#12. Create a function subtract(a, b) that prints the subtraction of two numbers.
def subtract(a,b):
    print(a-b)
a=40
b=20
subtract(a,b)
#13. Create a function multiply(a, b) that prints the multiplication of two numbers.
def multiply(a,b):
    print(a*b)
a=10
b=20
multiply(a,b)
#14. Create a function divide(a, b) that prints the division of two numbers.
def divide(a,b):
    print(a/b)
a=10
b=20
divide(a,b)
#15. Create a function student(name, age) that prints the student's name and age.
def student(name,age):
    print("Student's Name:",name,",","Age:",age)
student(name='John',age=23)
#Level 4: Real-Time Beginner Tasks
#16. Create a function employee(name, salary) that prints the employee's name and salary.
def employee(name,salary):
    print("Employee Name:",name,",","Salary:",salary)
name='Leena'
salary=25000
employee(name,salary)
#17. Create a function rectangle(length, width) that prints the area of a rectangle.
def rectangle(length,width):
    print(length*width)
length=45
width=20
rectangle(length,width)
#18. Create a function total_marks(m1, m2, m3) that prints the total marks.
def total_marks(m1,m2,m3):
    print(m1+m2+m3)
m1=12
m2=23
m3=50
total_marks(m1,m2,m3)
#19. Create a function bill(price, quantity) that prints the total bill amount.
def bill(price,quantity):
    print(price*quantity)
price=1500
quantity=2
bill(price,quantity)
#20. Create a function course(student_name, course_name) that prints the student's name
#and course name.
def course(student_name,course_name):
    print("Student Name:",student_name,",","Course_name:",course_name)
student_name='John'
course_name='Python Full Stack'
course(student_name,course_name)
