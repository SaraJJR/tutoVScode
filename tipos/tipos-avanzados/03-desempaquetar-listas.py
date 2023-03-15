numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Asignar el valor de cada elemento de la lista a cada variable
primero, segundo, tercero = numeros
print(primero, segundo, tercero)

primero, *otros = numeros  # Extraer el primer valor
primero, segundo, *otros = numeros
primero, *otros, ultimo = numeros
