#Task 1: Student & Address Management
class Address:
  def __init__(self,city,state,pincode):
    self.city=city
    self.state=state
    self.pincode=pincode
    print("City",self.city)
    print("State",self.state)
    print("Pincode",self.pincode)
class Student():
  def __init__(self,name,age):
    self.name=name
    self.age=age
    print("Name:",self.name)
    print("Age:",self.age)
    o=Address('Hyderabad','Telangana',450046)
o1=Student('John',45)
#Task 2: Employee & Department Management-17-11-2026
  class Department():
  def __init__(self,department_name,department_location):
    self.department_name=department_name
    self.department_location=department_location
    print("Department_Name:",self.department_name)
    print("Department_Location:",self.department_location)
class Employee():
  def __init__(self,employee_name,employee_id,salary):
    self.employee_name=employee_name
    self.employee_id=employee_id
    self.salary=salary
    print("Employee_name:",self.employee_name)
    print("Employee_id:",self.employee_id)
    print("Salary:",self.salary)
    o=Department("IT","Hyderabad")
o1=Employee("John",101,50000)
#Task 3: Car & Engine Management
class Engine():
  def __init__(self,engine_type,horsepower):
    self.engine_type=engine_type
    self.horsepower=horsepower
    print("Engine Type:",self.engine_type)
    print("Horsepower:",self.horsepower)
class Car():
  def __init__(self,car_brand,car_model):
    self.car_brand=car_brand
    self.car_model=car_model
    print("Car Brand:",self.car_brand)
    print("Car Model:",self.car_model)
    o=Engine("1.0L","70HP")
o1=Car("BMW","Maybach")
    
    
    
