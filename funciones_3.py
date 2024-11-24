def encontrar_maximo(numeros):
    return max(numeros)

# Pedimos al usuario que ingrese los números separados por comas
entrada = input("Ingresa una lista de números separados por comas: ")

# Convertimos la entrada en una lista de enteros
numeros = list(map(int, entrada.split(',')))

# Mostramos la lista correctamente
print(f"La lista es: {numeros}")

# Llamamos a la función y mostramos el resultado
print(f"El número máximo encontrado en {numeros} es: {encontrar_maximo(numeros)}")