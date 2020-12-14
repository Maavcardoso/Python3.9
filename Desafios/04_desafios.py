# Crie um programa que leia um nome completo e:
# -Faça todas as letras ficarem em maiúsculo;
# -Faça todas as letras ficarem em minusculo;
# -Conte quantas letras tem (sem contar espaços);
# -Conte quantas letras tem o primeiro nome.

print('\nExercício 1')
frase = input('\nDigite seu nome completo: ')
txt = frase.split()
prnome = txt [0]
cprnome = len(txt[0])
txt = ''.join(txt)

print(f'\nCom todas as letras maiusculas: {frase.upper()}')
print(f'\nCom todas as letras minusculas: {frase.lower()}.')
print(f'\nSeu nome possui {len(txt)} letras.')
print(f'\nSeu primeiro nome ({prnome}) possui {cprnome} letras\n')

# Crie um programa que leia um número de 0 à 9999
# e apresente cada digito separadamente.

print('\nExercício 2')
x = int (input('\nDigite um Número de 0 a 9999: '))
u = x // 1 % 10
d = x // 10 % 10
c = x // 100 % 10
m = x // 1000 % 10
print(f'\nO número digitado foi {x}')
print(f'\nUnidade: {u}')
print(f'\nDezena: {d}')
print(f'\nCentena: {c}')
print(f'\nMilhar: {m}')

# Essa eu precisei pesquisar. Planejava criar um contador com if-else, mas essa solução é bem
# mais simples e elegante, já que é apenas necessário que se divida a casa decimal por inteiro e
# então pegar o resto da divisão por 10. 

# Crie um programa que peça o nome de uma cidade e identifique se começa com "Santo"

print('\nExercício 3')
x = input('\nDigite o nome da sua cidade: ')
x.strip()
y = x.split()
z = 'Santo' in y[0]

if z == True:
    print(f'\n{x} começa com Santo!')
else:
    print(f'\n{x} não começa com Santo...')

# Crie um programa que leia uma frase e:
# Conte quantos caracteres procurados existem;
# a posição do primeiro caracter procurado,
# a posição do ultimo caracter procurado.

print('\nExercício 4')
frase = str(input('\nDigite uma frase qualquer: ')).upper()
frase.strip()
charf = str(input('\nQual carácter deseja buscar? ')).upper()
charf.strip()
print(f'\nSua frase possui {frase.count(charf)} "{charf}"')
frase = frase.split()
frase = ''.join(frase)
proc = frase.find(charf)+1
uroc = frase.rfind(charf)+1
print(f'\nA primeira ocorrência da letra {charf} é na posição {proc}')
print(f'\nA ultima ocorrência da letra {charf} é na posição {uroc}')

# Crie um programa que leia um nome e de o primeiro
# e o ultimo nome da pessoa.

frase = str(input('\nDigite seu Nome: '))
frase = frase.strip()
frase = frase.split()
prino = frase[0]
ultno = frase[-1]
print(f'\nO primeiro nome é: {prino}')
print(f'\nO último nome é: {ultno}\n')

