# Make a two-player Rock-Paper-Scissors game. User inputs 3 for Rock, 2 for paper, 1 for scissors and 0 to end the game.
# After each step show game result(for example human: 4 vs 4 :PC).

import datetime

def round_result(arg1, arg2):
    score1, score2 = 0, 0
    if arg1 == '3' and arg2 == '1':
        score1 += 1
    elif arg1 == '2' and arg2 == '3':
        score1 += 1
    elif arg1 == '1' and arg2 == '2':
        score1 += 1
    elif arg2 == '3' and arg1 == '1':
        score2 += 1
    elif arg2 == '2' and arg1 == '3':
        score2 += 1
    elif arg2 == '1' and arg1 == '2':
        score2 += 1
    return score1, score2

def game():
    human = input()
    current_human_score, current_PC_score = 0, 0
    while int(human) != 0:
        current_time = datetime.datetime.now()
        sum_of_time_components = current_time.year + current_time.month + current_time.day + \
                                 current_time.hour + current_time.minute + current_time.second + current_time.microsecond
        PC = sum_of_time_components % 3 + 1
        print(PC)
        human_score, PC_score = round_result(human, PC)
        current_human_score += human_score
        current_PC_score += PC_score
        print(f'human: {current_human_score} vs {current_PC_score} :PC')
        human = input()
    else:
        print('Game Over')

game()


