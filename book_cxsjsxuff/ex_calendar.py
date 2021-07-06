"""calendar.py
"""


def get_year():
    print("This program prints the calendar of a given year.")
    year = int(input("Please enter a year (after 1900):"))
    return year


def first_day(year):
    k = leap_years(year)
    n = (year - 1900) * 365 + k
    return (n + 1) % 7


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
    for month in range(12):
        heading(month)
        first = one_month(year, month, first)


def heading(m):
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]
    print(" %s " % (months[m]))
    print("Mon Tue Wed Thu Fri Sat Sun")


def one_month(year, month, first):
    d = days(year, month)
    frame = layout(first, d)
    print_month(frame)
    return (first + d) % 7


def days(y, m):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    d = month_days[m]
    if (m == 1) and (y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)):
        d = d + 1
    return d


def layout(first, d):
    frame = 42 * ['']
    if first == 0:
        first = 7
    j = first - 1
    for i in range(1, d + 1):
        frame[j] = '%d' % i
        j = j + 1
    return frame


def print_month(frame):
    for i in range(42):
        print("%3s " % (frame[i]), end='')
        if (i+1) % 7 == 0:
            pass
            print()


def main():
    year = get_year()
    w = first_day(year)
    print_calendar(year, w)


main()
