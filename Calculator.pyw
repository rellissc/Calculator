import math
from functools import partial
from tkinter import Tk, Label, Button, Frame

Equation = []


def PressKey(Key):
    print(str(Key) + ' was pressed.')
    Equation.append(str(Key))
    Answer.config(text=''.join(Equation))


def PressCalculate():
    print('Calculate Pressed')
    print(''.join(Equation))


# Defaults for Interface
Background = 'White'
BoldBaseFont = "Arial Bold"
BaseFont = "Arial"
FontColor = "Black"
ButtonPaddingX = 0
ButtonPaddingY = 6
ButtonWidth = 5
ButtonHeight = 2

# Start of Tkinter interface
CalcGUI = Tk()
CalcGUI.title("Calculator")
# CalcGUI.geometry("356x350")
# CalcGUI.iconbitmap('JudgeHammer.ico')
CalcGUI.configure(bg=Background)

AnswerFrame = Frame(CalcGUI, bg='Black')
AnswerFrame.grid(columnspan=4, row=0)

Answer = Label(AnswerFrame, text='Blank', anchor="w", width=20, font=(BoldBaseFont, 20), fg='white', bg='Black')
Answer.grid(columnspan=4, row=0, padx=150)

OneKey = Button(text='1', command=partial(PressKey, 1), font=BaseFont, width=ButtonWidth, height=ButtonHeight)
OneKey.grid(column=0, row=4, padx=ButtonPaddingX, pady=ButtonPaddingY)

TwoKey = Button(text='2', command=partial(PressKey, 2), font=BaseFont, width=ButtonWidth, height=ButtonHeight)
TwoKey.grid(column=1, row=4, padx=ButtonPaddingX, pady=ButtonPaddingY)

ThreeKey = Button(text='3', command=partial(PressKey, 3), font=BaseFont, width=ButtonWidth, height=ButtonHeight)
ThreeKey.grid(column=2, row=4, padx=ButtonPaddingX, pady=ButtonPaddingY)

FourKey = Button(text='4', command=partial(PressKey, 4), font=BaseFont, width=ButtonWidth, height=ButtonHeight)
FourKey.grid(column=0, row=3, padx=ButtonPaddingX, pady=ButtonPaddingY)

FiveKey = Button(text='5', command=partial(PressKey, 5), font=BaseFont, width=ButtonWidth, height=ButtonHeight)
FiveKey.grid(column=1, row=3, padx=ButtonPaddingX, pady=ButtonPaddingY)

SixKey = Button(text='6', command=partial(PressKey, 6), font=BaseFont, width=ButtonWidth, height=ButtonHeight)
SixKey.grid(column=2, row=3, padx=ButtonPaddingX, pady=ButtonPaddingY)

SevenKey = Button(text='7', command=partial(PressKey, 7), font=BaseFont, width=ButtonWidth, height=ButtonHeight)
SevenKey.grid(column=0, row=2, padx=ButtonPaddingX, pady=ButtonPaddingY)

EightKey = Button(text='8', command=partial(PressKey, 8), font=BaseFont, width=ButtonWidth, height=ButtonHeight)
EightKey.grid(column=1, row=2, padx=ButtonPaddingX, pady=ButtonPaddingY)

NineKey = Button(text='9', command=partial(PressKey, 9), font=BaseFont, width=ButtonWidth, height=ButtonHeight)
NineKey.grid(column=2, row=2, padx=ButtonPaddingX, pady=ButtonPaddingY)

ZeroKey = Button(text='0', command=partial(PressKey, 0), font=BaseFont, width=ButtonWidth, height=ButtonHeight)
ZeroKey.grid(column=1, row=5, padx=ButtonPaddingX, pady=ButtonPaddingY)

PeriodKey = Button(text='.', command=partial(PressKey, '.'), font=BaseFont, width=ButtonWidth, height=ButtonHeight)
PeriodKey.grid(column=2, row=5, padx=ButtonPaddingX, pady=ButtonPaddingY)

PlusKey = Button(text='+', command=partial(PressKey, '+'), font=BaseFont, width=ButtonWidth, height=ButtonHeight)
PlusKey.grid(column=3, row=4, padx=ButtonPaddingX, pady=ButtonPaddingY)

MinusKey = Button(text='-', command=partial(PressKey, '-'), font=BaseFont, width=ButtonWidth, height=ButtonHeight)
MinusKey.grid(column=3, row=3, padx=ButtonPaddingX, pady=ButtonPaddingY)

DivideKey = Button(text='/', command=partial(PressKey, '/'), font=BaseFont, width=ButtonWidth, height=ButtonHeight)
DivideKey.grid(column=3, row=1, padx=ButtonPaddingX, pady=ButtonPaddingY)

MultiplyKey = Button(text='X', command=partial(PressKey, '*'), font=BaseFont, width=ButtonWidth, height=ButtonHeight)
MultiplyKey.grid(column=3, row=2, padx=ButtonPaddingX, pady=ButtonPaddingY)

DeleteKey = Button(text='Delete', command=partial(PressKey, 'Delete'), font=BaseFont, width=ButtonWidth, height=ButtonHeight)
DeleteKey.grid(column=2, row=1, padx=ButtonPaddingX, pady=ButtonPaddingY)

ClearKey = Button(text='Clear', command=partial(PressKey, 'Clear'), font=BaseFont, width=ButtonWidth, height=ButtonHeight)
ClearKey.grid(column=1, row=1, padx=ButtonPaddingX, pady=ButtonPaddingY)

CalculateKey = Button(text='=', command=PressCalculate, font=BaseFont, width=ButtonWidth, height=ButtonHeight)
CalculateKey.grid(column=3, row=5, padx=ButtonPaddingX, pady=ButtonPaddingY)

CalcGUI.mainloop()
