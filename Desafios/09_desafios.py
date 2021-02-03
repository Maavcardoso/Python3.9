# Faça um programa que leia infinitamente os números dados pelo usuário até ele digitar 999.
# E que no fim mostre quantos valores foram lidos e a soma entre eles (desconsiderando o flag) 

print('\n','-=-' * 10) 
print('\n Exercício 1\n')

n = 0  
s = 0
c = 0
while True:
    n = int(input('Digite um número (Digite 999 para parar): '))
    if n == 999:
        break
    s += n
    c += 1
print(f'A soma dos {c} números é igual a {s}')

# Faça um programa que leia infinitamente os valores fornecidos pelo usuário e de a tabuada de cada um deles.
# o programa deve parar quando o usuário inserir um valor negativo.

print('\n','-=-' * 10) 
print('\n Exercício 2\n')

n = 0  
c = 1
print('\n', 5*'-=','Bem-vindo a tabuada 3.0!',5*'=-')
while True:
    c = 1
    n = int(input('\nDigite a tabuada desejada (Digite um número negativo para parar): '))
    if n < 0:
        break
    print(20*'-')
    while c != 11:
        print(f'{n} x {c} = {n*c}')
        c += 1
    print(20*'-')
print('\nObrigado por usar a Tabuada 3.0!\n')
