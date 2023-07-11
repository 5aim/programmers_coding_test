# 내 풀이
def solution(str1, str2):
    if 1<= len(str1) and len(str2) <= 10:
        answer = ''
        for i in range(0, len(str1)):
            answer += str1[i] + str2[i]
    return answer

# 방법1
def solution(str1, str2):
    answer = ''.join([str1[i] + str2[i] for i in range(len(str1))])
    return answer

# 방법2
def solution(str1, str2):
    res=''
    for s1,s2 in zip(str1,str2):
        res+=s1+s2
    return res

# 방법3
def solution(str1, str2):
    answer = []
    for i in range(len(str1)):
        answer.append(str1[i])
        answer.append(str2[i])
    return ''.join(answer)

# 방법4
def solution(str1, str2):
    answer = ''
    for i in range(len(str1)):
        answer += str1[i]
        answer += str2[i]         
    return answer