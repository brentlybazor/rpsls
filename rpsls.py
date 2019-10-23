from random import randint




def full_name(chosen):
    if chosen == 1 or chosen == 'r':
        computer = 'rock'
    elif chosen == 2 or chosen == 'p':
        computer = 'paper'
    elif chosen == 3 or chosen == 's':
        computer = 'scissors'
    elif chosen == 4 or chosen == 'l':
        computer = 'lizard'
    elif chosen == 5 or chosen == 'k':
        computer = 'spock'
    else:
        computer = chosen

    return computer

def short_name(chosen):
    if chosen == 1 or chosen == 'rock':
        computer = 'r'
    elif chosen == 2 or chosen == 'paper':
        computer = 'p'
    elif chosen == 3 or chosen == 'scissors':
        computer = 's'
    elif chosen == 4 or chosen == 'lizard':
        computer = 'l'
    elif chosen == 5 or chosen == 'spock':
        computer = 'k'
    else:
        computer = chosen

    return computer

def main():
    print('rock (r), scissors (s), paper (p), lizard (l), or spock (k)')
    player = input('Enter choice:')
    computer = randint(1,5)
    computer = short_name(computer)
    player_choice = full_name(player)
    computer_choice = full_name(computer)

    options = ['r', 's', 'p', 'l', 'k']

    print('')

    if player in options:
        vs_text = player_choice + ' vs ' + computer_choice
        print(vs_text)

    if player == computer:
        print('DRAW!')

    elif player == 'r' and computer == 's':
        print('Player Wins!')
    elif player == 'r' and computer == 'p':
        print('Computer Wins!')
    elif player == 'r' and computer == 'l':
        print('Player Wins!')
    elif player == 'r' and computer == 'k':
        print('Computer Wins!')

    elif player == 'p' and computer == 'r':
        print('Player Wins!')
    elif player == 'p' and computer == 's':
        print('Computer Wins!')
    elif player == 'p' and computer == 'k':
        print('Player Wins!')
    elif player == 'p' and computer == 'l':
        print('Computer Wins!')

    elif player == 's' and computer == 'p':
        print('Player Wins!')
    elif player == 's' and computer == 'r':
        print('Computer Wins!')
    elif player == 's' and computer == 'l':
        print('Player Wins!')
    elif player == 's' and computer == 'k':
        print('Computer Wins!')

    elif player == 'l' and computer == 'p':
        print('Player Wins!')
    elif player == 'l' and computer == 's':
        print('Computer Wins!')
    elif player == 'l' and computer == 'k':
        print('Player Wins!')
    elif player == 'l' and computer == 'r':
        print('Computer Wins!')

    elif player == 'k' and computer == 's':
        print('Player Wins!')
    elif player == 'k' and computer == 'p':
        print('Computer Wins!')
    elif player == 'k' and computer == 'r':
        print('Player Wins!')
    elif player == 'k' and computer == 'l':
        print('Computer Wins!')

    else:
        print('Something isn\'t right here')

    play = input('\nPlay again? [Y/n]')
    if play.lower() == 'n':
        continue_play = 'false'
    else:
        continue_play = 'true'
        main()

main()
