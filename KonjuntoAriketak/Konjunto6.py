'''

Asier Blazquez
  6.- Usando el operador de unión crear un conjunto con los 2 anteriores. '''

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

print(listaconj)

print(listaconj.union(trabajo))


listaconj.update(trabajo)
print(listaconj)
