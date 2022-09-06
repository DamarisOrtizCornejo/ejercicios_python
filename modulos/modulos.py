"""
Módulo:
Es un archivo con extension .py o pyc (Python compilado), que posee su propio espacio
y puede contener variables, funciones, clases o incluso otros modulos.

¿Para que sirven?
Para organizar mejor el codigo y poder reutilizarlo mejor.
Modularizacion y reutilizacion.
"""

#import funcionesMatematicas
#print(funcionesMatematicas.sumar(5, 6))
#print(funcionesMatematicas.multiplicar(5, 6))

from modulos.funcionesMatematicas import *

print(sumar(5, 6))
print(multiplicar(5, 6))