#1. Ternary Operator — 5 Questions
#1. Positive or Negative
#Take a number from the user and use a ternary operator to print "Positive" if the number is greater than or equal to 0, otherwise print "Negative".
n=int(input("Enter the number"))
a="Positive Number" if n>=0 else "Negative Number"
print(a)
#2. Even or Odd
#Take an integer from the user and use a ternary operator to print "Even" or "Odd".
n=int(input("Enter the number"))
a="Even number" if n%2==0 else "Odd Number"
print(a)
#3. Eligible to Vote
#Take the user's age and use a ternary operator to print "Eligible to vote" if age is 18 or above, "Not eligible".
n=int(input("Enter the age"))
a="Eligible to vote" if n>=18 else "Not Eligible"
print(a)
#4. Find the Larger Number
#Take two numbers from the user and use a ternary operator to print the larger number.
n=int(input("Enter the 1st Number"))
m=int(input("Enter the 2nd Number"))
a="n is larger number" if n>m else "m is largest number"
print(a)
#5. Pass or Fail
#Take marks from the user and use a ternary operator to print "Pass" if marks are 35 or above, otherwise "Fail".
n=int(input("Enter you marks"))
a="Pass" if n>=35 else "Fail"
print(a)
#2. Match Case — 5 Questions
#1. Day of the Week
#Take a number from 1–7 and use match-case to print the corresponding day.
#1 → Monday
#2 → Tuesday
#3 → Wednesday
#4 → Thursday
#5 → Friday
#6 → Saturday
#7 → Sunday
n=int(input("Enter the number"))
match n:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid")

#2. Simple Calculator
#Take two numbers and an operator (+, -, *, /) from the user. Use match-case to perform the selected operation.
a=int(input("Enter the 1st number"))
b=int(input("Enter the 2nd number"))
c=input("Enter the operator like + or - or * or /")
match c:
    case "+":
        print(a+b)
    case "-":
        print(a-b)
    case "*":
        print(a*b)
    case "/":
        print(a/b)
    case _:
        print("Invalid")

#3. Menu Selection
#Display the following menu. Take the user's choice and use match-case to print the selected operation.
#1. Add Student
#2. View Student
#3. Update Student
#4. Delete Student
a=input("Choose one of the following option:\n1. Add Student\n2. View Student\n3. Update Student\n4. Delete Student\n")
match a:
    case "Add Student":
        b=input("Enter the data")
        print(b)
    case "View Student":
        c={"Name":"John","Course":"Python","City":"US"}
        print(c)
    case "Update Student":
        d=input("Enter updated data")
        c=list()
        c.append(d)
        print(c)
    case "Delete Student":
        c={"Name":"John","Course":"Python","City":"US"}
        print(c)
        e=input("Enter the key to delete")
        c.pop(e)
        print(c)
    case _:
        print("Invalid")

#4. Grade Description
#Take a grade (A, B, C, D, F) and use match-case to display the corresponding description.
#A → Excellent
#B → Very Good
#C → Good
#D → Needs Improvement
#F → Fail
a=input("Enter your Grade like-(A,B,C,D,F):")
match a:
    case "A":
        print("Excellent")
    case "B":
        print("Very Good")
    case "C":
        print("Good")
    case "D":
        print("Needs Improvement")
    case "F":
        print("Fail")
    case _:
        print("Invalid")

#5. Traffic Signal
#Take a traffic-light color (red, yellow, green) and use match-case to display the corresponding action.
#Red → Stop
#Yellow → Wait
#Green → Go
#Any other value → Invalid signal
a=input("Enter the traffic-light color like-(Red,Yellow,Green):")
match a:
    case "Red":
        print("Stop")
    case "Yellow":
        print("Wait")
    case "Green":
        print("Go")
    case _:
        print("Invalid Signal")
