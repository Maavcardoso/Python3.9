from random import choice
from time import sleep
joke = ['pedra', 'papel', 'tesoura']
x = choice(joke)
print('Vamos jogar Jokenpô!\n\n[1] para Pedra\n[2] para Papel\n[3] para Tesoura')
y = int(input('\nFaça sua escolha: '))
print('\nJo...', end='')
sleep(0.5)
print('Ken...', end='')
sleep(0.5)
print('Pô!')
sleep(0.5)
if y == 1: # Usuário jogou pedra
    y = 'Pedra'
    print(f'\n\033[0;32m{y.capitalize()} \033[0;97mcontra \033[0;31m{x.capitalize()}\033[0;97m')
    if x == joke[0]:
        print('\nEmpate!\n')
    elif x == joke[1]:
        print('\n\033[0;31mO computador venceu!\n')
    else:
        print('\n\033[0;32mVocê venceu!\n')
elif y == 2: # Usuário jogou papel
    y = 'Papel'
    print(f'\n\033[0;32m{y.capitalize()} \033[0;97mcontra \033[0;31m{x.capitalize()}\033[0;97m')
    if x == joke[1]:
        print('\nEmpate!\n')
    elif x == joke[2]:
        print('\n\033[0;31mO Computador venceu!\n')
    else:
        print('\n\033[0;32mVocê venceu!\n')
elif y == 3: # Usuário jogou tesoura
    y = 'Tesoura'
    print(f'\n\033[0;32m{y.capitalize()} \033[0;97mcontra \033[0;31m{x.capitalize()}\033[0;97m')
    if x == joke[2]:
        print('\nEmpate!\n')
    elif x == joke[0]:
        print('\n\033[0;31mO computador venceu!\n')
    else:
        print('\n\033[0;32mVocê Venceu!\n')
else:
    print('Jogada Inválida!')