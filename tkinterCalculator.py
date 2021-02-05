from tkinter import *

root = Tk()

'''
#creating a Label widge
myLabel1 = Label(root , text = "Minha primeira aba,olá")
myLabel2 = Label(root, text = "My name is Victor ")
#or
myLabel3 = Label(root, text = 'I am 18').grid(row=2,column=2)

#showing into screen
#myLabel.pack()
myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1,column=1)

root.mainloop()
'''
'''
######  creating a button
def myClick():
    myLabel =Label(root, text='I clicked the button')
    myLabel.pack()



myText = Label(root, text="my first widge").pack()
#myButton = Button(root, text="Click on me",state=DISABLED,padx=50,pady=50)
myButton = Button(root, text='Button' ,command=myClick,fg='red',bg='blue')
#fg: figure ground color   bg = 'blue' or '#ffffff'
#bg:back ground color

myButton.pack()
'''

# input box
# e = Entry(root, width=50, bg='blue',fg = 'white')
'''
e = Entry(root,text='Name')
e.pack()
e.insert(0,'Enter yout name')

def myClick():
    myLabel = Label(root,text='Hello '+e.get())
    myLabel.pack()



myButton = Button(root,text='Enter yout name',command=myClick)
myButton.pack()
'''

root.title('Simple Calculator')
c = Entry(root, width=35, borderwidth=5)
c.grid(row=0, column=0, columnspan=3, padx=13, pady=13)


def button_click(number):
    current = c.get()
    c.delete(0, END)
    c.insert(0, str(current) + str(number))


def button_clear():
    c.delete(0, END)


def button_add():
    first_number = c.get()
    global f_num
    global math
    math = 'addition'
    f_num = float(first_number)
    c.delete(0, END)


def button_subtract():
    first_number = c.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = float(first_number)
    c.delete(0, END)


def button_multiply():
    first_number = c.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = float(first_number)
    c.delete(0, END)


def button_divide():
    first_number = c.get()
    global f_num
    global math
    math = 'division'
    f_num = int(first_number)
    c.delete(0, END)


def button_equal():
    second_number = c.get()
    c.delete(0, END)
    if math == 'addition':
        c.insert(0, f_num + float(second_number))
    elif math == 'subtraction':
        c.insert(0, f_num - float(second_number))

    elif math == 'multiplication':
        c.insert(0, f_num * float(second_number))

    elif math == 'division':
        c.insert(0, f_num / float(second_number))


button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_click(0))
Button_add = Button(root, text='+', padx=39, pady=20, command=button_add)
Button_equal = Button(root, text='=', padx=88, pady=20, command=button_equal)
Button_clear = Button(root, text='CE', padx=85, pady=20, command=button_clear, bg='red')

Button_subtract = Button(root, text='-', padx=41, pady=20, command=button_subtract)
Button_multiply = Button(root, text='X', padx=40, pady=20, command=button_multiply)
Button_divide = Button(root, text='/', padx=41, pady=20, command=button_divide)

# buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

Button_clear.grid(row=4, column=1, columnspan=2)
Button_add.grid(row=5, column=0)
Button_equal.grid(row=5, column=1, columnspan=2)

Button_subtract.grid(row=6, column=0)
Button_multiply.grid(row=6, column=1)
Button_divide.grid(row=6, column=2)

root.mainloop()





















