# Programa que declare una lista y la vaya llenando de números hasta que introduzcamos un número negativo.
# Entonces se debe imprimir el vector (sólo los elementos introducidos).

numero = []

n = int(input("Numero: "))
while n > 0:
    numero.append(n)
    n = int(input("Numero: "))
    
print(numero)