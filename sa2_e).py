lista = [5, 7, 2, 9, 4, 1, 3]
auxiliar = 0
for i in range(0,len(lista)):
    for j in range(0,len(lista)-1):
        if lista[i] < lista[j]:
            auxiliar = lista[i]
            lista[i] = lista[j]
            lista[j] = auxiliar
for i in lista:
    print(f'{i} ',end=' ')
