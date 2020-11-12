#   + = adição    - = Subtração   * = multiplicação
#   / = divisão   ** = Potência   // = divisão inteira
#   % = Resto da divisão    = Recebe    == Igualdade

#ORDEM DE PRECEDENCIA:
# 1. (), 2. Potência, 3. Multiplicação/Divisão(incluindo inteira e resto), 4.Adição/subtração

#n = input('Digite seu nome: ')
#print ('Olá, {}.'.format(n))
#print ('Olá, {:20}.'.format(n)) # Escreve o nome em 20 espaços
#print ('Olá, {:>20}.'.format(n)) # Alinha nome a direita de 20 espaços
#print ('Olá, {:=^20}.'.format(n)) # Alinha nome ao meio e preenche o resto com =
#print('Olá, {}, isto é um teste! '.format(n), end= ':D :D :D ') # end= adiciona um texto a escolha no fim do print.
n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
print('A soma será igual a: {}'.format(n1+n2))
print('A subtração será igual a: {}'.format(n1-n2))
print('A multiplicação será igual a: {}'.format(n1*n2))
print('A divisão será igual a: {}'.format(n1/n2)) # O resultado é o quociente
print('A divisão inteira será igual a: {}'.format(n1//n2)) # O resultado são quantas vezes que o dividendo será decomposto pelo divisor
print('O Resto da divisão será igual a: {}'.format(n1%n2)) # O resultado é o resto da divisão. 
print('A potência será igual a: {}'.format(n1**n2))
print('A Raiz quadrada de {} é igual a: {}'.format(n1, n1**0.5)) # Raiz quadrada é a mesma coisa que x^0.5 ou (1/2)
print('A Raiz cúbica de {} é igual a: {}'.format(n2,n2**(1/3))) # O mesmo vale para qualquer raiz. Apenas a formatação esta diferente.