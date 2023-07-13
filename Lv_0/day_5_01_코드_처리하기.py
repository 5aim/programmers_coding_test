# 내 풀이
def solution(code):
    mode = True
    ret = ""

    for i, n in enumerate(code):
        if mode and i % 2 == 0 and n != '1':
            ret += n
        elif not mode and i % 2 != 0 and n != '1':
            ret += n
        elif n == '1':
            mode = not mode

    return ret if ret else "EMPTY"

# 방법1
def solution(code):
    return "".join(code.split("1"))[::2] or "EMPTY"

# 방법2
def solution(code):
    answer = ''

    mode = 0
    for i in range(len(code)):
        if code[i] == '1':
            mode ^= 1
        else:
            if i % 2 == mode:
                answer += code[i]

    return answer if answer else 'EMPTY'

# 방법3
def solution(code):
    mode = 0
    ret = ""
    
    for idx in range(len(code)):
        if mode == 0:
            if code[idx] != "1":
                if idx % 2 == 0:
                    ret += code[idx]
            else:
                mode = 1
        else:
            if code[idx] != "1":
                if idx % 2 != 0:
                    ret += code[idx]
            else:
                mode = 0
    
    if not ret:
        return "EMPTY"
    
    return ret

# 방법4
def solution(code):
    mode = 0
    ret = ""

    for idx, char in enumerate(code):
        if (mode == 0 and idx % 2 == 0 and char != "1") or (mode == 1 and idx % 2 != 0 and char != "1"):
            ret += char
        elif char == "1":
            mode = 1 - mode

    return ret if ret else "EMPTY"