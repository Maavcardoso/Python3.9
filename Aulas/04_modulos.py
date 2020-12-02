# Os módulos servem para adiocionar diferentes funções ao programa python
# Como exemplo, usarei o módulo math. 
# Podemos chamar o método de duas formas:

import math # Importa todas as funções de Math
from math import sqrt # Importa uma função específica de Math, no caso, raiz quadrada.

n = int(input('Digite um número: '))
raiz = math.sqrt(n)
print(f'Raiz igual a: {raiz}')

# FUNÇÕES UTEIS DO math
# math.ceil(variavel) = arredonda pra cima
# math.floor(variavel) = arredonda pra baixo
# math.sqrt(variavel) = faz raiz quadrada

# https://docs.python.org/3.9/py-modindex.html
# A biblioteca do Python contém inúmeros módulos, como o random



