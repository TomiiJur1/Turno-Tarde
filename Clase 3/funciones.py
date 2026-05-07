#funciones -> bloque de codigo que realiza una tarea especifica
#a una funcion le podemos pasar valores -> parametros, argumentos

def nombre_funcion(num1 = 0, num2 = 0):
    print(f"El valor de num1 es: {num1}")
    print(f"El valor de num2 es: {num2}")
    result = num1 + num2
    return result

print(nombre_funcion(12, 34))

my_list = ["primero", "segundo", "tercero"]

for element in my_list:
    print(element, end=" ")



def my_func(element):
    my_list = []
    my_list.append(element)
    print(my_list)

my_func("Uno")
my_func("Dos")

#alcance de las variables

my_var = 10

def new_funcion():
    global my_var #con esta palabra le decimos que queremos usar la variable global y no crear una nueva variable local
    my_var = 20 #esto es una variable local y solo existe en el bloque de codigo de la funcion
    print(my_var)

new_funcion()
print(my_var)