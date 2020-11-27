# Faça um programa que peça nome de 4 pessoas e sorteie uma delas

from random import choice

a1 = input('\nInsira o Primeiro Nome: ')
a2 = input('\nInsira o Segundo Nome: ')
a3 = input('\nInsira o Terceiro Nome: ')
a4 = input('\nInsira o Quarto Nome: ')

lista = [a1, a2, a3, a4]
n = choice(lista)
print (f'\nO nome sorteado foi {n}\n')

# Agora um programa que liste os 4 sorteados em posições.

from random import sample

n = sample([a1, a2, a3, a4],4)
print(f'\nO primeiro sorteado foi {n[1]}\nO segundo sorteado foi {n[2]}\nO terceiro sorteado foi {n[3]}\nO quarto sorteado foi {n[4]}\n')