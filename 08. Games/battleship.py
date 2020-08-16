import random
import os
import string

size = 10
aSize = [i for i in string.ascii_uppercase[:10]]
monitoring = False

s_buffer = ","
s_ship = "0"
s_space = "."
s_hit = "X"
s_destroyed = "X"
s_miss = "*"

ships_list = [[1, 4], [2, 3], [3, 2], [4, 1]]


class Board(object):

    def __init__(self):
        self.board = []
        self.spawned = []

    def create(self):
        for row in range(size):
            self.board.append([s_space] * size)

    def random(self):

        for ship in ships_list:
            for unit in range(ship[0]):

                spawning = True
                while spawning:

                    global refer
                    refer = random.randrange(2)
                    if refer == 0:
                        location_y = random.randrange(size)
                        location_x = random.randrange(size - (ship[1] - 1))
                    else:
                        location_y = random.randrange(size - (ship[1] - 1))
                        location_x = random.randrange(size)

                    offset = 0
                    for testing in range(ship[1]):
                        if refer == 0 and self.board[location_y][location_x + offset] != s_space:
                            continue
                        elif refer == 1 and self.board[location_y + offset][location_x] != s_space:
                            continue
                        offset += 1
                        if offset == ship[1]:
                            spawning = False

                offset = 0
                current_ship = []
                for marker in range(ship[1]):
                    if refer == 0:
                        self.board[location_y][location_x + offset] = s_ship
                        current_ship.append([location_y, location_x + offset])
                    else:
                        self.board[location_y + offset][location_x] = s_ship
                        current_ship.append([location_y + offset, location_x])
                    offset += 1
                self.spawned.append(current_ship)

                for unit_point in current_ship:
                    for buffer_point in ([0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]):
                        b_point_y = unit_point[0] + buffer_point[0]
                        b_point_x = unit_point[1] + buffer_point[1]
                        if b_point_y in range(size) and b_point_x in range(size):
                            if self.board[b_point_y][b_point_x] == s_space:
                                self.board[b_point_y][b_point_x] = s_buffer

    def updating(self, ship):
        for unit in ship:
            for buffer_point in ([0, 0], [0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]):
                b_point_y = unit[0] + buffer_point[0]
                b_point_x = unit[1] + buffer_point[1]
                if b_point_y in range(size) and b_point_x in range(size):
                    if self.board[b_point_y][b_point_x] == s_buffer:
                        self.board[b_point_y][b_point_x] = s_miss
                    elif self.board[b_point_y][b_point_x] == s_hit:
                        self.board[b_point_y][b_point_x] = s_destroyed


def print_boards():
    print("\n    Your field" + (" " * (size + 5)) + "Enemy's field")
    print("    " + (" ".join(str(i) for i in aSize)), end=(" " * 2))
    print("    " + (" ".join(str(i) for i in aSize)))
    print("   " + (" _" * size), end=(" " * 2))
    print("   " + (" _" * size))
    n = 0
    for i in range(size):
        if monitoring:
            print(str(n) + " - " + " ".join(str(i) for i in player.board[n]), end=(" " * 2))
            print(str(n) + " - " + " ".join(str(i) for i in ai.board[n]))
        else:
            print(str(n) + " - " + " ".join(str(i) for i in player.board[n]).replace(s_buffer, s_space), end=(" " * 2))
            print(str(n) + " - " + " ".join(str(i) for i in ai.board[n]).replace(s_ship, s_space).replace(s_buffer,
                                                                                                          s_space))
        n += 1


def press_ent():
    input("Press ENTER to continue.\n")


def state_of_ships(enemy):
    global destroy
    destroy = False
    for d_ship in enemy.spawned:
        damage = 0
        for d_unit in d_ship:
            if enemy.board[d_unit[0]][d_unit[1]] == s_hit:
                damage += 1
        if damage == len(d_ship):
            enemy.updating(d_ship)
            enemy.spawned.remove(d_ship)
            destroy = True


def ai_pass():
    ai_guessing = True
    while ai_guessing:

        ai_intuition = random.randrange(size * 5)

        if ai_intuition == 0:
            ai_int_ship = random.randrange(len(player.spawned))
            ai_int_unit = random.randrange(len(player.spawned[ai_int_ship]))
            ai_guess_y = player.spawned[ai_int_ship][ai_int_unit][0]
            ai_guess_x = player.spawned[ai_int_ship][ai_int_unit][1]

        else:
            ai_guess_y = random.randrange(size)
            ai_guess_x = random.randrange(size)

        if player.board[ai_guess_y][ai_guess_x] == s_ship:
            player.board[ai_guess_y][ai_guess_x] = s_hit
            state_of_ships(player)
            if destroy:
                print("\nBot has destroyed your ship (X: %s, Y: %s)." % (ai_guess_x, ai_guess_y))
            else:
                print("\nBot has damaged your ship (X: %s, Y: %s)." % (ai_guess_x, ai_guess_y))
            break

        elif player.board[ai_guess_y][ai_guess_x] == s_space or player.board[ai_guess_y][ai_guess_x] == s_buffer:
            player.board[ai_guess_y][ai_guess_x] = s_miss
            print("\nBot shot past (X: %s, Y: %s)." % (ai_guess_x, ai_guess_y))
            break

        else:
            continue


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


print("Welcome to \"Battleship\"\n")
press_ent()

ai = Board()
ai.create()
ai.random()

while True:
    clear()
    player = Board()
    player.create()
    player.random()
    print_boards()
    print("If you are not satisfied with the location of your field, press ENTER to generate a random (random).")
    regenerate = input("If you are ready write \"y\"")
    if str(regenerate.lower()) != "y":
        continue
    else:
        break

print("\nOkay Getting Started! Get ready!\n")
press_ent()

game = True
while game:

    clear()
    ai_pass()
    print_boards()

    guessing = True
    while guessing:

        print("\nEnemy ships left: " + str(len(ai.spawned)) + ". ", end="")
        print("Ship left with you: " + str(len(player.spawned)) + ".")

        guess_x = input("Select X (column) to shoot:")
        guess_y = input("Choose Y (square) to shoot:")

        if (guess_x.isdigit() or len(guess_x) != 1) or not guess_y.isdigit():
            print("\nYou entered incorrect coordinates please check back.")
            continue

        guess_x = aSize.index((guess_x.upper()))
        guess_y = int(guess_y)

        if not (guess_x in range(size)) or not (guess_y in range(size)):
            print("\nThis cage is too far to hit! Choose another.")
            continue

        elif ai.board[guess_y][guess_x] == s_ship:
            ai.board[guess_y][guess_x] = s_hit
            state_of_ships(ai)
            if destroy:
                print("\nYou destroyed the enemy ship!", end=" ")
            else:
                print("\nYou have damaged the enemy vessel!", end=" ")
            press_ent()
            break

        elif ai.board[guess_y][guess_x] == s_space or ai.board[guess_y][guess_x] == s_buffer:
            ai.board[guess_y][guess_x] = s_miss
            print("\nYou missed (.", end=" ")
            press_ent()

        else:
            print("\nYou already shot this square please choose another")
            continue
        break

    if len(ai.spawned) == 0:
        input("YOU A WINNER! YOU DESTROYED ALL THE COURT OF THE OPPONENT! Press ENTER to complete the game.")
        break

    if len(player.spawned) == 0:
        print("YOU LOSE! THE OPPONENT DESTROYED ALL YOUR VESSEL (")
        input("Ships remaining at the enemy:" + str(len(ai.spawned)) + ".")
        break