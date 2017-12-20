"""
Trabajando con clases y POO
"""

class Thing:
    pass

thing = Thing()

# constructor sin argumentos o parámetros
class Fruit:
    def __init__(self):
        print('objeto fruta')

fruit = Fruit()

# argumentos del constructor
class CustomFruit:
    """Esta clase no vale para mucho pero me gusta escribir comentarios"""
    COUNTER = 0

    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.juices = 0
        CustomFruit.COUNTER += 1

    def __str__(self):
        return 'Soy fruta, me llamo {} y mi color es {}.\nHay {} frutas en total'\
            .format(self.name, self.color, CustomFruit.COUNTER)

    def make_juice(self, count):
        for n in range(count):
            print('Haciendo zumo de ', self.name)
            self.juices += 1

custom = CustomFruit('Pera', 'verde')
print(custom)
custom.make_juice(2)

c2 = CustomFruit('Limón', 'amarillo')
print(c2)
c2.make_juice(4)
print('Zumos hechos:', c2.juices)
