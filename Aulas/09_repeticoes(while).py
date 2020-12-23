 # O While é uma estrutura de repetição com teste lógico.
 # Quando não se sabe quantas vezes precisa se repetir o código,
 # While é a melhor escolha, já se for demarcado, o for continua sendo mais prático,
 # Porém, ambos possuem a mesma função.

for c in range (1,11): # Conta até 10 em for
    print(c)
print('Fim')

c = 1
while c < 11: # Conta até 10 em while
    print(c)
    c = c + 1
print('Fim')
# Como não sabemos quantas vezes o usuário quer digitar números, o while faz essa repetição infinitamente
# Até que o usuário queria parar.

r = 's' 
while r == 's':
    n = float(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).lower()
print('Fim')

par = 0
impar = 0
n = 1
print('Quantos pares/ímpares você escreveu?\n(Pressione 0 para encerrar)')
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0: # Essa etapa é necessária, pois caso o usuário digite 0 essa escolha não é contabilizada.
        if n % 2 == 0 :
            par = par + 1
        else:
            impar = impar + 1
print(f'Você digitou {par} Números pares e {impar} Ímpares.')

