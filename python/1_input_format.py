"""
Ejemplo para pedir input de usuario y formatear la respuesta
"""

PREGUNTA = '¿Cómo te llamas? '
RESPUESTA = input(PREGUNTA)

print('Hola', RESPUESTA, '¿cómo estás?')

respuesta_formateada = 'Hola {}, ¿cómo estás?'.format(RESPUESTA)
print(respuesta_formateada)