#from CalculatorGUI import *

Equation = []
NumberBuffer = ''
ToDisplay = ''
Finished = False


# todo Make everything clear if a number is pressed after = is pressed.

history='0'

def AddListToString(list, string):
    if(string==None):
        string=''
    for item in list:
        string+=item
    return string

def PressKey(Key):
    global Equation, NumberBuffer, ToDisplay,  Finished
    print('Pressed ' + str(Key))
    IntsAndDec = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, '.']
    if Key in IntsAndDec:
        if Finished:
            PressClear()
        NumberBuffer+=str(Key) #add item to list... why? USE A STRING
        ToDisplay+=str(Key)
    elif Key == '=':
        #NumberBuffer = ''.join(NumberBuffer)
        Equation.append(NumberBuffer) #GOOD
        NumberBuffer = ''
        print('Equation is ' + str(Equation))
        ToDisplay = AddListToString(Equation)
        #ToDisplay = ''.join(Equation)
        CalculateEquation(Equation)
        return
    else:
        NumberBuffer = ''.join(NumberBuffer)
        Equation+=NumberBuffer
        Equation+=str(Key)
        NumberBuffer = []
        ToDisplay = Equation
    global history
    history=str(''.join(ToDisplay))
    Finished = False
    print('Equation is ' + str(Equation))
    print('TempEq is ' + str(NumberBuffer))
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
    global history
    print('Delete was pressed.')
    global Equation
    try:
        del Equation[-1]
        history=''.join(str(Equation))
        print(Equation)
    except IndexError:
        print('Nothing to Delete')


def PressClear():
    global history
    print('Clear was pressed.')
    global Equation, NumberBuffer, ToDisplay
    Equation = []
    NumberBuffer = []
    ToDisplay = []
    history=' 0'


def CalculateEquation(EquationEntry):
    global history
    global NumberBuffer, Finished 
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
    history =' = ' + str(EquationEntry[0])
    Finished = True
    return EquationEntry

def GetHistory():
    return history
