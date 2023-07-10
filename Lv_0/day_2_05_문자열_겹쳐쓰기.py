# 내 풀이
def solution(my_string, overwrite_string, s):
    answer = my_string[:s] + overwrite_string + my_string[s+len(overwrite_string):]
    return answer

# 방법1
def solution(my_string, overwrite_string, s):
    return my_string[:s] + overwrite_string + my_string[s + len(overwrite_string):]

# 방법2
def solution(my_string, over, s):
    a=list(my_string)
    b=list(over)
    a[s:s+len(b)]=b
    return ''.join(a)