# Un método es una función que se encuentra dentro de un objeto.

# El método o función 'upper' es para transformar la expresión a mayúsculas.
animal = "chanchito feliz"
print(animal.upper())

# El método o función 'lower' es para transformar la expresión a minúsculas.
animal = "chanCHito feliz"
print(animal.lower())

# El método o función 'capitalize' es para transformar nuestro primer caracter en mayúscula y el resto lo deja en minúscula o como este.
animal = "chanCHito feliz"
print(animal.capitalize())

# El método o función 'title' transforma la primera letra de la primera palabra y la primera letra de la segunda palabra y las pone en mayúsculas.
animal = "chanCHito feliz"
print(animal.title())

# El método 'strip' va a remover todos los espacios que se encuentre tanto a la izquierda y a la derecha de nuestro string.
animal = "  chanCHito feliz  "
print(animal.strip())

animal = "  chanCHito feliz  "
print(animal.strip().capitalize())

# El método 'lstrip' consiste en sacar los espacios en blanco de la izquierda de nuestro string.
animal = "  chanCHito feliz  "
print(animal.lstrip())

# El método 'rstrip' consiste en sacar los espacios en blanco de la derecha de nuestro string.
animal = "  chanCHito feliz  "
print(animal.rstrip())

# El método 'find' va a buscar una cadena de caracteres que nosotros le indiquemos 'CH' y nos devolverá el indice correspondiente a esa cadena de caracteres.
animal = "  chanCHito feliz  "
print(animal.find("CH"))

# Cuando le ponemos una cadena de caracteres que no coincide, en este caso 'cH', nos da como resultado -1, esto significa que 'NO LO HA ENCONTRADO' Número positivo: ENCONTRADO; Número negativo: NO ENCONTRADO
animal = "  chanCHito feliz  "
print(animal.find("cH"))

# El método 'replace' nos indica que reemplaza por lo que le digamos.
animal = "  chanCHito feliz  "
print(animal.replace("nCH", "j"))

# La diferencia de esta manera con 'find', es que el método find devuelve el indice de donde se encuentra esa cadena de caracteres e in seguido de un espacio y la variable te va a devolver un boolean. Básicamente si ese caracter se encuentra o no.
animal = "  chanCHito feliz  "
print(("nCH" in animal))

# Con el not, le estamos indicando si esa cadena se encuentra o si no.
animal = "  chanCHito feliz  "
print(("nCH" not in animal))
