
i, c, itotal = [], 0, 1
n = int(input())- 1
while c <= n:
    car = int(input())
    i.insert(c, car)
    c = c + 1
c = 0
while c <= n:
    
    if itotal == c:
        itotal += 1

    elif i[c] % 2 != 0:
        i[c] = i[c] - 1
        c = c + 1
    elif i[c] % 2 == 0 and i[c] > 0:
        i[c] = i[c] - 1
        c = c - 1
    else:
        c = c - 1
    
    if c == 0:
        break    
   
cartot = sum(i)
print(itotal, cartot)
