# Escreva para aprovar um empréstimo bancário para comprar uma casa.
# O programa deve perguntar o valor do imóvel, o salário do comprador e
# em quantos anos ele irá pagar.
# Calcule a prestação mensal, sendo que ela não pode exceder 30% do salário,
# ou então o empréstimo será negado.

print('\n','-=-' * 10)
print('\n Exercício 1\n')
casa = float(input('Digite o valor da casa: '))
salar = float(input('\nDigite seu salário: '))
ano = int(input('\nDigite em quantos anos irá pagar o empréstimo: '))
prest = casa / (ano*12)
orcam = salar * 0.3
if prest > orcam:
    print(f'\nEmpréstimo negado. A prestação (R${prest:0.2f}) está acima do orçamento (R${orcam:0.2f}).')
else:
    print(f'\nEmpréstimo aprovado! Sua prestação irá ser de R${prest:0.2f}.')

# Escreva um programa que leia 2 números e diga qual é o maior ou se são iguais

print('\n','-=-' * 10)
print('\n Exercício 2\n')
x = float(input('\nDigite o primeiro número: '))
y = float(input('\nDigite o segundo número: '))
if x > y:
    print('\nO primeiro valor é maior.')
elif y > x:
    print('\nO segundo valor é maior.')
else:
    print('\nNão existe valor maior. Ambos são iguais.') 

# Escreva um programa que leia o ano de nascimento de um jovem e diga se:
# Ainda vai se alistar no serviço, se esta na hora de se alistar ou se já passou do tempo.
# E também deve mostrar quanto tempo falta para se alistar ou quanto tempo passou do prazo.

print('\n','-=-' * 10)
print('\n Exercício 3\n')
from datetime import date
x = int(input('Por favor, informe o ano do seu nascimento: '))
y = x + 18 # Ano de alistamento.
x = date.today().year - x # Calcula a idade da pessoa.
print(f'\nSeu ano de alistamento: {y}') 
if x < 18:
    print(f'\nAinda faltam {18-x} anos para o alistamento.')
elif x > 18:
    print(f'\nO alistamento está atrasado em {x-18} anos.')
else:
    print('\nEstá na hora de se alistar!')

# Escreva um programa que calcule a média de um aluno e diga se:
# foi reprovado (média abaixo de 5), está de recuperação (Média entre 5 e 6.9)
# ou foi aprovado (média 7 ou superior).

print('\n','-=-' * 10)
print('\n Exercício 4\n')
a1 = float(input('Digite sua nota A1: '))
a2 = float(input('\nDigite sua nota A2: '))
nf = (a1 + a2)/2
if nf < 5:
    print(f'\nVocê foi reprovado. Sua média {nf} está abaixo de 5.')
elif nf >= 5 and nf < 7:
    print(f'\nVocê está de recuperação. Sua média foi {nf}. Estude!')
else:
    print(f'\nParabéns! Você foi aprovado com média {nf}.')


# Escreva um programa que pergunte o ano de nascimento de um atleta e o classifique de acordo
# com a sua idade:
# Até 9 anos: Mirim
# Até 14 anos: Infantil
# Até 19 anos: Junior
# Até 25 anos: Sênior
# Acima: Master

print('\n','-=-' * 10)
print('\n Exercício 5\n')
from datetime import date
x = int(input('\nInforme o ano de Nascimento do Atleta: '))
x = date.today().year - x
print(f'\nHoje, o atleta tem {x} anos')
if x <= 9:
    print('\nO atleta pertence a categoria Mirim.')
elif x <= 14:
    print('\nO atleta pertence a categoria Infantil')
elif x <= 19:
    print('\nO atleta pertence a categoria Junior')
elif x == 25:
    print('\nO Atleta pertence a categoria Sênior')
else:
    print('\nO Atleta pertence a categoria Master')

# Existência de triangulos 2.0
# Além de falar se é possível criar um triangulo, também crie condições que analisem se:
# O triangulo é Escaleno, Equilátero ou Isósceles. 

print('\n','-=-' * 10) 
print('\n Exercício 6\n')

x = float(input('Digite o comprimento do primeiro lado: '))
y = float(input('\nDigite o comprimento do segundo lado: '))
z = float(input('\nDigite o comprimento do terceiro lado: '))

if x < y + z and y < x + z and z < x + y: # identifica se é possivel existir o triangulo
    if x == y != z or x == z != y or y == z != x: # identifica o tipo de triangulo
        print('\nEste é um triângulo ISÓSCELES, pois dois lados são iguais.\n')
    elif x == y and y == z:
        print('\nEste é um triângulo EQUILÁTERO, pois todos os lados são iguais.\n')
    else:
        print('\nEste é um triângulo ESCALENO, pois todos os lados são diferentes.\n')
else:
    print('\nNão é possivel existir um triângulo.\n')
    exit()

# Escreva um programa que leia a altura e o peso de uma pessoa, calcule seu IMC e mostre seu
# status de acordo com a tabela abaixo:
# abaixo de 18.5 - abaixo do peso
# entre 18.5 e 25 - peso ideal
# 25 até 30 - sobrepeso
# 30 até 40 - obesidade
# acime de 40 - obesidade mórbida

print('\n','-=-' * 10) 
print('\n Exercício 7\n')

peso = float(input('Digite seu peso (em KG): '))
altura = float(input('Digite sua altura (em Metros): '))
imc = peso/altura**2
print(f'Sua pontuação foi {imc:.2f}.', end=' ')
if imc < 18.5:
    print('Você está abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Você está no Peso Ideal!')
elif imc >= 25 and imc < 30:
    print('Você está com sobrepeso.')
elif imc >= 30 and imc <= 40:
    print('Você esta com obesidade.')
else:
    print('Você esta com obesidade mórbida.')


# Elabore um programa que calcule o valor a ser pago por um produto
# considerando seu preço normal e condição de pagamento.
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros 

print('\n','-=-' * 10) 
print('\n Exercício 8\n')

preco = float(input('Digite o preço do produto: R$'))
print('\nDigite a opção de pagamento:\n[1]--À vista em dinheiro/cheque\n[2]--À vista no cartão\n[3]--Em até 2x no cartão\n[4]--Em 3x ou mais no cartão.')
escolha = int(input('\nSua escolha: '))
if escolha == 1:
    preco = preco - (preco*0.1)
    print(f'\nVocê ganha 10% de desconto neste método de pagamento, portanto o novo preço será R${preco:.2f}\n')
elif escolha == 2:
    preco = preco - (preco*0.05)
    print(f'\nVocê ganha 5% de desconto neste método de pagamento, portanto o novo preço será R${preco:.2f}\n')
elif escolha == 3:
    print(f'\nO produto irá custar R${preco:.2f}, pagando duas parcelas de R${preco/2:.2f}\n')
else:
    parce = int(input('Em quantas vezes irá parcelar? '))
    preco = preco*1.2
    print(f'\nNeste método de pagamento haverá 20% de juros, portanto o novo preço será R${preco:.2f}\nCada parcela irá custar R${preco/parce:.2f}')







