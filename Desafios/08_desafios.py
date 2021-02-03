# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M', 'F' ou 'X'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

print('\n','-=-' * 10) 
print('\n Exercício 1\n')


dado = ''
while dado != 'M' and dado != 'F' and dado != 'X':
    dado = str(input('Informe seu gênero [M/F/X]: ')).upper().strip()[0] # Fatia a primeira letra, então se escrever "masculino" Só pega a letra 'M'.
    if dado == 'M' or dado == 'F' or dado == 'X':
        print(f'{dado} foi registrado com sucesso.')
        break
    else:
        print(f'{dado} é uma escolha inválida. Por favor',end=', ')
        # Minha solução


dado = str(input('Informe seu gênero [M/F/X]: ')).strip().upper()[0]
while dado not in 'MFX':
    dado = str(input('Dado inválido. Por favor, informe seu gênero.')).strip().upper()[0]
print(f'{dado} foi registrado com sucesso.')
        # Solução proposta pelo Guanabara. A condição do laço "while" dispensa o uso do if/else que criei na minha solução.

#Faça um programa que some os números dados pelo usuário e quando for digitado 999 pare a repetição e mostre o resultado da soma.

print('\n','-=-' * 10) 
print('\n Exercício 2\n')
n = int(input('Digite um número para a soma [999 para parar]: '))
if n == 999:
    print('Não houve soma!')
    exit()
n1 = 0
c = 0
while n != 999:
    n1 = n1 + n
    n = int(input('Digite um número para a soma [999 para parar]: '))
    c += 1
print(f'Foram digitados {c} números e a soma é igual a {n1}.')

#Faça um programa que leia um número e pergunte ao usuário se ele quer continuar. Quando ele não quiser mais, faça a média de todos os números e diga
#qual foi o maior e o menor valor digitados.

print('\n','-=-' * 10) 
print('\n Exercício 3\n')

n = int(input('Digite um número: '))
c = 1
menor = n 
maior = n
n1 = n
decisao = 'S'
while decisao != 'N':
    decisao = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while decisao != 'S' and decisao != 'N':
        decisao = str(input('Escolha inválida. Por favor, digite uma alternativa válida [S/N]: ')).strip().upper()[0]
    if decisao == 'S':
        n = int(input('Digite um número: '))
        n1 = n1 + n
        c += 1
        if menor > n:
            menor = n
        if maior < n:
            maior = n
n1 = n1/c
print(f'A média dos números é igual a {n1}.\nO maior número é {maior}.\nO menor número é {menor}.')