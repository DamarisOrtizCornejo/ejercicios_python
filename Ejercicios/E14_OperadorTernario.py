"""
String sexo:
sexo = (10 > 20) ? "Masculino" : "Femenino";
"""

# sexos = ("Hombre", "Mujer")
#
# posicion = True
# sexo = sexos[posicion] #Mujer
# print(sexo)
#
# sexo = sexos[not posicion] #Hombre
# print(sexo)

# Operadores Ternarios: nos permite acceder a una de dos
# opciones a partir de una condición.

class OperadoresTernarios:
    def OperadorTernario(self):
        sexos = ("Hombre", "Mujer")
        posicion = True #1
        sexo = sexos[posicion]  # Mujer
        print(sexo)
        sexo = sexos[not posicion]  # Hombre
        print(sexo)

# opt = OperadoresTernarios()
# opt.OperadorTernario()