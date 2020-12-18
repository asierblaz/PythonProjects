'''
18/12/2020 Asier Blazquez
8.  Pedir al usuario un día de la semana y usar la última tupla para repetir la petición hasta que el texto coincida con un día. '''

dias='Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo'

laborable= 'Lunes','Martes','Miercoles','Jueves','Viernes'
asteburu= 'Sabado','Domingo'

semana= laborable,asteburu


eguna = input("Introduce un dia de la semana :")
while eguna not in dias:
    eguna = input("Introduce un dia de la semana :")
