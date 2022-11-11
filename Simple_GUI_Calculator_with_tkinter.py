from tkinter import *
import tkinter.messagebox

# =========================== setting =====================================
root = Tk()
root.title("calculate")
root.geometry("300x200")
root.resizable(width=False, height=False)
color = 'gray'
root.configure(bg=color)

# =========================== variable ====================================
num1 = StringVar()
num2 = StringVar()
result = StringVar()

# =========================== frames ======================================
top_first = Frame(root, width=300, height=100, bg=color)
top_first.pack(side=TOP)

top_second = Frame(root, width=300, height=100, bg=color)
top_second.pack(side=TOP)

top_third = Frame(root, width=300, height=100, bg=color)
top_third.pack(side=TOP)

top_forth = Frame(root, width=300, height=100, bg=color)
top_forth.pack(side=TOP)


# =========================== functions ===================================
def MsgError(ms):
    if ms == 'error':
        tkinter.messagebox.showerror('Error', 'somethings is worn!')
    elif ms == 'division zero error':
        tkinter.messagebox.showerror('Division Error', 'can not divide by 0')


def plus():
    try:
        value = float(num1.get()) + float(num2.get())
        result.set(value)
    except:
        MsgError("error")


def minute():
    try:
        value = float(num1.get()) - float(num2.get())
        result.set(value)
    except:
        MsgError('error')


def mul():
    try:
        value = float(num1.get()) * float(num2.get())
        result.set(value)
    except:
        MsgError('error')


def div():
    if num2.get() == '0':
        MsgError('division zero error')
    else:
        try:
            value = float(num1.get()) / float(num2.get())
            result.set(value)
        except:
            MsgError('error')


# =========================== button ======================================
btn_plus = Button(top_third, text='+', highlightbackground=color, bg=color, width=8,
                  command=lambda: plus())
btn_plus.pack(side=LEFT, padx=3, pady=3)

btn_minus = Button(top_third, text='-', width=8, bg=color, command=lambda: minute())
btn_minus.pack(side=LEFT, padx=3, pady=3)

btn_mul = Button(top_third, text='*', width=8, bg=color, command=lambda: mul())
btn_mul.pack(side=LEFT, padx=3, pady=3)

btn_div = Button(top_third, text='/', width=8, bg=color, command=lambda: div())
btn_div.pack(side=LEFT, padx=3, pady=3)
# =========================== entries and labels ==========================
label_first_num = Label(top_first, text='Input Number 1: ', bg=color)
label_first_num.pack(side=LEFT, padx=10, pady=10)

first_num = Entry(top_first, textvariable=num1, highlightbackground=color)
first_num.pack(side=LEFT)

label_secend_num = Label(top_second, text='Input Number 2: ', bg=color)
label_secend_num.pack(side=LEFT, padx=10, pady=10)

secend_num = Entry(top_second, textvariable=num2)
secend_num.pack(side=LEFT)

label_res = Label(top_forth, text='Result:', bg=color)
label_res.pack(side=LEFT, pady=30)

res_num = Entry(top_forth, textvariable=result, width=20)
res_num.pack(side=LEFT, padx=20)

root.mainloop()
