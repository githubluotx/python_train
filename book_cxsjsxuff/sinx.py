import math


def print_point_picture(point):
    """point should be 2 dimension array"""
    for i in range(len(point)):
        for j in range(len(point[0])):
            print(point[i][j], end="")
        print()


def create_point_array():
    array = [650 * [" "] for i in range(211)]
    point = []
    for i in range(650):
        x_y = (i, 105 - int(math.sin(i / 100) * 100))
        point.append(x_y)
    for (x, y) in point:
        array[y][x] = "*"
    return array


def main():
    poi = create_point_array()
    print_point_picture(poi)


if __name__ == '__main__':
    main()
