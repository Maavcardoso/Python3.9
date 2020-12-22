# Faça um programa que faça uma contagem regressiva de 10 até 0, com pausa de 1 segundo entre eles.

print('\n','-=-' * 10) 
print('\n Exercício 1\n')
from time import sleep
for c in range (10, -1, -1):
    print(c,'...')
    sleep(1)
print('Feliz ano novo!!! :D :D :D')

#  Crie um programa que mostre na tela todos os números pares entre 1 e 50.

print('\n','-=-' * 10) 
print('\n Exercício 2\n')
for c in range(1, 51):
    if c % 2 == 0:
        print(c)
    else:
        pass

# Crie um programa que calcule a soma de todos os números ímpares multiplos de 3 que se encontra
# no intervalo entre 1 até 500.

print('\n','-=-' * 10) 
print('\n Exercício 3\n')
soma = 0 # Acumulador, soma os valores do contador
cont = 0 # Contador, conta o número de vezes que a repetição ocorreu.
for c in range (1, 501):
    if c % 3 == 0 and c % 2 != 0:
        soma = soma + c
        cont = cont + 1
    else: 
        pass
print(f'A soma dos {cont} números é igual a: {soma}')

# Refaça a tabuada mas dessa vez, num laço for.

print('\n','-=-' * 10) 
print('\n Exercício 4\n')
n = int(input('Digite a tabuada desejada: '))
for c in range (1,11):
    tabu = n * c
    print(f'{n} x {c} = {tabu}')

# Desenvolva um programa que leia 6 número inteiros e os soma apenas se forem pares, caso seja ímpar, desconsidere-o.

print('\n','-=-' * 10) 
print('\n Exercício 5\n')
s = 0
cont = 0
for c in range(0,6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s = s + n
        cont = cont + 1
    else:
        pass
if cont > 1:
    print(f'A soma dos {cont} números pares é igual a {s}')
elif cont == 1:
    print(f'Há apenas um número par, {s}')
else:
    print('Não há nenhum número par nesta sequência.')

# Escreva um programa que peça o primeiro número de uma PA e a sua razão, e então imprima os primeiros 10 números da PA.

print('\n','-=-' * 10) 
print('\n Exercício 6\n')
n = float(input('Digite o primeiro valor da PA: '))
r = float(input('Digite a razão da PA: '))
for c in range (0,10):
    pa = n + (r*c)
    print(f'{pa:.2f}',end=' ⇨ ')
print('Fim do programa.') 

# Faça um programa que leia um número inteiro e identifique se ele é ou não um número primo.
# (Divisivel somente por 1 e por ele mesmo)

print('\n','-=-' * 10) 
print('\n Exercício 7\n')
print('Seu número é primo?')

n = int(input('Digite um número: '))
count = 0

for c in range(1,n+1):
    if n % c == 0:
        print(f'\033[32m{c}',end=' ') # printa números divisiveis em verde.
        count = count + 1
    else:
        print(f'\033[31m{c}', end=' ') # printa números não divisiveis em vermelho.

print (f'\n\n\033[97m{n} foi divisível {count} vezes')

if count == 2: 
    print(f'\033[97mPortanto é um número primo!\n')
else:
    print(f'\033[97mPortanto é um número composto.\n')

# Escreva um programa que leia uma frase e diga se ela é um palíndromo 
# (Da esquerda para a direita e da direita para esquerda forma a mesma palavra/frase)

print('\n','-=-' * 10) 
print('\n Exercício 8\n')
n = str(input('Digite um texto: '))
print('\nAo contrário fica: ',end='')
n = n.strip()
n = n.split()
ncopia = ' '.join(n) #print(ncopia) == Frase com espaçamento correto.
n = ''.join(n)
n = n.lower()
s = str('') # String q será escrita ao contrário
for c2 in range ((len(ncopia)-1),-1,-1): # Escreve a frase ao contrário
    print((ncopia[c2]),end='')
for c in range ((len(n)-1),-1,-1): # Verifica se a frase é um Palíndromo
    n2 = (n[c])
    s = s + n2 # print(s) no fim da repetição: A Palavra ao contrário.
if s == n:
    print('\n\nEsta frase é um Palíndromo!')
else:
    print('\n\nEsta frase não é um Palíndromo.')

# Implementei algumas melhoras:
# Por mais espaços que tenha um frase, na hora de analisar não os considera (Como proposto no exercício),
# Contudo, criei um segundo for que também transcreve de maneira correta.

# Faça um programa que leia o ano de nascimento de 7 pessoas e diga quantas são menores e maiores de idade
# considere a maior idade de 21 pra cima. 

print('\n','-=-' * 10) 
print('\n Exercício 9\n')
from datetime import date
anos = []
x = date.today().year
for c in range (0,7):
    n = int(input(f'Digite o ano de nascimento da {c+1}ª pessoa: '))
    anos.insert(c, n) # .insert() permite que insira dados dentro de uma lista. na relação insert(x,y), x é o parametro e y o dado.
maior = 0
menor = 0
for c2 in range (0,(len(anos))):
    if x - anos[c2] > 21:
        maior = maior + 1
    else:
        menor = menor + 1
print(f'\n{maior} dessas pessoas são maiores de idade.\n{menor} dessas pessoas são menores de idade.')
