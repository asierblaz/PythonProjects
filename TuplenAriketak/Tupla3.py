'''
18/12/2020 Asier Blazquez
3.  Listar los elementos de ambas tuplas '''


laborable= 'Lunes','Martes','Miercoles','Jueves','Viernes'
asteburu= 'Sabado','Domingo'

semana= laborable,asteburu

for i,val in enumerate(semana):
    print(i,val)