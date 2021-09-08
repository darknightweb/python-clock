from tkinter import *
from time import *


def update():
    time_string= strftime("%I:%M:%S %p" )
    time_label.config(text = time_string)

    day_string= strftime("%A" )
    day_label.config(text = day_string)

    date_string= strftime("%B %d, %Y" )
    date_label.config(text = date_string)

    windows.after(1000, update)

windows = Tk()


time_label = Label(windows,font=("Arial",45),fg="green")
time_label.pack()

day_label = Label(windows,font=("Arial",45),fg="green")
day_label.pack()

date_label = Label(windows,font=("Arial",45),fg="green",bg="black")
date_label.pack()

update()

windows.mainloop()

