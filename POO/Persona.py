"""
¿En qué consiste la Programación Orientada a Objetos?
-En trasladar la naturaleza de los objetos de la vida real a código
de programación (en algún lenguaje de programación, cómo Python).

Los objetos de la realidad tienen características (atributos o propiedades)
y funcionalidades o comportamientos (funciones o métodos).

Ventajas:
-Modularización (división en pequeñas partes) de un programa completo.
-Código fuente muy reutilizable.
-Código fuente más fácil de incrementar en el futuro y mantener.
-Si existe un fallo en una pequeña parte del código el programa completo
no debe fallar necesariamente. Además, es más fácil de corregir esos fallos.
-Encapsulamiento: ocultamiento del funcionamiento interno de un objeto.
"""


class Personas():
    #Propiedades, caracteristicas o atributos:
    apellido = ""
    nombres = ""
    edad = 0
    despierta = False

    #Funcionalidades:
    def despertar(self):
        #self: Parametro que hace referencia a la instancia perteneciente a la clase.
        self.despierta = True
        print("Buen dia.")

# persona1 = Persona()
# persona1.apellidos = "Ortiz Cornejo"
# print(persona1.apellidos)
# persona1.despertar()
#
# persona2 = Persona()
# persona2.apellidos = "Yanez Pingo"
# print(persona2.apellidos)
# persona2.despertar()
