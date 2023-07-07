# 내 풀이
a, b = input().strip().split(" ")
b = int(b)
if 1 <= len(a) <= 10 and 1 <= b <= 5:
    print((a) * b)

# 방법1
a, b = input().strip().split(" ")
b = int(b)

result = a * b
print(result)

# 방법3
a, b = input().strip().split(" ")
b = int(b)

print(a * b)

# 방법2
a, b = input().strip().split(" ")
print(a * int(b))
