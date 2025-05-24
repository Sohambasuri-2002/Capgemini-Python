# i=0
# while(i<10):
#     print('kiit is bad')
#     i+=1

# i=0
# while(i<101):
#     if (i%2 == 0):
#         print(i,end=' ')
#     i+=1

# n = int(input('Enter a number: '))
# i=1
# while(i<11):
#     print(i*n,end=' ')
#     i+=1

# n = int(input('Enter a number: '))
# sum = 0
# while(n != 0):
#     sum = sum + n
#     n-=1
# print(sum)

# n = int(input('Enter a number: '))
# fact = 1
# while(n!=0):
#     fact = fact*n
#     n-=1
# print(fact)

# s = 'we are good and bad'
# for i in s:
#     if (i == ' '):
#         print('_',end=' ')
#     else:
#         print(i,end=' ')


# s = 'We are Good and Bad'
# out = ''
# for i in s:
#     if ('a' <= i <= 'z'):
#         out += i
# print(out)

# l = [10,345,5.6,True,'KIIT',[1,2,3,4,5]]
# out = ''
# for i in l:
#     if (type(i) == int):
#         out = out + str(i) + ' '
# print(out)

# l = [10,20,True,'hello','eye','level','malayalam']
# out = ''
# for i in l:
#     if (type(i) == str):
#         if i == i[::-1]:
#             out = out + i + ' '
# print(out)

# n = int(input('Enter a number: '))
# sum = 0
# while(n != 0):
#     rem = n%10
#     sum = sum + rem
#     n //=10
# print(sum)

# s = [10,20,40,10,30,40]
# out = []
# for i in s:
#     if i not in out:
#         out.append(i)
# print(out)

# s = [10,20,40,10,30,40]
# length = 0
# for i in s:
#     length+=1
# print('length is ',length)

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

l = ['jiocinema.com','flipkart.com','file.py','file.java']
# out = ['com','in','py','java']
out = []
for i in l:
    out.append(i.split('.')[1])
print(out)
