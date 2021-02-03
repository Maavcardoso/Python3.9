from random import randint # Importei o método random para escolher um número aleatório.
print(5*'-=','VAMOS JOGAR PAR OU ÍMPAR!',5*'=-')
n = 0
d = ''
vit = 0
npc = 0
total = 0
while True:
    n = int(input('Digite um valor: '))
    d = str(input('Par ou ímpar? [P/I]: ')).strip().upper()[0]
    npc = randint(0, 10)
    total = npc + n
    print(10*'-')
    print(f'Você jogou {n} e o Computador jogou {npc}.', end=' ')
    if total % 2 == 0:
        print(f'{total} é PAR')
        if d == 'P':
            print('Você venceu!')
            print('Vamos jogar novamente...')
            vit += 1
            print(10*'-')
        else:
            print('Você perdeu!')
            break
    else:
        print(f'{total} é ÍMPAR')
        if d == "I":
            print('Você venceu!')
            print('Vamos jogar novamente...')
            vit += 1
            print(10*'-')
        else:
            print('Você perdeu!')
            break
print(15*'=-=')
print(f'\nGame Over! Você venceu {vit} vezes consecutivas!\n')