# Collecion de datos
# E como por lo general las bases de datos regresan los datos

# Las llaves se definen con un string ej. "x" y "y" : el valor que asignamos
punto = {"x": 25, "y": 50}
print(punto)
print(punto["x"])  # Para acceder a un dato debemos poner entre [] la llave
print(punto["y"])

punto["z"] = 45     # Agregar una llave al diccionario
print(punto)
if "lala0" in punto:
    print("Encontre lala= ", punto["lala0"])

print(punto.get("x"))  # Obtener un valor
print(punto.get("lala0"), 97)  # 97 valor por defecto si no encuentra la llave

del punto["x"]  # Eliminar
del (punto["y"])
print(punto)

punto["x"] = 25

for valor in punto:
    print(valor, punto[valor])  # Acceder a los valor

for valor in punto.items():  # Obetener los valores de un diccionario
    print(valor)

for llave, valor in punto.items():  # Desempaquetar los valores de un diccionario
    print(llave, valor)


usuarios = [
    {"id": 1, "nombre": "Chanchito"},
    {"id": 2, "nombre": "Feliz"},
    {"id": 3, "nombre": "Nicolas"},
    {"id": 4, "nombre": "Felipe"}
]

for usuario in usuarios:  # Obtener datos
    print(usuario["nombre"])
