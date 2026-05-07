#listas -> ordenada, indexada, mutable

#sintaxis
my_list = [1, 200, "texto", [1,40, [5, 7, 23],3], True, 219, "texto"]

print(my_list[3][2][2])

#slicing

print(my_list[1:4])

print(my_list[0:4])
my_list[0] = "Nuevo valor"
print(my_list)

#Agregar elementos a una lista
number = 4567
my_list.append(number) #append -> agrega al final de la lista
print(my_list)

my_list.insert(1, "Artemis II") #insert -> agrega en la posicion que le indiquemos
print(my_list)

#Eliminar elementos de una lista
my_list.pop() #pop -> elimina el último elemento
print(my_list)

my_list.pop(2) #pop() -> elimina el elemento en la posicion que le indiquemos
print(my_list)

my_list.remove("texto") #remove -> elimina la primera ocurrencia del elemento que le indiquemos
print(my_list)