import sys

def primeFind(n):
    if (n == 1):
        print(f'"1" is not a prime number.You may have to enter a bigger number.')
    elif (n == 2):
        print(f'"2" is a prime number, but you can try a bigger number.')
    elif (n != 1 and n != 2):
        print(str(2) + ' ' + str(3) + ' ', end = '')
        count = 2
        if (n != 3):
            for i in range(4, n + 1):
                if (i % 2 == 0):
                    continue
                elif (i % 2 != 0):
                    for j in range(2, i  + 1):
                        if (i % j == 0 and j != i):
                            break
                        elif (i % j != 0 and j != i):
                            continue
                        elif (i % j == 0 and j == i):
                            print(str(i) + ' ', end = '')
                            break
        print()


if __name__ == '__main__': 
    print(f'This program is for find all prime numbers less or equal to a certain number.')

    while True:
        try:
            n = int(input('Enter a number: '))
            if (n != 0):
                primeFind(n)
            else:
                print(f'"0" cannot be the range! Try again.')
                continue
        except EOFError:
            print(f'\nThank you for using. Bye!')
            sys.exit()