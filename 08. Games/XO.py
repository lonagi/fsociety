import random as r
from time import sleep as s

a = ("play", "Play", "Menu", "menu", "Exit", "exit")
c = ("1","2","3","4","5","6","7","8","9")
d = ("Yes","yes","no","No","y","n","Y","N")
b = ""

def mainMenu():
    print("_____________")
    print("|_%s_|_%s_|_%s_|" % (1, 2, 3))
    print("|_%s_|_%s_|_%s_|" % (4, 5, 6))
    print("|_%s_|_%s_|_%s_|" % (7, 8, 9))
    print("Welcome to XO game!")
    print("---By Lonagi Impact---\n")
    print("-play")
    print("-menu")
    print("-exit")
    print("\nType command")

    global b
    b = input("")

    while b not in a:
        print("Type command")
        b = input("")

def Game():
    def Render(field):
        print("_____________")
        print("|_%s_|_%s_|_%s_|" % (field[0], field[1], field[2])," "*5 , "|_%s_|_%s_|_%s_|" % (1, 2, 3))
        print("|_%s_|_%s_|_%s_|" % (field[3], field[4], field[5])," "*5 , "|_%s_|_%s_|_%s_|" % (4, 5, 6))
        print("|_%s_|_%s_|_%s_|" % (field[6], field[7], field[8])," "*5 , "|_%s_|_%s_|_%s_|" % (7, 8, 9))

    def listenType(pl):
        print("You(%s): " % pl)
        global b
        b = input("")
        while b not in c:
            print("Type where. 1-9")
            b = input("")
        return b

    def checkVictory(f):
        if (f[0]==f[4] and f[8]==f[4]):
            return f[0]
        elif (f[2]==f[4] and f[6]==f[4]):
            return f[2]
        elif (f[0]==f[3] and f[6]==f[3]):
            return f[3]
        elif (f[1]==f[4] and f[4]==f[7]):
            return f[1]
        elif (f[2]==f[5] and f[5]==f[8]):
            return f[2]
        elif (f[0]==f[1] and f[1]==f[2]):
            return f[1]
        elif (f[3]==f[4] and f[4]==f[5]):
            return f[3]
        elif (f[6]==f[7] and f[6]==f[8]):
            return f[6]
        else:
            return "_"

    def help():
        pass

    def Victory(cv):
        print("Victory", cv)
        print("\n Play again? Yes, no")
        b = input()
        while b not in d:
            b = input()
        if (b == "Yes" or b == "yes" or b == "Y" or b == "y"):
            Game()
        else:
            mainMenu()

    # Init game
    playerP_random = r.random()
    if(playerP_random > 0.5):
        player = "X"
        bot = "0"
    else:
        player = "0"
        bot = "X"
    print("You play",player)
    field = ["_" for i in range(9)]
    # Init game

    # Game
    for i in range(9):
        while 1:
            Render(field)
            b = listenType(player)
            if (field[int(b) - 1] == "_"):
                field[int(b) - 1] = player
                break

        Render(field)
        print("\n")

        cv = checkVictory(field)
        if (cv != "_"):
            Victory(cv)
            break

        s(r.randrange(1,2))
        botS = r.randrange(0, 8)
        while 1:
            if(field[botS] == "_"):
                field[botS] = bot
                break
            botS = r.randrange(0, 8)
        print("Bot: ")

        cv = checkVictory(field)
        if (cv != "_"):
            Victory(cv)
            break
    # Game



mainMenu()

if (b == "Play" or b == "play"):
    Game()
elif(b == "Menu" or b == "menu"):
    mainMenu()
