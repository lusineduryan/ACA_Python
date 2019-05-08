# Make a two-player Rock-Paper-Scissors game. User inputs 3 for Rock, 2 for paper, 1 for scissors and 0 to end the game.
# After each step show game result(for example human: 4 vs 4 :PC).

import random

def game_result(arg1, arg2):
    '3' > '1'
    '2' > '3'
    '1' > '2'
    return int(arg1 > arg2)

def game():
    hum = input()
    while int(hum) != 0:
        comp = str(random.randint(1, 4))
        hum = input()
        print(game_result(hum, comp))

print(game())


