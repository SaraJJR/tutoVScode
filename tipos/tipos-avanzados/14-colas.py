#LIFO last in first out
pila = []
pila.append(1)
pila.append(2)
pila.append(3)
print(pila)

ultimoElemento = pila.pop()
pila.pop()
pila.pop()
print(ultimoElemento)
print(pila)


if not pila:
    print("Pila vacia")
