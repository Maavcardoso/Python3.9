# Este programa verifica se a função é quadrática e 
# calcula sua(s) raiz(es).5
# Também adicionei um código que printa a função na tela, assim
# O usuário pode ver tanto a função quanto os resultados.

a = float(input('Insira o valor de a: '))
b = float(input('Insira o valor de b: '))
c = float(input('Insira o valor de c: '))

print('\n{}x²'.format(a),end=' ')

if b > 0:
        print('+ {}x'.format(b), end=' ')
elif b < 0:
        print('{}x'.format(b), end=' ')
elif b == 0:
        pass
if c > 0:
        print('+ {}'.format(c),end=' ')
elif c < 0:
        print('{}'.format(c),end=' ')
elif c == 0:
        pass
print('= 0\n')
        


if a == 0:
    x = -c/b
    print('Esta função é linear.\nPortanto, X = {}\n'.format(x))
    quit()

else:
        d = b **2 - 4 *a *c

if d < 0:
        print('Delta negativo, não existe solução real.\n')

elif d == 0:

        x = -b/(2*a)
        print('Delta igual a zero: as duas raízes são {}\n'.format(x))

else:
        x1 = (-b + d**0.5)/(2*a)
        x2 = (-b - d**0.5)/(2*a)
        print("x'= {} \nx"'"= {}\n'.format(x1, x2))



