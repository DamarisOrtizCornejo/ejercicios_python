import os
from E4_Numeros_Operaciones import OperacionesconNumeros
from E5_Concatenacion import Concatenacion
from E6_Cadenas import Cadena
# import E7_Tuplas
# import E8_Listas
# import E9_Diccionarios
from E11_If_Else import Sentencia
from E12_Funciones import Funciones
from E13_OperadoresLogicos import OperadoresLogicos
from E14_OperadorTernario import OperadoresTernarios
from E15_Range import Range
from E16_For import For
from E17_If_in import If
from E18_Factorial import Factorial
from E19_While import While
from E20_Break_Continue_Pass import Instruccion
from E21_Generadores import Generador
from E22_Generadores2 import Generadores2
from E23_Excepciones import Excepciones
from E24_Raise import Raise
from Paquete1.FuncionesCadenas import contarLetras
# from Paquete1.FuncionesNumericas import *
from modulos.funcionesMatematicas import *
from POO.Persona import Personas
from POO.Curso import Curso
from POO.Cuenta import Cuenta
from POO.Herencia import *
from POO.HerenciaMultiple import *
from POO.Polimorfismos import *
from POO.RelacionesClases import *





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
    os.system("cls")
    if opc == "1":
        opc = ""
        os.system("cls")
        # numeros = ()
        print("Hola Mundo")
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "2":
        opc2 = ""
        #numeros = ()
        print("VARIABLES")
        print("Damaris Ortiz")
        print("25")
        print("True")
        print("205.10")
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "3":
        opc3 = ""
        #numeros = ()
        print("CONVERSIONES")
        numero1 = "35"
        numero2 = "18"
        print("numero1 + numero2")
        num1 = int(numero1)
        num2 = int(numero2)
        print(num1 + num2)
        sueldo = 1200.43
        sueldoEntero = int(sueldo)
        print(sueldoEntero)
        valor = "4500.89"
        valorDecimal = float(valor)
        print(valorDecimal * 3)
        edad = 100
        print(len(str(edad)))
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "4":
        opc4 = ""
        numOpe = OperacionesconNumeros()
        while opc4 != "7":
            os.system("cls")
            men4 = Menu("Menu Operaciones con Números",["1) Suma", "2) Resta", "3) Multiplicación", "4) División", "5) División Exacta", "6) Potencia","7) Salir"])
            opc4 = men4.menu()
            os.system("cls")

            if opc4 == "1":
                print("SUMA")
                num1 = int(input("Ingrese primer número: "))
                num2 = int(input("Ingrese segundo número: "))
                numOpe.Suma(num1,num2)
                input("Presione una tecla para continuar...")

            elif opc4 == "2":
                print("RESTA")
                num1 = int(input("Ingrese primer número: "))
                num2 = int(input("Ingrese segundo número: "))
                numOpe.Resta(num1, num2)
                input("Presione una tecla para continuar...")

            elif opc4 == "3":
                print("MULTIPLICACIÓN")
                num1 = int(input("Ingrese primer número: "))
                num2 = int(input("Ingrese segundo número: "))
                numOpe.Multiplicación(num1, num2)
                input("Presione una tecla para continuar...")

            elif opc4 == "4":
                print("DIVISIÓN")
                num1 = int(input("Ingrese primer número: "))
                num2 = int(input("Ingrese segundo número: "))
                numOpe.División(num1, num2)
                input("Presione una tecla para continuar...")

            elif opc4 == "5":
                print("DIVISIÓN EXACTA")
                num1 = int(input("Ingrese primer número: "))
                num2 = int(input("Ingrese segundo número: "))
                numOpe.DivisiónExacta(num1, num2)
                input("Presione una tecla para continuar...")
                os.system("cls")

            elif opc4 == "6":
                print("POTENCIA")
                num1 = int(input("Ingrese primer número: "))
                num2 = int(input("Ingrese segundo número: "))
                numOpe.Potencia(num1, num2)
                input("Presione una tecla para continuar...")
                os.system("cls")

    elif opc == "5":
        opc5 = ""
        conca = Concatenacion()
        print("CONCATENACIÓN")
        palabra1 = input("Ingrese una frase: ")
        palabra2 = input("Ingrese una frase: ")
        conca.concatenar(palabra1,palabra2)
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "6":
        opc6 = ""
        cad = Cadena()
        while opc6 != "9":
            os.system("cls")
            men6 = Menu("Menu Cadenas",["1) Lower", "2) Upper", "3) Title", "4) Find", "5) Count", "6) Replace","7) Isnumeric","8) Split","9) Salir"])
            opc6 = men6.menu()
            os.system("cls")

            if opc6 == "1":
                print("LOWER")
                frase = input("Ingrese una frase: ")
                cad.lower(frase)
                input("Presione una tecla para continuar...")

            elif opc6 == "2":
                print("UPPER")
                frase = input("Ingrese una frase: ")
                cad.upper(frase)
                input("Presione una tecla para continuar...")

            elif opc6 == "3":
                print("TITLE")
                frase = input("Ingrese una frase: ")
                cad.title(frase)
                input("Presione una tecla para continuar...")

            elif opc6 == "4":
                print("FIND")
                frase = input("Ingrese una frase: ")
                cad.find(frase)
                input("Presione una tecla para continuar...")

            elif opc6 == "5":
                print("COUNT")
                frase = input("Ingrese una frase: ")
                cad.count(frase)
                input("Presione una tecla para continuar...")
                os.system("cls")

            elif opc6 == "6":
                print("REPLACE")
                frase = input("Ingrese una frase: ")
                cad.replace(frase)
                input("Presione una tecla para continuar...")
                os.system("cls")

            elif opc6 == "7":
                print("ISNUMERIC")
                frase = input("Ingrese una frase: ")
                cad.isnumeric(frase)
                input("Presione una tecla para continuar...")
                os.system("cls")

            elif opc6 == "8":
                print("SPLIT")
                frase = input("Ingrese una frase: ")
                cad.split(frase)
                input("Presione una tecla para continuar...")
                os.system("cls")

    elif opc == "7":
        opc7 = ""
        print("TUPLAS")
        tupla2 = (7, "Oscar", True, 450.1, 16 + 7j, 15, "Felicidad", False)
        print(tupla2)
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "8":
        opc8 = ""
        print("LISTAS")
        lista1 = ["Damaris", 25, 98.3, True, "Angel", 56.3]
        print(lista1)
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "9":
        opc9 = ""
        print("Diccionarios")
        miDiccionarios = {"España": "Madrid", "Ecuador": "Quito", "Alemania": "Berlin"}
        print(miDiccionarios)
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "10":
        opc10 = ""
        print("INGRESO DE DATOS")
        nombre = input("Ingrse su nombre: ")
        edad = int(input("Ingrse su edad: "))
        sueldo = int(input("Ingrese sueldo: "))
        print("Hola, " + nombre)
        edadFutura = edad + 20
        print("Tu edad es:", edad)
        print("Tu edad (dentro de 20 años) sera:", edadFutura)
        print("Tu sueldo es:", sueldo)
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "11":
        opc11 = ""
        cond = Sentencia()
        print("CONDICIONALES")
        edad = int(input("Ingrese su edad: "))
        cond.condicionales(edad)
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "12":
        opc12 = ""
        fun = Funciones()
        while opc12 != "3":
            os.system("cls")
            men12 = Menu("Menu Funciones",["1) Saludar", "2) Sueldo", "3) Salir"])
            opc12 = men12.menu()
            os.system("cls")

            if opc12 == "1":
                print("SALUDAR")
                saludo = input("Ingrese saludo: ")
                print(saludo)
                input("Presione una tecla para continuar...")

            elif opc12 == "2":
                print("SUELDO MÍNIMO")
                sueldo = int(input("Ingrese primer número: "))
                fun.evaluarSueldoMinimo(sueldo)
                input("Presione una tecla para continuar...")

    elif opc == "13":
        opc13 = ""
        oplo = OperadoresLogicos()
        while opc13 != "3":
            os.system("cls")
            men13 = Menu("Menu Operadores Lógicos", ["1) Primer Ejercicio", "2) Segundo Ejercicio", "3) Salir"])
            opc13 = men13.menu()
            os.system("cls")

            if opc13 == "1":
                print("PRIMER EJERCICIO")
                print(oplo.PrimerEjercicio())
                input("Presione una tecla para continuar...")

            elif opc13 == "2":
                print("SEGUNDO EJERCICIO")
                print(oplo.SegundoEjercicio())
                input("Presione una tecla para continuar...")

    elif opc == "14":
        opc14 = ""
        opter = OperadoresTernarios()
        print("OPERADORES TERNARIOS")
        print(opter.OperadorTernario())
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "15":
        opc15 = ""
        ran = Range()
        print("RANGE")
        print(ran.Range())
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "16":
        opc16 = ""
        sen = For()
        while opc16 != "3":
            os.system("cls")
            men16 = Menu("Menu Funciones", ["1) Primer Ejercicio", "2) Segundo Ejercicio", "3) Salir"])
            opc16 = men16.menu()
            os.system("cls")

            if opc16 == "1":
                print("PRIMER EJERCICIO")
                print(sen.primer())
                input("Presione una tecla para continuar...")

            elif opc16 == "2":
                print("SEGUNDO EJERCICIO")
                print(sen.segundo())
                input("Presione una tecla para continuar...")

    elif opc == "17":
        opc17 = ""
        cond = If()
        print("IF_IN")
        curso = input("Ingrese un curso: ")
        cond.sentencia(curso)
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "18":
        opc18 = ""
        fac = Factorial()
        print("FACTORIAL")
        numero = int(input("Ingrese un número: "))
        fac.Factorial(numero)
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "19":
        opc19 = ""
        ini = While()
        print("WHILE")
        inicio = int(input("Ingrese un número: "))
        ini.While(inicio)
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "20":
        opc20 = ""
        ins = Instruccion()
        while opc20 != "4":
            os.system("cls")
            men20 = Menu("Menu Funciones", ["1) Break", "2) Continue", "3) Pass", "4) Salir"])
            opc20 = men20.menu()
            os.system("cls")

            if opc20 == "1":
                print("BREAK")
                print(ins.Break())
                input("Presione una tecla para continuar...")

            elif opc20 == "2":
                print("CONTINUE")
                print(ins.Continue())
                input("Presione una tecla para continuar...")

            elif opc20 == "3":
                print("PASS")
                print(ins.Pass())
                input("Presione una tecla para continuar...")

    elif opc == "21":
        opc21 = ""
        gen = Generador()
        print("GENERADORES")
        numero = int(input("Ingrese un número: "))
        limite = int(input("Ingrese un límite: "))
        gen.generarMultiplos7(numero,limite)
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "22":
        opc22 = ""
        gen2 = Generadores2()
        print("GENERADORES 2")
        gen2.devuelveLenguajes()
        lenguajesObtenidos = gen2.devuelveLenguajes("Python", "Java", "PHP", "Ruby", "JavaScript")
        print(next(lenguajesObtenidos))
        print(next(lenguajesObtenidos))
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "23":
        opc23 = ""
        excep = Excepciones()
        print("EXCEPCIONES")
        numero1 = int(input("Ingrese un número: "))
        numero2 = int(input("Ingrese un número: "))
        excep.excepcion(numero1,numero2)
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "24":
        opc24 = ""
        rai = Raise()
        print("RAISE")
        nota = int(input("Ingrese una nota: "))
        rai.Raise(nota)
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "25":
        opc25 = ""
        print("MODULOS")
        print(sumar(5, 6))
        print(multiplicar(5, 6))
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "26":
        opc26 = ""
        print("PAQUETE")
        print(multiplicar(5, 6))
        print(contarLetras("Damaris Ortiz"))
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "27":
        opc27 = ""
        per = Personas()
        print("POO")
        per.despertar()
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "28":
        opc28 = ""
        cur = Curso("Estructura","3","Ingeniera")
        print("MOSTRAR DATOS")
        nom = input("Ingrese nombre: ")
        cre = input("Ingrese créditos: ")
        pro = input("Ingrese profesión: ")
        print(cur.mostrarDatos())
        input("Presione una tecla para continuar...")
        os.system("cls")


    elif opc == "29":
        opc29 = ""
        cuenta1 = Cuenta("Damaris",500,"Dólar")
        print("CUENTA")
        print(cuenta1.get_Saldo())
        print(cuenta1.get_Moneda())
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "30":
        opc30 = ""
        per1 = Persona("Ortiz", "Cornejo", "Damaris")
        estu1 = Estudiante()
        print("HERENCIA")
        print(per1.mostrarNombreCompleto())
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "31":
        opc31 = ""
        hermul = ClaseA(3,4)
        print("HERENCIA MULTIPLE")
        print(hermul)
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "32":
        opc32 = ""
        poli = Trabajador()
        print("POLIMORFISMO")
        poli.describir()
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "33":
        opc33 = ""
        urba1 = ()
        ciudad1= ()
        print("RELACIONES DE CLASES")
        urba1 = Urbanizacion("Victoria del Rio", ciudad1)
        print(urba1)
        input("Presione una tecla para continuar...")
        os.system("cls")

    elif opc == "34":
            print("Gracias por usar el sistema ")
    else:
            print("Opcion no valida")

print("Lo esperamos en una proxima ocasion")


