# White: Estructura repetitiva que nos permite realizar multiples iteraciones
# basandonos en el resultado de una expresion logica que puede
# tener como resultado un valor True o False.

"""
indice = 1

while indice < 10:
    print("Valor actual: {0}".format(indice))
    indice = indice + 1

print("Hemos terminado el bucle while.")
# Continua el programa
"""

# inicio = 2
#
# while inicio <= 100:
#     print("Numero par: {0}".format(inicio))
#     inicio += 2
#
# print("Hemos terminado un bucle while.")

class While:
    def While(self,inicio):
        while inicio <= 100:
            print("Numero par: {0}".format(inicio))
            inicio += 2
        print("Hemos terminado un bucle while.")