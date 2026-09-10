#Task-1 3*3 Star Square
for i in range(3):
    for j in range(3):
        print("*",end=' ')
    print()
#Task-2  4*5 Star Square
for i in range(4):
    for j in range(5):
        print("*",end=' ')
    print()
#Task-3  Print 1-3 in every row
for i in range(1,4):
    for j in range(1,4):
        print(j,end=' ')
    print()
#Task-4 Print row number
for i in range(1,4):
    for j in range(1,4):
        print(i,end=' ')
    print()
#Task-5 Print column number
for i in range(1,4):
    for j in range(1,4):0
        print(j,end=' ')
    print()
# Task-6 Right Triangle Pattern
for i in range(1,6):
    for j in range(i):
        print("*",end=' ')
    print()
# Task-7 Inverted Right Triangle
for i in range(5,0,-1):
    for j in range(i):
        print("*",end=' ')
    print()
#Task-8 Number Triangle
for i in range(1,7):
    for j in range(1,i):
        print(j,end=' ')
    print()
#Task-9 Same Number Triangle
for i in range(1,6):
    for j in range(i):
        print(i,end=' ')
    print()
#Task-10 Inverted Number Pattern
for i in range(6,1,-1):
    for j in range(1,i):
        print(j,end=' ')
    print()
#Task-11 Increasing Odd Number Pattern
for i in range(1,7):
    for j in range(1,i):
        print(2*j-1,end=' ')        
    print()
#Task-12 Decreasing same number pattern
for i in range(5,0,-1):
    for j in range(i):
        print(i,end=' ')
    print()
#Task-13 Continous Number Pattern
s=1
for i in range(1,4):
    for j in range(1,4):
        print(s,end=' ')
        s=s+1
    print()
#Task-14 Multiplication Grid
for i in range(1,6):
    for j in range(1,6):
        print(i*j,end=' ')
    print()
#Task-15 Even Number Triangle
for i in range(1,7):
    for j in range(1,i):
        print(2*j,end=' ')        
    print()
#Task-16 Center Pyramid
for i in range(1,7):
    print(" " * (6-i),end='')
    print("* " * i)
#Task-17 Reverse the pyramid
for i in range(6,0,-1):
    print(" " * (6-i),end='')
    print("* " * i)
#Task-18 Hollow Square
for i in range(5):
    for j in range(5):
        if i==1 and j==1 or i==1 and j==2 or i==1 and j==3 or i==2 and j==1 or i==2 and j==2 or i==2 and j==3 or i==3 and j==1 or i==3 and j==2 or i==3 and j==3:
            print(" "*2,end='')
            continue
        else:
            
            print("*",end=' ')
            
    print()

#Task-19 X Pattern
for i in range(5):
    for j in range(5):
        if i==0 and j==0 or i==1 and j==1 or i==2 and j==2 or i==3 and j==3 or i==4 and j==4 or i==0 and j==4 or i==1 and j==3 or i==3 and j==1 or i==4 and j==0:
            print("*",end=' ')
        else:
            print(" ",end=' ')       
    print()
#Task-20 Butteerfly Pattern

for i in range(1, 6):
    for j in range(i):
        print("*", end='')
    
    print(" " * (10 - 2 * i), end='')
    
    for j in range(i):
        print("*", end='')
    
    print()

for i in range(4, 0, -1):
    for j in range(i):
        print("*", end='')
    
    print(" " * (10 - 2 * i), end='')
    
    for j in range(i):
        print("*", end='')
    
    print()


    

