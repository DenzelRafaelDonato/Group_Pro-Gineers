from tkinter import *
class MyWindow:
    def __init__(self, win):
        self.lbl1=Label(win, text='Laboratory Activity 5')
        self.lbl2=Label(win, text='Submitted to: Mam Sayo')
        self.lbl1.place(x=85, y=60)
        self.lbl2.place(x=80, y=80)

window = Tk()
mywin = MyWindow(window)
window.title('Label')
window.geometry("300x130+60+60")
window.mainloop()