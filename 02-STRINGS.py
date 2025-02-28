nombre_curso = "Ultimate Python"
descripción_curso = """este curso contempla todos los detalles 
que necesitas aprender para encontrar un trabajo como programador"""  # Las triple dobles comillas sirven para contemplar una descripción.
print(nombre_curso, descripción_curso)

# La función len() nos indica la longitud del argumento que queramos saber.
print(len(nombre_curso))

# El valor cero nos indica el primer índice. Nunca empieza por uno, siempre en python empieza desde el cero.
print(nombre_curso[0])

# Esto sirve para cortar un string, desde un principio hasta el final que más nos interese.
print(nombre_curso[0:8])

# Poniendo un número a la izquierda, cogerá desde esa posición hasta el final.
print(nombre_curso[9:])

# Poniendo un número a la derecha, cogerá desde esa posición hasta el principio.
print(nombre_curso[:8])

# Poniendo solo los dos puntos, nos dará como resultado la frase completa.
print(nombre_curso[:])


