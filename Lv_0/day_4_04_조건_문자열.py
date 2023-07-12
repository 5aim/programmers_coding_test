# 내 풀이
# 처음엔 ineq, eq를 풀어내서 n ineq eq m 순서대로 bool()함수에 넣으려 했음.
def solution(ineq, eq, n, m):
    if (ineq == "<" and eq == "=" and n <= m) or (ineq == ">" and eq == "=" and n >= m):
        return 1
    elif (ineq == "<" and eq == "!" and n < m) or (ineq == ">" and eq == "!" and n > m):
        return 1
    else:
        return 0

# 방법1
def solution(ineq, eq, n, m):
    return int(eval(str(n)+ineq+eq.replace('!', '')+str(m)))

def solution(ineq, eq, n , m):
    return int(eval(f"{n} {ineq}{eq} {m}"))
# eval()은 문자열로 표현된 파이썬 코드를 실행하는 역할을 함. 주어진 문자열을 파이썬 코드로 해석하고 해당 코드를 실행
# 유연성과 편의성이 있으나 보안관련 이슈가 있음.
# 외부입력을 포함하는 문자열을 eval()에 전달하면 악의적인 코드 실행에 취약해질 수 있음.
# 따라서 eval()사용시 신중하게 검증된 입력을 하거나 보안에 신경을 써야함.

# 방법2
def solution(ineq, eq, n, m):
    answer = 0
    if n > m and ineq ==">":
        answer = 1
    elif n < m and ineq == "<":
        answer = 1
    elif n == m and eq == "=":
        answer = 1

    return answer

# 방법3
def solution(ineq, eq, n, m):
    answer = 0

    if (ineq, eq) == ('<', '='):
        answer = int(n <= m)
    elif (ineq, eq) == ('>', '='):
        answer = int(n >= m)
    elif (ineq, eq) == ('<', '!'):
        answer = int(n < m)
    elif (ineq, eq) == ('>', '!'):
        answer = int(n > m)
    else:
        return 'wrong input'

    return answer