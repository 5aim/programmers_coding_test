# 내 풀이
str1, str2 = input().strip().split(' ')
if 1 <= len(str1) and len(str2) <= 10:
    str3 = str1 + str2
print(str3)

# 다시 풀었을 때 
str1, str2 = input().strip().split(' ')
if 1 <= len(str1) and len(str2) <= 10:
    print(str1+str2)

# 방법1
print(input().strip().replace(' ', ''))

# 방법2
print(''.join(input().strip().split(' ')))

# 방법3
str1, str2 = input().strip().split(' ')
print(str1, str2, sep='')