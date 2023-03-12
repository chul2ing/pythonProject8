
# 3의 배수만 제곱해주기
def Times3(x):
    if x % 3 == 0:
        return True
    else:
        return False

def Func(data):
    t3 = list(filter(Times3, data))
    val = list(map(lambda x: x**2, t3))
    return val

print(Func([1,2,3,4,5,6,7,8,9,10]))

# 양의 수는 양의 수끼리 음의 수는 음의 수끼리 합쳐지는 코드
def sum(*data):
    i = 0
    j = 0
    for k in data:
        if k > 0:
            i += k
        else:
            j += k

    return i,j

print(sum(1,-2,3.6,5,-8.2,4))
print(sum(4,2.5,-2,4))

=====================

def multi(x, y):
    min = x
    max = y

    if min > max:
        min, max = max, min

    result = 1

    for i in range(min, max + 1):
        result += i

    return result

print(multi(1, 100))
print(multi(100, 1))