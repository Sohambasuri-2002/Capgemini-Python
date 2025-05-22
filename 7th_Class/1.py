#1 FUNCTIONS WITHOUT ARGUMENTS AND RETURN VALUES

# WAP to get the following output
# s = '1001001010'
# out = '0110110101'
# def replace():
#     s = input('Enter str: ')
#     out = ''
#     for i in s:
#         if i == str(0):
#             out = out + str(1)
#         elif i == str(1):
#             out = out + str(0)
#         else:
#             out = out + i
#     print(out)
# replace()

# wap to extract only positive integers in a given list
# l =[10,20,-890,True,'hello',[1,2,3,4]]
# out = [10,20]
# def extract():
#     l = [10,20,-890,True,'hello',[1,2,3,4]]
#     out = []
#     for i in l:
#         if (type(i) == int and i > 0):
#             out.append(i)
#     print(out)
# extract()



#2 FUNCTIONS WITH ARGS AND WITHOUT RETURN VALUES

#SYNTAX:
# def fname(arg1,arg2,....argn):
#     ------------
#     SB
#     ------------
# fname(val1,val2,...valn) -> function calling
# wap to get the following output
# s = 'python'
# out = 'ptoyhn'
# def concat(l):
#     out = ''
#     for i in range(0,len(l)):
#         if (i % 2 == 0):
#             out = out + str(l[i])
#     for i in range(0,len(l)):
#         if (i % 2 != 0):
#             out = out + str(l[i])
#     print(out)
# concat(input('Enter string: '))
# APPROACH 2:
# def concat(l):
#     even = ''
#     odd = ''
#     for i in range(0,len(l)):
#         if (i % 2 == 0):
#             even += l[i]
#         else:
#             odd += l[i]
        
#     print(even+odd)
# concat(input('Enter string: '))

# wap to get the following output
# s = '1234567'
# out = '2461357'
# def concat(l):
#     even = ''
#     odd = ''
#     for i in l:
#         if (int(i) % 2 == 0):
#             even += i
#         else:
#             odd += i
#     print(even+odd)
# s = input('Enter string: ')
# concat(s)

#3 FUNCTIONS WITHOUT ARGS AND WITH RETURN VALUES
# SYNTAX :
# def fname():
#     --------
#     SB
#     --------
#     return val1,val2,...valn
# var1 , var2 ,... varn = fname()
# def com():
#     a = int(input('Enter : '))
#     b = int(input('Enter : '))
#     return a+b , a-b
# sum,diff = com()
# print(sum,diff)

#wap to check whether a given number is armstrong or not
# def arms():
#     num = int(input('Enter num: '))
#     temp = num
#     sum = 0
#     while(num != 0):
#         rem = num % 10
#         sum = sum + pow(rem,3)
#         num //= 10
#     if (temp == sum):
#         return 1
#     else:
#         return 0
# number = arms()
# if (number == 1):
#     print('Armstrong ')
# else:
#     print('Not Armstrong')

#wap to print all the prime numbers btw 2 to 100
# def Prime():
#     out = []
#     for num in range(2, 101):
#         count = 0
#         for i in range(2, num):
#             if num % i == 0: #HERE WE CHECK FOR NON PRIME NUMBERS
#                 count += 1
#                 break
#         if count == 0:
#             out.append(num)
#     return out
# l = []
# l = Prime()
# print(l)

#4 FUNCTIONS WITH ARGS AND WITH RETURN VALUES
# SYNTAX :
# def fname(arg1,arg2,....argn):
#     --------
#     SB
#     --------
#     return val1,val2,...valn
# var1 , var2 ,... varn = fname(val1,val2,...valn)
# var = fname(val1,val2,...valn)
# print(fname(val1,val2,...valn))

# wap to extract only  NDV from given list
# l = [90,80,0.0,0j,False,'hii',7+8j,'',[],{}]
# out = [90,80,'hii',7+8j]

# def nonde(s):
#     out = []
#     for i in s:
#         if bool(i): #DEFAULT VALUES ALWAYS RETURN FALSE AND NDV RETURNS ALWAYS TRUE
#             out.append(i)
#     return out

# l = [90,80,0.0,0j,False,'hii',7+8j,'',[],{}]
# # l = eval(input('Enter a list : '))
# out = []
# out = nonde(l)
# print(out)

# wap to check whether a number is spy number or not
# num = 123
# sum = 1+2+3 = 6
# mul = 1*2*3 = 6
# sum == pro ->spy


# def spynum(num):
#     sum = 0
#     pro = 1
#     while(num != 0):
#         rem = num % 10
#         sum = sum + rem
#         pro = pro * rem
#         num //= 10
#     if (sum == pro):
#         return 'Spy'
#     else:
#         return 'Not spy'
# num = int(input('Enter number: '))
# res = spynum(num)
# print(res)

#GLOBAL AND LOCAL VARIABLES 
# a=100
# b=200
# def sam():
#     print(a,b)
# sam()


#GLOBAL VARIABLES
# a=100
# b=200
# def sam():
#     global a #DECLARES A GLOBALLY ACROSS THE FUNCTION
#     a=1000
#     b=2000
#     print('Inside; ',a,b)
# print('befor mod ',a,b)
# sam()
# print('after mod ',a,b)

#LOCAL VARAIBLES
# def sam():
#     a=100
#     b=200
#     def inner():
#         nonlocal a,b
#         a=1000
#         b=2000
#         print('nested: ',a,b)
#     print('before mod: ',a,b)
#     inner()
#     print('after mod: ',a,b)
# sam()






