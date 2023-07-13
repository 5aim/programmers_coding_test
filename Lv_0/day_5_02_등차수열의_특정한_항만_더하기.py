# 내 풀이
# included 반복문, answer 까지는 생각했으나 두 코드를 합치는 방법에서 막혔음.
# a와 d의 등차수열을 리스트로 받고 included의 true의 인덱스 번호와 맞는 부분만 뽑아내려 생각함.
# included의 len만큼 range 
def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        if included[i]:
            answer += a + (i * d)
    return answer

# 방법1
# true, false의 int값을 곱하여 answer에 담는데 이러면 False일 때도 연산이 들어감.
def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        answer += (a + d * i) * int(included[i])
    return answer

# 방법2
# 리스트 컴프리헨션과 enumerate, sum함수를 활용.
# included리스트의 인덱스 i와 해당 요소 f(true, false)를 순회
# 등차수열 a + i * d
def solution(a, d, included):
    return sum(a + i * d for i, f in enumerate(included) if f)

# 방법3
# included[i]를 확인하는 방법의 차이일 뿐 위와 비슷함.
def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        if included[i]==True:
            answer+=a+i*d
    return answer