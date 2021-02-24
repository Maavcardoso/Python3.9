n = int(input('Digite a quantidade de elementos desejada: '))
n1 = 0
c = 0
n2 = 1
print('1',end=' > ')
while c < n:
    if c != n-1:
        n3 = n1 + n2
        print(n3,end=' > ')
        n1 = n2
        n2 = n3
        c += 1
    else:
        n3 = n1 + n2
        print(n3)
        c += 1
    

