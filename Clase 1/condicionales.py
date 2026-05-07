#Condicionales
#en python el espaciado importa (identación)

if 10 > 5:
    print("Hola")
elif 30 == 30:
    print("si son iguales")
else:
    print("no se cumple la condicion del if")



is_student = False

student = input("¿Sos estudiante? S/N: ")

if student == "S":
    is_student = True
elif student == "N":
    is_student = False
else:
    print("Opcion invalida")   

age = int(input("ingrese tu edad: "))

#AND: todas las condiciones tienen que cumplirse para que devuelva el true
#OR: que al menos una de las condiciones debe cumplirse para que devuelva el true

if age >= 18 and is_student == True:
    print("sos mayor de edad")
else:
    print("No sos mayor de edad")