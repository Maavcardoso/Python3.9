print('\n','-=-' * 10) 
print('\n Exercício 7\n')
n = str(input('Digite um texto: '))
print('\nAo contrário fica: ',end='')
n = n.strip()
ncopia = n
n = n.lower()
n = n.split()
n = ''.join(n)
s = str('') # String q será escrita ao contrário
for c2 in range ((len(ncopia)),0,-1): # Escreve a frase ao contrário
    print((ncopia[c2-1]),end='')
for c in range ((len(n)),0,-1): # Verifica se a frase é um Palíndromo
    n2 = (n[c-1])
    s = s + n2
if s == n:
    print('\n\nEsta frase é um Palíndromo!')
else:
    print('\n\nEsta frase não é um Palíndromo.')