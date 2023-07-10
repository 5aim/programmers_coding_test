# 내 풀이
a, b = map(int, input().strip().split(' '))
if 1 <= a and b <= 100:
    c = a + b
print(a, "+", b, "=", c)

# 방법1 format함수 활용
a, b = map(int, input().strip().split(' '))
c = a + b
print('{} + {} = {}'.format(a, b, c))

# 방법2 f string 활용
a, b = map(int, input().strip().split(' '))
print(f"{a} + {b} = {a + b}")