n = int(input('Digite um número: '))
c = 1
menor = n 
maior = n
n1 = n
decisao = 'S'
while decisao != 'N':
    decisao = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while decisao != 'S' and decisao != 'N':
        decisao = str(input('Escolha inválida. Por favor, digite uma alternativa válida [S/N]: ')).strip().upper()[0]
    if decisao == 'S':
        n = int(input('Digite um número: '))
        n1 = n1 + n
        c += 1
        if menor > n:
            menor = n
        if maior < n:
            maior = n
n1 = n1/c
print(f'A média dos números é igual a {n1}.\nO maior número é {maior}.\nO menor número é {menor}.')
