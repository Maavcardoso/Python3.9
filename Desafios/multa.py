p = float (input('Quantos kilos de peixe pescou?: '))
e = p - 50
if e > 0 and e < 1:
        print ('Você ultrapassou o limite por {} gramas.\nPortanto, terá que pagar {} R$ de multa.'.format(round(e*1000, 2),round(e*4, 2)))
elif e >= 1:
        print ('Você ultrapassou o limite por {} Kg.\nPortanto, terá que pagar {} R$ de multa.'.format(round(e, 3),round(e*4, 2)))

else:
        print ('Sua pesca está de acordo com a norma!')

