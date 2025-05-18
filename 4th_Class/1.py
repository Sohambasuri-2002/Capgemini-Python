# wap to print 'KIIT is worst' for 100 times
# i=0
# while i<10:
#     print('KIIT is worst ')
#     i=i+1

# wap to print even numbers between 1 to 100
# i=1
# while i<=10:
#     if (i % 2 == 0):
#         print(i,end=' ')
#     i+=1

# wap to print multiplication tables
# s = int(input('Enter value: '))
# i = 1
# while(i<=10):
#     print(s,'*',i,'=',s*i)
#     i+=1

# wap to find sum of n natural numbers
# s = int(input('Enter value: '))
# i=1
# sum = 0
# while i<=s:
#     sum+=i
#     i+=1
# print(sum)



# wap to find factorial for a given number
# n = int(input('Enter value: '))
# fact = 1
# i=1
# while i<=n:
#     fact*=i
#     i+=1
# print(fact)

# wap to get following output
# s = 'we are good and bad'
# s = input('Enter string : ')
# i=0
# length = len(s)
# while i<length:
#     if (s[i] == ' '):
#         print('_' , end=' ')
#     else:
#         print(s[i], end=' ')
#     i+=1


# wap to extract lowercase characters from the given str 
# s = input('Enter string : ')
# i=0
# out = ''
# while i < len(s):
#     if ('a' <= s[i] <= 'z'):
#         out = out + s[i]
#     i+=1
# print(out)

# wap to extract special charcetrs from a string
# s = input('Enter string : ')
# i=0
# out = ''
# while (i < len(s)):
#     if (not('a' <= s[i]<= 'z' or 'A' <= s[i]<= 'Z' or '0' <= s[i] <= '9')):
#         out = out + s[i]
#     i+=1
# print(out)

# wap to extract only integrs from a given list
# l = [10,345,5.6,True,'KIIT',[1,2,3,4,5]]
# l = eval(input('Enter : '))
# length = len(l)
# i=0
# out = []
# while i<length:
#     if (type(l[i]) == int):
#         out.append(l[i])
#     i+=1
# print(out)



# #wap to get following output
# l = [10,20,True,'hello','eye','level','malayalam']
# l = eval(input('Enter : '))
# out = []
# i=0
# while i<len(l):
#     if type(l[i]) == str:
#         if (l[i] == l[i][::-1]):
#             out.append(l[i])
#     i+=1
# print(out)

# wap to find the sum of individual values of an integer
# num = 123
# sum = 1+2+3 => 6
# num = int(input('Enter number: '))
# sum = 0
# while(num !=0):
#     rem = num%10
#     sum = sum + rem
#     num = num//10
# print(sum)

#wap to remove duplicate values from a given list
# l = eval(input('Enter List : '))
# i=1
# out = []
# while i < len(l):
#     if (l[i] not in out):
#         out.append(l[i])
#     i+=1
# print(out)


#LOOP STATEMENTS

# print(list(range(1,11)))
# print(list(range(0,51,2)))

# a = list(range(1,11))
# print(a)

# col = [10,23,4.5,True,'hello']
# col = {'a':100,'b':200}
# col = 'Good afternoon'
# for val in col:
#     # print(val, col[val])
#     print(val)

# for i in range(1,11):
#     print(i,end=' ')

# l = [1,2,3,4,5,6,7,8,9,10]
# for i in range(0,len(l)):
#     # print(i,end=' ')
#     print(l[i],end=' ')

#wap to print all integers present in a list
# l = eval(input('Enter list : '))
# for i in l:
#     if type(i) is int:
#         print(i)

#wap to find length of colection without using len()
# l = eval(input('Enter list: '))
# lenght=0
# for i in l:
#     lenght+=1
# print(lenght)

#wap to reverse a string wihtout using slicing
# s = input('Enter a string: ')
# for l in range(len(s)-1,-1,-1):
#     print(s[l],end=' ')
# rev = ''
# for i in s:
#     rev = rev + i
# print(rev)

#wap to extract all the even numbers presrnt in a tuple
# t = (1,2,3,4)
# t = eval(input('Enter tuple values: '))
# out = ()
# for num in t:
#     if num % 2 == 0:
#         # print(num, end=' ')
#         out = out + (num,)
# print(out)

# wap to get the following output
# s = 'icon star'
# out = {'icon':4 , 'star':4}
# s = 'icon star'
# length = len(s)
# d = s.split() 
# out = {}
# for i in d:
#     out[i] = len(i)
# print(out)

# wap to get the following output
# s='always keep smilling'
# out={'always':'syawla','keep':'peek'}
# s = input('Enter string: ').split()
# out = {}
# for i in s:
#     out[i] = i[::-1]
# print(out)

# wap to get the following output 
# l = ['jiocinema.com','flipkart.com','file.py','file.java']
# out = ['com','in','py','java']
# l = eval(input('Enter list: '))
# out = []
# for i in l:
#     out.append(i.split('.')[1])
# print(out)

# wap to get the following output 
# l = ['jiocinema.com','flipkart.com','file.py','file.java']
# out = {'com':['jiocinema','flipkart'],'py':[file],'java':['file']}
l = ['jiocinema.com','flipkart.com','file.py','file.java']
out = {}
for name in l:
    s = name.split('.')
    key = s[1]
    val = s[0]
    if key in out:
        out[key].append(val)
    else:
        out[key] = [val]
print(out)

# wap to get the following output
# l = ['hai',34,3.4,'hello','bytebye']
# out = ['hai':'hi','hello':'ho','bytebye':'be']
# l = ['hai',34,3.4,'hello','bytebye']
# out = {}
# for i in l:
#     if type(i) == str:
#         out[i] = i[0] + i[-1]
# print(out)

# wap to get the following 
# s = 'HELLO'
# out = {0:'H',1:'E',2:'L',3:'L',4:'O'}
# s = input('Enter string : ')
# out = {}
# for i in range(len(s)):
#     out[i] = s[i]
# print(out)
#approach 2
# for index,char in enumerate(s):
#     out[index] = char
# print(out)

# wap to get the following output
# s = 'always keep smiling'
# out = 'syawla peek gnilims'
# out = ''
# d = s.split(' ')
# for i in d:
#         out = out + i[::-1] + ' '
#APRROACH 2 : strip() -> removes starting and ending spaces in a string
# for i in d:
#         out += ' ' + i[::-1]
# print(out.strip())
#APPROACH 3 USING JOIN OPERATION
# out = []
# for word in d:
#     out.append(word[::-1])
# print(' '.join(out))



        
