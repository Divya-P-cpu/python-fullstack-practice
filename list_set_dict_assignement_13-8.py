#Part 1 — Python Lists
#1. Create a list containing 10 student names. Write a program to add a new student at the end, insert another student at the beginning,
#and remove one student by name. Display the final list.
l=["John","Robert","Thomas","Alaska","Chris","Leena","Max","Nimmy","Julie","Harry"]
l.append("Mitsey")
l.insert(3,"Sara")
l.remove("Leena")
print(l)
#2. Given the list numbers = [12, 5, 8, 21, 5, 30, 8, 15], write a program to find the maximum value, minimum value, total sum,
#and average of the numbers without using external libraries.
import statistics
numbers = [12, 5, 8, 21, 5, 30, 8, 15]
print("Maximum Value: ",max(numbers))
print("Manimum Value: ",min(numbers))
print("Total Value: ",sum(numbers))
print("Avg Value: ",statistics.mean(numbers))
"""
#3. Given numbers = [10, 20, 10, 30, 40, 20, 50], write a program to create a new list containing only unique values while preserving their original order.
m=[10, 20, 10, 30, 40, 20, 50]
n=m.index(10)
while n<=7:
    if m==n

"""
#4. Given a list of numbers, write a program to separate the even numbers and odd numbers into two different lists. Display both lists and their counts.
l=[1,2,3,4,5,6,7,8,9,10]
a=l.index(1)
x=list()
y=list()
m=list()
n=list()
while a<=9:
    if l[a]%2==0:
        x.append(l[a])
        c=x.count(l[a])
        m.append(c)
    else:
        y.append(l[a])
        d=y.count(l[a])
        n.append(d)
    a+=1
print("Even Numbers: ",x)
print("Count of each element in Even Number list: ",m)
print("Odd Numbers",y)
print("Count of each element in Odd Number list: ",n)
#5. Given marks = [78, 45, 92, 66, 35, 88, 55], write a program to sort the marks in ascending and descending order, then display the top three marks.
marks = [78, 45, 92, 66, 35, 88, 55]
marks.sort()
print("Marks in ascending order:",marks)
marks.reverse()
print("Marks in descending order:",marks)
print("Top three highest marks",marks[:3])
#Part 2 — Python Sets
#1. Create two sets: python_students and sql_students. Find and display the students who are learning both Python and SQL.
s1={"John","Robert","Thomas","Leena"}
s2={"Chris","Leena","John","Edison","Albert"}
print("Students enrolled in both courses",s1&s2)
#2. Using two sets of student names, find the students who are learning Python but not SQL. Also find the students who are learning SQL but not Python.
s1={"John","Robert","Thomas","Leena"}
s2={"Chris","Leena","John","Edison","Albert"}
print("Students enrolled in one course",s1^s2)
#3. Create a set from a list containing duplicate values. Write a program to remove the duplicates and then display the number of unique values.
s={1,4,3,8,4,9,5,4}
print(s)
print("Number of unique values are",len(s))
#4. Given two sets of numbers, demonstrate union, intersection, difference, and symmetric difference. Display the result of each operation with clear labels.
s={1,45,6,7,9,2,6,4}
s1={4,6,7,2,6,4,9,2,50}
print("Set-1",s)
print("Set-2",s1)
print("Union-Concating 2 sets:",s|s1)
print("Intersection-Common values from 2 sets:",s&s1)
print("Difference-Returns elements from set-1 where they are not in set 2:",s-s1)
print("Difference-Returns elements from set-1 where they are not in set 2 and vice versa:",s^s1)
#5. Create a set of employee IDs. Write a program that accepts an employee ID from the user and checks whether that ID exists in the set.
#Display an appropriate message such as 'Employee ID found' or 'Employee ID not found'.
s={101,102,103,104,105,106}
s1=set(input("Enter your Employee-Id"))
a=s.isdisjoint(s1)
if a==True:
    print("Employee ID found")
else:
    print("Employee ID not found")
#Part 3 — Python Dictionaries
#1. Create a dictionary containing a student's name, age, course, and marks.
#Write a program to add a new key called city, update the marks, and display all key-value pairs.
d={"Name":"John","Age":22,"Course":"Cloud","Marks":72}
print(d)
d.update({"City":"Nellore"})
print("After adding the city:",d)
d["Marks"]=80
print("After updating marks",d.items())


#2. Create a dictionary containing employee names as keys and their salaries as values.
#Write a program to find and display the employee with the highest salary and the employee with the lowest salary.
import statistics
d1={"John":20000,"Robert":50000,"Leena":30000,"Kia":60000}
x=list(d1.values())
x.sort()
x.reverse()
print("Highest Salary",x[0])
print("Lowest Salary",x[3])

#3. Given sales = {'Monday': 12000, 'Tuesday': 15000, 'Wednesday': 9000, 'Thursday': 18000, 'Friday': 14000},
#find the total sales, average sales, and day with the highest sales.
sales = {'Monday': 12000, 'Tuesday': 15000, 'Wednesday': 9000, 'Thursday': 18000, 'Friday': 14000}
x=list(sales.values())
print("Total sales are:",sum(x))
print("Average sales",statistics.mean(x))
x.sort()
x.reverse()
print("Highest Salary",x[0])

"""#4. Create a dictionary from two lists: names = ['Asha', 'Ravi', 'John'] and marks = [85, 72, 91].
#The names should become keys and the marks should become values. Display the resulting dictionary.
names = ['Asha', 'Ravi', 'John']
marks = [85, 72, 91]
a=dict.fromkeys(names)"""


#5. Create a dictionary to store department-wise employee salaries. Example: {'IT': [45000, 55000, 60000], 'HR': [40000, 48000], 'Sales': [35000, 50000, 65000]}.
#Write a program to calculate the total salary and average salary for each department.
import statistics
e={'IT': [45000, 55000, 60000], 'HR': [40000, 48000], 'Sales': [35000, 50000, 65000]}
z=list(e.items())
print("Total salary of IT Department",sum(e['IT']))
print("Total salary of HR Department",sum(e['HR']))
print("Total salary of Sales Department",sum(e['Sales']))
print("Average salary for IT Department",statistics.mean(e['IT']))
print("Average salary for HR Department",statistics.mean(e['HR']))
print("Average salary for Sales Department",statistics.mean(e['Sales']))














    




