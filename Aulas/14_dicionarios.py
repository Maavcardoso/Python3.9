# Dicionários são variáveis compostas que permitem 
# que os identificadores (Index) sejam personalizados, 
# tornando a identificação dos dados na estrutura mais clara.
 
# Declarando um dicionário:
filmes = dict()
alunos = {}      # ambas as formas são válidas.

# Também podemos declarar já preenchendo os dados
pessoa={'nome': 'Thais', 'sexo': 'F','idade': 27} 
print(pessoa['nome']) # Output: Thais
print(f'A {pessoa["nome"]} tem {pessoa["idade"]} anos.')
print(f'pessoas.keys(): {pessoa.keys()}') # Mostra os índices
print(f'pessoas.values(): {pessoa.values()}' ) # Mostra os valores
print(f'pessoas.items(): {pessoa.items()}') # Mostra a chave-valor

# Acessando chaves e valores com lanços

for k in pessoa.keys():
    print(k)

for v in pessoa.values():
    print(v)

# Acessando Items com laço

for k, v in pessoa.items():
    print(f'{k} : {v}')

# Deletando Items (Chave e Valor)
del pessoa['sexo']
for k, v in pessoa.items():
    print(f'{k} : {v}')

# Alterando o valor de uma chave:
pessoa['nome'] = "Mario" 
for k, v in pessoa.items():
    print(f'{k}: {v}')

# Criando Items:

pessoa['peso'] = 78.6  # Para adicionar um item na lista, basta declarar a nova key.
for k, v in pessoa.items(): # (Não precisa de .append())
    print(f'{k} : {v}')

# Criando um dicionário dentro de uma lista:
brasil=[]
estado1 = {'uf':'São Paulo','sigla':'SP'}
estado2 = {'uf':'Rio de Janeiro','sigla':'RJ'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[1]) #output: {'uf': 'Rio de Janeiro' 'sigla':'RJ'}

# Populando uma lista de dicionários:
estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf']=str(input('Unidade Federativa: '))
    estado['sigla']=str(input('Sigla: '))
    brasil.append(estado.copy()) # o método .copy() copia o estado atual do dicionário
                                # permitindo que um novo ponteiro seja indicado 
                                # para a proxima posição da lista.                            
print(brasil)

# Imprimindo de forma organizada

for estado in brasil:

    #print(estado) imprime item em cada linha
   # for k, v in estado.items(): # .items retorna cada item para acessar o valor-chave
        #print(f'{k} : {v}')
        
    for v in estado.values():
         print(v, end=' ')
    print()


