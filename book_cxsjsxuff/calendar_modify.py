"""calendar.py
every line print four month, it should optimize
"""


def get_year():
    print("This program prints the calendar of a given year.")
    year = int(input("Please enter a year (after 1900):"))
    return year


def first_day(year):
    k = leap_years(year)
    n = [0] * 4
    n[0] = (year - 1900) * 365 + k
    day = days(year, 0)
    for i in range(1, 4):
        n[i] = n[i - 1] + day[i - 1]
    for i in range(4):
        n[i] = (n[i] + 1) % 7
    return n


def leap_years(year):
    count = 0
    for y in range(1900, year):
        if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
            count = count + 1
    return count


def print_calendar(year, w):
    print()
    print("=========== " + str(year) + " ==========")
    first = w
    for month in range(0, 12, 4):
        heading(month)
        first = four_month(year, month, first)


def heading(m):
    months = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sept",
        "Oct",
        "Nov",
        "Dec",
    ]
    for i in range(4):
        print("{:<31} ".format(months[m + i]), end="")
    print()
    for i in range(4):
        print("Mon Tue Wed Thu Fri Sat Sun     ", end="")
    print()


def four_month(year, month, first):
    d = days(year, month)
    frame = layout(first, d)
    print_month(frame)
    first[0] = (first[3] + d[3]) % 7
    if month == 8:
        return first
    d = days(year, month + 4)
    for i in range(1, 4):
        first[i] = (first[i - 1] + d[i - 1]) % 7
    return first


def days(y, m):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # num = len(m)
    d = [0] * 4
    for i in range(4):
        d[i] = month_days[m + i]
        if (m == 1) and (y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)):
            d[i] = d[i] + 1
    return d


def layout(first, d):
    frame = [42 * [""] for i in range(4)]   # + [42 * [""]] + [42 * [""]] + [42 * [""]]

    for idx in range(4):
        if first[idx] == 0:
            first[idx] = 7
        j = first[idx] - 1
        for i in range(1, d[idx] + 1):
            frame[idx][j] = "%d" % i
            j = j + 1
    return frame


def print_month(frame):
    for i in range(6):
        for j in range(4):
            for idx in range(7):
                print("%3s " % (frame[j][i * 7 + idx]), end="")
            print("    ", end="")
        print()


def main():
    year = get_year()
    w = first_day(year)
    print_calendar(year, w)


# main()
