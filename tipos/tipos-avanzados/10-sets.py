# set significa grupo o conjunto
# Elimina datos dublicados
# No se puede accecer a sus elementos

primer = {1, 1, 2, 2, 3, 4}
# primer.add(5)
# primer.remove(1)
# print(primer)

segundo = [3, 4, 5]
segundo = set(segundo)
# print(segundo)

# print(primer | segundo)
# print(primer & segundo)  # Interseccion
# # Mostrar los datos del primer set y eliminar los que estan en el segundo
# print(primer - segundo)

# Diferencia simetrica, elimina los elementos que esten en ambos sets y devuelve los restantes
print(primer ^ segundo)
