# Hacer un programa que inicialice una lista de números con valores aleatorios (10 valores),
# y posterior ordene los elementos de menor a mayor.
import random

numeros = []

for n in range(0,10):
    n = random.randint(1,100)
    numeros.append(n)
print(numeros)
