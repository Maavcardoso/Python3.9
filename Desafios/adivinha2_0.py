# Melhore o jogo da adivinhação proposto no 1º exercício dos desafios 05, onde o computador vai gerar um
# número aleatório de 0 a 10, só que agora o jogador vai tentar adivinhar até acertar, mostrando no final
# quantos palpites foram necessários para vencer.
from random import randint
print('Jogo da adivinhação 2.0!\nEstou pensando em um número de 0 à 10...\nEm qual número eu pensei?')
rand = randint(0,10)
n = int(input('Seu palpite: '))
tentativa = 1
while n != rand:
    if n > rand:
        n = int(input('Menos...Tente novamente!\nSeu palpite: '))
        tentativa = tentativa + 1
    elif n < rand:
        n = int(input('Mais...Tente novamente!\nSeu palpite: '))
        tentativa = tentativa + 1
if tentativa == 1:
    print('Parabéns! Acertou de primeira!')
else:
    print(f'Você descobriu após {tentativa} tentativas!')
    