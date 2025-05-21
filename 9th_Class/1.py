#Polymorphism --> It is a process of making two methods of same name to behave in two different ways
# + -- > svd(sum)  mvd(concatenation)

# Poly -> many
# Morphy -> forms

# 1) Method overrding (run time polymorphism) --> if we have two methods of the same name. Previous method will be overided with the 
# latest method 
# Method overloading is not possible in python. if you try to do method overloading it will act like method overiding

# def add(a,b):
#     print(a+b)
# def add(a,b,c):
#     print(a+b+c)
# # add(10,20)
# add(1,2,3)


# if i want to have add(a,b) we have monkey patching
# for example
# def add(a,b):
#     print(a+b)
# prev=add # MONKEY PATCHING
# def add(a,b,c):
#     print(a+b+c)
# prev(1,2) 

#example :
# class A:
#     def add(self,a,b):
#         print(a+b)
# class B(A):
#     def add(self,a,b,c,d):
#         print(a+b+c+d)
# obj1 = A()
# obj2 = B()
# obj1.add(10,50)
# obj2.add(10,20,100,5.6)

# 2) operator overloading --> It is a process of making the operators to work on objects of user defined class by invoking respective 
# magic methods
# Ex: __add__ , __sub__

# class A:
#     def __init__(self,a):
#         self.a=a
#     def __add__(self , other):
#         return self.a + other.a
#     def __sub__(self , other):
#         return self.a - other.a
#     def __mul__(self , other):
#         return self.a * other.a
#     def __truediv__(self , other):
#         return self.a / other.a
#     def __floordiv__(self , other):
#         return self.a // other.a
#     def __mod__(self , other):
#         return self.a % other.a
#     def __pow__(self , other):
#         return self.a**other.a
# obj1 = A(100)
# obj2 = A(200)
# print(obj1+obj2)
# print(obj1-obj2)
# print(obj1*obj2)
# print(obj1/obj2)
# print(obj1//obj2)

# ENCAPSULATION --> It is a process of wraaping up the data together to provide security by using access specifier
# Access Specifier  -> It tell us whether a user can access a data outside the class or not. There are three types - public , provate and 
# protected
# Protected --> It works just like public it will not provide security. To create a protected member we have to use _ before variable 
# name or member name
#Private --> It provides security to the data. provate member cannot be accesed outside the class. To create a private member we have to use
# __(double underscore) before var_name or methodname
# To access private members outside 
# SYNTAX:  obj/cname._cname__var


#ABSTRACTION --> It is a process of hiding the implementation from the user by providing only functionality
# IMP TERMS:
# 1) abstractmethod : It contains only function declaration but not 
# 2) abstract class : 
# 3) concrete class : 


#General syntax for abtraction 
# from abc import ABC, abstractmethod   #abc --> abstract base class
# class abs_class(ABC):
#     @abstractmethod
#     def  method_name():
#         pass
#     @abstractmethod
#     def method_name():
#         pass
# class concrete_class(abs_class):
#     --------------
#     SB
#     --------------

