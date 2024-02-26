lista = [4,7,2,5,0,47,5]
def burbujeo(lista):
    desordenada = True
    while desordenada:
        desordenada = False
        for i in range(len(lista)-1):
            if lista[i] > lista[i+1]:
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
                desordenada = True
burbujeo(lista)
print(lista)