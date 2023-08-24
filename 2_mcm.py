#Escribir una función que calcule el mínimo común múltiplo entre dos números
num1 = int (input ("ingrese el primer numero: "))

num2 = int (input ("ingrese el segundo numero: "))

def mcm (num1, num2):

    aux = max(num1,num2)

    while True:
        if (aux % num1 == 0) and (aux % num2 == 0):

            return aux

        aux += 1

print(mcm(num1,num2))                


