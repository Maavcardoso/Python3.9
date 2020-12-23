# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Como desafio adicional, faça um programa em for e outro em while.

# Programa em While:

n = int(input('\nInforme o número a ser fatorado: '))
fat = n
print(f'{n}! ',end='=')
while n != 0:
    if fat == n:
        print(f' {n} ',end='x')
        n = n-1
    elif n > 1: 
        fat = fat*n
        print(f' {n} ',end='x')
        n = n -1
    if n == 1:
        print(f' {n} ',end='= ')
        break
print(fat)

 # Programa em For:

n = int(input('\nInforme o número a ser fatorado: '))
fat = n
print(f'{n}! ',end='=')
for c in range(n,0,-1):
    if fat == n:
         print(f' {n} ',end='x')
         n = n-1
    elif n > 1: 
        fat = fat*n
        print(f' {n} ',end='x')
        n = n -1
    if n == 1:
        print(f' {n} ',end='= ')
        break
print(fat)