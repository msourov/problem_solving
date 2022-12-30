import random
def game(dict, sys_move, player_move):
    if sys_move == 'r' and player_move == 's':
        return f'You Lost. System choose {dict[sys_move]} and you choose {dict[player_move]}.'
    elif sys_move == 's' and player_move == 'p':
        return f'You Lost. System choose {dict[sys_move]} and you choose {dict[player_move]}.'
    elif sys_move == 'p' and player_move == 'r':
        return f'You Lost. System choose {dict[sys_move]} and you choose {dict[player_move]}.'
    elif sys_move == player_move:
        return f'That\'s a tie!'
    else:
        return f'You Won! You choose {dict[player_move]} and System choose {dict[sys_move]}.'


if __name__ == '__main__':
    tup = ('r', 'p', 's')
    dict = {'r': 'Rock', 'p': 'Paper', 's': 'Scissor'}
    sys_move = random.choice(tup)
    player_move = input("""Your turn: 
    Enter r for Rock
    Enter p for Paper
    Enter s for Scissor\n""")
    print(game(dict, sys_move, player_move))