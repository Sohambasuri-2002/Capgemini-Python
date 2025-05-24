# 1) wap to keep summing the digits of a number until a single digit is left.
# s = 9875
# num = int(input("Enter a number: "))  # Input a number
# while num >= 10:  
#     sum = 0
#     while num > 0:
#         rem = num % 10
#         sum += rem
#         num //= 10
#     num = sum 
# print("Single digit sum is:", num)

# 2) Write a program to print the following series till n terms.


# n = int(input('Enter a range: '))
# out = ""
# for i in range(n):
#     out += "2"
#     if i < n :
#         print(out, end=",")



# 3) Write a program to get the following output 
#  output= {‘com’: [‘jiocinema’, ‘amazon’], ’py’:[ ‘file’ , ‘text’] , ‘html’:[‘web’]}

# s = ['jiocinema.com' , 'file.py' , 'web.html' , 'amazon.com' , 'text.py']
# out = {}
# for word in s:
#     s = word.split('.')
#     key = s[1]
#     val = s[0]
#     if key in out:
#         out[key].append(val)
#     else:
#         out[key] = [val]
# print(out)

# 4) wap to check the given number is Armstrong or not without using type casting.
# Input: n= 153
# Output: 1**3 + 5**3+ 3**3 = 153 (Armstrong)

# n = int(input('Enter a number: '))
# temp = n
# sum = 0
# while(n != 0):
#     rem = n%10
#     sum = sum + pow(rem,3)
#     n //= 10
# if (temp == sum):
#     print('armstrong number')
# else:
#     print('not armstrong number')

# 5) wap to find all elements that appear more than once in a list.
# Input: [4,3,2,7,8,2,3,1] → Output: [2,3]

# s = eval(input('Enter a list: '))
# out = []
# for i in s:
#     if i not in out:
#         if s.count(i) > 1:
#             out.append(i)
# print(out)
    

# 6) wap to get the following output
# Input: [100,200,50,400,300]
# N=300
# Out = [[100,200],[300]]

# l = [100,200,300,400,500,200]
# n = 600
# out = []
# for i in l:
#     if i == n:
#         out.append([i])
#     else:
#         for j in l:
#             if i+j == n and [i,j] not in out and [j,i] not in out:
#                 out.append([i,j]) 
# print(out)



# 7) wap in functions to get the following output
# Input: ‘bacbcaabbaa’
# Output: ‘b4a5c2’

# n = input('Enter s string: ')
# out = ''
# for i in n:
#     if i not in out:
#         length = n.count(i)
#         out = out + i + str(length)
# print(out)


# 8) write a function to check whether the given number is a strong number or not
# N= 145 → 1!+4!+5!= = 145
# n = int(input('Enter a number: '))
# temp = n
# sum = 0
# while(n != 0):
#     rem = n%10 # 5
#     fact = 1
#     while(rem!=0): # 51=0
#         fact = fact*rem
#         rem = rem -1
#     sum = sum + fact
#     n //= 10
# if (temp == sum):
#     print('strong number')
# else:
#     print('not strong number')

# 9) wap to get the following output
# L = [‘hai’, 34, 3.4, ‘hello’, 90, ‘byebye’]
# Out = {‘hai’: ‘hi’, ‘hello’ :’ho’, ‘byebye’: ‘be’

# l = ['hai',34,3.4,'hello',90,'byebye']
# out = {}
# for i in l:
#     if (type(i) == str):
#         out[i] = i[0] + i[-1]
# print(out)

# 10) wap to find maximum value present in a list without using any sorting 
# functions

# l = [1,122,5,17,4,9]
# l = eval(input('Enter a list: '))
# max = l[0]
# for i in range(1,len(l)):
#     if (l[i] > max) :
#         max = l[i]
# print(max)


    






