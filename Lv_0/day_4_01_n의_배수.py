# 내 풀이
def solution(num, n):
    if 2 <= num <= 100 and 2 <= n <= 9:
        if num % n == 0:
            return 1
        else:
            return 0

# 방법1
def solution(num, n):
    return int(not(num % n))

# python not() : 논리연산을 수행하는 함수. 단일 인자를 받으며, 해당 인자의 논리 상태를 뒤집어주는 역할임.
# 만약 인자가 True인 경우 False를 반환, 인자가 False인 경우 True를 반환
# 주로 조건문에서 사용되며 조건의 부정을 나타내는데 유용.
# 아래 예시 코드
x = 10

if not(x > 5):
    print("x는 5보다 크지 않습니다.")

# 방법2
def solution(num, n):
    return int(num % n == 0)

# 방법3
def solution(num, n):
    return 1 if num % n == 0 else 0

# 방법 4
def solution(num, n):
    return 1 if not num % n else 0