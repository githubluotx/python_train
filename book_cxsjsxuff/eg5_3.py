from tkinter import *
from math import sin, cos, pi
from time import sleep


def main():
    root = Tk()
    c = Canvas(root, width=300, height=200, bg="white")
    c.pack()
    orbit = c.create_oval(50, 50, 250, 150)
    sun = c.create_oval(110, 85, 140, 115, fill="red")
    earth = c.create_oval(245, 95, 255, 105, fill="blue")
    moon = c.create_oval(265, 98, 270, 103)
    e_x = 250  # earth's X
    e_y = 100  # earth's Y
    m2e_x = 20  # moon's X relative to earth
    m2e_y = 0  # moon's Y relative to earth
    t = 0
    while True:
        t = t + 0.01 * pi
        new_ex = 150 + 100 * cos(t)
        new_ey = 100 - 50 * sin(t)
        new_m2ex = 20 * cos(12 * t)
        new_m2ey = -15 * sin(12 * t)
        edx = new_ex - e_x
        edy = new_ey - e_y
        mdx = new_m2ex - m2e_x
        mdy = new_m2ey - m2e_y
        c.move(earth, edx, edy)
        c.move(moon, mdx + edx, mdy + edy)
        c.update()
        e_x = new_ex
        e_y = new_ey
        m2e_x = new_m2ex
        m2e_y = new_m2ey
        sleep(0.04)


main()
