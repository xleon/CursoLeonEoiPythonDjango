"""
Ejemplo del uso de expresiones regulares
"""

import re

phone = '605133587 # esto es un nùmero de teléfono'

# borrar comentarios
number = re.sub(r'#.*$', '', phone)
print('Teléfono:', number)

# borrar cualquier cosa que no sean dígitos
number = re.sub(r'\D', '', phone)
print('Teléfono:', number)