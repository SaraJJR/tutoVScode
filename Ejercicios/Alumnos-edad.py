# Queremos guardar los nombres y la edades de los alumnos de un curso. 
# Realiza un programa que introduzca el nombre y la edad de cada alumno. 
# El proceso de lectura de datos terminará cuando se introduzca como nombre un asterisco (*) 
# Al finalizar se mostrará los siguientes datos:

# Todos lo alumnos mayores de edad.
# Los alumnos mayores (los que tienen más edad)

alumnos = []
edad = []

while True:
    nombre = input("Nombre: ")
    if nombre != "*":
        alumnos.append(nombre)
        numero = int(input("Edad: "))
        edad.append(numero)
    if nombre == "*":
        break;
print(alumnos)
print(edad)
print("La edad mayor es ",max(edad))

print("Alumnos mayores de edad")
print("=======================")
for nombres,edades in zip(alumnos,edad):
	if edades >= 18:
		print(nombres)
	
# Alumnos mayores 

print("Alumnos mayores")
print("===============")
for nombres,edades in zip(alumnos,edad):
	if edades == max(edad):
		print(nombres)


