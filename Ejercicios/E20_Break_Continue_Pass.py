# Break: Permite salir de un bucle cuando se cumple una condicion.

"""
for numero in range(1, 6):
    if numero == 3:
        break #Descanso o interrupcion en este punto.
    print("El numero es: {0}".format(numero))

print("Bucle terminado.")
"""

# Continue: Omite una parte del bucle cuando se cumple una condicion y
# continua con el resto.

""" 
for numero in range(1, 6):
    if numero == 3:
        continue # Continua con el resto del bucle.
    print("El numero es: {0}".format(numero))

print("Bucle terminado.")
"""

# Pass: Permite continuar con una sentencia o funcion que ya no tiene
# o segun no tiene un bloque de codigo util.

"""
    for numero in range(1, 6):
    if numero == 3:
        #Aqui no pasa nada y el bucle sigue trabajando.
        pass
    else:
        print("El siguiente valor es mayor a 3:")
    print("El numero es: {0}".format(numero))

print("Bucle terminado.")

def funcionSinImplementar():
    pass
"""
class Instruccion:
    def Break(self):
        for numero in range(1, 6):
            if numero == 3:
                break  # Descanso o interrupcion en este punto.
            print("El numero es: {0}".format(numero))
        print("Bucle terminado.")

    def Continue(self):
        for numero in range(1, 6):
            if numero == 3:
                continue  # Continua con el resto del bucle.
            print("El numero es: {0}".format(numero))
        print("Bucle terminado.")

    def Pass(self):
        for numero in range(1, 6):
            if numero == 3:
                # Aqui no pasa nada y el bucle sigue trabajando.
                pass
            else:
                print("El siguiente valor es mayor a 3:")
            print("El numero es: {0}".format(numero))
        print("Bucle terminado.")
