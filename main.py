from calculadora import *
from persona import Persona

# Nombre
# nombre = input("Proporciona el Nombre: ")

# # Apellido
# apellido = input("Proporciona el Apellido: ")

# #Fecha de nacimiento
fechaNac = input("Proporciona la Fecha de Nacimiento: ")
# # numero 
# numero = input("Proporciona un numero: ")
edad = Persona.fecha_nac(fechaNac)
print(edad)

if edad  % 2 == 0:
     print("Tu edad es par!!")

# AQUI DEBO LLAMAR A LAS OPERACIONES QUE TENGO EN calculadora.py
# sumaEdad = add()
# restaEdad = substract()
# multiEdad = product()
# divEdad = div()

# print("Tu edad sumándole el numero " numero "es " sumaEdad)
# print("Tu edad restandole el numero " numero "es " restaEdad)
# print("Tu edad multiplicandole el numero " numero "es " multiEdad)
# print("Tu edad dividiendole el numero " numero "es " divEdad)

# PARA REQUERIMIENTO DEL OBJETO
# class Person:
#     nombre = ''
#     apellido = ''
#     fechaNac = ''
           
# persona = Person()
# persona.nombre = 'Norelis'
# persona.apellido = 'Mogollon'
# persona.fechaNac = '19/6/1978'
# print(persona.nombre)
# print(persona.apellido)
# print(persona.fechaNac)







