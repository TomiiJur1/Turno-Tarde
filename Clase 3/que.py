my_list = ["uno", "dos", "tres"]


def funcion_a(list_a):
    new_list = list_a.copy() #creamos una nueva lista a partir de la original para no modificarla
    new_list.append("cuatro")
    print("Mem de newlist: ", {id(new_list)})

funcion_a(my_list)

print(f"Mem de list_a: {id(my_list)}")
print(my_list)

#no conozco la cantidad de parametros

def sumatoria(*args):
    result = 0
    for number in args:
        result += number
    print(result)

num1 = int(input("Ingrese un numero: "))

sumatoria(num1)