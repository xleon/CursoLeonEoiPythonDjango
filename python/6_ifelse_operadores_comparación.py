"""
Operadores de comparación
"""

a = 21
b = 10
c = 0

if a == b:
    print('a == b')
else:
    print('a no es igual a b')

if a != b:
    print('a no es igual a b')
else:
    print('a es igual a b')

print(a < b)
print(a > b)

if a <= b:
    print('a es menor o igual que b')
else:
    print('a no es menor o igual que b')

print(a >= b)

print(a is b)
print(a is a)
print(a is not b)