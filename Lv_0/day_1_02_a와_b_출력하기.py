# 내 풀이
a, b = map(int, input().strip().split(" "))
if -100000 <= a and 100000 >= b:
    print("a =", a)
    print("b =", b)

a, b = map(int, input().strip().split(" "))
if -100000 <= a and 100000 >= b:
    print("a = " + str(a))
    print("b = " + str(b))

# 방법1
a, b = map(int, input().strip().split(" "))
print(f"a = {a}\nb = {b}")

# 방법2
a, b = map(int, input().strip().split(" "))
print("a = {}\nb = {}".format(a, b))

# 방법3
a, b = map(int, input().strip().split(" "))
print("a = {}".format(a))
print("b = {}".format(b))

# 방법4
a, b = map(int, input().strip().split(" "))
print("""a = %d""" % a)
print("""b = %d""" % b)
