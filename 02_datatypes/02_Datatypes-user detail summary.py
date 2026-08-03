#Datatypes-user detail summary
n=input("Enter Your Name: ")
a=int(input("Enter Your Age: "))
h=float(input("Enter Your Height: "))
s=input("You are a Student True/False: ")
is_student = (s == "True")
print(n,type(n))
print(a,type(a))
print(h,type(h))
print(is_student, type(is_student))
if is_student==True:
    print(f"My name is {n}, I am {a} old, {h} meters height pursuing my studies")
else:
    print(f"My name is {n}, I am {a} old, {h} meters height completed my studies")
