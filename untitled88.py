from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

root = Tk()
root.title("Drawing on canvas")
root.geometry("900x600")
root.maxsize(900, 700)

canvas = Canvas(root, width=900, height=500, bg="white", highlightbackground="black")
canvas.pack()

startx_get = StringVar()
startx = ttk.Combobox(
    root,
    textvariable=startx_get,
    state="readonly",
    values=[0, 100, 200, 300, 400, 500, 600, 700, 800],
)

text_startx = Label(root, text="startx")
text_startx.place(relx=0.05, rely=0.88, anchor=CENTER)

starx = startx_get.get()
starty_get = StringVar()
starty = ttk.Combobox(
    root, textvariable=starty_get, state="readonly", values=[0, 100, 200, 300, 400, 500]
)

text_starty = Label(root, text="starty")
text_starty.place(relx=0.27, rely=0.88, anchor=CENTER)

stary = starty_get.get()

endx_get = StringVar()
endx = ttk.Combobox(
    root,
    textvariable=endx_get,
    state="readonly",
    values=[0, 100, 200, 300, 400, 500, 600, 700, 800],
)

text_endx = Label(root, text="endx")
enx = endx_get.get()
endy_get = StringVar()
text_endx.place(relx=0.49, rely=0.88, anchor=CENTER)
endy = ttk.Combobox(
    root, textvariable=endy_get, state="readonly", values=[0, 100, 200, 300, 400, 500]
)

text_endy = Label(root, text="endy")
text_endy.place(relx=0.72, rely=0.88, anchor=CENTER)

eny = endy_get.get()

colour_get = StringVar()
colour = ttk.Combobox(
    root,
    textvariable=colour_get,
    values=("blue", "green", "yellow", "orange", "black", "purple", "red"),
)

text_colour = Label(root, text="Choose Color:")
text_colour.place(relx=0.68, rely=0.94, anchor=CENTER)

color = colour_get.get()

startx.insert(0, " ")
starty.insert(0, " ")
endx.insert(0, " ")
endy.insert(0, " ")
draw = ""


def rectangle(event):
    global draw
    global starx
    global stary
    global enx
    global eny
    global color
    color = colour_get.get()
    drawing = "rect"
    starx = startx_get.get()
    stary = starty_get.get()
    enx = endx_get.get()
    eny = endy_get.get()
    draw(drawing, stary, starx, enx, eny, color)


def circle(event):
    global draw
    global starx
    global stary
    global enx
    global eny
    global color
    color = colour_get.get()
    drawing = "circle"
    starx = startx_get.get()
    stary = starty_get.get()
    enx = endx_get.get()
    eny = endy_get.get()
    draw(drawing, stary, enx, starx, eny, color)


def line(event):
    global draw
    global starx
    global stary
    global enx
    global eny
    global color
    color = colour_get.get()
    drawing = "line"
    starx = startx_get.get()
    stary = starty_get.get()
    enx = endx_get.get()
    eny = endy_get.get()
    draw(drawing, stary, enx, starx, eny, color)


def draw(drawing, stary, starx, enx, eny, color):
    if color == "":
        color = "black"
    if drawing == "rect":
        canvas.create_rectangle(stary, starx, enx, eny, fill=color, width=3)
    elif drawing == "circle":
        canvas.create_oval(starx, stary, enx, eny, fill=color, width=3)
    elif drawing == "line":
        canvas.create_line(starx, stary, enx, eny, fill=color, width=3)


root.bind("<r>", rectangle)
root.bind("<c>", circle)
root.bind("<l>", line)
startx.place(relx=0.16, rely=0.88, anchor=CENTER)
starty.place(relx=0.38, rely=0.88, anchor=CENTER)
endx.place(relx=0.6, rely=0.88, anchor=CENTER)
endy.place(relx=0.83, rely=0.88, anchor=CENTER)
colour.place(relx=0.83, rely=0.94, anchor=CENTER)
root.mainloop()
