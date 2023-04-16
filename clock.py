from tkinter import *
from tkinter.ttk import *
from time import strftime

#creating an UI or our clock
root = Tk()
root.title("Clock")

def timecall():
    str = strftime('%H : %M : %S  %p')
    label.config(text=str)
    label.after(1000, timecall)

#create a label to store the clock
label = Label(root, font=("ds-digital",80), background="blue", foreground="yellow")
#Now pack the label
label.pack(anchor='center')
timecall()

mainloop()