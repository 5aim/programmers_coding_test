# 내 풀이
# 예상대로라면 control의 리스트 내 원소들을 식 문자열로 변경하고 n을 join해서 eval로 풀어서 계산
# 리스트를 변환할 생각 자체가 잘못됨. 일을 두번하는 꼴임.
# 반복문을 돌면서 원소를 조회하고 원소에 맞는 값을 그대로 n에 산술하면 됨.
# 너무 고민하지말고 최소한으로 풀 방법을 생각해보자
def solution(n, control):
    for i in control:
        if i == "w":
            n += 1
        elif i == "s":
            n -= 1
        elif i == "d":
            n += 10
        elif i == "a":
            n -= 10
    return n


# 방법1
# zip 함수로 원소별 식을 대입해서 dictionary를 만듬
# 결론적으로 value를 모두 더한 값에 n을 더하면 결과 값과 같음.
def solution(n, control):
    key = dict(zip(["w", "s", "d", "a"], [1, -1, 10, -10]))
    return n + sum([key[c] for c in control])


# 방법2
# 처음에 내가 생각한 방법이랑 비슷함.
def solution(n, control):
    control_dict = {"w": "1", "s": "-1", "d": "10", "a": "-10"}
    return eval("+".join(control_dict[letter] for letter in control)) + n
