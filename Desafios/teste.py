print('\n','-=-' * 10) 
print('\n Exercício 7\n')
n = str(input('Digite um texto: '))
print('\nAo contrário fica: ',end='')
n = n.strip()
n = n.split()
ncopia = ' '.join(n) #print(ncopia) == Frase com espaçamento correto.
n = ''.join(n)
n = n.lower()
s = str('') # String q será escrita ao contrário
for c2 in range ((len(ncopia)-1),-1,-1): # Escreve a frase ao contrário
    print((ncopia[c2]),end='')
for c in range ((len(n)-1),-1,-1): # Verifica se a frase é um Palíndromo
    n2 = (n[c])
    s = s + n2 # print(s) no fim da repetição: A Palavra ao contrário.
if s == n:
    print('\n\nEsta frase é um Palíndromo!')
else:
    print('\n\nEsta frase não é um Palíndromo.')

# Implementei algumas melhoras:
# Por mais espaços que tenha um frase, na hora de analisar não os considera (Como proposto no exercício),
# Contudo, criei um segundo for que também transcreve de maneira correta.