# 내 풀이
str = input()

if 1 <= len(str) <= 20:
    print(str.swapcase())

# 방법1
print(input().swapcase())

# 방법2
print(''.join(x.upper() if x == x.lower() else x.lower() for x in input()))


# 방법3
str = input()
a = ''

for s in str :
    if(s.isupper()) :
        a = a + s.lower()
    else : 
        a = a + s.upper()

print(a)

# 방법4
str = input()

answer = ''

for a in str:
    if a.isupper() : answer += a.lower()
    else : answer += a.upper()

print(answer)

# 방법5
str = input()

answer = ""
for i in list(str):
    if i.isupper() == True:
        answer += i.lower()
    else:
        answer += i.upper()

print(answer)

# 할당연산자
# sep, end