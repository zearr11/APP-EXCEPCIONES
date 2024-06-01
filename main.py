
from operaciones.calculadora import *

num1=input("Ingresa el numero 1: ")
num2=input("Ingresa el numero 2: ")

print("{} + {} = {}".format(num1,num2,sumar(num1,num2)))
print("{} - {} = {}".format(num1,num2,restar(num1,num2)))
print("{} * {} = {}".format(num1,num2,multiplicar(num1,num2)))
print("{} / {} = {}".format(num1,num2,divi(num1,num2)))