mensaje = """
Bienvenidos a la calculadora
Para salir escibre Salir
Las operaciones son suma, multiplicacion, resta y division.
"""
print(mensaje)

resultado = ""
while True:
    if not resultado:
        resultado = input("ingresa numero:  ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    op = input("Ingresa una opreacion:  ")
    if op.lower() == "salir":
        break
    n2 = input("Ingresa siguiente numero:  ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)
    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multiplicacion":
        resultado *= n2
    elif op.lower() == "division":
        resultado /= n2
    else:
        print("Operacion no valida")
        break

    print(f"El resultado es {resultado}")
