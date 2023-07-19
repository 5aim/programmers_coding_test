# 내 풀이
def solution(num_list):
    if num_list[-1] > num_list[-2]:
        num_list.append(int(num_list[-1]) - int(num_list[-2]))
    else:
        num_list.append(int(num_list[-1]) * 2)
    return num_list


# int로 변환하지 않고 작성해도 동작함.
def solution(num_list):
    if num_list[-1] > num_list[-2]:
        num_list.append(num_list[-1] - num_list[-2])
    else:
        num_list.append(num_list[-1] * 2)
    return num_list


# chatgpt 리펙토링
# 시간복잡도는 위와 아래가 같기 때문에 큰 리펙토링은 필요하지 않은 것으로 판단됨.
# 참고로 int로 굳이 변환하지 않아도 산술식은 동작되기 때문에 굳이 int로 변환할 필욘 없음.
def solution(num_list):
    last_num = int(num_list[-1])
    second_last_num = int(num_list[-2])

    if last_num > second_last_num:
        num_list.append(last_num - second_last_num)
    else:
        num_list.append(last_num * 2)

    return num_list


# 방법1
def solution(l):
    l.append(l[-1] - l[-2] if l[-1] > l[-2] else l[-1] * 2)
    return l
