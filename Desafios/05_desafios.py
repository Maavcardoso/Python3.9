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

from datetime import date
x = int(input('Digite um ano ou digite 0 para utilizar o ano atual:  '))
if x == 0:
    x = date.today().year
if x % 4 == 0:
    if x % 100 == 0 and x % 400 != 0:
        print(f'\n{x} Não é bissexto')
    else:
        print(f'\n{x} é bissexto')
else:
    print(f'\n{x} Não é bissexto')

# Faça um programa que leia 3 números e diga qual deles é o maior e o menor.

print('\n','-=-' * 10) 
print('\n Exercício 6\n')

x = float(input('Digite o primeiro número: '))
y = float(input('\nDigite o segundo número: '))
z = float(input('\nDigite o terceiro número: '))

if x < y and x < z:
    menor = x
elif y < x and y < z:
    menor = y
elif z < x and z < y:
    menor = z
print (f'znO menor número é {menor}')

if x > y and x > z:
    maior = x
elif y > x and y > z:
    maior = y
elif z > x and z > y:
    maior = z
print(f'znO maior número é {maior}')

# Faça um programa que realize um ajuste salarial de acordo com o salário do usuário. 
# Se ele ganhar mais que 1250 R$, acrescentar 10%. Se igual ou menos, acrescentar 15%.

print('\n','-=-' * 10) 
print('\n Exercício 7\n')

x = float(input('Digite seu salário: '))

if x > 1250:
    y = x*1.1
    print (f'Com o reajuste de 10%, seu novo salário será {y:0.2f}, {y-x:0.2f}R$ a mais.')
else:
    y = x*1.15
    print(f'Com o reajuste de 15%, seu novo salário será {y:0.2f}, {y-x:0.2f}R$ a mais.')


#Faça um programa que analise a existencia de um triangulo. (1.0) 
# * Para um triangulo existir, o maior lado deve ser menor que a soma dos outros dois lados.
# EX: a = 10, b = 5, c = 6. Seria possivel ter um triangulo, pois a < b + c.

print('\n','-=-' * 10) 
print('\n Exercício 8\n')

x = float(input('Digite o comprimento do primeiro lado: '))
y = float(input('\nDigite o comprimento do segundo lado: '))
z = float(input('\nDigite o comprimento do terceiro lado: '))

if x > y and x > z:
    if x < y + z:
        print(f'\nÉ possível existir um triângulo., pois {x} < {y+z}')
    else:
        print(f'\nNão é possível existir um triângulo, pois {x} = > {y+z}')
if y > x and y > z:
    if y < x + z:
        print(f'\nÉ possível existir um triângulo, pois {y} < {x+z}')
    else:
        print(f'\nNão é possível existir um triângulo, pois {y} = > {x+z}')
if z > y and z > x:
    if z < x + y:
        print(f'\nÉ possível existir um triângulo, pois {z} < {x+y}')
    else:
        print(f'\nNão é possível existir um triângulo, pois {z} = > {x+y}')
