from tkinter import *


def get_marks():
    a, b, c, d, f = 0, 0, 0, 0, 0
    mark = int(input("Enter a mark: "))
    while mark >= 0:
        if mark >= 90:
            a = a + 1
        elif mark >= 80:
            b = b + 1
        elif mark >= 70:
            c = c + 1
        elif mark >= 60:
            d = d + 1
        else:
            f = f + 1
        mark = int(input("Enter a mark: "))
    return a, b, c, d, f


def main():
    a, b, c, d, f = get_marks()
    win = Tk()
    cv = Canvas(win, width=300, height=200, bg="white")
    cv.pack()
    n = a + b + c + d + f
    ea, sa = 360.0 * a / n, 0
    eb, sb = 360.0 * b / n, ea
    ec, sc = 360.0 * c / n, ea + eb
    ed, sd = 360.0 * d / n, ea + eb + ec
    ef, sf = 360.0 * f / n, ea + eb + ec + ed
    bb = (90, 40, 210, 160)
    pie_a = cv.create_arc(bb, start=sa, extent=ea, fill="yellow")
    pie_b = cv.create_arc(bb, start=sb, extent=eb, fill="green")
    pie_c = cv.create_arc(bb, start=sc, extent=ec, fill="black")
    pie_d = cv.create_arc(bb, start=sd, extent=ed, fill="gray")
    pie_f = cv.create_arc(bb, start=sf, extent=ef, fill="red")
    cv.create_rectangle(240, 40, 260, 50, fill="yellow")
    cv.create_rectangle(240, 40 + 24, 260, 50 + 24, fill="green")
    cv.create_rectangle(240, 40 + 48, 260, 50 + 48, fill="black")
    cv.create_rectangle(240, 40 + 72, 260, 50 + 72, fill="gray")
    cv.create_rectangle(240, 40 + 96, 260, 50 + 96, fill="red")
    cv.create_text(270, 40, text="A", anchor=N)
    cv.create_text(270, 40 + 24, text="B", anchor=N)
    cv.create_text(270, 40 + 48, text="C", anchor=N)
    cv.create_text(270, 40 + 72, text="D", anchor=N)
    cv.create_text(270, 40 + 96, text="F", anchor=N)
    pie_pct = cv.create_text(40, 100, text="")

    def in_pie_a(event):
        pct = "%5.1f%%" % (100.0 * a / n)
        cv.itemconfig(pie_pct, text=pct)

    def in_pie_b(event):
        pct = "%5.1f%%" % (100.0 * b / n)
        cv.itemconfig(pie_pct, text=pct)

    def in_pie_c(event):
        pct = "%5.1f%%" % (100.0 * c / n)
        cv.itemconfig(pie_pct, text=pct)

    def in_pie_d(event):
        pct = "%5.1f%%" % (100.0 * d / n)
        cv.itemconfig(pie_pct, text=pct)

    def in_pie_f(event):
        pct = "%5.1f%%" % (100.0 * f / n)
        cv.itemconfig(pie_pct, text=pct)

    cv.tag_bind(pie_a, "&lt;Enter&gt;", in_pie_a)
    cv.tag_bind(pie_b, "&lt;Enter&gt;", in_pie_b)
    cv.tag_bind(pie_c, "&lt;Enter&gt;", in_pie_c)
    cv.tag_bind(pie_d, "&lt;Enter&gt;", in_pie_d)
    cv.tag_bind(pie_f, "&lt;Enter&gt;", in_pie_f)
    win.mainloop()


main()
