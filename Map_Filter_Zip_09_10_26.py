#Level 1: Beginner (Questions 1–6)
#Q1 Double every number using map()
l=[1,2,3,5]
z=map(lambda a:a+a,l)
print(list(z))
#Q2 Convert numbers into squares using map()
l=[1,2,3,5]
z=map(lambda a:a**2,l)
print(list(z))
#Q3 Find even numbers using filter()
l=[1,2,3,5]
z=filter(lambda a:a%2==0,l)
print(list(z))
#Q4 Find names containing more than four characters using filter()
l=['sdfsfs','sfdss','dsfsf','sfs']
z=filter(lambda a:len(a)>4,l)
print(list(z))
#Q5 Combine names and ages using zip()
l=['John','Lisa','Harry']
l1=[45,30,25]
z=zip(l,l1)
print(list(z))
#Q6 Add corresponding numbers using zip()
l = [99, 126, 26]
l1 = [45, 30, 25]
result = map(lambda a: a[0] + a[1], zip(l, l1))
print(list(result))
#Q7 Convert Celsius to Fahrenheit using map()
l=[45,57,4]
z=map(lambda a:a*9/5+32,l)
print(list(z))
#Q8 Increase every employee salary by 10% using map()
l=[45000,20000,63000]
z=map(lambda a:a+(a*a/100),l)
print(list(z))
#Q9 Find employees who passed using filter()
l=[45,23,34]
z=filter(lambda a:a>=45,l)
print(list(z))
#Q10 Filter products priced above ₹1,000
l=[1000,4646,600]
z=filter(lambda a:a>1000,l)
print(list(z))
#Q11 Combine employee names and departments using zip()
l=['John','Leena','Harry']
l1=['HR','IT','Sales']
r=zip(l,l1)
print(list(r))
#Q12 Create full names using map() and zip()
l = ['JOHN', 'HARRY', 'Dany']
l1 = ['Mathew', 'CENA', 'Cristanio']
z = map(lambda a: a[0] + " " + a[1], zip(l, l1))
print(list(z))
#Q13 Find numbers greater than 50, then square them
l = [45, 65, 54, 95]
z = map(lambda a: a ** 2, filter(lambda a: a > 50, l))
print(list(z))
#Q14 Find employees whose salaries are above ₹30,000 using zip() and filter()
l1 = [45115, 97464, 449797, 20000]
l = ['John', 'Harry', 'Sarah', 'Henry']
z = filter(lambda a: a[0] > 30000, zip(l1, l))
print(list(z))
#Q15 Convert all names to uppercase using map()
l=['john','Kars','Leena']
z=map(lambda a:a.upper(),l)
print(list(z))

