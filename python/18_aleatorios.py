"""
Generando números aleatorios
"""

import random

for n in range(10):
    print('entero aleatorio:', random.randint(10, 20))

# números aleatorios entre 0 y 1
for n in range(4):
    print(random.random())

L = ['oscar', 'lucia', 'jaime', 'pepe', 'cris', 'yolanda', 'taimi']

# elemento aleatorio de una lista
for n in range(8):
    print(random.choice(L))

# elementos aleatorios de una lista (pueden llegar repetidos)
r = random.choices(L, k=3) # k es el número de elementos que queremos
print(r)

# cambiar orden de elementos de una lista, de forma aleatoria
random.shuffle(L)
print(L)
random.shuffle(L)
print(L)

# a partir de una lista, crear otra con k elementos que no estén repetidos
print(random.sample(L, k=2))
print(random.sample(L, k=2))
print(random.sample(L, k=2))
print(random.sample(L, k=2))
print(random.sample(L, k=2))
print(random.sample(L, k=2))
print(random.sample(L, k=2))
print(random.sample(L, k=2))