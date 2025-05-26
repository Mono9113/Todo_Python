class paciente:
    #Cada vez que se use self es que se va a orientar o pertenecen a la class
    #Constructor
    def __init__(self,nombre,edad,peso,altura):
        self.nombre=nombre
        self.edad=edad
        self.peso=peso
        self.altura=altura
    def calcular_imc(self):
        return round (self.peso/(self.altura**2),2)
    def mostrar_info(self):
        print(f"Paciente: {self.nombre} edad: {self.edad}")
        imc=self.calcular_imc()
        print(f"IMC: {imc}")
        if imc <= 18.5: print("Bajo peso.")
        elif imc <= 24.9: print("Paso normal.")
        elif imc <= 29.9: print("Sobre peso.")
        elif imc <= 34.9: print("Obesidad 1.")
        elif imc <= 39.9: print("Obesidad 2.")
        elif imc <= 44.9: print("Obesidad 3.")
        elif imc <= 45: print("Obesidad 4.")
        else: print("Fuera de rango.")

#Programa
nombre=input("Ingrese su nombre: ")
edad=int(input("Edad: "))
peso=float(input("Ingrese peso: "))
altura= float(input("Ingrese su estatura en mts: "))
objeto=paciente(nombre,edad,peso,altura)
objeto.mostrar_info()