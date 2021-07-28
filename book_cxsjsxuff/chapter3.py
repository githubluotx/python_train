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


train14()
