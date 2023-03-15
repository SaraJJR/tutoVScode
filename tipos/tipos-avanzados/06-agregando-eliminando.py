mascotas = ["Wolfgang", "Pulga", "Pelusa", "Pulga", "Felipe", "Chanchito"]

mascotas.insert(1, "Melvin")
mascotas.append("Chanchito triste")  # Agrega un elemento al final

mascotas.remove("Pulga")  # Solo elimina el primer elemento Pulga
mascotas.pop()  # Eliminar el ultimo elemento
del mascotas[0]  # Entre corchetes anotar el indice
mascotas.clear()
print(mascotas)
