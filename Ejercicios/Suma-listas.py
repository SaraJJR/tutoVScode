# Programa que declare tres listas ‘lista1’, ‘lista2’ y ‘lista3’ de cinco enteros cada uno, 
# pida valores para ‘lista1’ y ‘lista2’ y calcule lista3=lista1+lista2.

lista1 = []
lista2 = []
lista = []
for n in range(0,5):
    n = int(input("Ingrese numero 1: "))
    lista1.append(n)

for i in range(0,5):
    i = int(input("Ingrese numero 2: "))
    lista2.append(i)

for k in range(0,5):
    o = lista1[k] + lista2[k]
    lista.append(o)
print(lista)
