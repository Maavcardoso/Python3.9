#Faça um programa que leia o teclado e mostre seu tipo primitivo e todas as informações possiveis sobre ele.

n = input('Digite algo: ')
print ('{} é uma variável do tipo: '.format(n), type(n))
print ('{} é numérico? '.format(n), n.isnumeric())
print ('{} esta em caixa alta? '.format(n), n.isupper())
print ('{} esta em caixa baixa? '.format(n), n.islower())
print ('{} é alfabético? '.format(n), n.isalpha())
print ('{} é alfanumérico? '.format(n), n.isalnum())
print ('{} é apenas espaços? '.format(n), n.isspace())
print ('{} esta capitalizado? '.format(n), n.istitle())

# Um exercício simples, demonstrando as possibilidades da função is().
# Pode vir a ser um operador útil para se criar condições booleanas. 