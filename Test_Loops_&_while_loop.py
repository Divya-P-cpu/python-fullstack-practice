#For loops
#1-Print 1-10-range
for i in range(1,11):
    print(i)
#2-Even Numbers-1-20
for i in range(1,20):
    if i%2==0:
        print(i)
#3-Sum of 1-N
u=int(input("Enter the value"))
s=0
for i in range(1,u):
    s=s+i
print(s)
#4-Multiplication-user
u=int(input("Enter the value"))
for i in range(1,11):
    t=u*i
    print(u,"*",i,"=",t)
    
#5 Vowels-Programming
p="Programming"
s=0
v="aeiou"

for i in p:
    if i in v:
        s+=1

print(s)        
#6-Print squares 1-10
for i in range(1,11):
    z=i**2
    print(i,"square","=",z)
#7-Divisible by both 3 and 5 between 1-50
for i in range(1,50):
    if i%3==0 and i%5==0:
h        print(i,"is divisible by both 3 and 5")
#8-Sum of a list-[4,8,15,16,23,42]
l=[4,8,15,16,23,42]
s=0
for i in l:
    s=s+i
print("Sum if the given list =",s)
#9-Find the Largest Number — Given a list of numbers, find the largest one using a for loop (do not use the max() function).
numbers = [10, 25, 7, 45, 156]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number is:", largest)


#10-Reverse hello
r="Hello"
s=""
for i in range(len(r)):
    z=r[i]
    s=s+z
    y=s[::-1]
print(y)

#1. Countdown from 10 — Print numbers from 10 down to 1 using a while loop.
i=10
while i>=1:
    print(i)
    i-=1
#2. Print 1 to 10 (While) — Same as For Loop Question 1, but implement it using a while loop.
i=1
while i<=10:
    print(i)
    i+=1
#3. Sum Until Zero — Keep asking the user to enter numbers; stop when they enter 0, and print the total sum of all entered numbers.

s=0
while True:
    u=int(input("Enter you guess value"))
    if u!=0:        
        s=s+u       
    else:
        break
print(s)    
#4. Simple Guessing Game — Set a secret number (e.g., 7). Keep looping and asking the user to guess until they get it right, printing "Try again" for each wrong attempt.
g=3
u=int(input("Enter you guess value"))
i=0
while i<=10:
    if g==u:
        print("Correct")
        break;
    else:
        print("Try Again")
        u=int(input("Enter you guess value"))
    i+=1
    
#5. Count Digits in a Number — Given a number like 12345, count how many digits it has using a while loop.
u=789413213

s=0
while u!=0:
    z=u%10
    s=s+1
    u=u//10
    
print(s)
#6-Reverse a number
u=12345
while u!=0:
    z=u%10
    print(z,end='')
    u=u//10
#7-ATM-start with 1000 ask the user to withdraw the amount until the balance is 0
a=1000
while a!=0:
    u=int(input("Enter the value how much you to withdraw"))
    z=a-u
    a=z
    print("Available Balance",a)    
    if a==0:
        
        break
#8-Multiples of 3 upto 30
m=3
i=1
while i<=30:
    print(m,"*",i,"=",m*i)
    i+=1
#9-Factorial given number
u=int(input("Enter the value"))
i=1
z=1
while i<=u:
    z=z*i
    i+=1
print(z)
#10-Correct Password
p=123

i=1
while i<=3:
    u=int(input("Enter the value"))
    if u==p:
        print("Access Granted")
        break
    else:
        print("Access Denied")
    i+=1
    

    
    
    
    
        
      
      
      
      
      
      
    
    
    
    


    

