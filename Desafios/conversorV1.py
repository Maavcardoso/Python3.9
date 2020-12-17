print('\nBem-Vindo ao conversor de Números 1.0!')
dec = int(input('Por favor, digite um número inteiro qualquer: '))
print('Escolha um sistema de numeração:\n1--Binário\n2--octal\n3--Hexadecimal ')
escolha = int(input('Sua opção: '))
if escolha == 1:
    bin_a = bin(dec)
    print(f'Conversão de Decimal para Binário:\n{dec} = {bin_a}')
elif escolha == 2:
    oct_a = oct(dec)
    print(f'Conversão de Decimal para Octal:\n{dec} = {oct_a}')
elif escolha == 3:
    hex_a = hex(dec)
    print(f'Conversão de Decimal para Hexadecimal:\n{dec} = {hex_a}')
else:
    print('Não existe essa opção.')
