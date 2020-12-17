# Não necessariamente precisamos ter decisões binárias
# pelo if-else. Há a possibilidade de fazermos a quantidade
# de escolhas que nos for necessária através do aninhamento 
# de condições.

x = float(input('Digite um número: '))

print('\nSeu número é maior que 10?\n') # Só executa se a condição de if for True.

if x < 10:
    print(f'\n{x} é menor que 10!') # Identação para dentro pode ser executado ou não.

elif x == 10:
    print('\nSeu número é 10!') # Excessão, só executa se a condição de if for False.

else:
    print(f'\n{x} é maior que 10!') # Só executa se a condição de if for False.

print('\nFim do programa!\n') # Se esta alinhado à esquerda sempre irá printar

# Aqui existem 3 possibilidades, através do elif, que cria uma terceira condição.