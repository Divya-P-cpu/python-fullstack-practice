a,b,c,d,e,f,g="Option 1-Reverse a String","Option 2-Palindrome Check","Option 3-Censor a Word","Option 4-Extract a Substring", "Option 5 Split and Rejoin String (Part A)","Option 6- Split and Rejoin String (Part B)", "Option 7-Truncate text (preview)"
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
i,j,k,l,m,n,o="1", "2", "3", "4", "5", "6", "7"
h="Choose one of the option like Example-1"
print(h)
var1=input("Choose the Option you want")
if var1==i:
    var2=input("Enter the String")
    print(var2[::-1])
elif var1==j:
    var2=input("Enter the Value")
    res=var2[::-1]
    if res==var2:              
        print("It is a palindrome")
    else:
        print("It is not a palindrome")
elif var1==l:
    var2=input("Enter the String")
    var3=int(input("Enter the Start Index Value:"))
    var4=int(input("Enter the Stop Index Value:"))
    print(var2[var3:var4+1:])
elif var1==m:
    var2=input("Enter the String")
    var3=int(input("Enter the 1st Start Index Value to Divide:"))
    var4=int(input("Enter the 2nd Start Index Value:"))
    print(var2[var3:]+var2[:var4])
elif var1==n:
    var2=input("Enter the String")
    var3=int(input("Enter the 1st Start Index Value to Divide:"))
    var4=int(input("Enter the 2nd Start Index Value:"))
    print(var2[var3:]+var2[:var4])
elif var1==o:
    var2=input("Enter the String")
    var3=int(input("Enter Limit from where you should Truncate"))
    print(var2[:var3+1]+"...")
elif var1==k:
    var2=input("Enter the String")
    var3=len(var2)
    print(var2[0]+"*"*(var3-2)+var2[-1])
else:
    print("Invalid")
    
    
     

