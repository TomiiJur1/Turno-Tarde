#comentario de una sola linea

"""
comentario de multiples lineas
otra linea
"""

#python es un lenguaje interpretado, es un lenguaje multiparadigma -> estructurado
#                                                                  -> funcional
#                                                                  -> orientado a objetos 
#es de tipado dinamico

#Data types
CONSTANT = 10 #constante no cambia en tiempo de ejecucion
number = 5 #variable de tipo entero
word = "Hola" #variable de tipo string
decimal = 3.14 #variable de tipo float
boolean = True #variable de tipo booleano

print("Esta es la clase de programacion II")
print("El valo de numero es: ", number) #esta nose puede usar

#3 formatos para cancatenar textos
print("El valor de number es: %d, el valor de word: %s" % (number, word)) #formato antiguo
print("El valor de number es: {1} el valor de word es: {0}".format(number, word)) #formato moderno
print(f"El valor de number es: {number} el valor de word es: {word}") #formato f-string
