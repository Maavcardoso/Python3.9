# Faça um programa que peça para o usuário quantos metros quadrados será necessário pintar,
# e printar na tela somente a quantidade de latas, de galões e o negócio mais rentável.
# considere que:
# 1 litro de tinta pode pintar 6 metros quadrados,
# 1 lata contém 18 litros de tinta e um galão 3.6,
# há uma folga de 10% e as latas e galões devem estar cheios.
# Também implementei um código que verificar se há excesso de tinta.

lt = float(80)
gt = float(25)
ql = 18*0.9 
qg = 3.6*0.9
m = float(input('Quantos Metros Quadrados serão pintados? '))
t = m/6

print('\nSerá necessário {} Litros de tinta.\nVocê pode comprar:\n '.format(round(t,2)))

restol = round(t % ql,2)

if restol != 0:
    qlt = (t//ql)+1
    dspl = round(qlt*ql-t,2)
    precl = qlt*lt

    if qlt == 1:
        print('{} Lata, que custará {} R$. Mas haverá desperdício de {} litros.\n'.format(qlt,precl,dspl))
    else:
        print('{} Latas, que custarão {} R$. Mas haverá desperdício de {} Litros.\n'.format(qlt,precl,dspl))
else:
    qlt = (t/18)
    precl = qlt*lt
    if qlt == 1:
        print('{} Lata, que custará {} R$.\n'.format(qlt,precl))
    else:
        print('{} Latas, que custarão {} R$\n'.format(qlt,precl))

restog = round(t % qg,2)

if restog != 0 and restog != qg: # Aqui foi o pulo do gato: Se não fosse pelo restog != qg, a função iria bugar*.
    qgt = (t//qg)+1
    dspg = round(qgt*qg-t,2)
    precg = qgt*gt

    if qgt == 1:
        print('{} Galão, que custará {} R$. Mas haverá desperdício de {} litros.\n'.format(qgt,precg,dspg))
    else:
        print('{} Galões, que custarão {} R$. Mas haverá desperdício de {} litros.\n'.format(qgt,precg,dspg))
else:
    qgt = (t/qg)
    precg = qgt*gt

    if qgt == 1:
        print('{} Galão, que custará {} R$.\n'.format(qgt, gt))
    else:
        print('{} Galões, que custarão {} R$\n'.format(qgt, precg))

restox = restol%qg
x = restol//qg
qlt2 = t//ql
precx = qlt2*lt+x*gt

if restox == 0:
    print('O melhor negócio são {} Latas e {} Galões, que custarão {} R$\n').format(qlt2, x, precx)
else:
    x = x + 1
    dsp = round(qg - restox,2)
    precx = qlt2*lt+x*gt
    print('O melhor negócio são {} Latas e {} Galões, que custarão {} R$. Mas haverá desperdício de {} Litros\n'.format(qlt2,x,precx,dsp))

# * A função iria bugar pois a operação t%qg, sendo t um número que se divide inteiramente com 3.6,
# Por conta do compilador trabalhar com o sistema numeral binário, não decimal, há um pequeno desvio
# de cálculo no qual restog é igual 