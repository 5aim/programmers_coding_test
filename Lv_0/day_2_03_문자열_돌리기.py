# 내 풀이
str = input()
if 1 <= len(str) <= 10:
    for i in str:
        print(i)

# 다시 풀었을 때 
str = input()
if 1 <= len(str) <= 10:
    print('\n'.join(str))

# 방법1
print('\n'.join(input()))

# 방법2
for a in input():
    print(a)