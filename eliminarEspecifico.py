mi_lista = [1, 2, 3, 4, 5]
elemento_a_eliminar = 3

nueva_lista = []
for elemento in mi_lista:
    if elemento != elemento_a_eliminar:
        nueva_lista.append(elemento)

if len(nueva_lista) < len(mi_lista):
    print(f"Elemento {elemento_a_eliminar} eliminado. Lista actualizada: {nueva_lista}")
else:
    print(f"El elemento {elemento_a_eliminar} no está en la lista.")
