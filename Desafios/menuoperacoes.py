# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar, [2] multiplicar, [3] maior, [4] novos numeros e [5] sair do programa
# O programa deverá realizar as opreações solicitadas em cada caso. 
print('-='*5,'Bem-Vindo ao Operador 1.0!','=-'*5)
n1 = float(input('\n Por favor, informe o primeiro valor: '))
n2 = float(input('\n Agora, o segundo: '))
menu = 0
decisao = ''
while menu != 5:
    menu =int(input('\n O que você deseja fazer?\n\n[1] Somar Valores\n[2] Multiplicar Valores\n[3] Maior valor\n[4] Alterar valores\n[5] Sair do programa\n\nSua escolha > '))
    if menu == 1:
        soma = n1 + n2
        print(f'\n{n1} + {n2} = {soma}')
        decisao = str(input('\nDeseja realizar outra operação? [S/N] > ')).upper().strip()[0]
    elif menu == 2:
        multi = n1 * n2
        print(f'\n{n1} x {n2} = {multi}')
        decisao = str(input('\nDeseja realizar outra operação? [S/N] > ')).upper().strip()[0]
    elif menu == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
        elif n2 > n1:
            print(f'{n2} é maior que {n1}')
        else:
            print(f'Os dois valores são iguais!')
        decisao = str(input('\nDeseja realizar outra operação? [S/N] > ')).upper().strip()[0]
    elif menu == 4:
        n1 = float(input('Informe o primeiro valor: '))
        n2 = float(input('Informe o segundo valor: '))
        print('\nValores Alterados com sucesso.')
        decisao = str(input('\nDeseja realizar outra operação? [S/N] > ')).upper().strip()[0]
    elif menu == 5:
        print('\nObrigado por usar o Operador 1.0')
        break
    else:
        print('\nOpção inválida! Informe sua opção novamente.')
    if decisao == 'N':
        print('\nObrigado por usar o Operador 1.0')
        break
    while decisao != 'S' and decisao != 'N':
        decisao = str(input('Opção inválida! Informe sua opção novamente [S/N] > ')).strip().upper()[0]
        if decisao == 'N':
            print('\nObrigado por usar o Operador 1.0')
            quit()

    