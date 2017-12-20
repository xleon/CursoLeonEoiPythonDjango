"""
Ejemplos para trabajar con diccionarios
"""

ALUMNO = {
    'nombre': 'David',
    'edad': 21,
    'clase': 'python'
}

print(ALUMNO['nombre'])
print(ALUMNO['edad'])
print(ALUMNO['clase'])

ALUMNO['edad'] = 18
print(ALUMNO)

ALUMNO['sexo'] = 'masculino'
print(ALUMNO)

del ALUMNO['sexo']
print(ALUMNO)

ALUMNO.clear()
print(ALUMNO)

del ALUMNO
print(ALUMNO)