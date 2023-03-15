# Una tupla es exactamento lo mismo que una lista PERO NO SE PUEDE MODIFICAR

numeros = (1, 2, 3) + (4, 5, 6)
print(numeros)

punto = tuple([1, 2])  # Recibe tipo de datos iterables
print(punto)

menosNumero = numeros[:2]  # No se modifica  crea una nueva tupla
print(menosNumero)
primero, segundo, *otros = numeros
print(primero, segundo, otros)

# Creamos una lista con una tupla y modificamos la lista
listaNumeros = list(numeros)
listaNumeros[0] = "Chanchito Feliz"
print(listaNumeros)
