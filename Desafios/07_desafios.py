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
maior = 0
menor = 0
for c in range (0,7):
    n = int(input(f'Digite o ano de nascimento da {c+1}ª pessoa: '))
    anos.insert(c, n) # .insert() permite que insira dados dentro de uma lista. na relação insert(x,y), x é o parametro e y o dado.
    if x - n >= 21:
        maior = maior + 1
    else:
        menor = menor + 1

for c2 in range (0,(len(anos))):
    if x - anos[c2] >= 21:
        print('\033[1;32m',anos[c2],end=' ')
        
    else:
        print('\033[1;33m', anos[c2],end=' ')
        
print(f'\n\033[1;32m{maior} dessas pessoas são maiores de idade.\n\033[1;33m{menor} dessas pessoas são menores de idade.')

# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
print('\n','-=-' * 10) 
print('\n Exercício 10\n')
peso = []
for c in range (0,5):
    n = float(input(f'Digite o peso da {c+1}ª pessoa (Em Kg): '))
    peso.insert(c, n) # Preenche a lista os valores lidos
peso = sorted(peso) # Organiza os valores da lista em ordem crescente.
print(f'O peso mais leve é {peso[0]}Kg\nO peso mais pesado é {peso[4]}Kg')
# A maneira como eu consegui de resolver o exercício: manipulação de lista com for.
# contudo, a maneira como o Guanabara resolveu não precisa de lista, apenas do algoritmo
# certo.

maior = 0
menor = 0
for c in range (0,5):
     n = float(input(f'Digite o peso da {c+1}ª pessoa (Em Kg): '))
     if c == 1:
         menor = n # O primeiro peso sempre vai ser maior e menor, já que não há valor antes disso.
         maior = n
     else:
         if n > maior: # Aqui o programa lê o próximo valor, se for maior ele substitui o valor da variavel 'maior'
             maior = n
         elif n < menor: # Caso seja menor, ele substitui o valor da variavel 'menor'
             menor = n
print(f'O peso mais leve é {menor}Kg\nO peso mais pesado é {maior}Kg')

print('\n','-=-' * 10) 
print('\n Exercício 11\n')
mascv = 0 # guarda a idade do homem mais velho
mascn = '' # guarda o nome do homem mais velho
femid = 0 # guarda a quantidade de vezes aparece uma mulher com menos de 20 anos
mediaid = 0 # guarda a soma das idades.
for pess in range(0,4):
    print(f'----- {pess+1}ª Pessoa -----') # Pede os dados pessoais
    n = str(input('Nome: ')).strip().capitalize()
    i = int(input('Idade: '))
    s = str(input('Gênero [M/F/X]: ')).upper().strip()
    mediaid = mediaid + i # Soma a idade com a média
    if i > mascv and s == 'M': # altera o valor se um homem mais velho for colocado na lista
        mascv = i
        mascn = n
    if s == 'F' and i < 20: # Acrescenta ao contador se a pessoa for mulher e tiver menos de 20 anos
        femid = femid + 1
mediaid = mediaid/4 # Média da idade
print(f'\nA média de idade do grupo é de {mediaid} anos.')
print(f'\nO homem mais velho tem {mascv} anos e se chama {mascn}.')
print(f'\nAo todo são {femid} mulheres com menos de 20 anos.')

