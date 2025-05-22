
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