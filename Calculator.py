from tkinter import *

# Initialize
windows = Tk()
# Title
windows.title('Python Calculator')
# Calculator size
windows.geometry('350x470')
windows.resizable(False, False)

# Font
Font = ('Helvetica', 26)

# Buttons
BH = 1  # Buttons height
BW = 3  # Buttons width
BC = 'SkyBlue1' # Buttons color

# Button functions
string = ""
text_display = StringVar()


def clear():
    global string
    string = ""
    text_display.set("0")


def get_number(number):
    global string
    string += str(number)
    text_display.set(string)


def result():
    global string
    try:
        r = str(eval(string))
        string = r
    except:
        r = "ERROR"
    text_display.set(r)


clear()

Button(windows, text='1', font=Font, height=BH, width=BW, bg=BC, command=lambda: get_number(1)).grid(row=4, column=0)
Button(windows, text='2', font=Font, height=BH, width=BW, bg=BC, command=lambda: get_number(2)).grid(row=4, column=1)
Button(windows, text='3', font=Font, height=BH, width=BW, bg=BC, command=lambda: get_number(3)).grid(row=4, column=2)
Button(windows, text='4', font=Font, height=BH, width=BW, bg=BC, command=lambda: get_number(4)).grid(row=3, column=0)
Button(windows, text='5', font=Font, height=BH, width=BW, bg=BC, command=lambda: get_number(5)).grid(row=3, column=1)
Button(windows, text='6', font=Font, height=BH, width=BW, bg=BC, command=lambda: get_number(6)).grid(row=3, column=2)
Button(windows, text='7', font=Font, height=BH, width=BW, bg=BC, command=lambda: get_number(7)).grid(row=2, column=0)
Button(windows, text='8', font=Font, height=BH, width=BW, bg=BC, command=lambda: get_number(8)).grid(row=2, column=1)
Button(windows, text='9', font=Font, height=BH, width=BW, bg=BC, command=lambda: get_number(9)).grid(row=2, column=2)
Button(windows, text='0', font=Font, height=BH, width=BW, bg=BC, command=lambda: get_number(0)).grid(row=5, column=1)
Button(windows, text='.', font=Font, height=BH, width=BW, bg=BC, command=lambda: get_number(".")).grid(row=5, column=0)
Button(windows, text='+', font=Font, height=BH, width=BW, bg=BC, command=lambda: get_number("+")).grid(row=2, column=3)
Button(windows, text='-', font=Font, height=BH, width=BW, bg=BC, command=lambda: get_number("-")).grid(row=3, column=3)
Button(windows, text='*', font=Font, height=BH, width=BW, bg=BC, command=lambda: get_number("*")).grid(row=4, column=3)
Button(windows, text=u"\u00f7", font=Font, height=BH, width=BW, bg=BC, command=lambda: get_number("/")).grid(row=5, column=3)
Button(windows, text='=', font=Font, height=BH, width=BW, bg=BC, command=lambda: result()).grid(row=5, column=2)
Button(windows, text='AC', font=Font, height=BH, width=BW, bg=BC, command=lambda: clear()).grid(row=1, column=0)

# Display
display = Entry(windows, bd=3, width=15, justify=RIGHT, font=Font, textvariable=text_display) \
    .grid(row=0, column=0, columnspan=4, padx=30, pady=30)

windows.mainloop()
