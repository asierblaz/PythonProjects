'''
18/12/2020 Asier Blazquez

9.  Indicar qué número de día de la semana (1º, 2º ... 7º) se ha leído.
'''

dias='Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo'

laborable= 'Lunes','Martes','Miercoles','Jueves','Viernes'
asteburu= 'Sabado','Domingo'

semana= laborable,asteburu


eguna = input("Introduce un dia de la semana :")
while eguna not in dias:
    eguna = input("Introduce un dia de la semana :")

if(eguna in dias):
    print(dias.index(eguna)+1,eguna)
