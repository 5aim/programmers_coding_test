# 내 풀이
a = int(input())
if 1 <= a <= 1000:
    if a % 2 == 0:
        print(f'{a} is even')
    else:
        print(f'{a} is odd')

# 다시 풀었을 때 
a = int(input())
if 1 <= a <= 1000:
    print(f"{a} is {'even' if a % 2 == 0 else 'odd'}")

# 방법1
n=int(input())
print(f"{n} is {'eovdedn'[n&1::2]}")

# 방법2
N = int(input())
print(f"{N} is {'even' if N % 2 == 0 else 'odd'}")

# 방법3
a = int(input())
print(f'{a} is', 'odd' if a % 2 else 'even')