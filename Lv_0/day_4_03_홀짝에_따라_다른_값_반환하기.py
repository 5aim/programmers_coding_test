# 내 풀이
# 짝/홀 구분, range 반복문까지는 갔으나 sum()함수를 몰라서 시간을 소비함.
# sum()함수를 쓸 생각을 했더라면...
# 방법 3이 가장 비슷했는데 뭔가 풀이과정의 인내를 못참고 chatgpt돌린거 같다..
def solution(n):
    answer = 0
    if 1 <= n <= 100:
        if n % 2 == 0:
            answer = sum(i**2 for i in range(2, n+1, 2))
        else:
            answer = sum(range(1, n+1, 2))
    return answer

# 방법1
def solution(n):
    return sum(x ** (2 - x % 2) for x in range(n + 1) if n % 2 == x % 2)

# 방법2
def solution(n):
    if n%2:
        return sum(range(1,n+1,2))
    return sum([i*i for i in range(2,n+1,2)])

# 방법3
def solution(n):
    answer = 0
    if n%2:
        for i in range(1,n+1,2):
            answer += i
    else:
        for i in range(2,n+1,2):
            answer += i**2
    return answer