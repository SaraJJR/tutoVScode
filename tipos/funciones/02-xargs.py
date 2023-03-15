def suma(*numeros):  # * parametros itelables
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma(2, 5, 7)
suma(2, 9)
