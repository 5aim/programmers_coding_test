# 내 풀이
def solution(arr):
    if 1 <= len(arr) <= 200:
        answer = ''
        for i in arr:
            answer += ''.join(i)
    return answer

# 방법1
def solution(arr):
    return ''.join(arr)

# 방법2
solution = lambda l: ''.join()

# 방법3
def solution(arr):
    answer = ''
    for i in arr:
        answer += i
    return answer