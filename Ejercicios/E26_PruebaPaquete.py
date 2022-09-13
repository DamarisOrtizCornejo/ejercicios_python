"""
Paquetes:
Directorios (carpetas) donde se almacenan modulo relacionados entre si.

¿Para que sirven?
Para organizar  mejor el codigo y poder reutilizarlo mejor (modularizacion y reutilizacion).

¿Como se crea un paquete?
Crear una carpeta o directorio con un archivo dentro llamado __init__.py

lo que hace __init__.py es "convertir" un directorio en un modulo (paquete)
que contiene otros modulo, y esto lo hace para poder importarlos.
"""



from Paquete1.FuncionesCadenas import contarLetras
from Paquete1.FuncionesNumericas import *

print(multiplicar(5, 6))
print(contarLetras("Damaris Ortiz"))