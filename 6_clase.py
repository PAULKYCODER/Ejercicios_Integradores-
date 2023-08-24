"""Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los
siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. Hay que validar las entradas de
datos.
 mostrar(): Muestra los datos de la persona.
 Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad"""

class Persona:
    def __init__(self, Nombre, Edad, DNI):
        self.__Nombre = Nombre
        self.__Edad = Edad
        self.__DNI = DNI 
    
    

    @property
    def Nombre(self):
        return self.__Nombre
    @property
    def Edad(self):
        return self.__Edad
        
    @property
    def DNI(self):
        return self.__DNI
    
    @Nombre.setter
    def Nombre(self, new_nombre):
        self.__Nombre = new_nombre

    @Edad.setter
    def Edad(self, new_Edad):
        self.__Edad = new_Edad
        

    @DNI.setter
    def DNI(self, new_DNI):
        self.__DNI = new_DNI
    
    
    def Es_mayor_de_edad(self):
        if Edad > 21:
           return print("Eres una persona mayor de edad")
        
    

    def Mostrar(self):
        print(f"Nombre: {self.Nombre}")
        print(f"Edad: {self.Edad}")
        print(f"DNI: {self.DNI}") 
        #print("\n")



persona1 = Persona("Pablo", 34, 34179093)
Nombre = persona1.Nombre
Edad = persona1.Edad
DNI = persona1.DNI

persona2 = Persona("Maria", 19, 20345678)
Nombre = persona2.Nombre
Edad = persona2.Edad
DNI = persona2.DNI


persona1.Es_mayor_de_edad() 
persona1.Mostrar()


persona2.Es_mayor_de_edad()
persona2.Mostrar()


# persona1.Nombre="pedro"




