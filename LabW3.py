import random
import sys

def rps(status):
    if status == 'r':
        return 1
    elif status == 'p':
        return 2
    elif status == 's':
        return 3

def punch(statusPlayer, statusCom):
    if statusPlayer == 1:
        if statusCom == 2:
            print(f'You lose. Try again.\n')
            return -1
        elif statusCom == 3:
            print(f'You WIN! See you next time!\n')
            return 1
        elif statusCom == 1:
            print(f'Tie. Try again.\n')
            return 0
    elif statusPlayer == 2:
        if statusCom == 3:
            print(f'You lose. Try again.\n')
            return -1
        elif statusCom == 1:
            print(f'You WIN! See you next time!\n')
            return 1
        elif statusCom == 2:
            print(f'Tie. Try again.\n')
            return 0
    elif statusPlayer == 3:
        if statusCom == 1:
            print(f'You lose. Try again.\n')
            return -1
        elif statusCom == 2:
            print(f'You WIN! See you next time!\n')
            return 1
        elif statusCom == 3:
            print(f'Tie. Try again.\n')
            return 0

class WrongPunch(Exception):
    def __init__(self):
        super().__init__


if __name__ == '__main__':
    print(f'This program is for playing rock-paper-scissors,\n"r" for the rock, "p" for the paper, "s" for the scissor.')

    while True:
        try:
            statusList = [1, 2, 3]
            status = input(f'Please enter your punch: ')
            statusPlayer = rps(status)

            if (statusPlayer != 1) and (statusPlayer != 2) and (statusPlayer != 3):
                raise WrongPunch
            else:
                statusCom = random.choice(statusList)
                result = punch(statusPlayer, statusCom)

                if result == 1:
                    break
                elif result == -1:
                    continue
                elif result == 0:
                    continue
        except EOFError:
            print(f'\nThank you for using. Bye!')
            sys.exit()
        except WrongPunch:
            print(f'Invalid punch. Are you Spock?\n')
            continue