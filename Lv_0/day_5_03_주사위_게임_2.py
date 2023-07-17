# 내 풀이
# 원래 나의 풀이는 위 조건문과 연산식이 맞았지만 첫번째 조건문에 a != b != c를 적었고 다음으로 a == b or a == c or b == c를 적었음.
# 마지막 조건으로 a == b == c 였는데 chatgpt에서 순서를 바꿔서 제시해줌.
# 풀이는 성공적이었으나 답이 제대로 나오지 않아서 시간을 소모함.
# 변수에 미리 값을 할당해주고 나머지 예외를 적는 방법을 항상 염두해두자.
def solution(a, b, c):
    answer = a + b + c
    if a == b == c:
        answer *= (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
    elif a == c or a == b or b == c:
        answer *= a**2 + b**2 + c**2
    return answer


# 방법1
# set으로 중복값 제외하고 check==0은 중복값이 없다는 얘기임.
# check == 2는 하나의 중복값이 있는 것이고 check == 1은 셋 다 같은 숫자란 뜻.
# set을 활용한 기발한 아이디어.
def solution(a, b, c):
    check = len(set([a, b, c]))
    if check == 1:
        return 3 * a * 3 * (a**2) * 3 * (a**3)
    elif check == 2:
        return (a + b + c) * (a**2 + b**2 + c**2)
    else:
        return a + b + c


# 방법2
def solution(a, b, c):
    answer = a + b + c
    if a == b or b == c or a == c:
        answer *= a**2 + b**2 + c**2
    if a == b == c:
        answer *= a**3 + b**3 + c**3
    return answer


# 방법3
# 대부분의 유형이 아래와 같음.
def solution(a, b, c):
    answer = 0
    if a == b == c:
        answer = (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
    elif a == b or a == c or b == c:
        answer = (a + b + c) * (a**2 + b**2 + c**2)
    else:
        answer = a + b + c
    return answer
