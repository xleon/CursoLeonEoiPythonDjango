"""
Ejemplos de funciones simples
"""

def hi():
    print('hola')

hi()

def hi_to(name):
    print('Hi', name)

hi_to('Ramón')

def add_name(name_list, name):
    name_list.append(name)
    print(name_list)

l = ['Patricia', 'Maria']
add_name(l, 'Carlota')

# modificar argumento dentro de la función
def talk(word):
    word = 'cambio'
    print(word)

talk('hola')
