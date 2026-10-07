#1. Square of a number Task: Write a lambda function that accepts a number and returns its square.
z=lambda a:a**2
print(z(20))
#2. Cube of a number Task: Write a lambda function that accepts a number and returns its cube.
z=lambda a:a**3
print(z(20))
#3. Check even number Task: Write a lambda function that returns True if a number is even, otherwise False.
z=lambda a:True if a%2==0 else False
print(z(50))
#4. Check odd number Task: Write a lambda function that returns True if a number is odd, otherwise False.
z=lambda a:True if a%2!=0 else False
print(z(50))
#5. Add two numbers Task: Write a lambda function to add two numbers.
z=lambda a,b:a+b
print(z(45,20))
#6. Subtract two numbers Task: Write a lambda function to subtract the second number from the first.
z=lambda a,b:a-b
print(z(45,20))
#7. Multiply two numbers Task: Write a lambda function to multiply two numbers.
z=lambda a,b:a*b
print(z(45,20))
#8. Find the larger number Task: Write a lambda function that returns the larger of two numbers.
z=lambda a,b:a if a>b else b
print(z(15,43))
#9. Find the smaller number Task: Write a lambda function that returns the smaller of two numbers.
z=lambda a,b:a if a<b else b
print(z(15,43))
#10. Check positive or negative Task: Write a lambda function that returns 'Positive', 'Negative', or 'Zero'.
z=lambda a:"Positive" if a>0 else "Negative" if a<0 else "Zero" 
print(z(0))
#11. Find the maximum of three numbers Task: Write a lambda function to return the largest among three numbers.
z=lambda a,b,c:a if a>b and a>c else b if b>a and b>c else c
print(z(10,25,30))
#12. Calculate simple interest Task: Write a lambda function to calculate Simple Interest using P, R, and T.
z=lambda p,t,r:(p*t*r)/100
print(z(15,36,45))
#13. Convert Celsius to Fahrenheit Task: Write a lambda function to convert Celsius into Fahrenheit.
z=lambda c: (c * 9 / 5) + 32
print(z(45))
#14. Check divisibility by 5 Task: Write a lambda function that returns True when a number is divisible by 5.
z=lambda a:True if a%5==0 else False
print(z(45))
#15. Calculate area of a circle Task: Write a lambda function to calculate the area of a circle using radius.
z=lambda a:3.14*a**2
print(z(45))
#16. Calculate total price Task: Write a lambda function that accepts price and quantity and returns total price.
z=lambda q,p:q*p
print(z(2,560))
#17. Apply discount Task: Write a lambda function that accepts price and discount percentage and returns the final price.
z=lambda p,d:p-(p*d/100)
print(z(456,12))
#18. Check whether a number is a multiple of 10 Task: Write a lambda function that returns True if a number is a multiple of 10.
z=lambda a:True if a%10==0 else False
print(z(45))
#19. Find the last character Task: Write a lambda function that accepts a string and returns its last character.
z=lambda a:a[-1]
print(z("John"))
#20. Convert a string to uppercase Task: Write a lambda function that accepts a string and returns it in uppercase.
z=lambda a:a.upper()
print(z('John'))
