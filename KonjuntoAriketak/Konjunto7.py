'''

Asier Blazquez
    8.- Comprobar que el equipo de empleados comunes está incluido en el segundo equipo creado. '''

trabajo= set()
trabajo.add('Jefe')
trabajo.add('Administrativo')
trabajo.add('Secretario')

print("añadimos trabajador")

trabajo.add('Medico')
print(trabajo)
trabajo.remove('Medico')
print(trabajo)


listaconj= set(['taxista', 'Albañil','Jardinero'])

nuevo =set(trabajo & listaconj)

print(nuevo)