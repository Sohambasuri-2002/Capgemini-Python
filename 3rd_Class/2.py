# print('hello')
# input('message...') --> Take input from console but takes input as string but to take <---int(input())---->
# print() -> prints output in console

# name = input('Enter your name:')
# print('output is ', name)
# print('type is ', type(name))

# age = int(input('Enter age:'))
# print('age is ', age)
# print('type is ', type(age))

# l = list(input('Enter values: '))
# print(l)

#eval -> can take all 9 datatypes
# l = eval(input('enter values: '))
# print(l)
# print(type(l))

# age = int(input('Enter age :'))
# if age > 18:
#     print('Eligible to vote')

# charac = input('Enter character:')
# if (charac == 'a' or charac == 'e' or charac == 'i' or charac == 'o' or charac == 'u') :
#     print('in voewls')
# if charac in 'aeiouAEIOU':
#     print('in voewls')
# if charac not in 'aeiouAEIOU':
#     print('in consonants')

# num = int(input('Enter number:'))
# if (num % 2 == 0):
#     print('Even')

# data = eval(input('Enter value: '))
# if (type(data) is float):
#     print('float')

# data = eval(input('enter data :'))
# if (type(data) is list or type(data) is set or type(data) is dict):
#     print('mutable')

# char = input('enter a character: ')
# if 'A' <= char <= 'Z' :
#     print('In uppercase')
# if 'a' <= char <= 'z' :
#     print('In lowercase')

# data = int(input('Enter data :'))
# if 0 <= data <= 9 :
#     print('in digits')

# wap to chck a character is a special chacter or not
# char = input('Enter a character : ')
# if not ('A' <= char <= 'Z' or 'a' <= char <= 'z' or '0' <= char <= '9'):
#     print('spl charcetr')

# num = int(input('enter a number:'))
# if (num % 2 == 0) :
#     print('Even')
# else :
#     print('Odd')


# num = int(input('enter a number:'))
# if (num % 9 == 0):
#     print('9 possible')
# else:
#     print('not possible')


# char = input('Enter a string : ')
# if char == char[::-1] :
#     print('Palindrome')
# else:
#     print('not palindrome')

# char = input('Enter a string : ')
# if ('A' <= char <= 'Z'):
#     print('uppercase')
# elif ('a' <= char <= 'z'):
#     print('Lowercase')
# elif ('0' <= char <= '9'):
#     print('Digit')
# else :
#     print('Special chacters')

# inte = int(input('Enter digit: '))
# final = str(inte)
# if (len(final) == 1 ):
#     print('one digit')
# elif (len(final) == 2):
#     print('2 digit')
# elif(len(final) == 3):
#     print('3 digit')
# else :
#     print('more than 3 digit')

# n1 = int(input('Enter digit: '))
# n2 = int(input('Enter digit: '))
# n3 = int(input('Enter digit: '))

# if (n1 > n2 and n1 > n3):
#     print(n1,' greatest')
# elif (n2 > n1 and n2 > n3):
#     print(n2,' greatest')
# else :
#     print(n3,' greatest')

# og_username = 'utkrashwsx'
# og_password = 'iloveut'
# username = input('Enter username: ')
# if (username == og_password):
#     password = input('Enter Password: ')
#     if (password == og_password):
#         print('Login success')
#     else:
#         print('Login unsuccess')
# else :
#     print('Username unsuccess')


# name = input('Enter string: ')
# s = len(name)
# if (s % 2 == 0):
#     print('No middle elemnt')
# else :
#     if ('A' <= name[(s//2)] <= 'Z'):
#         print(name[(s//2)])


# sub1 = int(input('Enter first subject: '))
# sub2 = int(input('Enter second subject: '))
# sub3 = int(input('Enter third subject: '))

# if (0 <= sub1 <= 100 and 0<=sub2<=100 and 0<=sub3<=100):
#     if (sub1 > 40 and sub2 > 40 and sub3 > 40):
#         print('Pass in evry subject')
#     else:
#         print('Fail in one subject')
# else :
#     print('Invalid numbers')


# age = int(input('Enter age: '))
# income = int(input('Enter Income: '))

# if (1 <= age <= 120 and 0 <= income <= 100000):
#     if (age >= 60 and income <= 25000) :
#         print('eligible for senior citizen benefits')
#     else :
#         print('Not eligible')
# else :
#     print('Invalid details')

# amount = int(input('Enter amount: '))
# member = input('Enter membership details: ')

# if (0 < amount <= 100000 and member in 'yesYES'):
#         print('You get a 15% discount')
# else:
#         print('No discount')

# member = input('Enter membership: ').lower()
# cart_value = int(input('Enter case value: '))
# num_items = int(input('Enter number items: '))

# if (member is 'premium' or cart_value >= 5000 and num_items >= 3):
#     print("Discount applied")
# else:
#     print("No disocunt")


amount = int(input('Enter amount: '))
balance = int(input('Enter balance: '))

if (amount // 100  and amount <= balance-50):
    print('Withdrawal successful')
else:
    print('Transaction declined')
    
