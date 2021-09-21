from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("clock")


def time():
    # this is for 24 hour format
    # string = strftime('%H :%M: %S %p')
    # this is fo r 12 hour format
    string = strftime('%I :%M: %S %p')

    label.config(text=string)
    label.after(1000, time)


label = Label(root, font=("ds-digital", 80), background="black", foreground="blue")
label.pack(anchor='center')
time()

mainloop()

