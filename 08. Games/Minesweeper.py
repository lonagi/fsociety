import random as r
import time as t
import string

_FIELD = 8

_MINES = int(18/64 * _FIELD**2)
_CooY = tuple(i for i in string.ascii_uppercase[:_FIELD])
_Coo = []
_Coo.extend(_CooY)
_Coo.extend(tuple(i for i in string.ascii_lowercase[:_FIELD]))

testL = []
testL.extend(_CooY)
testL.extend([i for i in range(_FIELD)])

Field = []

def GenerateMap(Field, t = False):
    if(t == True):
        for i in range(_FIELD+1):
            Field.append([])
            for j in range(_FIELD+1):
                Field[i].append("_")
        return Field
    else:
        for i in range(_FIELD):
            Field.append([])
            for j in range(_FIELD):
                Field[i].append("_")
        return Field

def GenerateMines(mField,x,y):
    rm = _MINES-1
    mField[x][y] = "0"
    while rm != 0:
        y = _CooY.index(r.choice(_CooY))
        x = r.randrange(0,_FIELD)
        if(mField[x][y] != "0" and mField[x][y] == "_"):
            if (mField[x+1][y] != "0"):
                if (mField[x-1][y] != "0"):
                    if (mField[x][y+1] != "0"):
                        if (mField[x][y-1] != "0"):
                            if (mField[x+1][y+1] != "0"):
                                if (mField[x+1][y-1] != "0"):
                                    if (mField[x-1][y+1] != "0"):
                                        if (mField[x-1][y-1] != "0"):
                                            mField[x][y] = "m"
                                            rm -= 1
    return mField

def RenderMap(Field):
    print(" ", _CooY)
    for i in range(len(Field)):
        print(i, Field[i])

def Move(Field):

    print(".Type For Example A" + str(r.randrange(0, _FIELD)))
    st = input()
    #st = str(r.choice(testL)) + str(r.choice(testL))
    at = 2

    def While1(st, Field):
        at = int(st[1])
        while (st[0] not in _Coo) or (len(st) != 2) or (at >= _FIELD) or (Field[int(st[1])][_CooY.index(st[0].upper())] != "_"):
            print("Type letter and number")
            st = input()
            #st = str(r.choice(testL)) + str(r.choice(testL))
            at = int(st[1])
        return st

    def While2():
        print("...Type For Example A" + str(r.randrange(0, _FIELD)))
        st = input()
        #st = str(r.choice(testL)) + str(r.choice(testL))
        return st

    try:
        st = While1(st, Field)
        print("Your move is",st)
        return st
    except:
        print("..Type For Example A" + str(r.randrange(0, _FIELD)))
        st = input()
        #st = str(r.choice(testL))+str(r.choice(testL))
        ast = st[1]
        while type(ast) == type('str'):
            try:
                st = While1(st, Field)
                ast = int(st[1])
                return st
            except:
                st = While2()

def isMine(x,y,mField):
    if(mField[x][y]=="m"):
        return True

def countMines(x,y,mField):
        counter = 0
        #x = num
        #y = let
        if (mField[x][y + 1] == "m"):
            counter += 1
        if (mField[x][y - 1] == "m"):
            counter += 1
        if (mField[x + 1][y] == "m"):
            counter += 1
        if (mField[x - 1][y] == "m"):
            counter += 1

        if (mField[x + 1][y + 1] == "m"):
            counter += 1
        if (mField[x + 1][y - 1] == "m"):
            counter += 1
        if (mField[x - 1][y + 1] == "m"):
            counter += 1
        if (mField[x - 1][y - 1] == "m"):
            counter += 1

        return str(counter)

def Lose(Field, mField, x, y):
    print("Looseeee")
    RenderMap(Field)
    print("\n")
    RenderMap(mField)
    print("Looseeee", "Your choice is", _CooY[y], x)

def testMoves():
    with open("teee.txt", "w") as file:
        for i in range(5000):
            file.write(Move())

Field = GenerateMap(Field)
mField = GenerateMap([],True)
RenderMap(Field)
FM = Move(Field)

y = _CooY.index(FM[0].upper())
x = int(FM[1])
Field[x][y] = '0'
RenderMap(Field)
GenerateMines(mField,x,y)

MyMove = ""
while MyMove=="":
    m = Move(Field)
    y = _CooY.index(m[0].upper())
    x = int(m[1])
    if(isMine(x,y,mField)):
        Lose(Field,mField,x,y)
        break
    Field[x][y] = countMines(x,y,mField)
    RenderMap(Field)