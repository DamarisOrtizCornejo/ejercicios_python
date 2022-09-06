# Cuando indicamos un * adelante del parametro de una funcion,
# estamos indicando que se va a recibir un numero indeterminado
# de parametros. Ademas, esos parametros se recibiran en forma de tupla.


"""
def devuelveLenguajes(*lenguajes):
    for leng in lenguajes:
        yield leng
"""
"""
def devuelveLenguajes(*lenguajes):
    for leng in lenguajes:
        for letra in leng:
            yield letra

lenguajesObtenidos = devuelveLenguajes("Python", "Java", "PHP", "Ruby", "JavaScript")

print(next(lenguajesObtenidos))
print(next(lenguajesObtenidos))
"""

class Generadores2:

    def devuelveLenguajes(*lenguajes):
        for leng in lenguajes:
            yield leng

    lenguajesObtenidos = devuelveLenguajes("Python", "Java", "PHP", "Ruby", "JavaScript")

    # print(next(lenguajesObtenidos))
    # print(next(lenguajesObtenidos))