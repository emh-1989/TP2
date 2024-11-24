def sumar_lista(numeros):
    return sum(numeros)

# Pedimos al usuario que ingrese los números separados por comas
entrada = input("Ingresa una lista de números separados por comas: ")

# Convertimos la entrada en una lista de enteros
numeros = list(map(int, entrada.split(',')))

# Mostramos la lista correctamente
print(f"La lista es: {numeros}")

# Llamamos a la función y mostramos el resultado
print(f"La suma de los números {numeros} es: {sumar_lista(numeros)}")
