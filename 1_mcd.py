#Escribir una función que calcule el máximo común divisor entre dos números

num1 = int (input ("ingrese el primer numero: "))

num2 = int (input ("ingrese el segundo numero: "))


def mcd (num1, num2) :
    while num1 % num2 != 0:
        num1, num2 = num2, num1 

    return num2


print(mcd(num1,num2))    


