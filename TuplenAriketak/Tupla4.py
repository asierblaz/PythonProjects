'''
18/12/2020 Asier Blazquez

4.  Recorrer y mostrar por pantalla todos los elementos de la última tupla, indicando en qué posición están.
'''

laborable= 'Lunes','Martes','Miercoles','Jueves','Viernes'
asteburu= 'Sabado','Domingo'

semana= laborable,asteburu

for i,val in enumerate(asteburu):
    print(i,val)