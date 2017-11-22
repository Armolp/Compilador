from tkinter import *
from math import sin, cos
import time

tk = Tk()
c = Canvas(tk, width=300, height=300)
c.pack()

a = 0

while True:
    c.delete(ALL)
    a += 0.01

    x = 100 * sin(4 * a)+150
    y = 100 * cos(3 * a)+150
    c.create_line(150,150,x,y)

    x = 100 * sin(4*a) + 150
    y = 100 * cos(3*a) + 150
    c.create_rectangle(x-10,y-10,x+10,y+10,fill='black')

    x = 100 * sin(4*(a-0.1)) + 150
    y = 100 * cos(3*(a-0.1)) + 150
    c.create_oval(x-5, y-5, x+5, y+5, fill='black')
    c.create_line(150,150,x,y)

    x = 100 * sin(4*(a-0.2)) + 150
    y = 100 * cos(3*(a-0.2)) + 150
    c.create_oval(x-1, y-1, x+1, y+1, fill='black')
    c.create_line(150,150,x,y)

    time.sleep(0.01)
    tk.update()
