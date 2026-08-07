#Level 1-5 tasks and theory questions as provided:
#1. Create list fruits...
a=["Apple","Orange","Strawberry","Mango"]
print(a)
#2. Append Grapes.
a.append("Grapes")
print(a)
#3. Insert Pineapple at index 2.
a.insert(1,"Pineapple")
print(a)
a.remove("Orange")
print(a)
#5. Pop last element.
a.pop()
print(a)
a.clear()
print(a)
#7. Copy colors list.
b=["Yellow","Red","Blue"]
a=b.copy()
print(a)
#8. Find length.
print(len(a))
#9. Reverse.
a.reverse()
print(a)
#10. Sort.
a.sort()
print(a)
#11. Extend numbers with 40,50,60.
a.extend([40,50,60])
print(a)
#12. Merge lists using extend.
c=["Hello"]
d=["World"]
c.extend(d)
print(c)
#13. Replace Mumbai with Chennai.
i=["Vizag","Tamil Nadu","Mumbai"]
i[2]=("Chennai")
print(i)
#14. Remove John.
x=["John","Robert","Lisa"]
x.remove("John")
print(x)
#15. Delete Bag by index.
y=["Uniform","Bag","Shoes"]
del(y[1])
print(y)
#16. Find max/min.
k=[10,5,6,45,36,89]
k.sort()
print("Min Value",k[0])
print("Mix Value",k[5])
#17. Find index of Green.
b=["Yellow","Red","Blue","Green"]
c=b.index("Green")
print(c)
#18. Count 10.
z=[1,2,3,4,5,6,7,8,9,10,4,6,20,10]
l=z.count(10)
print("Count of 10 is",l)
#19. Remove first 10.
z=[1,2,3,4,5,6,7,8,9,10,4,6,20,10]
print(z)
z.remove(10)
print("List after removing 1st 10",z)
#20. Reverse list.
z=[1,2,3,4,5,6,7,8,9,10,4,6,20,10]
print(z)
z.reverse()
print("Reversing the list",z)
#21-30: Employee, HR, shopping cart, courses list update tasks.
e=["Ravi","Robert","John","Reena"]
h=["Employee Name","Qualification","Experience","Notice Period","Salary"]
cart=["Shampoo","Detergent","Soaps","HandWash","Snacks"]
courses=["Python Full Stack","Java Full Stack","Data Science","Cybersecurity"]
print(e)
print(h)
print(cart)
print(courses)
e.append("Thomas")
cart.extend(["Biscuits","Dal","Salt"])
print("After adding new employee",e)
print("After updating cart",cart)
cart.remove("Shampoo")
print("After removing from cart",cart)
h.insert(0,"Employee Id")
print("After Updating HR's Details Manual",h)
#31-40: Sort, reverse, clear, backup, max/min/sum, append vs extend tasks..
Details=[45,34,28,93,4,92]
Details_2=[45,34,28,93,4,92]
print(Details)
Details.sort()
print("Arranged Student Details are ",Details)
Details.reverse()
print("Arranged Student Details are ",Details)
Details.sort()
print(Details)
print("Min Value",Details[0])
print("Mix Value",Details[4])

#Sum
"""Details=[45,34,28,93,4,92]
b=Details[0]
c=Details.index(b)
z=len(Details)
sum=0
while c<z:
    sum=sum+b
    print(sum)
    c=c+1
    b=Details[c]"""

Details.append([100,646,55])
print("After adding new elements",Details)
Details.extend([100,646,55])
print("After adding new elements",Details)
Details.clear()
print(Details)
#41-50: Predict outputs for append, extend, copy, pop, insert, assignment, etc.
Details=[1,2,3,5]
Details.append([6,7,8])
print("After adding new elements",Details)#[1,2,3,5,[6,7,8]]
Details.extend([6,7,8])
print("After adding new elements",Details)#[1,2,3,5,[6,7,8],6,7,8]
Details=[1,2,3,5]
b=Details.copy()
print("Copied from one var to another var",b)#[1,2,3,5]
b.pop()
print("Deleted the last element",b)#[1,2,3]
b.insert(2,5)
print("Inserted a value ",b)#[1,2,5,3]
c=b[0]
print("Assigned one value from one list to another list "c)#1
#Theory:
#What is a list? Mutable?-A list is heterogenous datatype, where it is ordered collection of elements in order of various datatypes. And also list supports homogenous
#elements as well
#append-append is a built method where it is used to add element in last index of list,we can add multiple elements but it stores as inner list
#extend-extend is a built method where it is used to add element in last index of list,we can add multiple elements but it stores as same list(continues with existing index elements)
#remove-remove is a built method where it is used to remove the particular element of it's first occurance in list
#pop-pop is a list's in built method where it is used to remove last element of the index value in list
#copy-copy is used to copy the elements from list to another list variable
#=-is a assignment operator where it is used to assign a value to a variable
#sort-sort is a built in method where it is used to sort the list's elements in order either in ascending or descending order
#sorted-
#clear-it is a built in method used to clear all elements in the list
#index-it is used to know the index number of the value in the list
#count-it is used to know number of occurences of a value in the list
#insert-it is used to insert the value in particular index value in list where we want to add
#reverse-it is used to print the elements in reverse order of its original order
#merge lists-it is process of merging of two or more lists into one list
#remove/pop errors-
#copy usage-it is used to copy the elements from one list into another list
#len vs count-length method is used to number of elements in list where the count method is used to know number of occurences of a value in the list

    




    
    


   






