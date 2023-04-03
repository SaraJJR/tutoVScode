# Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno 
# (comprendidas entre 0 y 10). A continuación debe mostrar todas las notas, la nota media, 
# la nota más alta que ha sacado y la menor.

calf = []

for nota in range(0,5):
    nota = int(input("Ingrese calificacion:"))
    calf.append(nota)
print(calf)
print(max(calf))
print(min(calf))
print(sum(calf)/len(calf))