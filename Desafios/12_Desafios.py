# Faça um programa que leia o nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# a) Quantas pessoas foram cadastradas;
# b) Uma listagem com as pessoas mais pesadas;
# c) Uma listagem com as pessoas mais leves.

pessoas = []
dado = list()
pesomai = pesomen = 0
while(True):
    dado.append(str(input("Nome: ")))
    dado.append(float(input("Peso: ")))
    pessoas.append(dado[:])
    dado.clear()
    choice = str(input("Deseja continuar? [S/N] ")).upper().split()[0]
    if choice == "N":
        break
for p in pessoas:
    if p[1] > pesomai:
        pesomai = p[1]
    if p[1] < pesomen or pesomen == 0:
        pesomen = p[1]
print(f'\nAo todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {pesomai}Kg. Peso de:',end=" ")
for p in pessoas:
    if p[1] == pesomai:
        print(p[0],end=" ")
print(f'\nO menor peso foi de {pesomen}Kg. Peso de:',end=" ")
for p in pessoas:
    if p[1] == pesomen:
        print(p[0],end=" ")

# Crie um programa onde o usuário possa digitar sete valores númericos e 
# cadastre-os em uma lista única que mantenha separados os valores pares e 
# ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

nums = [[],[]]
for i in range(0,7):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        nums[0].append(num)
    else:
        nums[1].append(num)
print(f"Lista de números pares: {sorted(nums[0])}")
print(f"Lista de números impares: {sorted(nums[1])}")
