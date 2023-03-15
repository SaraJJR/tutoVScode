numeros = [2, 5, 1, 8, 4]

# numeros.sort()      #Ordenar la lista menor a mayor
# numeros.sort(reverse = True)        #Ordenar de mayor a menor

# Regresa una nueva lista ordenada no afecta la lista original
# numeros2 = sorted(numeros)
# Regresa una nueva lista ordenada de mayor a menor que no afecta la original
numeros2 = sorted(numeros, reverse=True)


# usuarios = [[4, "chanchito"], [1, "Felipe"], [5, "Pulga"]]
# usuarios.sort()  # Solo ordena numeros a menos que le indiques con una funcion
# print(usuarios)


usurarios = [["Felipe", 6], ["Chanchito", 1], ["Juan", 9]]


# def ordenar(elemento):      # Definimos la funcion ordenar
#     return elemento[1]
# # Ingresamos la funcion ordenar para que ordene la tabla
# usurarios.sort(key=ordenar)
# print(usurarios)


usurarios.sort(key=lambda el: el[1], reverse=True)  # Acceder a una elemento
print(usurarios)
