
def call():
    print("1-Addition")
    print("2-Subtraction")
    print("3-Multiplication")
    print("4-Division")
    print("0-Exit")
call()
z=int(input("Choose one of the option"))

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def exit():
    print("Exiting")


if z == 1:
    x = int(input("Enter 1st value"))
    y = int(input("Enter 2nd value"))
    print("Addition result:", add(x, y))

elif z == 2:
    x = int(input("Enter 1st value"))
    y = int(input("Enter 2nd value"))
    print("Subtraction result:", sub(x, y))

elif z == 3:
    x = int(input("Enter 1st value"))
    y = int(input("Enter 2nd value"))
    print("Multiplication result:", mul(x, y))

elif z == 4:
    x = int(input("Enter 1st value"))
    y = int(input("Enter 2nd value"))
    if y == 0:
        print("Cannot divide by zero")
    else:
        print("Division result:", div(x, y))

elif z == 0:
    exit()

else:
    print("Invalid option")

    
    
    
    
    
    


    



