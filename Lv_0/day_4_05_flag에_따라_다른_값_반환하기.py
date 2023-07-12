# 내 풀이
# True는 1, False는 0을 알고 난 후 flag == 1 을 썼다는게 참...ㅋㅋㅋ
def solution(a, b, flag):
    answer = 0
    if -1000 <= a and b <= 1000:
        if flag == 1:
            answer = (a + b)
        else:
            answer = (a - b)
    return answer

# 방법1
def solution(a, b, flag):
    if flag: return a+b
    return a-b

# 방법2
def solution(a, b, flag):
    return a + b if flag else a - b

# 방법3
def solution(a, b, flag):
    answer = 0
    if flag==True:
        answer=a+b
    else:
        answer=a-b
    return answer