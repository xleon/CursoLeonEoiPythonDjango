"""
Ejemplos para trabajar con tuplas
"""

TUP = (1, 2, 3, 4, 5, "seis")

print(TUP)
print(TUP[0])
print(TUP[4])
print(TUP[2:5])
print(TUP[:3])
print(TUP[2:])

size = len(TUP)
print('tamaño de la tupla:', size)

# concatenar dos tuplas
TUP += ('siete', 8, True, False)
print(TUP)

SUMA = (3 + 2) - 1

T2 = (3,) # tupla de un solo elemento
print(T2)
print(type(T2))
