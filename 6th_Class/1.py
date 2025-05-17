#Take one dict from user key - your frnds name, value - marks/score
# 1) find maximum score pair without using max()
# 2) find minimum score pair without using min()
# 3) sort dict based on value(score) without using sorted()
# 4) take name from user check the name is already present or not if not ask value from user add this 
# pair(key, value) to dict
# 5) remove least score pair

# s = {'Soham':10,'Subhadeep':220,'Utkarsh':100,'fejqs':130}
# max = 0
# for i in s:
#     if (max < s[i]):
#         max = s[i]
# print('maximum number is ',max)
# for minimum number
# min = max
# for i in s :
#     if (min > s[i]):
#         min = s[i]
# print('minimum number is ',min)
# name = input('Enter New Name: ')
# if name not in s:
#     print('no name found')
#     mark = int(input('Enter marks : '))
#     s[name] = mark
# print(s)

# 1) upper()
# 2) islower() -> checks all lowercase characters 
# 3) isupper() -> checks all uppercase characters
# 4) s.capitalize() -> Capitalize first character
s = 'kiit.com'
print(s.split('.'))
# print(s.capitalize())
# print(s.swapcase())
# print('  suiiii  '.strip())
# print('aba'.strip('a'))
# print('aaabb'.removeprefix('a'))
# print('aaabb'.removesuffix('a'))

s = ('Today is a good day'.split())
out = ''
print(s)
for i in s:
    out = out + i[::-1] + ' '
print(out)
