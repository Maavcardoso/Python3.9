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






