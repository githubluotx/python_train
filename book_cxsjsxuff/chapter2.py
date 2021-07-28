"""think and way of programming design homework training
"""
import math


def train_3_12(radius):
    """calculate the volume and surface area of the sphere
    input the radius type: int
    """
    volume = 3 / 4 * math.pi * (radius ** 3)
    surface = 4 * math.pi * (radius ** 2)
    return volume, surface


def train_3_13():
    """calculate the distance between two point
    input:two point coordinate, use tuple type"""
    x1 = int(input("input x1:"))
    y1 = int(input("input y1:"))
    x2 = int(input("input x2:"))
    y2 = int(input("input y2:"))
    dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    print("\n the distance is:%.3f" % dist)


def train_cal_bmi():
    data = input("input the high(m) and weigh(Kg)")
    health = int(data[1]) / (int(data[0]) ** 2)
    if health < 19:
        print("light weight")
    elif health < 25:
        print("normal weight")
    else:
        print("heavy weight")
    return 0


def train_3_14():
    high = float(input("input the high(m):"))
    high = high / 0.305
    high_foot = int(high)
    high_inches = (high - high_foot) * 12
    print("{}foot {:.3f}inches".format(high_foot, high_inches))


def train_3_15():
    """calculate the average of five numbers
    """
    num1 = float(input("input the first number:"))
    num2 = float(input("input the second number:"))
    num3 = float(input("input the third number:"))
    num4 = float(input("input the forth number:"))
    num5 = float(input("input the firth number:"))
    ave = (num1 + num2 + num3 + num4 + num5) / 5
    print("the average is :{}".format(ave))


def train_3_22():
    num2letter = {'5': "A", '4': "B", '3': "C", '2': "D", '1': "E", '0': "F"}
    num = input("input the number:")
    print("the letter is:{}".format(num2letter[num]))


def train_3_23():
    num = int(input("input the grades(0-100):"))
    if num >= 90:
        print("A")
    elif num >= 80:
        print("B")
    elif num >= 70:
        print("C")
    elif num >= 60:
        print("D")
    else:
        print("F")


# train_3_14()
# train_3_15()
# train_3_22()
# train_3_23()
