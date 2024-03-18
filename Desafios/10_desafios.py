
# Crie um programa que tenha um tupla preenchida com uma contagem por extenso de 0 a 20.
# O programa deverá ler um número pelo teclado (entre 0 e 20) e mostra-la por extenso.

print('\n','-=-' * 10) 
print('\n Exercício 1\n')

num = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove',
'Dez','Onze','Doze','Treze','Quatorze','Quinze','Dezesseis','Dezesete','Dezoito','Dezenove','Vinte')
while True:
    numex = int(input('\nDigite um número entre 0 e 20: '))
    while numex < 0 or numex > 20:
        numex = int(input('\nTente novamente. Digite um número entre 0 e 20: '))
    print(f'\nVocê digitou o número {num[numex]}.')
    escolha = str(input('\nDeseja continuar? [S/N]: ')).strip().upper()[0]
    if escolha == 'N':
        break
print('\nObrigado por usar o contador!')

# Crie uma tupla preenchida com os 20 primeiros colocados do Brasileirão, na ordem e colocação. Depois mostre:
# A - Apenas os 5 primeiros colocados;
# B - Os últimos 4 colocados;
# C - Uma lista com os times em ordem alfabética;
# D - Em que posição na tabela está o Palmeiras. 

placar = ('Internacional', 'Flamengo', 'Atlético Mineiro', 'São Paulo', 'Fluminense', 'Grêmio', 'Palmeiras','Corinthians',
'Bragantino','Santos','Athletico-PR','Atlético Goiano','Ceará','Sport Recife','Fortaleza', 'Bahia','Vasco da Gama','Goiás','Coritiba', 'Botafogo')
print(40*'=-=')
print(f'Lista de Times do Brasileirão: {placar}')
print(40*'=-=')
print(f'Os cinco primeiros são: {placar[0:5]}')
print(40*'=-=')
print(f'Os quatro ultimos são: {placar[16:]}')
print(40*'=-=')
print(f'Times em ordem alfabética: {sorted(placar)}')
print(40*'=-=')
print(f'O Palmeiras está na {placar.index("Palmeiras")+1}ª posição')

#Crie um programa que gere 5 números aleatórios e os coloque em uma
#tupla. Mostre os números listados e indique o menor e o maior valor.

import random
tupla_random = (random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10))
print("Os números sorteados foram: ",end="")
for nums in tupla_random:
    print(f" {nums}",end='')
print(f"\nO menor número sorteado foi:{min(tupla_random)}")
print(f"O maior número sorteado foi:{max(tupla_random)}")

#Crie um programa que leia 4 valores e os insira em uma tupla. Após isso, deve:
# A - Quantas vezes apareceu o número 9,
# B - Em que posição foi digitado o primeiro valor 3,
# C - Quais foram os números pares.

tupla_num = (int(input("Digite o 1º valor: ")),
             int(input("Digite o 2º valor: ")),
             int(input("Digite o 3º valor: ")),
             int(input("Digite o 4º valor: ")))
print(f'Os números digitados foram: {tupla_num}')
vezes9 = tupla_num.count(9)
print(f"O número 9 apareceu {vezes9} vezes.")
if 3 in tupla_num:
    print(f"O número 3 foi digitado na {tupla_num.index(3)+1}ª Posição")
else:
    print("O valor 3 não foi digitado nenhuma vez.") 
pares = 0
for nums in tupla_num:
    if nums % 2 == 0 and pares == 0:
        print("Os números pares digitados foram: ",end="")
        print(f"{nums}",end="")
        pares = 1
    elif nums % 2 == 0 and pares == 1:
            print(f" {nums}", end="")
    elif nums % 2 != 0:
        pass
if pares == 0:
        print(f'Nenhum número par foi digitado')

# Crie um programa que imprima produtos e preços de uma tupla em formato de tabela.

produtos = ("Leite", 4.25, "Amendoim", 16.66, "Chinelo", 170.25,"Kit Copo",1290.72,'Pó de mico', 69.99)
print(30*'-')
print('{:^30}'.format('Tabela de Preços'))
print(30*'-')
for i in range(0,len(produtos),2):
    print('{:.<20}'.format(produtos[i]),end='')
    print('R${:>8}'.format(produtos[i+1]))
print(30*'-')

# Crie um programa que contenha uma tupla com várias palavras. O programa deve
# mostrar todas as vogais de cada palavra.

palavras=("Aprender","Rolar","Palhaço","Fazueli","Cocada","Hipopotamo","Barterapia")
vogais = ("A","E","I","O","U") 
for palavra in palavras:
    palavra = palavra.upper()
    x = list(palavra)
    print(f"\nA palavra {palavra} possui as vogais: ",end="")
    for letra in x:
        if letra in vogais:
            print(f'{letra} ',end="")
