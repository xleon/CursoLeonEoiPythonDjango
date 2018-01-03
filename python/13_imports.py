"""
Ejemplos de cómo importar módulos y funciones.
Más información útil aquí: https://www.codementor.io/sheena/python-path-virtualenv-import-for-beginners-du107r3o1
"""

import utils

utils.lib_method()

from libs import bombing

bombing.where_are_the_bombs()

from libs.bombing import where_are_the_bombs as where

where()

from libs.eating import *
# from libs.eating import eat_apples, eat_pie
eat_apples(5)
eat_pie('300 gr')

