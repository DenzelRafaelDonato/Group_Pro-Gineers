from tkinter import *
from tkinter import ttk
win = Tk()
win.geometry("300x200+10+20")
win.title("Major Subjects")

var = StringVar()
var.set("reading")
info = "reading","writing","arithmetic","coding"
listbox = Listbox(win,height=5,selectmode= 'single')
info = "reading"
info1 = "writing"
info2 = "arithmetic"
info3 = "coding"

listbox.insert(END,info)
listbox.insert(END, info1)
listbox.insert(END, info2)
listbox.insert(END, info3)
listbox.place(x=80, y = 35 )

win.mainloop()