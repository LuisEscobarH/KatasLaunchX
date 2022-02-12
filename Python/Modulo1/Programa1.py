from traceback import print_list
from typing import Type
from numpy import product
from datetime import date

print('Hola desde la consola')
#--------------------------------------------------------------------
sum = 1 + 2 # 3
product = sum*2
print(product)

#----------------------------------------------------------------------
planetas_en_el_sistema_solar = 8 # int, plutón era considerado un planeta pero ya es muy pequeño
distancia_a_alfa_centauri = 4.367 # float, años luz
puede_despegar = True
transbordador_que_aterrizo_en_la_luna = "Apollo 11" #string

print("Planetas en el sistema solar:", planetas_en_el_sistema_solar)
print(type(planetas_en_el_sistema_solar))
print("La distancia a alfa centauri es:", distancia_a_alfa_centauri)
print(type(distancia_a_alfa_centauri))

#----------------------------------------------------------------------------------------------
print("La fecha actual es: ", date.today())
print("La fecha actual es: " + str(date.today()))

#-----------------------------------------------------------------------------------------------
print("Bienvenido al programa de bienvenida")
name = input("Introduzca su nombre: ")
print("Saludos " + name)

#---------------------------------------------------------------------------------------
print("Calculadora")
primer_numero = input("Primer número: ")
segundo_numero = input("Segundo número: ")
print(int(primer_numero) + int(segundo_numero))