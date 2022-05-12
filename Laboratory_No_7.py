from tkinter import *
window = Tk()
window.title("Calculator")
window.geometry("320x435")
window.config(background='Light Blue')

def button_show(number):
    current = txt1.get()
    txt1.delete(0, END)
    txt1.insert(0, str(current) + str(number))

def button_clear():
    txt1.delete(0, END)

def button_add():
    first_number = txt1.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    txt1.delete(0, END)

def button_equals():
    second_number = txt1.get()
    txt1.delete(0, END)

    if math == "addition":
        txt1.insert(0, f_num + float(second_number))
    if math == "subtraction":
        txt1.insert(0, f_num - float(second_number))
    if math == "multiplication":
        txt1.insert(0, f_num * float(second_number))
    if math == "division":
        txt1.insert(0, f_num / float(second_number))

def button_sub():
    first_number = txt1.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    txt1.delete(0, END)

def button_times():
    first_number = txt1.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    txt1.delete(0, END)

def button_divide():
    first_number = txt1.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    txt1.delete(0, END)

txt1 = Entry(window,bd=10,font=('Helvetica',36),width=11)
txt1.place(x=1,y=1)

btnc = Button(window,text="C",width=18,height=1,font=('Helvetica', 20, 'bold'),command=lambda:button_clear())
btnc.place(x=2,y=82)

btn7 = Button(window, text="7",width=4,height=1,font=('Helvetica', 20, 'bold'),command=lambda:button_show(7))
btn7.place(x=1, y=141)

btn8 = Button(window, text="8", width=4, height=1, font=('Helvetica', 20, 'bold'),command=lambda:button_show(8))
btn8.place(x=81, y=141)

btn9 = Button(window, text="9", width=4, height=1, font=('Helvetica', 20, 'bold'),command=lambda:button_show(9))
btn9.place(x=161, y=141)

btnd = Button(window, text="/", width=4, height=1, font=('Helvetica', 20, 'bold'),command=lambda:button_divide())
btnd.place(x=241, y=141)

btn4 = Button(window, text="4", width=4, height=1, font=('Helvetica', 20, 'bold'),command=lambda:button_show(4))
btn4.place(x=1, y=200)

btn5 = Button(window, text="5", width=4, height=1, font=('Helvetica', 20, 'bold'),command=lambda:button_show(5))
btn5.place(x=81, y=200)

btn6 = Button(window, text="6", width=4, height=1, font=('Helvetica', 20, 'bold'),command=lambda:button_show(6))
btn6.place(x=161, y=200)

btnx = Button(window, text="*", width=4, height=1, font=('Helvetica', 20, 'bold'),command=lambda:button_times())
btnx.place(x=241, y=200)

btn1 = Button(window, text="1", width=4, height=1, font=('Helvetica', 20, 'bold'),command=lambda:button_show(1))
btn1.place(x=1, y=259)

btn2 = Button(window, text="2", width=4, height=1, font=('Helvetica', 20, 'bold'),command=lambda:button_show(2))
btn2.place(x=81, y=259)

btn3 = Button(window, text="3", width=4, height=1, font=('Helvetica', 20, 'bold'),command=lambda:button_show(3))
btn3.place(x=161, y=259)

btnm = Button(window, text="-", width=4, height=1, font=('Helvetica', 20, 'bold'),command=lambda:button_sub())
btnm.place(x=241, y=259)

btn0 = Button(window, text="0", width=5, height=1, font=('Helvetica', 20, 'bold'),command=lambda:button_show(0))
btn0.place(x=8, y=318)

btnt = Button(window, text=".", width=5, height=1, font=('Helvetica', 20, 'bold'),command=lambda:button_show('.'))
btnt.place(x=112, y=318)

btna = Button(window, text="+", width=5, height=1, font=('Helvetica', 20, 'bold'),command=lambda:button_add())
btna.place(x=215, y=318)

btne = Button(window, text="=", width=18, height=1, font=('Helvetica', 20, 'bold'),command=lambda:button_equals())
btne.place(x=2, y=377)


window.mainloop()