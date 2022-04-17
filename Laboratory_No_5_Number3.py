from tkinter import *
class MyWindow:
    def __init__(self, win):
        self.lbl1=Label(win, text='Charles Babbage', bg = "Cyan", font="Verdana 18")
        self.lbl1.place(x=55, y=50)

window = Tk()
mywin = MyWindow(window)
window.title('Father of Computer')
window.geometry("300x150+60+60")
window.mainloop()