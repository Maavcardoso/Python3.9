# Refaça o exercício 6 dos desafios 7, lendo o primeiro termo e a razão da PA, mostrando os primeiros 10 termos da progressão usando while.
# Para complementar o exercício, crie um código que pergunte ao usuário quantos termos ele quer além dos 10 primeiros e o permita
# sair caso peça mais 0 termos.


print('\nPA 2.0!\n')
n = float(input('Informe o primeiro termo: '))
r = float(input('Informe a razão da PA: '))
count = 0
print('Os primeiros 10 termos dessa PA são:')
while count < 10:
    if count < 9:
        pa = n + (r*count)
        count = count + 1 
        print(pa,end=' > ')
    elif count == 9:
        pa = n + (r*count)
        count = count + 1 
        print(pa)
decisao = int(input('Quantos termos a mais da PA você deseja ver (0 para parar): '))
if decisao == 0:
    print('Fim do programa.')
    quit()
else:
    decisao = decisao + count
    while count <= decisao:
        pa = n + (r*count)
        count = count + 1 
        print(pa,end=' > ')