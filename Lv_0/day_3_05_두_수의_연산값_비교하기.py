# 내 풀이
def solution(a, b):
    return max(int(str(a) + str(b)), 2 * a * b)

# 방법1
def solution(a, b):
    if int(str(a) + str(b)) < 2*a*b:
        return 2*a*b
    else:
        return int(str(a) + str(b))

# 방법2
def solution(a, b):
    res = int(str(a) + str(b))
    comp = 2*a*b
    return max(res,comp)