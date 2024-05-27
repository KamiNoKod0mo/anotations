from tkinter import *


def button_press(nun):
    global equacao_t
    equacao_t = equacao_t + str(nun)
    equacao_l.set(equacao_t)


def equal():
    global equacao_t
    try:
        total = str(eval(equacao_t))
        equacao_l.set(total)

        equacao_t = total
    except ZeroDivisionError:
        equacao_l.set("error")
        equacao_t = ""
    except SyntaxError:
        equacao_l.set("error")
        equacao_t = ""


def clear():
    global equacao_t
    equacao_l.set("")
    equacao_t = ""


window = Tk()
window.title("Calculadora")
window.geometry("500x500")

equacao_t = ""
equacao_l = StringVar()

label = Label(window, textvariable=equacao_l, font=(
    'consolas', 20), bg='white', width='24', height='2')
label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame, text=1, height=4, width=9, font=35,
                 command=lambda: button_press(1))
button1.grid(row=0, column=0)
button2 = Button(frame, text=2, height=4, width=9, font=35,
                 command=lambda: button_press(2))
button2.grid(row=0, column=1)
button3 = Button(frame, text=3, height=4, width=9, font=35,
                 command=lambda: button_press(3))
button3.grid(row=0, column=2)
button4 = Button(frame, text=4, height=4, width=9, font=35,
                 command=lambda: button_press(4))
button4.grid(row=1, column=0)
button5 = Button(frame, text=5, height=4, width=9, font=35,
                 command=lambda: button_press(5))
button5.grid(row=1, column=1)
button6 = Button(frame, text=6, height=4, width=9, font=35,
                 command=lambda: button_press(6))
button6.grid(row=1, column=2)
button7 = Button(frame, text=7, height=4, width=9, font=35,
                 command=lambda: button_press(7))
button7.grid(row=2, column=0)
button8 = Button(frame, text=8, height=4, width=9, font=35,
                 command=lambda: button_press(8))
button8.grid(row=2, column=1)
button9 = Button(frame, text=9, height=4, width=9, font=35,
                 command=lambda: button_press(9))
button9.grid(row=2, column=2)
button0 = Button(frame, text=0, height=4, width=9, font=35,
                 command=lambda: button_press(0))
button0.grid(row=3, column=0)

plus = Button(frame, text='+', height=4, width=9, font=35,
              command=lambda: button_press('+'))
plus.grid(row=0, column=3)
minus = Button(frame, text='-', height=4, width=9, font=35,
               command=lambda: button_press('-'))
minus.grid(row=1, column=3)
multiply = Button(frame, text='*', height=4, width=9, font=35,
                  command=lambda: button_press('*'))
multiply.grid(row=2, column=3)
divide = Button(frame, text='/', height=4, width=9, font=35,
                command=lambda: button_press('/'))
divide.grid(row=3, column=3)
equal = Button(frame, text='=', height=4, width=9, font=35,
               command=equal)
equal.grid(row=3, column=2)
decimal = Button(frame, text='.', height=4, width=9, font=35,
                 command=lambda: button_press('.'))
decimal.grid(row=3, column=1)
cleara = Button(window, text='clear', height=4, width=12, font=35,
                command=clear)
cleara.pack()
window.mainloop()
