from functools import partial
from tkinter import Tk, Label, Button, Frame

Equation = []
TempEq = []
ShownEQ = []
Finished = False


# todo Make everything clear if a number is pressed after = is pressed.
def PressKey(Key):
    global Equation, TempEq, ShownEQ,  Finished
    print('Pressed ' + str(Key))
    IntsAndDec = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, '.']
    if Key in IntsAndDec:
        if Finished:
            PressClear()
        TempEq.append(str(Key))
        ShownEQ.append(str(Key))
        ShownEQ = ''.join(ShownEQ)
    elif Key == '=':
        TempEq = ''.join(TempEq)
        Equation.append(TempEq)
        TempEq = []
        print('Equation is ' + str(Equation))
        ShownEQ = Equation
        PressCalculate()
        return
    else:
        TempEq = ''.join(TempEq)
        Equation.append(TempEq)
        Equation.append(str(Key))
        TempEq = []
        ShownEQ = Equation
    Answer.config(text=str(''.join(ShownEQ)))
    Finished = False
    print('Equation is ' + str(Equation))
    print('TempEq is ' + str(TempEq))
    print('')


def PressDelete():
    print('Delete was pressed.')
    global Equation
    try:
        del Equation[-1]
        Answer.config(text=''.join(str(Equation)))
        print(Equation)
    except IndexError:
        print('Nothing to Delete')


def PressClear():
    print('Clear was pressed.')
    global Equation, TempEq, ShownEQ
    Equation = []
    TempEq = []
    ShownEQ = []
    Answer.config(text=' 0')


def CalculateAnswer(operator, number1, number2):
    if operator == '+':
        return number1+number2
    elif operator == '-':
        return number1-number2
    elif operator == '*':
        return number1*number2
    elif operator == '/':
        return number1/number2
    elif operator == '**':
        return number1**number2
    else:
        raise NameError('Incorrect Operator')


def PressCalculate():
    global Equation, TempEq, Finished
    OrderOp = ['**', '*', '/', '+', '-']
    print('Calculate Pressed')
    for part in Equation:
        for Op in OrderOp:
            if Op in Equation:
                OpLo = Equation.index(Op)
                OpAnswer = CalculateAnswer(Op, int(Equation[OpLo-1]), int(Equation[OpLo+1]))
                for item in range(3):
                    Equation.pop(OpLo-1)
                Equation.insert(OpLo-1, OpAnswer)
    Answer.config(text=' = ' + str(Equation[0]))
    Finished = True


test1 = '5 + 6 * 2**5'
print(eval(test1))

# Defaults for Interface
Background = 'White'
Button1bg = 'White'
Button2bg = 'light sky blue'
Button3bg = 'gray80'
BoldBaseFont = "Arial Bold"
BaseFont = ("Arial", 24)
FontColor = "Black"
ButtonPaddingX = 1
ButtonPaddingY = 3
ButtonWidth = 3
ButtonHeight = 1

# Start of Tkinter interface
CalcGUI = Tk()
CalcGUI.title("Calculator")
CalcGUI.iconbitmap('Calculator.ico')
CalcGUI.configure(bg=Background)

AnswerFrame = Frame(CalcGUI, bg='Black')
AnswerFrame.grid(columnspan=4, row=0)

Answer = Label(AnswerFrame, text=' 0', anchor="w", width=15, font=(BoldBaseFont, 25), fg='white', bg='gray12')
Answer.grid(columnspan=4, row=0)

OneKey = Button(text='1', command=partial(PressKey, 1), bg=Button1bg, font=BaseFont, width=ButtonWidth, height=ButtonHeight)
OneKey.grid(column=0, row=4, padx=ButtonPaddingX, pady=ButtonPaddingY)

TwoKey = Button(text='2', command=partial(PressKey, 2), bg=Button1bg, font=BaseFont, width=ButtonWidth, height=ButtonHeight)
TwoKey.grid(column=1, row=4, padx=ButtonPaddingX, pady=ButtonPaddingY)

ThreeKey = Button(text='3', command=partial(PressKey, 3), bg=Button1bg, font=BaseFont, width=ButtonWidth, height=ButtonHeight)
ThreeKey.grid(column=2, row=4, padx=ButtonPaddingX, pady=ButtonPaddingY)

FourKey = Button(text='4', command=partial(PressKey, 4), bg=Button1bg, font=BaseFont, width=ButtonWidth, height=ButtonHeight)
FourKey.grid(column=0, row=3, padx=ButtonPaddingX, pady=ButtonPaddingY)

FiveKey = Button(text='5', command=partial(PressKey, 5), bg=Button1bg, font=BaseFont, width=ButtonWidth, height=ButtonHeight)
FiveKey.grid(column=1, row=3, padx=ButtonPaddingX, pady=ButtonPaddingY)

SixKey = Button(text='6', command=partial(PressKey, 6), bg=Button1bg, font=BaseFont, width=ButtonWidth, height=ButtonHeight)
SixKey.grid(column=2, row=3, padx=ButtonPaddingX, pady=ButtonPaddingY)

SevenKey = Button(text='7', command=partial(PressKey, 7), bg=Button1bg, font=BaseFont, width=ButtonWidth, height=ButtonHeight)
SevenKey.grid(column=0, row=2, padx=ButtonPaddingX, pady=ButtonPaddingY)

EightKey = Button(text='8', command=partial(PressKey, 8), bg=Button1bg, font=BaseFont, width=ButtonWidth, height=ButtonHeight)
EightKey.grid(column=1, row=2, padx=ButtonPaddingX, pady=ButtonPaddingY)

NineKey = Button(text='9', command=partial(PressKey, 9), bg=Button1bg, font=BaseFont, width=ButtonWidth, height=ButtonHeight)
NineKey.grid(column=2, row=2, padx=ButtonPaddingX, pady=ButtonPaddingY)

ZeroKey = Button(text='0', command=partial(PressKey, 0), bg=Button1bg, font=BaseFont, width=ButtonWidth, height=ButtonHeight)
ZeroKey.grid(column=1, row=5, padx=ButtonPaddingX, pady=ButtonPaddingY)

PeriodKey = Button(text='.', command=partial(PressKey, '.'), bg=Button1bg, font=BaseFont, width=ButtonWidth, height=ButtonHeight)
PeriodKey.grid(column=2, row=5, padx=ButtonPaddingX, pady=ButtonPaddingY)

PlusKey = Button(text='+', command=partial(PressKey, '+'), bg=Button2bg, font=BaseFont, width=ButtonWidth, height=ButtonHeight)
PlusKey.grid(column=3, row=4, padx=ButtonPaddingX, pady=ButtonPaddingY)

MinusKey = Button(text='-', command=partial(PressKey, '-'), bg=Button2bg, font=BaseFont, width=ButtonWidth, height=ButtonHeight)
MinusKey.grid(column=3, row=3, padx=ButtonPaddingX, pady=ButtonPaddingY)

DivideKey = Button(text='/', command=partial(PressKey, '/'), bg=Button2bg, font=BaseFont, width=ButtonWidth, height=ButtonHeight)
DivideKey.grid(column=3, row=1, padx=ButtonPaddingX, pady=ButtonPaddingY)

MultiplyKey = Button(text='X', command=partial(PressKey, '*'), bg=Button2bg, font=BaseFont, width=ButtonWidth, height=ButtonHeight)
MultiplyKey.grid(column=3, row=2, padx=ButtonPaddingX, pady=ButtonPaddingY)

ExpoKey = Button(text='^', command=partial(PressKey, '**'), bg=Button2bg,  font=BaseFont, width=ButtonWidth, height=ButtonHeight)
ExpoKey.grid(column=2, row=1, padx=ButtonPaddingX, pady=ButtonPaddingY)

DeleteKey = Button(text='Del', command=PressDelete, bg=Button3bg, font=BaseFont, width=ButtonWidth, height=ButtonHeight)
DeleteKey.grid(column=1, row=1, padx=ButtonPaddingX, pady=ButtonPaddingY)

ClearKey = Button(text='C', command=PressClear, bg=Button3bg, font=BaseFont, width=ButtonWidth, height=ButtonHeight)
ClearKey.grid(column=0, row=1, padx=ButtonPaddingX, pady=ButtonPaddingY)

CalculateKey = Button(text='=', command=partial(PressKey, '='), font=BaseFont, width=ButtonWidth, height=ButtonHeight)
CalculateKey.grid(column=3, row=5, padx=ButtonPaddingX, pady=ButtonPaddingY)

CalcGUI.mainloop()
