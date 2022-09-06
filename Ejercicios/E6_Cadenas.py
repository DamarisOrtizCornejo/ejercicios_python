# texto = "Bienvenidos a mis ejercicios"
#
# print(texto)
# print(texto.lower()) #Pone todas las letras en minuscula
# print(texto.upper()) #Pone todas las letras en mayuscula
# print(texto.title()) #Convierte el comienzo de cada palabra en mayuscula
# print(texto.find("a")) #Posicion donde encuentra la cadena o porcion
# print(texto.count("e")) #Cantidad de ocurrencias de una letra o porcion.
#
# textoFinal = texto.replace("e", "3") #Reemplazar caracteres
# print(textoFinal)
#
# valor = texto.isnumeric() #Arroja True o False dependiendo si es un número.
# print(valor)
#
# cadenaSeparada = texto.split(" ") #Separar un valor o parametro
# print(cadenaSeparada)

class Cadena:
    def lower(self,frase):
        palabra = frase.lower()
        print(palabra)

    def upper(self,frase):
        palabra = frase.upper()
        print(palabra)

    def title(self,frase):
        palabra = frase.title()
        print(palabra)

    def find(self,frase):
        palabra = frase.find("a")
        print(palabra)

    def count(self,frase):
        palabra = frase.count("o")
        print(palabra)

    def replace(self,frase):
        palabra = frase.replace("e","3")
        print(palabra)

    def isnumeric(self,frase):
        palabra = frase.isnumeric()
        print(palabra)

    def split(self,frase):
        palabra = frase.split(" ")
        print(palabra)