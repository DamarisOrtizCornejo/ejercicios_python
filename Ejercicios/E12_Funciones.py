# Funciones: Es un conjunto de instrucciones que realizan un proceso.
# Su principal ventaja es que nos ayudan a evitar código repetido.

# def saludar():
#     print("Ortiz")
#     print("Damaris")
#     print("Damaris Ortiz")
#     return "Hola"
#
# print(saludar())
#
# def evaluarSueldoMinimo (sueldo):
#     if sueldo >= 850:
#         print("Cumples con el sueldo")
#     else:
#         print("Ganas menos que el sueldo minimo")
#
# evaluarSueldoMinimo(1200)

class Funciones:
    def saludar(self,saludo):
        return "Hola"

    def evaluarSueldoMinimo(self,sueldo):
        if sueldo >= 850:
            print("Cumples con el sueldo")
        else:
            print("Ganas menos que el sueldo minimo")

    # evaluarSueldoMinimo(1200)

# fun = Funciones()
# print(fun.saludar("Hola"))
# fun.evaluarSueldoMinimo(1200)