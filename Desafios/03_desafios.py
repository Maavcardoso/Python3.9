#Faça um código que leia um número real e mostre sua porção inteira:

# import math --- apenas com esse código eu não precisaria mais referenciar cada
# método de math, mas para exercício irei pedir o método especifico para cada problema.

from math import floor

n = float(input('\nDigite um número qualquer: '))
ni = floor(n)
print('A porção inteira é: {}'.format(ni))

#Faça um código que calcule a hipotenusa de um triângulo retângulo:

from math import hypot

x = float (input('\nDigite o valor do Cateto Oposto: '))
y = float (input('\nDigite o valor do Cateto Adjacente: '))
z = hypot(x, y)
print('\nO valor da hipotenusa é igual a: {}'.format(z))

#Faça um código que leia um ângulo e devolva seu seno, cosseno e tangente:

from math import sin, cos, tan

x = float(input('\nDigite o valor do ângulo: '))
sinx = round(sin(x),2)
cosx = round(cos(x),2)
tanx = round(tan(x),2)
print('O Seno de {}° é {}\nO Cosseno de {}° é {}\nA Tangente de {}° é {}\n'.format(x,sinx,x,cosx,x,tanx))

