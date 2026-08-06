print("\n----- Grocery List Manager -----")
print("1. View List")
print("2. Remove Item")
print("3. Count Items")
print("4. Sort List")
print("5. Reverse List")
print("6. Clear List")
print("7. Exit")

a = input("Enter your list: ").split(",")# Take list input from the user
for i in range(len(a)):
    a[i] = a[i].strip()
z=int(input("Choose one of the Menu from 1-7 "))
if z==1:
    print("Grocery List is ",a)    
elif z==2:
    b = input("Enter the items to remove: ")
    if b in a:
        a.remove(b)# Remove an item
        print("Final List ",a)
    else:
        print("Not there") 
elif z==3:
    print("Number of items are ",len(a))# Display list length
elif z==4:
    print("Arranged List",sorted(a))# Sort the list
elif z==5:
    a.reverse()# Reverse the list
    print("Reversing the list",a)
elif z==6:
    print("Clearing the list",a.clear())# Clear the list
else:
    print("Thank you for using Grocery List Manager!")




