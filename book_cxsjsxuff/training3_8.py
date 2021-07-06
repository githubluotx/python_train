"""think and way of programming design homework training
"""
import math
import re


def train_2_8_12(radius):
    """calculate the volume and surface area of the sphere
    input the radius type: int
    """
    volume = 3 / 4 * math.pi * (radius ** 3)
    surface = 4 * math.pi * (radius ** 2)
    return volume, surface


def train_2_8_13():
    """calculate the distance between two point
    input:two point coordinate, use tuple type"""
    x1 = int(input('input x1:'))
    y1 = int(input('input y1:'))
    x2 = int(input('input x2:'))
    y2 = int(input('input y2:'))
    dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    print('\n the distance is:%.3f' % dist)


def train_3_8_():
    num = int(input("input the number:"))
    if num > 0:
        print("Positive")
    elif num < 0:
        print('Negative')
    else:
        print("Zero")
    return 0


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


# Train_JudgePosOrNag()
# Train_CalBMI()
# print(str(train_2_8_12(4)))
# train_2_8_13()

s = 'ERRC_PHY_tttt'
if re.match('ERRC_PHY', s):
    print(True)
else:
    print(False)
