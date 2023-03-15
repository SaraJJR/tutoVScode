# Parametro ej: nombre, apellido = "Feliz" asigna el Feliz como valor por defecto
def hola(nombre, apellido="Feliz"):
    print("Hola mundo")
    print(f"Bienvenido {nombre} {apellido}")


hola("Sara", "Jimenez")  # Argumento ej: Sara
hola("Chanchito")


# Definir a que Parametro pertenece el argumento
hola(apellido="Jimenez", nombre="Sara")
