print(20*'=-=')
print('LOJAS BARATÃO')
print(20*'=-=')
prectot = countmil = menorprec = c = 0
menorprod = ''
while True:
    prod = str(input('Nome do produto: '))
    prec = float(input('Preço: R$'))
    c += 1
    if c == 1 or prec < menorprec: # Grava o menor preço e o nome do produto.
        menorprec = prec
        menorprod = prod
    prectot += prec
    if prec > 1000: # contador de produtos com valor acima de 1000
        countmil += 1
    escolha = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break
    while escolha != 'N' and escolha != 'S': # Cria um loop quando a escolha é inválida.
        escolha = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]     
print(5*'-','FIM DO PROGRAMA',5*'-')
print(f'O total da compra foi R${prectot:.2f}')
print(f'Temos {countmil} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {menorprod} que custa R${menorprec:.2f}')

    

     
