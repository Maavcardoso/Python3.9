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
print(f'\nO maior número foi {max(list_num)} nas {maiorc}ª posições.\nO menor número foi {min(list_num)} na {menorc}ª posição')
