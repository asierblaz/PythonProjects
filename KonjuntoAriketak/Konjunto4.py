'''

  4.- Eliminar un empleado del equipo anterior. '''


trabajo= set()
trabajo.add('Jefe')
trabajo.add('Administrativo')
trabajo.add('Secretario')

print("añadimos trabajador")

trabajo.add('Medico')
print(trabajo)
trabajo.remove('Medico')
print(trabajo)