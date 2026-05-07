#Tuplas

coordenadas = (1.347, 6.2345)

print(f"Latitud: {coordenadas [0]} y longitud: {coordenadas[1]} ")

dimension = 40, 30, 20

alto, ancho, profundo = dimension

print(type(dimension))

print(f"La dimension es: alto={alto} * ancho={ancho} * profundo={profundo}")


#diccionarios

#está compuesta por una clave : valor
#la clave no puede estar repetida
#el value puede ser cualquier tipo de dato
#accedemos al valor de una key a traves de su key#

elementos = {"Litium" : 1, "Helio" : 2, "Plata" : 3}

elementos["Helio"] = 4

print(f"El numero atomico del Litio es: {elementos['Litium']}")
print(elementos)

elementos_mejorado = {"Litium" : {"numero" : 1, "peso" : 2.324, "simbolo" : "Li"}, "Helio" : {"numero" : 2, "peso" : 5.243, "simbolo" : "He"}, "Plata" : {"numero" : 3, "peso" : 9.234, "simbolo" : "Ag"}}

print(elementos_mejorado)

#agregar elementos a un diccionario

oxigeno = {"numero" : 6, "peso" : 2.453, "simbolo" : "O"}
elementos_mejorado["Oxigeno"] = oxigeno

print(elementos_mejorado)


#conjuntos
my_list = [1, 6, 7, 2, 1, 1, 8, 2, 4, 0]
my_new_list = set(my_list)

print(my_new_list)

my_set = set()

my_set1 = {1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9}

print(my_set1)