"""Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una
cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero
del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el
ejercicio tanto de manera iterativa como recursiva."""

#ITERATIVA:
def get_int(numero):
    while True:
        try:
            entrada = input(numero)
            salida = int(entrada)
            return salida
        except ValueError:
            print("El valor ingresado es incorrecto")

numero = get_int("Ingresa un número entero: ")
print("El número que ingresaste es:", numero)



