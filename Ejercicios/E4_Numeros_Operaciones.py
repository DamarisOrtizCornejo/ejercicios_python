entero = 23
decimal = 31.78
complejo = 12 + 5j
booleano = True

"""
print(entero)
print(decimal)
print(complejo)
print(booleano)
"""

# num1 = 20
# num2= 4
#
# print("Suma:", (num1 + num2))
# print("Resta:", (num1 - num2))
# print("Multiplicación:", (num1 * num2))
# print("División:", (num1 / num2))
# print("División Exacta:", (num1 // num2))
# print("Potencia:", (num1 ** num2))

class OperacionesconNumeros:

    def Suma(self,num1,num2):
        suma = num1 + num2
        print(suma)

    def Resta(self,num1,num2):
        resta = num1 - num2
        print(resta)

    def Multiplicación(self,num1,num2):
        multiplicación = num1 * num2
        print(multiplicación)

    def División(self,num1,num2):
        división = num1 / num2
        print(división)

    def DivisiónExacta(self,num1,num2):
        divisionExacta = num1 // num2
        print(divisionExacta)

    def Potencia(self,num1,num2):
        potencia = num1 ** num2
        print(potencia)

numOp = OperacionesconNumeros()
# numOp.Suma()
# numOp.Resta()
# numOp.Multiplicación()
# numOp.División()
# numOp.DivisiónExacta()
# numOp.Potencia()