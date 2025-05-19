#TYPES OF ARGUMENTS
#1 POSITIONAL ARGUMENTS
# def add(a,b):
#     print(a+b)
# add(10,20) 

# #2 DEFAULT ARGUMENTS
# def sam(a,b,c=0): # HERE C=0 IS DEFAULT ARGUMENT
#     print(a+b+c)
# sam(10,20)

#3 KEYWORD ARGUMENTS
# def sam(a,b,c):
#     print(a,b,c)
# sam(c=30,b=20,a=10)

#4 VARIABLE LENTGH ARGS
# def sam(*a,**b): #HERE REFER TO THE COPY FOR FURTHER DETAILS
#     print(a,b)
# sam(10,20,30,40,x=50,y=98,z=77)


#RECURSION
# Syntax : 
# def fname(args):
#     if term:
#         return val
#     -----------
#     SB
#     -----------
#     return fname(args)
# print(fname(values))

# def sam(n=5):
#     if n <= 0:
#         return
#     print('hello')
#     sam(n-1) #recursive call
# sam() 

#wap to find factorial
# def facto(n):
#     if (n == 0):
#         return 1
#     else:
#         return n*facto(n-1)
    
# num = facto(int(input('Enter number: ')))
# print(num)

#converting looping programs to recursion
#wap to extract lowercase characters from a given string
# def extract(s,out='',i=0):
#     if i >= len(s):
#         return out
#     if ('a' <= s[i] <= 'z'):
#         out = out + s[i]
#     return extract(s,out,i+1)
# s = input('Enter a string: ')
# print(extract(s))

#wap to get the following output
# s = '1001010101&*^'
# out = '0110101010&*^'
# def replacing(s,out='',i=0):
#     if (i >= len(s)):
#         return out
#     if s[i] == '0':
#         out = out + str(1)
#     elif s[i] == '1':
#         out = out + str(0)
#     else:
#         out = out + str(i)
#     return replacing(s,out,i+1)
# s = input('Enter string: ')
# print(replacing(s))

#FUNCTION OBJECTS 
# In Python
# 1) Functions can be passed to variables
# 2) Functions can be passsed as arguments to another function

# def sam():
#     print('Hello world')
# print(sam)

# def greetings(name):
#     return f"Hello good afternoon {name}"
# say_hello = greetings
# print(say_hello('KIIT STUDENTS'))

def evaluate(fname,num):
    return fname(num)
def square(n):
    return n*n
num = int(input('Enter a num: '))
print(evaluate(square,num))
