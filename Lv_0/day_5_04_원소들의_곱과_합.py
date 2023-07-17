# 내 풀이
# else: answer = 0을 써줘야 함.
def solution(num_list):
    answer = 0
    if 2 <= len(num_list) <= 10:
        num = 0
        a = 1
        b = 0
        for i in num_list:
            a *= i
            b += i
            if a < (b**2):
                answer = 1
            else:
                answer = 0
    return answer


# chatgpt 리펙토링
def solution(num_list):
    if 2 <= len(num_list) <= 10:
        product = 1
        total = sum(num_list)
        for num in num_list:
            product *= num
        if product < total**2:
            return 1
    return 0


# 방법1
# 리스트 원소의 합의 제곱을 s변수에 할당하고 리스트 원소의 곱을 m변수에 할당하였음.
# eval을 사용해서 num_list의 원소들을 나열하고 중간에 *으로 join하였음.
# return에서 shorthand로 값을 출력함.
def solution(num_list):
    s = sum(num_list) ** 2
    m = eval("*".join([str(n) for n in num_list]))
    return 1 if s > m else 0


# 방법2
# else문을 작성하지 않아도 return이 되는건가??
def solution(num_list):
    a = 1
    b = 0
    for x in num_list:
        a *= x
        b += x
    if a < b * b:
        return 1
    return 0


# 방법3
# math import는 생각도 못했다..
import math


def solution(num_list):
    answer = 0
    if math.prod(num_list) < (sum(num_list) ** 2):
        answer = 1
    return answer
