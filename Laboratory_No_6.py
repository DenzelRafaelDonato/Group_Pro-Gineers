from tkinter import *
class MyWindow:
    def __init__(self, win):
        self.lbl1 = Label(win, text='Semestral Grade', font="Georgia 20", fg="Blue")
        self.lbl1.place(x=115, y=20)

        self.lbl2=Label(win, text='Prelim Grade:', font="Times 14")
        self.lbl2.place(x=60, y=90)
        self.En = Entry (window,bd=6)
        self.En.place(x=220, y=90)
        self.En.place(width=150, height=28)

        self.lbl3=Label(win, text='Midterm Grade:', font="Times 14")
        self.lbl3.place(x=60, y=140)
        self.En1 = Entry(window,bd=6)
        self.En1.place(x=220, y=140)
        self.En1.place(width=150, height=28)

        self.lbl4=Label(win, text='Final Grade:', font="Times 14")
        self.lbl4.place(x=60, y=190)
        self.En2 = Entry(window,bd=6)
        self.En2.place(x=220, y=190)
        self.En2.place(width=150, height=28)

        self.btn=Button(window,text="View Grade", font="Georgia 10", fg="White", bd=8, bg="Blue", command=self.Grade)
        self.btn.place(x=170,y=240)

        self.lbl5=Label(window,text="Semestral Grade:", font="Times 14")
        self.lbl5.place(x=60,y=300)
        self.En3=Entry(window,bd=6)
        self.En3.place(x=220,y=300)
        self.En3.place(width=150, height=28)

    def Grade(self):
        self.En3.delete(0,'end')
        Prelim=int(self.En.get())
        Midterm=int(self.En1.get())
        Finals= int(self.En2.get())
        Semestral = (Prelim*0.30)+(Midterm*0.30)+(Finals*0.40)
        self.En3.insert(END,str(Semestral))

window = Tk()
mywin = MyWindow(window)
window.geometry("400x360+20+20")
window.title('Semestral Grade')

window.mainloop()
