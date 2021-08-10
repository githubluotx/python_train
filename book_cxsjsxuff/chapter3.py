def train10():
    num = int(input("input the number:"))
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")
    return 0


def train11():
    # high = float(input("input the high(m):"))
    # weight = float(input("input the weight(KG):"))
    # bmi = weight / (high * high)

    # str.split(str="", num=string.count(str))
    # split()指定分隔符对字符串进行切片，如果参数 num 有指定值，则分隔 num+1 个子字符串
    t0, t1 = input("input high and weight(m, KG):").split(",")
    bmi = float(t1) / float(t0) ** 2
    if bmi < 19:
        print("Light")
    elif bmi < 25:
        print("Normal")
    elif bmi < 28:
        print("Overweight")
    else:
        print("Fat")


def train13():
    year = int(input("input the year:"))
    is_leap = ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)
    print(is_leap)


def train14():
    ope1, sym, ope2 = input("input the expression:").split()
    ope1, ope2 = float(ope1), float(ope2)
    if sym == "A":
        print(ope1 + ope2)
    elif sym == "D":
        print(ope1 / ope2)
    elif sym == "S":
        print(ope1 - ope2)
    elif sym == "M":
        print(ope1 * ope2)
    else:
        print("error operator symbol")


def train15():
    """ Fibonacci the first number more than 100
    """
    num = [0, 1, 1]
    while num[2] < 100:
        num[0], num[1] = num[1], num[2]
        num[2] = num[0] + num[1]
    print("the first number more than 100 in Fibonacci is: {}".format(num[2]))


def train16():
    n = int(input("input the n:"))
    sum_n = 0
    for i in range(1, n + 1):
        sum_n = i * 10 + i + sum_n
    print("the sum is: {}".format(sum_n))


def train17():
    price = float(input("input the price of the thing(<=1):"))
    price = 100 - int(price * 100)
    remain = {"50": 0, "20": 0, "10": 0, "5": 0, "2": 0, "1": 0}
    for key in remain.keys():
        remain[key] = int(price / int(key))
        price = price % int(key)
    print("5角:{}, 2角:{}, 1角:{}, 5分:{}, 2分:{}, 1分:{}".format(
        remain["50"], remain["20"], remain["10"], remain["5"], remain["2"], remain["1"]
    ))


def train18():
    score = input("input the score(split by ',':").split(",")
    num = int(score[0])
    total = 0
    qualified = 0
    for idx in range(1 , num + 1):
        add = int(score[idx])
        if add > 59:
            qualified = qualified + 1
            total = total + add
    print("the qualified number is:{}, the sum of score is:{}".format(qualified, total))


def train19():
    total = 0
    for n in range(1000):
        if (n % 3 == 0) and (n % 5 != 0):
            total = total + n
    print("the sum is:{}".format(total))


# train14()
# train15()
# train16()
# train17()
# train18()
train19()
