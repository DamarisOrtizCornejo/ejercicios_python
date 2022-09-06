# Listas: Son estructuras de datos que nos permiten almacenar distintos valores
# (equivalentes a los arrays en otros lenguajes de programacion

#Son estructuras dinamicas, pueden MUTAR

lista1 = ["Damaris", 25, 98.3, True, "Angel", 56.3]
print(lista1)
print(lista1[:]) # Toda la lista
print(lista1[2]) # Posicion 2
print(lista1[-1]) # Primera posicion de atras hacia adelante

print(lista1[0:3])
print(lista1[:2])
print(lista1[3:])

lista1.append("Damaris Ortiz")
print(lista1)

lista1.insert(4,"Ecuador")
print(lista1)

lista1.extend(["Lizbeth", 110, False])
print(lista1)

print(lista1.index("Angel"))

lista1.remove(56.3)
print(lista1)

lista1.pop() # Elimina el ultimo elemento de la lista
print(lista1)

lista2 = ["Durán", "Jhon"]
lista3 = lista1 + lista2
print(lista3)

print(lista2*4)

print("Damaris Ortiz" in lista1)