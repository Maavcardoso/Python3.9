# Listas são decladas com colchetes []
# Listas são mútaveis, ou seja, suas variavéis podems er alteradas, ao contrário das tuplas.

lista = ["pizza","burguer","suco","frango"]
print(lista)
lista[3] = "sorvete" # Frango será substituido por sorvete
print(lista)

# Para inserir um elemento ao fim da lista, utilizamos o método .append()
lista.append("Cookie")
print(lista)

# Para inserir um elemento em qualquer posição, utilizamos o método .insert()
lista.insert(0,"Cachorro Quente") # Há 2 parâmetros: o primeiro é a posição que iremos adicionar o item
print(lista)                      # e o segundo é o item que iremos adicionar. O python renumera as posições.

# Para organizar a lista por ordem crescente utilizamos o método .sort()
numeros = [4,7,3,8,0,5]
numeros.sort()
print(numeros)

# Podemos listar em ordem decrescente adicionando o parametro .sort(reverse=True)
numeros.sort(reverse=True)
print(numeros)

# Para remover o último item da lista, utilizamos o método .pop() sem parâmetros.
# utilizando parâmetros, podemos retirar o valor do indice desejado.

numeros.pop()
print(numeros)

numeros.pop(2)
print(numeros)

# O método .remove() elimina apenas a primeira ocorrência do número digitado no parâmetro.
numeros.append(25)
numeros.append(25)
print(numeros)
numeros.remove(25)
print(numeros)

# Caso o número que será removido não exista, o python retornará uma excessão.
# Para evitar isso, precisamos tratar com uma condição:

if 6 in numeros:
    numeros.remove(6)
else:
    print("Não há o número 6")


#Contar quantos elementos há na lista:

print(f"Há {len(numeros)} elementos na lista")

# Printar valores com chaves

for c, v in enumerate(numeros):
    print(f'O número {v} está na posição {c} ')

# Ler valores e inseri-los em uma lista
valores = [] # Também podemos declarar uma lista vazia com list()
for i in range(0,5):
    valores.append(int(input("Digite um Número: ")))    
print(valores)

# Copiar uma lista
a = [1,2,3,4,5]
b = a # Assim a lista b estará vinculada a lista a, ou seja, toda mudança em b afetará a
b.append(6)
print(f'Lista A: {a}\nLista B: {b}')

# Para copiar uma lista, é necessário utilizar um "recorte" inteiro de a, como a seguir:
b = a[:] # Agora foi criado uma cópia
b.append(7)
print(f'Lista A: {a}\nLista B: {b}')