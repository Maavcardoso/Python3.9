# Faça um programa que leia o nome e a média de um aluno. Após isso,
# Também indique sua situação


aluno = {}
aluno['nome'] = str(input("Nome do Aluno: "))
aluno['media'] = float(input(f"Média de {aluno['nome']}: "))
if aluno['media'] < 5:
    aluno['situacao'] = "Reprovado"
else:
    aluno['situação'] = 'aprovado'

for k,v in aluno.items():
    print(f'{k} é igual a {v}')

# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
# dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

import random
import time

jogadas = {
    'jogador1':random.randint(1,6),
    'jogador2':random.randint(1,6),
    'jogador3':random.randint(1,6),
    'jogador4':random.randint(1,6)
}
ranking = sorted(jogadas.items(),key=lambda x: x[1],reverse=True)

print('Jogadas: ')
for k,v in jogadas.items():
    time.sleep(1);
    print(f'{k} tirou {v} no dado.')
print('Ranking dos jogadores: ')
for k,v in enumerate(ranking):
    time.sleep(1);
    print(f'{k+1}º colocado: {v[0]} com {v[1]} pontos')

# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade) em um dicionário
# se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário. Calcule
# acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

import datetime
funcionario = {}
funcionario['nome'] = str(input('Nome: '))
anoNascimento = int(input('Ano de Nascimento: '))
funcionario['idade'] = datetime.datetime.now().year - anoNascimento
funcionario['ctps'] = int(input('CTPS: '))
if (funcionario['ctps'] != 0):
    funcionario['anoContratacao'] = int(input('Ano de Contratação: '))
    funcionario['salario'] = int(input('Salário: '))
    funcionario['aposentadoria'] = funcionario['anoContratacao'] - anoNascimento + 35
for k,v in funcionario.items():
    print(f'{k} tem valor {v}')

# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada
# pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A. Quantas pessoas foram cadastradas;
# B. A média de idade do grupo;
# C. Uma lista com todas as mulheres
# D. Uma lista com todas as pessoas com idade acima da média.

pessoas = []
while(True):
    pessoa = {}
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
    while (pessoa['sexo'] != 'M' and pessoa['sexo'] != 'F' ):
        pessoa['sexo'] = str(input("Sexo inválido. Insira novamente [M/F]: ")).upper().strip()[0]
    pessoa['idade'] = float(input("Idade: "))
    pessoas.append(pessoa.copy())
    choice = str(input('Deseja Continuar? [S/N]: ')).upper().strip()[0]
    while (True):
        if choice in 'SN':
            break
        choice = str(input('Opção inválida. Digite S ou N: ')).upper().strip()[0]
    if choice == 'N':
        break
print('=-=' * 20)
print(f'- O grupo possui {len(pessoas)} pessoas.')
media = 0 
mulheres = []
for i in pessoas:
    media = media + i['idade']
    if (i['sexo'] == 'F'):
        mulheres.append(i['nome'])
media = media / len(pessoas)
print(f'- A média de idade é de {media:,.2f} anos.')
print(f'- As mulheres cadastradas foram: ',end="")
for m in mulheres:
    print(f'{m}',end=" ")
acima_media = []
for p in pessoas:
    if (p['idade'] >= media):
        acima_media.append(p.copy())
print('\n- Lista de pessoas que estão acima da média: ')
for p in acima_media:
    for k,v in p.items():
        if k == 'nome':
            print(f'\n{k} = {v}',end='; ')
        else:
            print(f'{k} = {v}',end='; ')

# Crie um programa que gerencie o aproveitamentto de um jogador de futebol. 
# O programa vai ler o nome do jogador e quantas partidas ele jogou. 
# Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
# guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {}
jogador['nome'] = str(input("Nome do Jogador: "))
jogador['gols'] = []
jogador['total'] = 0
partidas = int(input(f"Quantas partidas {jogador['nome']} jogou?"))
for p in range(0,partidas):
    gol = int(input(f"Quantos gols na partida {p}?"))
    jogador['gols'].append(gol)
    jogador['total'] += gol
print('-='*30)
print(jogador)
print('-='*30)
for k,v in jogador.items():
    print (f'O campo {k} tem o valor {v}')
print('-='*30)
print(f"O Jogador {jogador['nome']} jogou {len(jogador)} partidas.")
for p,g in enumerate(jogador['gols']):
    print(f'    => Na partida {p}, fez {g} gols.')
print(f'Foi um total de {jogador["total"]} gols.')