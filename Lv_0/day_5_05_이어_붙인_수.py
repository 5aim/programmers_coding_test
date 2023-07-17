# 내 풀이
# join이 되지 않음.
# 해당 문제에서 중요한 것은 시간복잡도와 숫자를 어떻게 일렬로 합치는지.
def solution(num_list):
    answer = 0
    even = ''
    odd = ''
    for i in num_list:
        # 짝수
        if i % 2 == 0:
            even = ''.join(i)
        # 홀수
        else:
            odd = ''.join(i)
    answer = int(even) + int(odd)
    return answer

# chatgpt 리펙토링
# 리스트의 원소를 짝수 홀수로 나누고 이 수들을 일렬로 이어붙이는 부분에서 막힘.
# 숫자를 일렬로 배열하는데 10승을 함.
def solution(num_list):
    odd_sum = 0
    even_sum = 0
    for num in num_list:
        if num % 2 == 0:
            even_sum = even_sum * 10 + num
        else:
            odd_sum = odd_sum * 10 + num
    return odd_sum + even_sum

# 방법1
# i를 str로 변환해서 a, b에 붙이고 결과값은 int로 출력
def solution(num_list):
    answer = 0
    a=""
    b=""
    for i in num_list:
        if i%2!=0:
            a+=str(i)
        else:
            b+=str(i)
    return int(a)+int(b)

# 방법2
# list변수에 i를 str로 담고 join을 활용해 a를 합치고 int로 result함.
def solution(num_list):
    answer = 0
    a = []
    b = []
    for i in num_list:
        if i % 2 == 0:
            a.append(f"{i}")
        else:
            b.append(f"{i}")
    a = "".join(a)
    b = "".join(b)
    answer = int(a) + int(b)
    return answer

# 방법3
# 가장 기본적으로 풀 경우 위 방법1과 같지만 방법3이 더 보기 좋음.
# 변수이름도 그렇고 한눈에 이해가 되는 점이 방법1과 변수명의 차이인 것 같음.
def solution(num_list):
    even = ""
    odd = ""
    for i in num_list:
        if i % 2 == 0:
            even += str(i)
        else:
            odd += str(i)

    return int(even) + int(odd)