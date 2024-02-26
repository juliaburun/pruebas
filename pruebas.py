lista = [3,1,8,4]
n = len(lista)

for i in range(n - 1):
    for j in range(0, n - i - 1):
        if lista[j] > lista[j+1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]

print(lista)