# 내 풀이
def solution(number, n, m):
    if 10 <= number <= 100 and 2 <= n and m <= 10:
        return 1 if number % (n * m) == 0 else 0
# >>> 정확성 94.7

# 재시도
def solution(number, n, m):
    if 10 <= number <= 100 and 2 <= n and m <= 10:
        return 1 if number % n == 0 and number % m == 0 else 0

# 방법1
def solution(number, n, m):
    return int(bool(number % n == 0) & bool(number % m == 0))
# bool 함수 숫자입력 : 0 = False, 0이 아닌 모든 숫자 = True
# bool 함수 문자열 : 빈문자열 = False, 비어있지 않은 모든 문자열 = True
# bool 함수 컨테이너 : 비어있으면 = False, 비어있지 않으면 = True
# bool 함수 None : False

# 방법2
def solution(number, n, m):
    return int(number%n == 0 and number%m == 0)