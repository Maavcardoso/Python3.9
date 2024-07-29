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

