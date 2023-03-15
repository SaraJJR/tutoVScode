def get_product(**datos):
    print(datos["id"], datos["name"])


# Cuando se hace uso del ** al llamar a la funcion debemos escribir el nombre del argumento
get_product(id="id",
            name="Iphone",
            desc="Esto es una iphone")
