# Excepcion: Error en tiempo de ejecucion (durante la ejecucion de un programa).

"""
numero1 = 20
numero2 = 0

print("La division de {0} entre {1} es: {2}".format(numero1, numero2, (numero1 / numero2)))

try:
    resultado = numero1 / numero2
# except:
except ZeroDivisionError:
    print("No se puede dividir entre 0...")
finally:
    print("Yo siempre aparezco.")

print("Aqui termina el programa.")
"""
class Excepciones:
    def excepcion(self,numero1,numero2):
        try:
            resultado = numero1 / numero2
        # except:
        except ZeroDivisionError:
            print("No se puede dividir entre 0...")
        finally:
            print("Yo siempre aparezco.")
        print("Aqui termina el programa.")