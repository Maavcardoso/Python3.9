
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


 
