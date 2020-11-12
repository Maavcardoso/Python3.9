# quando o valor é circundado por '' ele se torna uma string,
# portanto, os prints abaixo irão imprimir resultados diferentes.
# sendo a linha 5 uma soma de números e a linha 6 uma junção de strings.
print ('hello, world!')
print (1 + 3) # resultado é 4
print ('1' + '3') # resultado é 13
# print ('hello' + 1) irá falhar, pois o compilador tentará somar string com int
print ('hello', 1) # Já este funciona, pois está concatenando dois valores string.

# Printando Variáveis.
# OBS: Toda variável em Python é um objeto.
nome = 'Mario' # String
idade = 23 # Int
peso = 70.8 # Float
print(nome, idade, peso)