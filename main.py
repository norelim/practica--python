from calculadora import *
from persona import Persona

# Nombre
nombre = input("Proporciona el Nombre: ")

# # Apellido
apellido = input("Proporciona el Apellido: ")

# # #Fecha de nacimiento
fecha_nac = input("Proporciona la Fecha de Nacimiento: ")

# # # numero 
numero = input("Proporciona un numero: ")
edad = Persona.calcular_edad(fecha_nac)
# # AQUI DEBO LLAMAR A LAS OPERACIONES QUE TENGO EN calculadora.py
suma_edad = adiccionar(edad,numero)
resta_edad = restar(edad,numero)
multi_edad = multiplicar(edad,numero)
div_edad = dividir(edad,numero)

print ("Tu edad sumándole el numero: " + str(numero) + " es " + str(suma_edad))
print ("Tu edad restandole el numero: " + str(numero) + " es " + str(resta_edad))
print ("Tu edad multiplicandola el numero: " + str(numero) + " es " + str(multi_edad))
print ("Tu edad dividiendola el numero: " + str(numero) + " es " + str(div_edad))
# PARA REQUERIMIENTO DEL OBJETO
class Person:
    nombre = ''
    apellido = ''
    fechaNac = ''

persona = Person()
persona.nombre = nombre
persona.apellido = apellido
persona.fechaNac = fecha_nac
print(persona.nombre)
print(persona.apellido)
print(persona.fechaNac)

if edad  % 2 == 0:
     print("Tu edad es par!!")





