#hacer calculadora que: pida que ingrese los numeros y que operación quiere hacer. Luego que pregunte si quiere seguir haciendo cuentas

print("CALCULADORA")

print("empezar? (s/n) :")
option = input()

while option == "s" or option == "S":
    print("Ingrese el primer numero: ")
    num1 = float(input())

    print("Ingrese que operacion quiere hacer (+, -, *, /) :")
    operacion = input()

    print("Ingrese el segundo numero: ")
    num2 = float(input())

    if operacion == "+":
        print("El resultado es: ", num1 + num2)
    elif operacion == "-":
        print("El resultado es: ", num1 - num2)
    elif operacion == "*":
        print("El resultado es: ", num1 * num2)
    elif operacion == "/":
        if num2 != 0:
            print("El resultado es: ", num1 / num2)
        else:
            print("No se puede dividir por cero")

    print("¿Quiere seguir haciendo cuentas? (s/n): ")
    option = input()

    if option == "s" or option == "S":
        continue
    else:
        print("Adios!")