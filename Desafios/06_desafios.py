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












