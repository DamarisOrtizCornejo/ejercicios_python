# Generadores: Permiten extraer valores de una funcion y almacenarlo
# ( de uno en uno) en objetos iterables (que se pueden recorrer),
# sin la necesidad de almacenar TODOS A LA VEZ en la memoria RAM.


# def generarMultiplos7(limite):
#     numero = 1
#     listaNumeros = []
#
#     while numero <= limite:
#         listaNumeros.append(numero * 7)
#         numero = numero + 1
#     return listaNumeros #Retorna toda la lista creada.
#
# print(generarMultiplos7(10))




# def generadorMultiplos7(limite):
#     numero = 1
#
#     while numero <= limite:
#         yield numero * 7 #Ceder. La instruccion "yield" genera un objeto iterable.
#         numero = numero + 1
#
# obtieneMultiplos7 = generadorMultiplos7(10)

"""
# print(obtieneMultiplos7)
for n in obtieneMultiplos7:
    print(n)
    """

# next(): Retorna el siguiente elemento de un objeto iterable:


# print(next(obtieneMultiplos7))
# print("Aca hay 300 lineas de codigo...")
# print(next(obtieneMultiplos7))
# print("Aca hay 1000 lineas de codigo...")
# print(next(obtieneMultiplos7))


# Son mis eficiente que las funciones tradicionales.
# Muy utiles con listas de valores infinitos.
# Entre llamada y llamada, el objeto iterable entra en un estado de pausa (suspension).

class Generador:
    def generarMultiplos7(self,numero,limite):
        listaNumeros = []
        while numero <= limite:
            listaNumeros.append(numero * 7)
            numero = numero + 1
        return listaNumeros  # Retorna toda la lista creada.
