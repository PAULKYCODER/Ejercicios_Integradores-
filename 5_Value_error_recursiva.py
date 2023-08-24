#RECURSIVA

def get_int():
    try:
        entrada = input("Ingrese un valor entero: ")
        salida_int = int(entrada)
        return salida_int
    except ValueError:
        print("Error: El valor ingresado no es un entero válido. Inténtelo de nuevo.")
        return get_int()

# Llamada a la función
valor = get_int()
print("Valor entero ingresado:", valor)
