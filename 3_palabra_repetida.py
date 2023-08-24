"""Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con
cada palabra que contiene y la cantidad de veces que aparece (frecuencia)."""

def contar_palabras(texto):
    # Separar la cadena en palabras y borrar caracteres especiales
    palabras = texto.lower().split()
    palabras = [palabra.strip('.,!?()[]{}"\'') for palabra in palabras]

    
    diccionario = {}

    # Contar la frecuencia de cada palabra
    for palabra in palabras:
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1

    return diccionario

# Solicitar al usuario que ingrese un texto
texto = input("Escriba un texto: ")

# Crear diccionario de frecuencias
diccionario_frecuencias = contar_palabras(texto)

# Mostrar diccionario de frecuencias
print("Diccionario de Frecuencias:")
for palabra, frecuencia in diccionario_frecuencias.items():
    print(f"{palabra}: {frecuencia}")
