import tkinter as tk
import attendence
from tkinter import *
from time import strftime
def time():
	string = strftime('%H:%M:%S %p')
	lbl.config(text = string)
	lbl.after(1000, time)
windows = tk.Tk()
windows.title("ATTENDANCE MANAGEMENT SYSTEM")
windows.config(bg="#FCE6C9")
windows.geometry("1200x500")
f = tk.Frame(bd=2,width=1150,height=70,padx=19,pady=10,bg="#9932CC")
f.pack()
t = tk.Label(f,text = "ATTENDANCE MANAGEMENT SYSTEM USING FACE RECOGNITION", font=('aharoni',24,'bold'))
t.pack()
s = tk.Frame(bd=2,width=150,height=70,padx=19,pady=10,bg="#EEAD0E")
s.pack()
b = tk.Button(s,text = "START", font=('broadway', 20, 'bold'), height=1, width=10, bd=4, command=attendence.start)
b.pack()
lbl = Label(windows, font = ('chiller', 30, 'bold'),background = 'purple',	foreground = 'white')
lbl.pack(side=BOTTOM, anchor="e", padx=5, pady=5)
time()

windows.mainloop()