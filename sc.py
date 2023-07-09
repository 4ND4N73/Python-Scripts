lista =[]
lista.append([7,8])
lista.append([2,3])
lista.append([4,5])
lista.append([6,7])
lista.append([8,9])
lista.append([0,5])

for ix, iy in lista:
    print(ix,iy)

lista.insert(0,[9,9])
print(lista)


