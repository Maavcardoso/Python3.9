# Uma tupla é uma variável composta, ou seja, ela contém mais de 1 informação.
# Até agora todos os exercícios e exemplos foram criados com variáveis simples, que possuem apenas
# um conteúdo e, caso receba um novo valor, o anterior é sobrescrito. 
# Uma variável composta nos permite alocar diversos valores em uma variável. Existem 3 tipos de variáveis compostas:
# Tupla, lista e dicionário.
# Na aula 5, aprendemos a manipular strings, que se comportam como listas, portanto, os comandos usados para manipulação de variaveis
# são exatamente os mesmos.
# Vale lembrar também que TUPLAS SÃO IMUTÁVEIS, ou seja, não é possível alterar uma variável que está na tupla enquanto o programa estiver executando.

lanche = ('Burguer','Suco','Pizza','Pudim') # Tuplas sempre são indicadas com (). Cada tipo de variável composta é declarada por simbolos diferentes.
print(lanche) #Output: ('Burguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[1]) #Output: Suco
print(lanche[-2]) #Output: Pizza
print(lanche[1:3]) # Output: ('Suco', 'Pizza')
print(lanche[2:]) #Output: ('Pizza', 'Pudim')
print(sorted(lanche)) #Output:['Burguer', 'Pizza', 'Pudim', 'Suco']

# !!! TUPLAS SÃO IMUTÁVEIS !!!

#lanche[1] = 'Refri' # Vai dar erro, pois não se pode atribuir uma nova variável a tupla.

#Também podemos criar um laço de repetição que percorre os elementos da tupla:

for comida in lanche:
    print(f'Vou comer {comida}')
print('Comi pra caramba!')

for cont in range(0, len(lanche)):
    print(f'Vou comer {lanche[cont]}')
print('Estou farto!') 

# Podemos enumerar os elementos conforme sua posição:

for cont in range(0, len(lanche)):
    print(f'Vou comer {lanche[cont]} na posição {cont}')
print('Estou farto!') 

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Chega, não aguento mais!')

# Também podemos concatenar e procurar elementos em tuplas.

a = (2,5,4)
b = (5,8,1,2)
c = a + b
print(c) # Output: (2, 5, 4, 5, 8, 1, 2). Valores 
print(c.index(8)) #Output: 4. Procura a posição do primeiro elemento desejado.
print(c.count(2)) #Output: 2. Conta quantas vezes o elemento aparece na tupla

# No Python, a tupla pode receber vários tipos de variável. Portanto, ela comporta tanto uma string quanto um valor inteiro ou float, por exemplo:

pessoa = ('Mario', 23, 'M', 75,50)
del (pessoa) # apaga a tupla do espaço de memória.
print (pessoa)
