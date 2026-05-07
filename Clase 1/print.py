number_1 = int(input("Ingresa el primer numero: "))
number_2 = int(input("Ingresa el segundo numero: "))

print(type(number_1))

result = number_1 + number_2
print(result)

print(f'El resultado de la "suma" {number_1} y {number_2} es {result} ')

"""comparadores > mayor
                < menor
                <= menor o igual
                >= mayor o igual
                == igual
                != distinto
"""

mayor = number_1 > number_2

print(f"el valor de mayor: {mayor} el tipo es {type(mayor)}")

#python es case sensitive, (diferente entre mayusculas y minusculas)
