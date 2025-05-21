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
check = lambda s1 , s2 : s1+s2 if (len(s1) == len(s2)) else s1[0]+s2[0]
a = input('enter string1 :')
b = input('enter string2 :')
print(check(a,b))

