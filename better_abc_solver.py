a = int(input('A: '))
b = int(input('B: '))
c = int(input('C: '))
square = b**2 - 4*a*c
if square == 0:
    print('One Real Solution')
    print(f'{b}/{2*a}')
    print('aka ',(-b)/(2*a))
elif square < 0:
    print('No Real Solution')
    print('i')
else:
    print('Two Real Solution')
    print(f'{-b}+sqrt({square})/{2*a}')
    print(f'aka {(-b+(square**0.5))/(2*a)}')
    print(f'{-b}-sqrt({square})/{2*a}')
    print(f'aka {(-b-(square**0.5))/(2*a)}')