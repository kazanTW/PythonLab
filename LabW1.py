#CompArch PythonLab W1 Demo

import sys

def D(a, b, c):
    return (b ** 2) - (a * c * 4)

def rootFormulaMinus(a, b, c):
    return ((-b) - D(a, b, c) ** (1 / 2)) / (a * 2)

def rootFormulaPlus(a, b, c):
    return ((-b) + D(a, b, c) ** (1 / 2)) / (a * 2)

if __name__ == '__main__':
    print('This program is for calculating roots of a quadratic equation in one variable.')
    
    while True:
        try:
            a, b ,c = map(float ,input('Print coefficients of the quadratic eqution(a, b, c): ').split())
            if (D(a, b, c) > 0):
                print('The roots of the equation is: ' + str('%.2f'%(rootFormulaMinus(a, b, c))) + ',' + str('%.2f'%(rootFormulaPlus(a, b, c))))
            elif (D(a, b, c) == 0):
                print('The roots of the equation is: ' + str(((b * (-1)) / (a * 2))) + '(repeated root)')
            elif (D(a, b, c) < 0):
                print('The equation has no real number root.')
        except EOFError:
            print('Thank you for using. Bye!')
            sys.exit(0)
        except ZeroDivisionError:
            print(f'You cannot divide 0! Try again.')
            continue