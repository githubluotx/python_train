import tkinter

root = tkinter.Tk()
c = tkinter.Canvas(root, width=300, height=200, bg='white')
c.pack()

r1 = c.create_rectangle(20,20,100,80, tags="#1")
r2 = c.create_rectangle(40,50,200,180, tags=("myRect", "#2"))
c.itemconfig(r1, tags=("myRect","rectOne"))
c.addtag_withtag("ourRect","rectOne")
print(c.gettags(r1), ('myRect', 'rectOne', 'ourRect'))
