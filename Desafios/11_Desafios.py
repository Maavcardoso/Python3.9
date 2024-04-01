# Crie uma lista que leia 5 números, e depois diga qual foi o maior e o menor
# valor digitado e todas as posições (Se houver mais de um dos mesmo) na lista.

list_num = []
menorc = []
maiorc = []
for i in range(0,5):
    list_num.append(int(input("Digite um número: ")))
for c, v in enumerate(list_num):
    if v == max(list_num):
        maiorc.append(c+1)
    elif v == min(list_num):
        menorc.append(c+1)
print(f'\nO maior número foi {max(list_num)} nas posições:',end="")
for i in range(0,len(maiorc)):
    print(f' {maiorc[i]}',end="")
print(f'\nO menor número foi {min(list_num)} nas posições:',end="")
for i in range(0,len(menorc)):
    print(f' {menorc[i]}',end="")

#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#Caso o número já exista, ele não será adicionado. No final, exiba todos os valores únicos digitados
#Em ordem crescente.

list_uni = []
while True:
    num = int(input("Digite um número: "))

    if num not in list_uni:
        list_uni.append(num)

    else:  
        print("Número duplicado, não será adicionado.")

    choice = input("Deseja continuar? S/N: ").strip()[0].upper()
    if choice == "N":
        break

print(f"Os números inseridos foram: {sorted(list_uni)}")

#Crie um programa onde o usuário possa digitar cinco valores numéricos
#e cadastre-os em uma lista, já na posição correta de inserção (Sem usar sort()).
#Ao final, mostre a lista ordenada na tela.

list_ord = []
for i in range (0,5):
    num_ord = (int(input("Digite um número: ")))
    if not list_ord or num_ord > list_ord[len(list_ord)-1]:
        list_ord.append(num_ord)
        print("Valor inserido na última posição.")  
    else:
        for c, v in enumerate(list_ord):
            if num_ord < list_ord[c]:
                list_ord.insert(c,num_ord)
                print(f"Valor inserido na posição {c}.")
                break # Precisei adicionar pois o contador (c) é incrementado no momento em que adiciona o novo valor,
                      # Criando assim um loop infinito.
print(f"A lista ordenada é: {list_ord}")

# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso mostre: 
# A) Quantos números foram digitados;
# B) A lista de valores, ordenada de forma decrescente;
# C) Se o valor 5 foi ou não digitado na lista.

listin = []
while(True):
    num_listin = int(input("Digite um número: "))
    listin.append(num_listin)
    choice = input("Deseja inserir outro número? S/N: ").upper().strip()[0]
    if choice == "N":
        break
listin.sort(reverse=True)
print(f"A - Foram digitados {len(listin)} números")
print(f"B - A lista com valores decrescentes: {listin}")
if 5 in listin:
    print("C - O número 5 existe na lista!")
else:
    print("C - O número 5 não existe na lista.")
