# Crie um script python que leia o nome da pessoa e de uma mensagem de boas-vindas de acordo com o valor digitado.
nome = input('qual é seu nome? ')
#print ('Olá',',',nome,'.','Seja Bem-vindo! :)')
print ('Olá, {}. Seja Bem-vindo! :)'.format(nome))

# Crie um Script python que leia o dia, mês e ano que uma pessoa nasceu e imprima a data já formatada.
dia = input(' Que dia você nasceu? ')
mes = input(' Que mês você nasceu? ')
ano = input(' Que ano você nasceu? ')
#print ('Você nasceu em:', dia,'de',mes,'de',ano)
print ('Você nasceu em: {} de {} de {}.'.format(dia, mes, ano))

# Leia dois números e os some

n1 = int (input('Digite o primeiro número: '))
#n1 = input('digite o primeiro numero')
n2 = int (input('Digite o segundo número: '))
#n2 = input ('digite o segundo numero')
#int_n1 = int(n1)
#int_n2 = int(n2)
soma = n1 + n2
#soma = int_n1 + int_n2
#print ('A soma',n1,'+',n2,'é igual a:', soma)
print ('A soma {} + {} é igual a: {}'.format( n1, n2, soma)) #Código mais redundante.

# O exercício original propunha a indução ao erro: o método input() por padrão cria uma string,
# não variáveis numéricas. Portanto, o resultado da soma apenas iria
# concatenar os valores (Ex: n1 = 3 + n2 = 1 resultaria em 31).
# A solução que encontrei foi transformar as strings em valores Int,
# contudo, a resolução acima é mais elegante, já que basta anunciar o input() dentro de um tipo, 
# assim o compilador entende que quero somar os valores, não concatena-los.
# Também realizei a operação em uma variável "soma", com o objetivo de tornar o código mais redundante. 