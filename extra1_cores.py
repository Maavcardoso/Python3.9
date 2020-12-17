# Usaremos o ANSI para colorir o código.
# Para representar uma cor em python no sistema ANSI, representamos da seguinte maneira:
# \033[0;33;44m
# o primeiro número (0) é o estilo do texto 
#( 0 - nenhum 1 - negrito 4 - sublinhado 7 - negativo )
# o segundo número (33) é a cor do texto
#(dos números 30 a 37 possuem as cores de texto)
# o terceiro número (44) é a cor do background do texto
#(dos número 40 a 47 possuem as cores do background)

print('\033[7;31;42mHello World')