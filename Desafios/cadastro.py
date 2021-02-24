countid = 0
countmasc = 0
countfem = 0
while True:
    print('\n')
    print(20*'-')
    print('CADASTRE UMA PESSOA')
    print(20*'-')
    idade = int(input('\nIdade: '))
    sexo = str(input('\nGênero [M/F/X]: ')).strip().upper()[0]
    while sexo != 'M' and sexo != 'F' and sexo != 'X': # Cria um loop se o usuário der uma alternativa inválida
         sexo = str(input('\nGênero [M/F/X]: ')).strip().upper()[0]
    if idade >= 18: # contador idade
        countid += 1
    if sexo == 'M': # contador masculino
        countmasc += 1
    if idade < 20 and sexo == 'F': # contador feminino
        countfem += 1
    escolha = str(input('\nDeseja continuar? [S/N]: ')).strip().upper()[0]
    while escolha != 'S' and escolha != 'N':
        escolha = str(input('\nDeseja continuar? [S/N]: ')).strip().upper()[0] # Cria um loop se o usuário der uma alternativa inválida
    if escolha == 'N': # quebra o looping quando a escolha for não
        break
print('\n')
print(5*'=','FIM DO PROGRAMA', 5*'=')
print(f'\nTotal de pessoas com mais de 18 anos: {countid}')
print(f'Ao todo temos {countmasc} homens cadastrados.')
print(f'E temos {countfem} mulheres com menos de 20 anos.\n')
        