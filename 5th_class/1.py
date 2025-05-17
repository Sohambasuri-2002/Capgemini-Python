#INTERMEDIATE TERMINATION
#1 PASS KEYWORD
# a = 10
# if a == 10:
#     pass
# for i in range(1,11):
#     pass

#2 BREAK STATEMENT
# for i in range(1,11):
#     if i==6:
#         break
#     print(i)

#1 wap to check given program is prime or not
# s = int(input('Enter number: '))
# count = 0
# for i in range(2,s):
#     if (s % 1 == 0 and s % i == 0):
#         print('not Prime number')
#         break
# else:
#     print('prime')

#2 wap to develop a dynamic login functionality 
# og_username = 'soham'
# og_password = 'iamfaith'
# while True:
#     uname = input('Enter usrename: ')
#     if og_username == uname:
#         pwd = input('Enter Password: ')
#         if (pwd == og_password):
#             print('Login successfull')
#             break
#         else:
#             print('Incorrect password')
#     else:
#         print('Incorrect username')

#random function used to create random numbers
# import random
#random.randint(sv,sv)
# num = random.randint(1,5)
# print(num)

#3 wap for guessing a number game
# import random
# print('Guess a number between 1 to 100: ')
# num = random.randint(1,100)
# while True:
#     guess = int(input('Enter a number: '))
#     if (guess > num):
#         print("ur number is greater")
#     elif (guess < num):
#         print("ur number is lesser")
#     else:
#         print("ur answer is correct")
#         break

#4 wap to check whether a string is having all lowercase characters or not
# s = 'helLo'
# for i in s:
#     if ('a' <= i <= 'z'):
#         pass
#     else:
#         print('Incorrect uppercase found')
#         break
# else:
#     print('all lowercase')

#5 wap to cheack whethe a collection is homogenous or heterogenous
# l = [10,20,30,40,True]
# check_type = type(l[0]) #checking one value with other value
# verify = True
# for i in l:
#     if type(i) == check_type:
#         verify = True
#     else:
#         verify = False
#         break
# if (verify == True):
#     print('homo')
# else:
#     print('hetero')
#APPROACH 2:
# l = eval(input('enter value: '))
# for i in l:
#     if (type(l[0] != type(i))):
#         print('hetero')
#         break
# else:
#     print('homo')
    

#CONTINUE STATEMENTS
# for i in range(1,11):
#     if i==3 or i==7:
#         continue
#     print(i)

#6 wap to print all the odd numbers between 1 to 100 using continue
# for i in range(1,101):
#     if (i % 2 != 0):
#         print(i, end=' ')
#     else:
#         continue

#7 wap to extract all uppercase char from a given string
# s = 'Be the change that you wish to see in the world'
# out = ''
# for i in s:
#     if ('A' <= i <= 'Z'):
#         out = out + i
#     else:
#         continue
# print(out)

#8 wap to get the following output 
#s1 = '111001010'
#s2 = '110001000'
#out = 2
# s1 = "111001010"
# s2 = "110001000"
# count = 0
# if (len(s1) == len(s2)):
#     for i in range(0,len(s1)):
#         if (s1[i] != s2[i]):
#             count +=1
#         else:
#             continue
# print(count)

#DEL KEYWORD
# l = [10,20,30,40]
# del l[2]
# print(l)
# del l[-1]
# print(l)
# del l[-1]
# print(l)
# del l[-1]
# print(l)

#NESTED FOR LOOP
# for i in range(1,6):
#     for j in range(1,6):
#         print(i,j)

#9 wap to get the following output
#s = 'mission impossible'
#output = {'mission': 7, 'impossible': 10}
# s = 'mission impossible'.split()
# out = {}
# for word in s:
#     length = 0
#     for char in word:
#         length +=1
#     out[word] = length
# print(out)
        
#10 wap to get the following output 
#s = 'power star'
#out = {'power':2,'star':1}
# s = 'power star'.split()
# out = {}
# for word in s:
#     count = 0
#     for vowel in word:
#         if (vowel in ('a','e','i','o','u','A','E','I','O','U')):
#             count+=1
#         out[word] = count
# print(out)

#11 wap to check whether a given integer is strong number or not (1,2,145,40585)
# num = int(input('Enter a number: '))
# s = str(num) #145 i = 1
# sum = 0
# for i in s:
#     fact = 1
#     for j in range(1,int(i)+1):
#         fact*=j
#     sum += fact
# print(sum)

# if (sum == num):
#     print('strong')
# else:
#     print('not strong')

#12 wap to get the following output
# s = 'bacbcaabbccc'
# out = 'b4c5a3'
# for i in s:
#     if (i not in out):
#         out = out + i + str(s.count(i))
# print(out)
#APPROACH 2 :
# for i in s:
#     count = 0
#     for j in s:
#         if i == j :
#             count +=1 
#     if i not in out:
#         out = out + i + str(count)
# print(out)    
    
#13 wap to get the following output
# s = {10:'star',20:'bye',30:'oo',40:'apple'}
# out = {10:'a',20:'e',30:'oo',40:'ae'}
# out = {}
# for i in s:
#     vowel = ''
#     for char in s[i]:
#         if (char in ('aeiou')):
#             vowel += char
#     out[i] = vowel
# print(out)









