# Primeiro, veremos como funciona um laço com variável de controle,
# Ou seja, uma condição que se repete até que a condição seja realizada. 

print('\n','-=' * 10) 
for c in range(1,10):  # laço c no intervalo (1,10), irá conta de 1 à 9
    print(c)
print('fim')           # repare que a identação do fim está diferente do conteudo do laço. 
print('\n','-=' * 10)  # por isso, 'fim' sempre será printado apenas uma vez depois da repetição

for c in range (6, -1, -1):
    print(c)
print('\n','-=' * 10) 

# Aqui ele irá fazer uma contagem regressiva de 6 até 0, pois o terceiro termo dentro da condição representa 
# 'os passos' dentro do laço. Perceba que o primeiro número sempre tem que ser maior, se não a repetição vai acabar
# antes de começar. 

for c in range (0, 11, 2):
    print(c)
print('\n','-=' * 10) 
# Aqui ele irá contar a cada 2 elementos. Portanto, irá printar (a partir do 0) um número sim e o outro não.

n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)

# O usuário pode atribuir uma variavel de controle se assim desejarmos. Note que o n+1 serve para imprimir até o número desejado,
# já que o 'ultimo' número o range ele irá parar o loop antes de se contar.
print('\n','-='* 10, '\n') 
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for c in range(i,f,p):
    print(c)

# Nesse caso, o usuário está indicando todas as variáveis, dando autonomia para a repetição. Teste diferentes variáveis e veja os resultados! 

s = 0
for c in range (0,4):
    n = int(input('Digite um número: '))
    s = s + n
print(f'A soma dos números é igual a {s}')

# Podemos resolver somas de número com for, visto que a cada repetição a variável 's' recebe um valor diferente de 'n' e vai somando até que a repetição acabe.
# perceba que o scan está dentro do laço, sendo portanto possivel juntar diferentes estruturas num laço de repetição  
