# Agora que já sabemos o que a repetição while faz, agora vamos entender como interrompe-lo.
# Isso é um grande passo e uma ferramenta útil, já que podemos criar uma repetição infinita que
# irá parar quando o algoritmo por si só criar o que nós queremos, sem necessidade de uma chave ou
# confirmação do usuário.
 
c = 1
while True: # enquanto for igual TRUE, a repetição continua infinitamente.
     print(c,end=' ')
     c += 1
     if c == 11:
         break # esse comando interrompe a repetição, portanto, ele só irá conta do 1 ao 10. 

# Por exemplo, o somador abaixo recebe qualquer valor dado pelo usuário, contudo, se o mesmo for igual a 0,
# Um if irá quebrar a repetição, permitindo que todo n != 0 seja somado. 
s = 0
n = 0
while True:
    n = int(input('\nDigite um número (Digite 0 para parar): '))
    if n == 0:
        break # Sai do loop
    s += n # Soma o número ao total se for diferente de 0
print(f'A soma dos valores é igual a {s}')

