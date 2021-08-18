from tkinter import *


def canvas_func(event):
    if c.itemcget(t, "text") == "Hello!":
        c.itemconfig(t, text="Goodbye!")
    else:
        c.itemconfig(t, text="Hello!")


def text_func(event):
    if c.itemcget(t, "fill") != "white":
        c.itemconfig(t, fill="white")
    else:
        c.itemconfig(t, fill="black")


root = Tk()
c = Canvas(root, width=300, height=200, bg="white")
c.pack()
t = c.create_text(150, 100, text="Hello!")
c.bind("<Button-1>", canvas_func)
c.tag_bind(t, "<Button-3>", text_func)
root.mainloop()
