# lambda Function -> is a keyword which is used to solve some simple calculations ,
# ->  we can solve if , if-else problems using lambda , 
# -> lambda is an anonymous or nameless function ,
# -> we have to save or store lambda expression into a variable
# -> It helps us to write code in a single line

# SYNTAX : var = lambda args: expression
#          print(var(value))

#1) wap to check number is even or odd using lambda
# even = lambda num: num%2 == 0
# print(even(13))

#2) wap to check whether a given string palindrome or not 
# check = lambda chck: chck == chck[::-1]
# print(check(input('Enter a string: ')))
#OR
# check = lambda chck: chck == chck[::-1]
# res = check(input('Enter string: '))
# if res:
#     print('Palindrome')
# else:
#     print('not Palindrome')

# 3)wap to check whether a given data is mutable or not 
# mut = lambda s: s in (set,dict,list)
# print(mut(eval(input('Enter any form: '))))

# 4) wap to convert a char into uppercase
# upp = lambda s: s.upper()
# print(upp(input('Enter input : ')))

# 5) wap to find the ascii value of a given character
# asc = lambda s: ord(s)
# print(asc(input('Enter character: ')))

# SYNTAX:  var = lambda args: TSB if cond else FSB
#          print(var(val))

# 6) wap to check whether the last digit of an integer is 5 or not
# chck = lambda s: 'True' if s%10 == 5 else 'False' 
# print(chck(int(input('Enter a number: '))))

# 7) wap to print length of a string if it is palindrome or else reversed string 
# check = lambda s: len(s) if s==s[::-1] else s[::-1]
# print(check(eval(input('Enter a number: '))))

# 8) wap to check whether a given string a keyword or not 
# import keyword
# check = lambda s: 'Keyword' if keyword.iskeyword(s) else 'No keyword'  or keyword = lambda s: 'keyword' if s in keyword.kwlist else 'not'
# print(check(input('Enter keyword: ')))

# 9) wap to take two strings as input. return the concatenated output if both has same length else return concatenated output od=f start
# end char from both the strings
# check = lambda s1 , s2 : s1+s2 if (len(s1) == len(s2)) else s1[0]+s2[0]
# a = input('enter string1 :')
# b = input('enter string2 :')
# print(check(a,b))

# l = [10,50,2,34,21]
# print(sorted(l))

# l = [('rice',300),('dal',250),('fruits',500),('spices',56)]
# print(sorted(l,key = lambda t: t[1] , reverse=True))

# l = ('eye','level','hello','kiit','apple','umbrella')
# print(sorted(l,key=lambda s: s[0] in ('aeiouAEIOU') , reverse=True))


# COMPREHENSIONS  -> It is a process of creating new mutable collection by using single line of instruction.
# --> It is possible only for mutable collections (list , set , dict) because we can modify the existing data
# Types are :-
# 1) List Comprehension --> It is a process of creating a new list collection by using single line of instructions

# SYNTAX :
# 1st priority  --> loops
# 2nd priority --> conditions
# 3rd priority --> storing values

# (i)var = [val for var in collection]
# (ii) var = [val for var in collection if condition]
# (iii) var = [TSB if condition else FSB for var in collection]
# (iv) var = [val for var1 in collection for var2 in collection..... if condition]

# 1) wap to store n natural numbers from 1 to 20
# n = int(input('Enter a number: '))
# out = []
# [i for i in range(1,n+1)]
# print(out)

# 2) store even numbers
# n = int(input('Enter a number: '))
# out = [i for i in range(1,n+1) if i%2==0]
# print(out)

# 3) wap to store of all even numbers and cube of all odd numbers
# out = print([i**2 if i%2==0 else i**3 for i in range(1,11)])
# print(out)

# 4) wap to get the following outpur :
# s = 'program on list compr'
# out = [7,'no','tsil',5]
# s = 'program on list compr'.split()
# out = [i[::-1] if len(i)%2==0 else len(i) for i in s ]
# print(out)

# 5) wap to get output
s='hai'
# out = [('h',0),('h',1),('h',2),('a',0),('a',1)......]
# out = [(i,j) for i in s for j in range(0,len(s))]
# print(out)


# 2) Set Comprehension --> It is a process of creating a new set collection by using single line of instructions
# (i)var = {val for var in collection}
# (ii) var = {val for var in collection if condition}
# (iii) var = {TSB if condition else FSB for var in collection}
# (iv) var = {val for var1 in collection for var2 in collection..... if condition}

# 1)wap to store sqaure of natural nos from 1 to 20
# print({i**2 for i in range(1,51)})

# 2)store all prime nos btw 1 to 100
###### WRONG ##########
# n = int(input('Enter number: '))
# def is_prime(n):
#     for i in range(2,100):
#         if n%i==0:
#             return False
#     else:
#         return True
# print({i for i in range(2,100) if is_prime(i)})



# 3) Dict Comprehension --> It is a process of creating new dictionary collection by using single line of instruction

# zip() --> It is used to iterate through mulyiple collections simultaneously. 
# -->No of variables should be equal to no of collections.
# -->No of iterations should be equal to length of smallest collection
# l1 = [10,20,30,40,50]
# l2 = [100,200,300,400,500]
# for i,j in zip(l1,l2):
#     print(i,j)


# SYNTAX:
# (i) var = {k:v for var in collection} --> 1 col
# (ii) var = {k:v for var1,var2 in zip(col1,col2)} --> 2 col
# (iii) var = {k:v for var in collection if condition}
# (iv) var = {k:v1 if cond else v2 cond for var in collection }

# 1) wap to create a dict where n natural numbers acts as keys and sqaures of natural numbers acts as values
# n=5
# out = {1:1,2:4,3:9,4:16}
# n = int(input('Enter number: '))
# print({i:i**2 for i in range(1,n+1)})

# 2) wap to get the following output 
# l1 = ['a','b','c','d']
# l2 = [100,200,300,400]
# out = {'a':100,'b':200,'c':300,'d':400}
# print({i:j for i,j in zip(l1,l2)})

# 3) wap to get the following output
# s = 'Hai HeLlo'
# out = {'H':72,'L':76,'O':79}
print({i:ord(i) for i in s if i.isupper()})

# 4) wap to get the following output
# print({i:i**3 if i%2!=0 else i**2 for i in range(1,6)})

# 5) wap to get the output
l = [['Bangaore',8000] , ['Mumbai',6000],['hyderabad',5000],['Pune',4000],['Bhubaneswar',7000]]
# i) fetch location and rent where rent is less than 7000
# print({ i[0]:i[1] for i in l if i[1] < 7000})
# ii) fetch location and rent where rent is more than 5000
# print({i[0]:i[1] for i in l if i[1] > 5000})
print({i[0]:i[1] for i in l if i[0][0].lower() == 'b' })

