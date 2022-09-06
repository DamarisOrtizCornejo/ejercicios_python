# AND: Equivalente a "Y si ademas..."
# OR: "O sino..."
# NOT -> negacion

# distancia = 400
# numeroHermanos = 3
# salariosPadres = 3000
# tieneBeneficio = False
#
# if (distancia > 1000 and numeroHermanos > 2) or salariosPadres < 2000:
#     tieneBeneficio = True
#
# print(not tieneBeneficio)
#
# if (5 > 3) or (8 < 6):
#     print("Verdad")
# else:
#     print("Es mentira...")

class OperadoresLogicos:
    def PrimerEjercicio(self):
        distancia = 400
        numeroHermanos = 3
        salariosPadres = 3000
        tieneBeneficio = False

        if (distancia > 1000 and numeroHermanos > 2) or salariosPadres < 2000:
            tieneBeneficio = True
        print(not tieneBeneficio)

    def SegundoEjercicio(self):
        if (5 > 3) or (8 < 6):
            print("Verdad")
        else:
            print("Es mentira...")