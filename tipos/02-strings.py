nombre_curso = "Ultimate Pyhton"

# Variable de string con varios renglones se usan las dobles triple comillas
descripcion_curso = """
Ultimate Pyhton este curso contempla todos los detalles que necesitas para aprender para encontrar 
un trabajo como programador.
"""
print(len(nombre_curso))    # Para saber la longitus de una variable string
print(nombre_curso[0])      # Imprimir la primera letra del string nombre_curso
# Quitar caracteres [donde empieza : cuantos debo quitar]
print(nombre_curso[0:8])
print(nombre_curso[9:])     # Elimina desde 9 hasta el final
print(nombre_curso[:8])     # Elimnima desde el 0 hasta el 8
print(nombre_curso[:])      # Deja todo
