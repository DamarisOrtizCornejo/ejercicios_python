# Diccionarios: Son estructuras de datos que permiten almacenar
# distintos valores.

# Es que los datos almacenan asociados a una clave unica, tenemos una relacion
# clave:valor

# Los elementos almacenados estan en desorden, el orden es indiferente a la forma
# de almacenamiento.

miDiccionarios = {"España":"Madrid", "Ecuador":"Quito", "Alemania":"Berlin"}
print(miDiccionarios["Ecuador"])
print(miDiccionarios)

miDiccionarios["Venezuela"] = "Caracas" #añade un elemento
print(miDiccionarios)

miDiccionarios["España"] = "Barcelona"
print(miDiccionarios)

del miDiccionarios["España"] # del: Borra un elemento (delete)
print(miDiccionarios)

dic2={"Ortiz":"Damaris", 20: True, "Sueldo": 150.80}
print(dic2[20])

llaves=("España","Francia","Inglaterra")
dicPaises = {llaves[0]:"Madrid", llaves[1]:"Paris", llaves[2]:"Londres"}
print(dicPaises)

datosPersonales={"Apellido":"Ortiz","Años":{1:2010, 2:2011, 3:2012, 4:2013, 5: 2014}}
print(datosPersonales)
print(datosPersonales["Años"])

print(datosPersonales.get('Apellido', "Angel"))

print(datosPersonales.keys())

valores=list(datosPersonales.values())
print(valores)

valores=tuple(datosPersonales.values())
print(valores)