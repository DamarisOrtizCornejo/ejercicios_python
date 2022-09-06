import os

class Menu:
    def __init__(self,titulo,opciones=[]):
        self.titulo=titulo
        self.opciones=opciones
    def menu(self):
        print(self.titulo)
        for opcion in self.opciones:
            print(opcion)
        opc=input("Elija opcion[1...{}]:".format(len(self.opciones)))
        return opc

opc =""
while opc !="34":
    os.system("cls")
    men = Menu("Menu Operaciones",["1) Hola Mundo","2) Variables","3) Conversiones","4) Números y Operaciones Matemáticas ","5) Concatenación","6) Funciones de Cadena","7) Tuplas","8) Listas","9) Diccionarios","10) Lectura de Datos","11) Estructura Condicional","12) Funciones","13) Operadores Lógicos","14) Operadores Ternarios","15) Funcion Range","16) Bucle For","17) If con Tuplas y Listas","18) Factorial de un Número","19) Bucle While","20) Sentencia Break, Continue y Pass","21) Generadores","22) Generadores 2","23) Excepciones","24) Sentencia Raise","25) Módulos","26) Paquetes","27) POO","28) Curso y __str__","29) Método Accesores","30) Herencia, Sobreescritura de Método y Principio de Sustitución","31) Herencia Múltiple","32) Polimorfismo","33) Relaciones entre Clases","34) Salir"])
    opc = men.menu()
    if opc == "1":
        opc1 =""
        numeros = ()
        while opc1 !="7":
            os.system("cls")
            men1 = Menu("\033[3;36m"+"Menu Listas",["\033[0;33m"+"1) Push","2) Pop","3) Show","4) Eliminar","5) Insertar","6) Buscar","7) Salir"])
            opc1 = men1.menu()
            os.system("cls")

            if opc1 == "1":
                print("PUSH")
                dato = input("Ingrese un dato a la Lista: ")
                numeros.push(dato)
                print(numeros.lista)
                input("Presione una tecla para continuar...")
                os.system("cls")

            elif opc1 == "2":
                print("POP")
                dato = numeros.pop()
                if dato: print("El dato eliminado es: {}".format(dato))
                else: print("La lista esta vacia")
                input("Presione una tecla para continuar...")

            elif opc1 == "3":
                print("SHOW")
                numeros.mostrar()
                input("Presione una tecla para continuar...")

            elif opc1 == "4":
                print("ELIMINAR")
                dato = int(input("Ingrese la posicion del valor ha eliminar: "))
                numeros.eliminarElemento(dato)
                print(numeros.lista)
                input("Presione una tecla para continuar...")

            elif opc1 == "5":
                print("INSERTAR")
                pos = int(input(("Ingrese la posicion en la que desea insertar el valor: ")))
                valor = input("Ingrese el dato a insertar en la Lista: ")
                numeros.insertarElemento(pos,valor)
                print(numeros.lista)
                input("Presione una tecla para continuar...")

            elif opc1 == "6":
                print("BUSCAR")
                dato = input("Ingrese el dato que desea buscar: ")
                print(numeros.buscar(dato))
                input("Presione una tecla para continuar...")

    elif opc =="2":
        opc2 =""
        pila1 = ()
        while opc2 !="6":
            os.system("cls")
            men2 = Menu("\033[3;36m"+"Menu Pilas",["\033[0;33m"+"1) Push","2) Pop","3) Show","4) Buscar","5) Longitud","6) Salir"])
            opc2 = men2.menu()
            os.system("cls")

            if opc2 == "1":
                print("PUSH")
                dato = input("Ingrese un dato a la Pila: ")
                pila1.push(dato)
                print(pila1.lista)
                input("Presione una tecla para continuar...")

            elif opc2 == "2":
                print("POP")
                dato = pila1.pop()
                if dato: print("El dato eliminado es: {}".format(dato))
                else: print("La pila esta vacia")
                input("Presione una tecla para continuar...")

            elif opc2 == "3":
                print("SHOW")
                print(pila1.show())
                input("Presione una tecla para continuar...")

            elif opc2 == "4":
                print("BUSCAR")
                buscar = input("Ingresar el valor a buscar: ")
                print(pila1.buscar(buscar))
                input("Presione una tecla para continuar...")

            elif opc2 == "5":
                print("LONGITUD")
                print(pila1.longitud())
                input("Presione una tecla para continuar...")

    elif opc == "3":
        opc3 =""
        cola1 = ()
        while opc3 !="6":
            os.system("cls")
            men3 = Menu("\033[3;36m"+"Menu Colas",["\033[0;33m"+"1) Push","2) Pop","3) Show","4) Buscar","5) Longitud","6) Salir"])
            opc3 = men3.menu()
            os.system("cls")

            if opc3 == "1":
                print("PUSH")
                dato = input("Ingrese el dato a encolar: ")
                cola1.push(dato)
                print(cola1.cola)
                input("Presione una tecla para continuar...")

            elif opc3 == "2":
                print("POP")
                dato = cola1.pop()
                if dato: print("El dato eliminado es: {}".format(dato))
                else: print("La cola esta vacia")
                input("Presione una tecla para continuar...")

            elif opc3 == "3":
                print("SHOW")
                cola1.show()
                input("Presione una tecla para continuar...")

            elif opc3 == "4":
                print("BUSCAR")
                buscar = input("Ingresar el valor a buscar: ")
                print(cola1.buscar(buscar))
                input("Presione una tecla para continuar...")

            elif opc3 == "5":
                print("LONGITUD")
                print(cola1.longitud())
                input("Presione una tecla para continuar...")

    elif opc == "4":
            print("Gracias por usar el sistema ")
    else:
            print("Opcion no valida")

print("Lo esperamos en una proxima ocasion")


