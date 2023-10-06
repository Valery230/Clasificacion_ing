#Examen individual, clase y atributos
#Valery Nickol Rosero

class calculadora:
    def __init__(self):
        self.num1 = int(input("Por favor ingrese el primer número para operar: "))
        self.num2 = int(input("Por favor ingrese el segundo número para operar: "))

    def suma(self):
        return self.num1 + self.num2
    
    def resta(self):
        return self.num1 - self.num2
    
    def multiplicación(self):
        return self.num1 * self.num2
    
    def división(self):
        return self.num1 / self.num2
    
calculadora1 = calculadora()

print("El resultado de suma es: ", calculadora1.suma())
print("El resultado de resta es: ", calculadora1.resta())
print("El resultado de multiplicación es: ", calculadora1.multiplicación())
print("El resultado de división es: ", calculadora1.división())