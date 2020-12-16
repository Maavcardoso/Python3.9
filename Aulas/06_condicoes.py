#  if é uma condição que escreve um código se a comparação for Verdadeira (True)
# e else se for falsa.

# EX: Estrutura Composta:

x = float(input('Digite um número: '))

print('\nSeu número é maior que 10?\n') # Só executa se a condição de if for True.

if x < 10:
    print(f'\n{x} é menor que 10!') # Identação para dentro pode ser executado ou não.

elif x == 10:
    print('\nSeu número é 10!') # Excessão, só executa se a condição de if for False.

else:
    print(f'\n{x} é maior que 10!') # Só executa se a condição de if for False.

print('\nFim do programa!\n') # Se esta alinhado à esquerda sempre irá printar.

# Numa condição, sempre se executa o bloco verdadeiro ou falso, nunca os dois juntos.

# Estrutura Simples: Apenas com If,
# Estrutura Composta: Com if, elif e else. 

# EX: Estrutura Simples:

x = str(input('\nDigite seu nome: ')).strip()
x = x.lower()
if x == 'mario':
    print('\nQue nome lindo você tem!')
x = x.capitalize()
print(f'\nSeja Bem-Vindo, {x}!\n')

