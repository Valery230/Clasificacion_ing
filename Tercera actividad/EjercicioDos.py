#Ejercicio dragrama de clases 2.
#Hecho por Valery Nickol Rosero Molina.
#Ingeniería de Software.
#24/09/2023.

#Aplicación para almacenar información sobre empresas, sus empleados y sus clientes.

print("¡Bienvenido!")

empresa = input("Por favor, ingrese el nombre de la empresa: ")

def ingreso_de_datos():

    directivos = int(input(f"¿Cuántos datos de directivos de {empresa.title()}desea ingresar?: "))
    for a in range(directivos):
        a = input("Ingrese el nombre: ")
        e = int("Digite la edad: ")
    
    empleados = int(input(f"¿Cuántos datos de empleados de {empresa.title()}desea ingresar?: "))
    for a in range(empleados):
        a = input("Ingrese el nombre: ")
        e = int("Digite la edad: ")
    
    clientes = int(input(f"¿Cuántos datos de clientes de {empresa.title()}desea ingresar?: "))
    for a in range(clientes):
        a = input("Ingrese el nombre: ")
        e = int("Digite la edad: ")
        i = int("Ingrese su número de teléfono: ")

ingreso_de_datos()