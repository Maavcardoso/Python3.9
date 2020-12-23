# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M', 'F' ou 'X'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

print('\n','-=-' * 10) 
print('\n Exercício 1\n')


dado = ''
while dado != 'M' and dado != 'F' and dado != 'X':
    dado = str(input('Informe seu gênero [M/F/X]: ')).upper().strip()[0] # Fatia a primeira letra, então se escrever "masculino" Só pega a letra 'M'.
    if dado == 'M' or dado == 'F' or dado == 'X':
        print(f'{dado} foi registrado com sucesso.')
        break
    else:
        print(f'{dado} é uma escolha inválida. Por favor',end=', ')
        # Minha solução


dado = str(input('Informe seu gênero [M/F/X]: ')).strip().upper()[0]
while dado not in 'MFX':
    dado = str(input('Dado inválido. Por favor, informe seu gênero.')).strip().upper()[0]
print(f'{dado} foi registrado com sucesso.')
        # Solução proposta pelo Guanabara. A condição do laço "while" dispensa o uso do if/else que criei na minha solução.
