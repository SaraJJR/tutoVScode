# Crea una lista e inicializala con 5 cadenas de caracteres leídas por teclado.
# Copia los elementos de la lista en otra lista pero en orden inverso, y muestra sus elementos por la pantalla.

texto = []

for palabra in range(0,5):
    p = input("Escribe una palabra: ")
    # print(p)
    texto.append(p)
print(texto)

#Inverte el orden de una lista 
# i = len(texto) - 1
# texto_inverso = [] 
# while (i >= 0):
#   texto_inverso.append(texto[i])
#   i = i - 1
# print(texto_inverso)

texto_inverso = list(reversed(texto))
print(texto_inverso)


