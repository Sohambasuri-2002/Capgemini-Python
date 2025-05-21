#OBJECT ORIENTED PROGRAMMING
#class
# object
# types of propeties
# constructor
# types of methods
# inheritance  -> code reuasablity
# polymorphism  --> multi behaviour nature
# encapsulation --> data security
# abstraction --> data hiding
# four pillars provide security

# class --> It is a blueprint which is used to store propeties and funcionalities of an object
# object -> It is a real world entity or instance of a class
# syntax:
# class class_name: (pascal)
#     -----------------
#     propeties
#     -----------------
#     funcionalities
#     -----------------

# obj_name = class_name(args)

# EXAMPLE:
# class Demo:
#     a=10
#     b=20

# obj1 = Demo()
# obj2 = Demo()
# obj3 = Demo()

#Accessing propeties of a class
# 1) class_name.propertyname
# 2) obj_name.propertyname
# print(Demo.a,Demo.b)
# print(obj1.a,obj1.b)

# modifying propeties
# class_name.propertyname = new_value
# obj_name.propertyname = new_value

# class Bank:
#     b_name = 'ICICI'
#     ifsc = 'iciv0059'
#     loc = 'bhubaneswar'
# c1 = Bank()
# c2 = Bank()
# print('Bank: ' , Bank.b_name , Bank.ifsc , Bank.loc)
# print('Customer 1 : ' , c1.b_name , c1.ifsc , c1.loc)
# print('Customer 2 : ' , c2.b_name , c2.ifsc , c2.loc)

# Bank.loc = 'Hyderabad'
# c1.loc = 'kolkata'

# print()
# print('After modifying')
# print('Bank: ' , Bank.b_name , Bank.ifsc , Bank.loc)
# print('Customer 1 : ' , c1.b_name , c1.ifsc , c1.loc)
# print('Customer 2 : ' , c2.b_name , c2.ifsc , c2.loc)

# if you try to modify a property using class name it will modify in all the other objects
# if you try to modify a property using object name it will modify in that particular object

# create a class school with some propeties and try with accessing and modification
 
# class school:
#     school_name = 'AGCS'
#     board = 'ICSE'
#     address = 'Haldia'
# s1 = school()
# s2 = school()
# print('School details: ', school.school_name , school.board , school.address)
# print('Student 1 :', s1.school_name , s1.board , s1.address)
# print('Student 2 :', s2.school_name , s2.board , s2.address)

# school.address = 'Kolkata'
# s1.board = 'CBSE'

# print()
# print('School details: ', school.school_name , school.board , school.address)
# print('Student 1 :', s1.school_name , s1.board , s1.address)
# print('Student 2 :', s2.school_name , s2.board , s2.address)

# Types of states/propeties
# 1) class member --> are common for all objects
# Ex: Bank -> name,location,contact,email
# 2) object member --> these are diffrent for all the objects
# Ex: Bank -> name, acno , bank-balance , custid , phno , address

# class Bank:
#     name = 'ICICI'
#     ifsc = 'SBIN008'
#     loc = 'haldia'
# c1 = Bank()
# c2 = Bank()
# c3 = Bank()

# constructor : (__init__) --> initialization method
# 1) it is method which is used to initialize the object member
# 2) __init__ is a self invoking method (no need to call) at the time of object creation it will get called automatically
# 3) It is mandotory to use self as an argument and it should be 1st argument
# 4) Self is used to accept object address automatically
# 5) a/c to convention it is compulsory to use self as argument

# SYNTAX:
# class Cname:
#     def __init__(self,arg1,arg2,...argn):
#         self.arg1=arg1
#         self.arg2=arg2
#         ......
#         self.argn=argn

# class Bank:
#     name = 'ICICI'
#     ifsc = 'SBIN008'
#     loc = 'haldia'

#     def __init__(self,name,acno):
#         self.name = name
#         self.acno = acno

# c1 = Bank('iamfaith',84734378463)
# c2 = Bank('subhadeep',34983949820)
# c3 = Bank('shreyon',2845725878)

# print(c1.name,c1.acno)
# print(c2.name,c2.acno)
# print(c3.name,c3.acno)

# class Zoo:
#     name = 'xyz zoo'
#     loc = 'KIIT'
#     contact = 5539048948
#     email = 'xyz123@gmail.com'

#     def __init__(self,animal_name , gender , age , health_status):
#         self.Animal_Name = animal_name
#         self.Gender = gender
#         self.Age = age
#         self.Health = health_status

# lion = Zoo('Lion','male',18,'healthy')
# dogesh = Zoo('Dog','female',36,'Unhealthy')
# godzilla = Zoo('Godzilla','NA',200,'No disease only destruction')

# print(lion.Animal_Name , lion.Gender , lion.Age , lion.Health)
# print(dogesh.Animal_Name , dogesh.Gender , dogesh.Age , dogesh.Health)
# print(godzilla.Animal_Name , godzilla.Gender , godzilla.Age , godzilla.Health)

# Types of Methods:
# 1) object Methods --> To access and modify object members we will use object method , it is mandatory to pass self as 1st argument , self
# will store object address
# SYNTAX:
# i) objname.methodname(args)
# ii) cname.methodname(objname)

#PLEASE RECTIFY THIS PROGRAM

# class Bank:
#     bname = 'SBI'
#     loc = 'Hyderabad'
#     def __init__(self,name, acno):
#         self.name = name
#         self.acno = acno
#     #object method
#     #To access obj members
#     def display(self):
#         print('Name:', self.name)
#         print('Acno: ',self.acno)
#     #To modify obj members
#     def chnge_name(self):
#         new_name = input('Enter name: ')
#         self.name = new_name

# c1 = Bank('iamfaith',9083676736)
# c2 = Bank('subhadeep', 38928098)
# c3 = Bank('raju',913890282)

# c3.display()
# # c2.display()
# # c3.display()
# c3.chnge_name()
# c3.display


# class Bank:
#     bname = 'SBI'
#     loc = 'bangalore'
#     def __init__ (self,name,acno):
#         self.name = name
#         self.acno = acno
#     #To Access 
#     def display(self):
#         print('Name : ',self.name) # You have to use self keyword everytime inside class
#         print('Acno : ',self.acno)
#     #To update
#     def update(self):
#         new_name = input("Enter Name")
#         self.name = new_name
#     #To access class members
#     @classmethod
#     def disp(cls):
#         print('Bank Name: ',cls.bname)
#         print('Bank loc: ',cls.loc)
#     #To modify class members
#     @classmethod
#     def change_loc(cls,new):
#         cls.loc = new


# c1 = Bank('Sourin',8759063283)
# c2 = Bank('Soham',9123456123)
# c3 = Bank('Sayan',8137110501)

# c3.display()
# c3.update()
# c3.display()
# print(c1)
# print(c2)
# print(c3)

# 2) class method --> To access and modify the class members we will use class method , To create class method it is mandatory 
# @classmethod decorator , it is compulsory to use cls as first argument where cls will store address of class.
# SYNTAX:
# class_name.method_name(args)
# objname.methodname(args)

# 3) Static Method : it is neither related to class nor related to object members it acts as a suportive method , it is mandatory to use
# @staticmethod decorator , no need to use self or cls arguments 
# SYNTAX :
# self.methodname(args) --> to access static methods inside object emthod
# cls.methodname(args) --> to access static methods inside class method

class Bank:
    bname = 'SBI'
    loc = 'bangalore'
    def __init__ (self,name,acno,pin):
        self.name = name
        self.acno = acno
        self.bal = 0
        self.pin=pin
    #To Access 
    def display(self):
        print('Name : ',self.name) # You have to use self keyword everytime inside class
        print('Acno : ',self.acno)
    #To update
    def update(self):
        new_name = input("Enter Name")
        self.name = new_name
    #To access class members
    @classmethod
    def disp(cls):
        print('Bank Name: ',cls.bname)
        print('Bank loc: ',cls.loc)
    #To modify class members
    @classmethod
    def change_loc(cls,new):
        cls.loc = new
    @staticmethod
    def add(bal,amt):
        return bal+amt
    def chck_bal(self):
        pin = int(input('Enter 4 digit pin: '))
        if pin == self.pin:
            print('Account bal is ',self.bal,' Rs ')
        else:
            print('Incorrect pin')
    def deposit(self):
        pin = int(input('Enter a pin: '))
        if pin == self.pin:
            amt = int(input('Enter amount to deposit: '))
            self.bal = self.add(self.bal , amt)
            print(f'amount of {amt} Rs deposited successfully')
        else:
            print('Incorrect pin')
    @staticmethod
    def sub(bal,amt):
        if amt > bal:
            print("Insufficient balance.")
            return bal
        return bal - amt
    def withdraw(self):
        pin = int(input('Enter 4 digit pin: '))
        if pin == self.pin:
            amt = int(input('Enter amount to withdraw: '))
            if (amt <= 0):
                print('Invalid input')
                return
            new_bal = self.sub(self.bal, amt)
            if new_bal != self.bal:
                self.bal = new_bal
                print(f'Amount of {amt} Rs withdrawn successfully.')
        else:
            print('Incorrect pin')
            

c1 = Bank('Sourin',8759063283,1234)
c2 = Bank('Soham',9123456123,9876)
c3 = Bank('Sayan',8137110501,3452)

# c3.display()
# c3.update()
# c3.display()

c1.chck_bal()
c1.deposit()
c1.chck_bal()
