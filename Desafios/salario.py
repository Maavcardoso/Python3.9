# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
# , 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# a. salário bruto.
# b. quanto pagou ao INSS.
# c. quanto pagou ao sindicato.
# d. o salário líquido.
# e. calcule os descontos e o salário líquido

sh = float(input('Quanto é seu salário/hora? : '))
ht = float(input('Quantas horas você trabalhou? : '))
sb = sh * ht
di = sb * 0.08
ds = sb * 0.05
dr = sb * 0.11
sl = sb - (di+ ds + dr)
print ('Seu salário bruto será de: {} R$ '.format(sb))
print ('Foi descontado {} R$ para o INSS'.format(di))
print ('Foi descontado {} R$ para o Sindicato'.format(ds))
print ('Foi descontado {} R$ para o IR'.format(dr))
print ('Seu salário líquido será de: {} R$'.format(sl))