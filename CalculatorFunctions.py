from CalculatorGUI import *

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
        PressCalculate(Equation)
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


def PressCalculate(EquationEntry):
    global TempEq, Finished
    OrderOp = ['**', '*', '/', '+', '-']
    print('Calculate Pressed')
    for part in EquationEntry:
        for Op in OrderOp:
            if Op in EquationEntry:
                OpLo = EquationEntry.index(Op)
                OpAnswer = CalculateAnswer(Op, int(EquationEntry[OpLo - 1]), int(EquationEntry[OpLo + 1]))
                for item in range(3):
                    EquationEntry.pop(OpLo - 1)
                EquationEntry.insert(OpLo - 1, OpAnswer)
    Answer.config(text=' = ' + str(EquationEntry[0]))
    Finished = True
    return EquationEntry
