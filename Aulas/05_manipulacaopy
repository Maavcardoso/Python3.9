# Toda frase apenas com letras é uma string, ou cadeia de caracteres

frase = str('Hello World')

# A variável frase aloca um espaço na memória do computador para o hello world,
# contudo, cada caractere (inclusive o espaço) ocupam uma unidade de memória,
# portanto, o computador consegue identificar cada carectere presente na string.

# Podemos imaginar que a string divide seus caracteres assim como os dados 
# de uma lista, tanto que para se indincar um caractere, se utiliza a mesma
# sintaxe de uma lista.

# Fatiamento
# O fatiamento é justamente a forma como a string será dividida, e através
# dessa ferramenta, podemos utilizar cada caractere de acordo com a necessidade.
# Segue alguns exemplos de fatiamento:

# EX 1:

print (frase[4])

# output: 'o' ( Na posição 4 da string se encontra o 'o' do 'Hello')

# EX 2:

print (frase[0:5])

# output: 'Hello' ( Copia a string da posição 0 a posição 4. O 5 é um delimitador
# que não aparecerá no print. Portanto, numa relação frase[x:y], x e todos os
# caracteres até y estão inclusos, menos y. Atentar ao detalhe do :, x limita
# o começo, e o y o fim. A importância fica mais clara quando observamos os
# exemplos 4 e 5).

# EX 3:

print (frase[0:12:2])

# output: 'HloWrd' ( Depois do primeiro caractere, printa um caractere a cada 2
# 'espaços', nesse caso, na frase 'Hello World', ele printa o 'H', pula o 'e'(1),
# printa o 'l'(2), pula o outro 'l'(1), printa o e assim por diante).

# EX 4:

print (frase[:7])

# output: 'Hello W' ( Semelhante ao segundo exemplo, mas apenas com o caracter
# limitante. Sendo assim, o programa irá printar desde a primeira unidade até
# a unidade antecessora ao limite).

# EX 5:

print (frase[6:])

# output: 'World' (Semelhante ao exemplo anterior, mas apenas com o
# caracter inicial. Sendo assim, o programa irá printar a partir da unidade
# indicada até o fim).

# EX 6:

print(frase[6::2])

# output: 'Wrd' ( Aqui indicamos o início do fatiamento e 
# para pular dois caracteres até o final da string)

# Análise
# Os recursos de análise permitem que possamos coletar dados de uma string, 
# como por exemplo, qual o primeiro caractere, o tipo, comprimento, etc.
# Segue o exemplo de algumas análises:

# EX 7:

print('\n7--', len(frase))

# output: '11' (Demonstra o comprimento da string, ou seja, quantos caracteres a compõem).

# EX 8:

print('\n8--', frase.count('l'))
print('\n8_2--', frase.count('l',6,12))

# output: '3' e '1' ( Conta quantas vezes o termo ou caractere desejado aparece na string.
# O segundo exemplo contém um fatiamento específico para o 'World', portanto, contará apenas um 'l').

# EX 9:

print('\n9--', frase.find('Wor'))
print('\n9_2--', frase.find('Olá'))

# output: '6' e '-1' ( Procura o termo na string e indica a posição de onde se inicia.
# No segundo exemplo, como 'Olá' não existe nessa string, a função irá retornar -1, que
# significa que a string citada para busca não se encontra dentro da string frase.)

# EX 10: 

print('\n10--', 'Hello' in frase)
print('\n10_2--', 'Olá' in frase)

# output: 'True' e 'False' ( Nesse caso, in é um operador, não uma função, que irá identificar
# se a string desejada está dentro da string frase. Ele retornará um valor booleano, portanto,
# apesar de ser um operador, ele pode ser usado como método de análise).

# Transformação
# Uma lista de string é imutável, ou seja, não se altera os dados dela diretamente,
# mas .

# EX 11:

print('\n11--', frase.replace('World','Mundo'))

# output: 'Hello Mundo' ( Substitui um termo da string por outra a escolha)

# EX 12:

print('\n12_01--',frase.upper()) # Deixa a string em maiusculo.
print('\n12_02--',frase.lower()) # Deixa a string em minusculo.
print('\n12_03--',frase.capitalize()) # Deixa a primeira letra em maiusculo e o resto em minusculo.
print('\n12_04--',frase.title()) # Deixa a primeira letra de cada palavra em maiusculo.

# EX 13:

frase = str('   Hello World   ')

print ('\n13--', frase.strip())
print ('\n13_02--', frase.rstrip())

# Output: 'Hello World' e '   Hello World' (A função .strip retira os espaços 'inuteis', como no caso dessa string.
# O segundo código retira apenas espaços 'inuteis' no fim da string).

# EX 14: 

frase = str('Hello World')



