#1 SUM OF N NATURAL NUMBERS
# num = int(input('Enter a number: '))
# res = num*(num+1)/2
# print(res)
# sum = 0
# for i in range(0,num+1):
#     sum += i
# print(sum)

#2 SUM OF SQAURES OF N NATURAL NUMBERS
# num = int(input('Enter a number: '))
# res = 0
# for i in range(1,num+1):
#     res =  res + pow(i,2)
# print(res)

#3 EVEN NUMBERS 
# num = int(input('Enter a range: '))
# for i in range(0,num+1):
#     if (i % 2 == 0):
#         print(i,end=' ')

#4 SUM OF DIGITS
# num = int(input('Enter a range: '))
# sum = 0
# while(num != 0):
#     rem = num % 10
#     sum += rem
#     num /= 10
# print(int(sum))

#S5 SUM OF SQUARES
# num = int(input('Enter a range: '))
# sum = 0
# while(num != 0):
#     rem = num % 10
#     sum = sum + pow(rem,3)
#     num = num // 10
# print(sum)

#6 ARMSTRONG NUMBERS 
# num = int(input('Enter a range: '))
# sum = 0
# for i in range(1,num+1):
#     rem = num%10
#     sum *= pow(rem,3)
#     num //= 10
# print(sum)

#7 REVERSE A NUMBER
# num = int(input('Enter a range: '))
# rev = 0
# while(num != 0):
#     rev = (rev*10) + (num%10)
#     num //= 10
# print(rev) 

#8 PALINDROME NUMBERS 
# num = int(input('Enter a range: '))
# rev = 0
# t = num
# while(num != 0):
#     rev = (rev*10) + (num%10)
#     num //= 10
# if (rev == t):
#     print('Palindrome number')
# else:
#     print('Not palindrome number')

# 9 FIBONACCI NUMBERS
# num = int(input('Enter a range: '))
# x = 0
# y = 1
# print(x,end=' ')
# print(y,end=' ')
# for i in range(1,num+1):
#     z = x+y
#     print(z,end=' ')
#     x=y
#     y=z

#10 MAX AND MIN NUMBERS
# num = [4,8,3,7]
# max = num[0]
# for i in range(1,len(num)):
#     if (num[i] > max):
#         max = num[i]
# print(max)

#11 SECOND MAX
# num = [4,8,3,7]
# max = num[0]
# for i in range(1,len(num)):
#     if (num[i] > max):
#         max = num[i]
# print(max)
# num.remove(max)
# print(num)
# max = num[0]
# for i in range(1,len(num)):
#     if (num[i] > max):
#         max = num[i]
# print('second max number is ',max)

# l = [1,2,3,[4,5,6,7,8],(10,20,30,40),'hello world']
# print(l[4][1])
# print(l[-1][1])
# s = 'Hello World'
# print(s[::-1])
# s = 'I live in England'.split()
# print(s)
# out = ''
# for i in s:
#     out = out + i[::-1] + ' '
# print(out)

# s = 'kiit is worst'
# for i in range(1,101):
#     print(s+' ' + str(i))

# for i in range(0,101):
#     if (i % 2 == 0):
#         print(i, end=' ')

# n = int(input('Enter a number: '))
# for i in range(1,11):
#     res = n * i
#     print(res,end=' ')

# n = int(input('Enter a number: '))
# sum = 0
# for i in range(1,n+1):
#     sum = sum + i
# print('Sum of n natural numbers is ', sum)

# s = 'we are good in maths'
# for i in range(0,len(s)):
#     if (s[i] == ' '):
#         print('_',end=' ')
#     else:
#         print(s[i],end=' ')

# num = int(input('Enter a number: '))
# fact = 1
# while(num != 0):
#     fact = fact*num
#     num = num -1
# print('Factorial is ',fact)

# s = input('Enter a string: ')
# out = ''
# for i in s:
#     if ('a' <= i <= 'z'):
#         out = out + i
# print(out)

# s = input('Enter a string: ')
# out = ''
# for i in s:
#     if not ('a' <= i <= 'z' or 'A' <= i <= 'Z' or '0' <= i <= '9'):
#         out = out + i
# print(out)

# l = [10,345,5.6,True,'KIIT',[1,2,3,4,5]]
# out = ''
# for i in l:
#     if type(i) == int:
#         out = out + str(i) + ' '
# print(out)

# l = [10,20,True,'hello','eye','level','malayalam']
# out = ''
# for i in l:
#     if (type(i) == str):
#         if (i == i[::-1]):
#             out = out + i + ' '
# print(out)

# num = int(input('Enter a number: '))
# sum = 0
# while(num != 0):
#     rem = num % 10
#     sum += rem
#     num //=10
# print(sum)

# l = [10,20,10,30,20,40]
# out = ''
# for i in l:
#     if str(i) not in out:
#         out = out +  str(i) + ' '
# print(out)

# l = [10,20,10,30,20,40]
# length = 0
# for i in l:
#     length += 1
# print(length)

# num = int(input('Enter Number: '))
# rev = 0
# while(num != 0):
#     rev = (rev*10) + (num % 10)
#     num //= 10
# print(rev)

# s = 'icon star'.split()
# out = {}
# for i in s:
#     out[i] = len(i)
# print(out)

# s='always keep smilling'.split()
# out = {}
# for i in s:
#     out[i] = i[::-1]
# print(out)

# l = ['jiocinema.com','flipkart.com','file.py','file.java']
# out = []
# for i in l:
#     if i.split('.')[1] not in out:
#         out.append(i.split('.')[1])
# print(out)

# l = ['jiocinema.com','flipkart.com','file.py','file.java']
# out = {}
# for i in l:
#     s = i.split('.')
#     key = s[1]
#     val = s[0]
#     if val in out:
#         out[key].append(val)
#     else :
#         out[key] = [val]
# print(out)

# l = ['hai',34,3.4,'hello','bytebye']
# out = {}
# for i in l:
#     if type(i) == str:
#         out[i] = i[0] + i[-1]
# print(out)

# s = 'HELLO'
# out = {}
# count = 0
# for i in s:
#     out[count] = i
#     count += 1
# print(out)

# num = 6
# for i in range(2,num):
#     if (num % 1 == 0 and num % i == 0):
#         print('Not ')
#         break
# else:
#     print('prime')

# s1 = '111001010'
# s2 = '110001000'
# count = 0
# if len(s1) == len(s2):
#     for i in range(0,len(s1)):
#         if (s1[i] != s2[i]):
#             count += 1
# print(count)

# s = 'bacbcaabbccc'
# out = ''
# for i in s:
#     if i not in out:
#         out = out + i + str(s.count(i))
        
# print(out)