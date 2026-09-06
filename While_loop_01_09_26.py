#Basic Level — Questions 1 to 7 1.Print Numbers
# Write a Python program using a while loop to print numbers from 1 to 10.
n=1
while n<=10:
    print(n)
    n+=1

#2. Even Numbers Write a program to print all even numbers from 1 to 50.
n=1
while n<=50:
    if n%2==0:
        print(n)
    n+=1
#3. Odd Numbers Write a program to print all odd numbers from 1 to 50.
n=1
while n<=50:
    if n%2!=0:
        print(n)
    n+=1
#4. Reverse Counting Write a program to print numbers from 10 to 1.
n=10
while n>=1:
    print(n)
    n-=1
    
#5. Sum of Numbers Take a number n from the user and find the sum of numbers from 1 to n.
u=int(input("Enter the Number"))
s=0
n=1
while n<=u:
    s=s+n
    n+=1
print(s)
#6. Multiplication Table Take a number from the user and print its multiplication table from 1 to 10.
u=int(input("Enter the Number"))
n=1
while n<=10:
    s=u*n
    print(s)
    n+=1
    


#7. Count Numbers Take a number n from the user and count how many numbers are present between 1 and n.
u=int(input("Enter the Number"))
n=1
s=0
while n<=u:
    s=s+1
    n+=1
print("Digits Present between the", 1,"and",u,"are",s-2)
#Intermediate Level — Questions 8 to 14 8.
#Count Digits Take an integer from the user and find the number of digits using a while loop. Do not use len() or string conversion.
u=int(input("Enter the integer"))
s=0
while u>0:
    t=u%10
    s=s+1
    u=u//10
print(s)

#9. Sum of Digits Take an integer and find the sum of its digits. Example: Input 12345 → Output 15.
a=64646
c=0
sum=0
while a>0:
    r=a%10
    c+=1
    sum+=r
    a=a//10
print(sum)
#10.Reverse a number
u=int(input("Enter the integer"))

while u>0:
    t=u%10
    print(t,end='')
    u=u//10
#11-Palindrome or not
u=int(input("Enter the integer"))
rev=0
t=u
while u>0:
    a=u%10
    rev=rev*10+a
    u=u//10
if rev==t:
    print('Palindrome')
else:
    print('Not palindrome')
#count of even and odd digits
u=int(input("Enter the integer"))
s=0
y=0

while u>0:
    z=u%10
    if z%2==0:
        s=s+1
    else:
        y=y+1
    u=u//10
print("Count of even numbers",s)
print("Count of odd numbers",y)
#Product of digits
u=int(input("Enter the integer"))
s=1
while u>0:
    l=u%10
    s=s*l
    u=u//10
print(s)
#Armstrong number or not
u=int(input("Enter the integer"))
s=1
a=0
t=u
while u>0:
    z=u%10
    s=1
    s=s*(z**3)
   
    a=a+s
    u=u//10

if t==a:
    print("Armstrong Number")
        
else:
    print("Not Armstrong Number")
#Factors of given number
u=int(input("Enter the integer"))
i=1
while i<=u:
    if u%i==0:
        print(i,end=',')
    i+=1
#Perfect number or not
u=int(input("Enter the integer"))
i=1
s=0
while i<u:
    if u%i==0:
        s=s+i
        
    i+=1

if s==u:
    print("Perfecct Number")
        
else:
    print(" Not Perfecct Number")
#Find HCF/GCD
u=int(input("Enter the integer"))
m=int(input("Enter the integer"))
if u<m:
    l=u
else:
    l=m
i=l
while i<=l:
    if u%i==0 and m%i==0:
        print(i)
        break;
    i-=1

#Decimal to Binary
u=int(input("Enter the integer"))
i=0
r=0
s=0
j=1
while u!=0:
    t=u
    print("t value",t)
    z=int(u/2)
    print("z value",z)
    y=t%2
    print("y value",y)
        
    u=z
    print("u value",u)
    r=r*10+y
    s=s+1

    

while j<=s:
    e=r%10
    print(e,end='')
    r=r//10
    j+=1
#Number Guessing Game
u=int(input("Enter the integer"))
c=65

while True:
    if u<c:
        print("Too low")
        u=int(input("Enter the integer"))
    elif u>c:
        print("Too High")
        u=int(input("Enter the integer"))
    elif u==c:
        print("Correct")
        break

        
        
    


    
    

    
    
   

    

        


            
            

    

    




    

    
    
