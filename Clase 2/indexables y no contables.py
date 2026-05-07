#string indexables y no contables
#indexable = puede acceder a cada caracter a partir de su index -> izquierda a derecha 0, 1, 2, 3, 4
#                                                               -> derecha a izquierda -4, -3, -2, -1

word = "Hola clase"

#word[1] = "T" #no mutable

print(word[-1])

#slicing
#inicio -> inclusive
#final -> exclusive

print(word[0:4])
print(word[:6])
print(word[1:])
