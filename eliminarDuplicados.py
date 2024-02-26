def eliminar_duplicados(vector):
    vector_sin_duplicados = []

    for elemento in vector:
        if elemento not in vector_sin_duplicados:
            vector_sin_duplicados.append(elemento)

    return vector_sin_duplicados

# Ejemplo de uso
mi_vector = [1, 2, 3, 2, 4, 5, 1, 6, 7, 7, 8]
vector_sin_duplicados = eliminar_duplicados(mi_vector)

print(f"Vector original: {mi_vector}")
print(f"Vector sin duplicados: {vector_sin_duplicados}")
