#Ejercicio dragrama de clases 1.
#Hecho por Valery Nickol Rosero Molina.
#Ingeniería de Software.
#24/09/2023.

#Programa para la información de las recervas de una empresa dedicada al alquiler de automóviles.

print("¡Bienvenido!")

print("Antes de todo, identifícate.")


nombre = input("Por favor, ingresa tu nombre: ")
dni = int("Ingrese su documento de identidad: ")
dirección = input("Ingrese su dirección: ")
telefono = int("Por último, ingrese su número de teléfono: ")


coches = int("¿Cuántos coches desea alquilar?: ")
fecha_inicio = int(input("Registre la fecha de inicio: "))
fecha_entrega = int(input("Registre la fecha de entrega: "))

gasolina = 30000 * coches
totalCoches = coches * 50000
total = gasolina * totalCoches

print("Cuenta total.")
print("Nombre: ", nombre)
print("Dirección: ", dirección)
print("Coches: ", coches) 
print("Fecha de inicio: ", fecha_inicio)
print("Fecha de entrega: ", fecha_entrega)
print("Gasolina: ", gasolina)

print("Total: ", total)

print("Por favor, devolver el auto al mismo garaje donde fue entregado.")