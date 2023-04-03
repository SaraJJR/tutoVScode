# Crea un programa que pida un número al usuario un número de mes (por ejemplo, el 4) y diga cuántos días tiene (por ejemplo, 30)
# y el nombre del mes. Debes usar listas. Para simplificarlo vamos a suponer que febrero tiene 28 días.

meses = [
   'Enero tiene 31 días', 
   'febrero 29 días', 
   'marzo 31', 
   'abril 30', 
   'mayo 31', 
   'junio 30', 
   'julio 31', 
   'agosto 31', 
   'septiembre 30', 
   'octubre 31', 
   'noviembre 30',  
   'diciembre 31 días'
]

mes = int(input("Ingresa un numero del 1 al 12: ")) - 1
print(meses[mes])