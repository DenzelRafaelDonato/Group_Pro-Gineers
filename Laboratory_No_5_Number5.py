from tkinter import *
import random
window = Tk()
window.title("Button")
window.geometry('{}x{}'.format(400, 200))

def set_color():
  button.configure(bg = random.choice(['yellow', 'blue', 'yellow']))


button = Button(window, text= "Color", fg = 'Red', bg='Blue')
button.place(x=50, y=70)

button2 = Button(window, text = "<---Click to change the color of the button", command=set_color)
button2.place(x = 100, y = 70)

window.mainloop()