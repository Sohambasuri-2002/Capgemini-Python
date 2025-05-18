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



