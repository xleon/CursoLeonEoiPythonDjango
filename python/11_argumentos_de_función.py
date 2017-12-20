"""
Diferentes maneras de usar argumentos
"""

# argumentos posicionales obligatorios
def hi(name):
    print('Hi', name)

# hi() # esto falla porque "name" es obligatorio

# valores por defecto de argumento
def f(n='uno'):
    print(n)

f()

def f2(one, two, three=3):
    print('one:', one, ', two:', two, ', three:', three)

# usar argumentos por orden
f2(45, 10, 22)

# usar argumentos como keywords
f2(three=89, two=90, one=23)

def dime_cosas(*args):
    print(args)

dime_cosas(20, 30, 90, True, False, 'hola')

def f3(name, *args):
    print('hola', name)
    print(args)

f3('Pedro', 20, 30, 90, True, False, 'hola')

t = ('Pedro', 20, 30, 90, True, False, 'hola')
f3('Diego', *t)

def f4(**kwars):
    print(kwars)

f4(c='uno', b='tres', a='manolo', f=True)

o = {'c':'uno', 'b':'tres', 'a':'manolo', 'f':True}
f4(**o)