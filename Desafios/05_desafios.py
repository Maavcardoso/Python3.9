# Jogo da Adivinhação 1.0: O Computador deve gerar um número aleatório de
# 0 à 5 e deve perguntar ao usuário que número foi gerado, informando
# se o usuário errou ou acertou

from random import randint
from time import sleep

print('\n','-=-' * 10)
print('\n Exercício 1\n')
print('Estou pensando em um número de 0 a 5.')
y = randint(0,5)
x = int(input('\nEm Qual Número eu pensei? '))
print('\nVejamos...')
sleep(2)
if x == y:
    print('\nParabéns! Você acertou!')
else:
    print(f'\nOps! O número certo era {y}. Tente Novamente!\n')

print('\n','-=-' * 10)

# Escreva um programa que leia a velocidade de um Carro.
# Se o Carro ultrapassar dos 80 km/h, o motorista deve ser mutado
# em R$ 7,00 para cada Km acima do limite

print('\n','-=-' * 10)
print('\n Exercício 2\n')

vel = float(input('Qual é a velocidade do Carro (em KM/H)? '))
if vel <= 80:
    print('Você está dentro do limite de velocidade!')
else:
    multa = (vel - 80)*7
    print(f'Está acima do limite de velocidade! Portanto, será cobrado uma multa de {multa:0.2f}R$')
print('\n','-=-' * 10)

# Escreva um programa que identifique se o numero dado pelo usuário
# é par ou ímpar.

print('\n','-=-' * 10) 
print('\n Exercício 3\n')

x = float(input('\nDigite um número: '))
if x % 2 == 0:
    print(f'\n{x} é um número par!')
else:
    print(f'\n{x} é um número ímpar!')
print('\n','-=-' * 10)

# Escreva um programa que calcule o preço do bilhete de
# uma viagem baseado em quantos KMs serão rodados.
# Cada KM custa 0,50 R$ até 200KM. Se a viagem for maior,
# a Kilometragem passa a custar 0,45 R$

print('\n','-=-' * 10) 
print('\n Exercício 4\n')

x = float(input('\nInforme quantos KM você irá viajar: '))
if x <= 200:
    preco = x*0.5
    print(f'\nUma viagem de {x}KM irá custar {preco:0.2f}R$.')
else:
    preco = x*0.45
    print(f'\nUma viagem de {x}KM irá custar {preco:0.2f}R$, ganhando desconto de 10% por ser mais longa que 200KM!') 

print('\n','-=-' * 10)

# Escreva um programa que calcule se o número fornecido pelo usuário é bissexto ou não.

print('\n','-=-' * 10) 
print('\n Exercício 5\n')

x = int(input('Digite um ano: '))
if x % 4 == 0:                         
    if x % 100 == 0 and x % 400 != 0:
        print('Não é bissexto')
    else:
        print('é bissexto')
else:
    print('Não é bissexto')
        
