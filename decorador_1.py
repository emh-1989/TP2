def decorador_mensaje(func):
    def envoltura():
        print("Inicio de la función.")
        func()
        print("Fin de la función.")
    return envoltura

@decorador_mensaje
def funcion_principal():
    print("Esta es la función principal.")

# Prueba la función decorada
funcion_principal()
