# 내 풀이
def solution(a, b):
    if int(str(a) + str(b)) < int(str(b) + str(a)):
        return int(str(b) + str(a))
    else:
        return int(str(a) + str(b))

# 방법1
def solution(a, b):
    return int(max(f"{a}{b}", f"{b}{a}"))

# 방법2
def solution(a, b):
    a, b = str(a), str(b)
    return int(max(a+b, b+a))