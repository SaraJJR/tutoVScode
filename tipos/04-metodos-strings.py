animal = "  chanchito feliz"
print(animal.upper())  # Poner todo en mayusculas
print(animal.lower())  # Todo minusculas
print(animal.capitalize())  # Primera posicion en mayusculas
print(animal.title())  # Primera letra de cada palabra en mayuscula
print(animal.strip())  # Remueve los expacios en blanco de izquierda y derecha

# Los metodos se pueden encadenar
print(animal.strip().capitalize())

print(animal.lstrip())  # Quita los espacios en blanco de la izquierda
print(animal.rstrip())  # Quita los espacios de la derecha

# Devuelve la posicion en la que estan los caracteres, si es positivo lo encopntro
# si es negativo no lo encontro
print(animal.find("ch"))

# Reemplaza los caracteres ("argumento existente", "el reemplazo")
print(animal.replace("nch", "i"))

print("nch" in animal)  # Dice si existe
print("nch" not in animal)  # Ver si no esta
