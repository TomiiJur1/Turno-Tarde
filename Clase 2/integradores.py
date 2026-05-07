import time
#for - while
#for (i = 0; i < 10; i++) -> así era en c
#cuando pasa un parametro se considera el valor final
#con dos parametros se considera el valor inicial y el valor final
#con 3 parametros se considera el valor inicial, el valor final y el incremento

for counter in range(10, 0, -5):    #si pongo -1 en el tercer valor va a contar hacia atrás
    print(counter)
    time.sleep(1)
print("BOOOOOOOOOOOOOMMM!!!")

my_list = ["lalalala", "lelelele", "lililili", "lolololo"]

#vamos a ir literando por cada elemento de la lista, lo vamos guardando en element

for element in my_list:
    print(element, end=" ") #end -> es un parametro que le indica a print que no haga un salto de linea, sino que termine con el valor que le indiquemos

for counter in range(len(my_list)): #len -> es una función que devuelve la cantidad de elementos que tiene una lista, un string, etc...
    print(my_list[counter])

#interrumpir un ciclo
for counter in range(10):
    print(counter)
    if counter == 5:
        break #break -> interrumpe el ciclo


#while para cuando no conozco la cantidad de literaciones 

conter = 0
while conter < 10:
    if conter == 6:
        conter += 1 #pongo += 1 para que el contador vaya aumentando en 1 cada vez que se ejecute el ciclo, sino sería un ciclo infinito.
        continue #continue -> salta a la siguiente iteración del ciclo, es decir, no ejecuta el código que está debajo de continue en esa iteración, pero sigue con la siguiente iteración del ciclo.
    print(conter)
    conter += 1

student_list = []
option = input("Quiere ingresar una persona? (s/n): ")

while option == "s" or option == "S":
    name = input("Ingrese su nombre: ")
    student_list.append(name)
    option = input("Quiere ingresar otra persona? (s/n): ")
else:
    print("Adios!")