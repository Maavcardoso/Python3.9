print('{:^30}'.format('BANCO BOM DE GRANA'))
valor = int(input('Digite o valor a ser resgatado: R$'))
nota50  =  nota20 = nota10 = nota1 = 0
while True:
    while valor >= 50:
        valor = valor - 50
        nota50 += 1
    while valor >= 20 and valor < 50: 
        valor = valor - 20
        nota20 += 1
    while valor >= 10 and valor < 20: 
        valor = valor - 10
        nota10 += 1
    while valor < 10 and valor > 0: 
        valor = valor - 1
        nota1 += 1
    break
print('\n')
print(20*'=')
if nota50 > 0:
    print(f'{nota50} cédulas de R$50')
if nota20 > 0:
    print(f'{nota20} cédulas de R$20')
if nota10 > 0:
    print(f'{nota10} cédulas de R$10')
if nota1 > 0:
    print(f'{nota1} cédulas de R$1')
print(20*'=')
print('\nTransação finalizada. Obrigado por usar Bom de Grana!')

# Solução do Guanabara, muito elegante comparado a minha. Irei escrever pois não pensei dessa forma.

print('{:^30}'.format('BANCO BOM DE GRANA'))
valor = int(input('Digite o valor a ser resgatado: R$'))
cel = 50
celcount = 0
print('\n')
print(20*'=')
while True:
    if valor >= cel:
        valor -= cel
        celcount += 1
    else:
        if celcount > 0:
            print(f'Total de {celcount} cédulas de R${cel}')
        if cel == 50:
            cel = 20
        elif cel == 20:
            cel = 10
        elif cel == 10:
            cel = 1
        celcount = 0
        if valor == 0:
            break
print(20*'=')
print('\nTransação finalizada. Obrigado por usar o Bom de Grana !')