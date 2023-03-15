usuarios = [["Felipe", 6], ["Chanchito", 1], ["Juan", 9]]

# nombres = []
# for usuarios in usuarios:
#     nombres.append(usuarios[0])
# print(nombres)

# Tomas una lista y transformas cada uno de los elementos para obtener el primer elemento
# nombres = [usuario[0] for usuario in usuarios]
# print(nombres)

# Filtrar
# nombres = [usuario for usuario in usuarios if usuario[1] > 2]


# nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]


# nombres = list(map(lambda usuario: usuario[0], usuarios))     #map

menosUsuarios = list(
    filter(lambda usuario: usuario[1] > 2, usuarios))  # Filter
print(menosUsuarios)
