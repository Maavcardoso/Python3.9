#Podemos inserir listas dentro de cada index de uma lista, assim formando matrizes
#Para isso, basta criarmos 2 variavéis de lista diferentes: uma para receber os dados,
#E outra para guarda-los.
pessoas = []
dados = ["Pedro",25]

# Para inserirmos os dados corretamente sem referencia-los, devemos usar o comando
# .append()

pessoas.append(dados[:]) # o : copia toda a lista dados e a insere na lista pessoas.

# Demonstração sobre como o ponteiro funciona na lista python, mostrando a necessidade
# de se criar uma cópia ao invés de referi-lo diretamente.

teste = ["Zezão",36]
galera = list() # Forma alternativa de se declarar lista
galera.append(teste)
teste[0] = "Jalim"
teste[1] = 24
galera.append(teste)
print(galera) # Outuput: [["Jalim",24],["Jalim",24]]

# Em python, quando uma lista é referenciada diretamente, se cria uma "ligação"
# com ela, ou seja, o ponteiro referência o conteúdo da lista, portanto, qualquer
# alteração posterior afeta ambas as lista.

# Nesse caso, precisamos que a lista galera possua as duas pessoas, por isso
# se faz necessário criar uma cópia da lista para que então se altere os dados
# da lista original sem afetar os resultados gravados na lista galera.

teste = ["Zezão",36]
galera = list() 
galera.append(teste[:]) # [:] Copia toda a lista em um "novo" ponteiro
teste[0] = "Jalim"
teste[1] = 24
galera.append(teste[:])
print(galera) # Outuput: [["Zezão",36],["Jalim",24]]


# Em uma lista composta, podemos acessar individualmente cada elemento utilizando
# dois indices, sendo que o primeiro elemento representa a posição da lista  na
# lista onde está inserida e o segundo a posição do elemento.

pessoas = [["Pedro",25],["Maria",54],["Enzo",12]]
print(pessoas[0][0]) # Output: Pedro
print(pessoas[0][1]) # Output: 25
print(pessoas[1][1]) # Output: 54
print(pessoas[2][0]) # Output: Enzo
print(pessoas[1]) # Output: ["Maria",54]

# Percorrendo uma lista:

for p in pessoas:
  print(f'{p[0]} tem {p[1]} anos de idade')
  
# Preenchendo uma lista:

galera = []
dado = list()
for c in range(0,3):
  dado.append(str(input("Nome: ")))
  dado.append(int(input("Idade: ")))
  galera.append(dado[:])
  dado.clear()

# Interando uma lista:

totmai = totmen = 0

for p in galera:
    if p[1] >= 21:
      print(f'{p[0]} é maior de idade.')
      totmai += 1
    else:
      print(f'{p[0]} é menor de idade.')
      totamen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')


