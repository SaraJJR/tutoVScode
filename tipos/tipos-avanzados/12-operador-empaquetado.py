lista1 = [1, 2, 3, 4]
# print(*lista)       #Extrae los datos como elemtos

lista2 = [5, 6]

combinada = ["Hola", *lista1, "Mundo", *lista2]
print(combinada)

punto1 = {"x": 19}
punto2 = {"y": 15}
nuevoPunto = {**punto1, "lala": 8, **punto2, "z": 58}
print(nuevoPunto)
