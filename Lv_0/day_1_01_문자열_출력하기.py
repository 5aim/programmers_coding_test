# 내 풀이
str = input()
print(str)

# 방법1 - while문
str = input()
while True:
    if len(str) >= 1 and len(str) <= 1000000 and str != " ":
        print(str)
        break
    else:
        continue


# 방법2 - 함수형
def printinput(str):
    """check input data and print"""
    if str.count(" ") >= 1:
        print("error")
        return False
    if len(str) < 1 and len(str) > 1000000:
        print("error")
        return False
    else:
        return str


str = input()
result = printinput(str)
print(result)

# 방법3 - 조건문
str = input()
if len(str) >= 1 and len(str) <= 1000000:
    print(str)

# 방법4 - 방법3 조건문 shorthand
str = input()
if 1 <= len(str) <= 1000000:
    print(str)
