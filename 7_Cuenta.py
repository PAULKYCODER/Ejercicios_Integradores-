"""Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una
persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
opcional. Crear los siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
directamente, sólo ingresando o retirando dinero.
 mostrar(): Muestra los datos de la cuenta.
 ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
negativa, no se hará nada.
 retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números
rojos."""

class cuenta:


    def __init__(self, Titular="" , Cantidad=None):
        self.__Titular = Titular
        self.__Cantidad = Cantidad
    
    #getters para ver datos
    @property
    def Titular(self):
        return self.__Titular
    
    @property
    def Cantidad(self):
        return self.__Cantidad
    
    #setters para modificar datos
    @Cantidad.setter
    def Cantidad(self, N_Cantidad):
        self.__Cantidad = N_Cantidad
        
    
    def Ingresar_dinero(Cantidad):
        return print(f"El dinero ingresado es: ${cuenta1.Cantidad}\n")
    
    def Retirar_dinero(Cantidad):
        return print(f"El dinero que retiro es ${cuenta1.Cantidad}\n")
        
    
    
    def Mostrar(self):
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print(f"El titular de la cuenta es: {cuenta1.Titular}")
        print(f"El monto en su cuenta es de: u${cuenta1.Cantidad}")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    



cuenta1=cuenta("Pedro", 500)

#Getters
cuenta1.Mostrar()

#setters de ingreso y retiro de dinero









