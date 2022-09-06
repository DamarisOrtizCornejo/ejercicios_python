# Factorial: Es el producto de todos los numeros positivos enteros comprendidos entr 1 y un determinado numero

# Factorial de 5: 1 * 2 * 3 * 4 * 5 = 120
# Factorial de 4: 1 * 2 * 3 * 4 = 24

# numero = int(input("Ingrese un número: "))
#
# factorial = 1
# for n in range(1, (numero + 1)):
#     factorial = factorial * n
#
# print("El factorial de {0} es: {1}".format(numero, factorial))

class Factorial:
    def Factorial(self,numero):
        factorial = 1
        for n in range(1, (numero + 1)):
            factorial = factorial * n
        print("El factorial de {0} es: {1}".format(numero, factorial))