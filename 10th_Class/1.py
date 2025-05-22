#EXCEPTION HANDLING : It is a process of handling the exceptions or handling the errors
#Exception --> It is an unauthorized event (error) which will interupt the program execution
# Except syntax error remaining all are exception

# Types of error:
# 1) NameError
# 2) ValueError
# 3) TypeError

# Types of Exception Handling:
# 1) Specific Exception Handling:
# 2) generic Exception Handling
# 3) Default Exception Handling

# 1) Specific Exception Handling --> It we know what errors we will get then we will use specific Exception Handling

# SYNTAX :

# try:
#     ---
#     Problem statement
#     ---
# except ErrorName1:
#     solution
# except ErrorName2:
#     solution
# ----
# ----
# except ErrorName;
# solution

# try: It consist of problem statement
# except : It will handle exceptions and the solution for problem must be mentioned here 

# SYNTAX: 
# try:
#     a = int(input('Enter num1 :'))
#     b = int(input('Enter num2 :'))
#     print('Division : ', a/b)
# except ValueError:
#     print('value error should enter only integer type: ')
# except ZeroDivisionError:
#     print('Dividing by zero: cant divide a value by zero')
# print('My imp code is written here')
# print('My imp code is written here')
# print('My imp code is written here')
# print('My imp code is written here')

# try:
#     a = eval(input('Enter val1: '))
#     b = eval(input('Enter val2: '))
#     print(a+b)
# except NameError:
#     print('Name error : Name not defined')
# except TypeError:
#     print('Type error: plss enter same type of data')
# print('My imp code is written here')
# print('My imp code is written here')
# print('My imp code is written here')
# print('My imp code is written here')

# 2) generic Exception Handling : It we dont know what type of error then we can use generic exception handling.
# SYNTAX:
# try:
#     ----
#     PS
#     ----
# except Exception:
#     common
#     solution

# NOTE : exception class handles all types of errors except KeyboardInteruptError. 

# try:
#     # import keyword
#     # print(keyword.kwlist)

    # a = int(input('Enter num1 :'))
    # b = int(input('Enter num2 :'))
#     print(a/b) 
# except Exception as error:
#     print(f'Error: {error} All Exceptions got handled')
# print('My imp code is written here')
# print('My imp code is written here')
# print('My imp code is written here')
# print('My imp code is written here')

# NOTE 
# try:
#     while True:
#         print('Banana')
# except Exception as error:
#     print(f'Error: {error} got handled')

# 3) Default Exception Handling: It we dont know what type of error then we can use default Exception Handling. It will handle all the errors
# including KeyboardInteruptError

# we use alias name to store error 

# SYNTAX: 

# try:
#     ----
#     PROBLEM STATMENT
#     -----
# except:
#     ----
#     common
#     solution
#     -----


# try:
#     # while True:
#     #     print('Banana')

#     a = int(input('Enter num1 :'))
#     b = int(input('Enter num2 :'))
#     print(a/b)
# except:
#     print('All errors got handled')

# try , except , else , finally 

# try:
#     ----
#     PROBLEM STATEMENT
#     ----
# except:
#     solution
# else:
#     alternate Block
# finally:
#     STATEMENT BLOCK

# else : If try dont have error then else will execute
# finally: It is independent on other blocks

# EXAMPLE
# try:
#     a = int(input('Enter num1: '))
#     b = int(input('Enter num2: '))
#     print('sum is ',a+b)
# except:
#     print('All errors got handled')
# else:
#     print('Program has no errors')
# finally:
#     print('Completed')
#     print('My imp code is written here')
#     print('My imp code is written here')
#     print('My imp code is written here')
#     print('My imp code is written here')

# NOTE : Custom Exception Handling : It is a process of creating user-defined errors
# 1) raise  
# 2) assert  

# Creating custom Exceptions using raise keyword:

# SYNTAX :

# raise ErrorName(message)

# Ex:
# class OutofLimit(Exception):
#     pass

# game (num---> 2 and 8)
# num=int(input('Enter a num: '))
# if num<2 or num>8:
#     raise OutofLimit('please enter number greater than and less than 8')
# else:
#     print('Entered correct: ',num)

# without any class 
# num=int(input('Enter a num: '))
# if num<2 or num>8:
#     raise NameError('please enter number greater than and less than 8')
# else:
#     print('Entered correct: ',num)

# NOTE Assertion error: using assert keyword

# SYNTAX :

# assert condition, message

# s=input('Enter string: ')
# assert 'A' <= s[0] <= 'Z' , 'first char should be in uppercase'
# print('String: ',s)

# num = int(input('Enter a num: '))
# assert num>0 , 'Number should be positive'
# print('Correct: ',num)

# --------------------------------------------------------------------------------------------------------------

# MODULES AND PACKAGES

# MODULES --> (i) It is a file which consists of a set of instructions. (ii) direct import no installation. For example : import keyword,
# import time , import math , import random 

# PACKAGE --> (i) Collection of Modules or Folder. (ii) It is mandatory to install a package. For example :( pip install package_name )
# or conda install package_name or pip install numpy , matplotlib , plotly , selenium   

# MODULE HAS TYPES:
# 1) Inbuilt Module --> math , random, keyword, time, itertools
# SYNTAX:
# 1) import module_name
# 2) User-Defined Module


#Accessibility will be given to specific function 

# from math import sqrt,factorial
# print(sqrt(10))
# print(factorial(3))

# 3) from module import *
# Accessibility will be given to all the functions
#use:   fname(args)
# from random import *
# # print(randint(1,10))
# l = ['apple','banana','watermelon']
# shuffle(l)
# print(l)

# print(choice(['salarr','sholay']))

# PACKAGES : It is a collection of modules or folders. It is mandatory to install a package( pip install pandas , pip install numpy)
# TYPES :
# 1) inbuilt package: 


# SYNTAX: 
# 1) from pack1.module1 import fname
# 2) from pack1.module1 import fname1,fname2,....fnamen
# 3) from pack1.module1 import * 
# 4) from pack1 import mod1,mod2.....modn --> 
# mod1.fname(args)
# mod2.fname(args)


# 1) working w.r.t to modules of same package
# 2) working w.r.t to modules of different package


