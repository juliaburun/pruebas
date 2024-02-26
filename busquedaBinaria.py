def busqueda_binaria(lista, elemento):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2

        # Comprobar si el elemento está en la mitad
        if lista[medio] == elemento:
            return medio
        elif lista[medio] < elemento:
            # Descartar la mitad izquierda
            inicio = medio + 1
        else:
            # Descartar la mitad derecha
            fin = medio - 1

    # Si llegamos aquí, el elemento no está en la lista
    return -1

# Ejemplo de uso
mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
elemento_a_buscar = 7

resultado = busqueda_binaria(mi_lista, elemento_a_buscar)

if resultado != -1:
    print(f"El elemento {elemento_a_buscar} se encuentra en la posición {resultado}.")
else:
    print(f"El elemento {elemento_a_buscar} no está en la lista.")
