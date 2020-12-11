'''
08/12/2020 Asier Blazquez

Write a Python program that reads two integers representing a month and day and prints the season
for that month and day.Expected Output:Input the month (e.g. January, February etc.):
july  Input the day: 31   Season is autumn
'''

mes = (input("Sartu hila: "))
dia = int(input("Sartu eguna "))
mes = mes.lower()
estacion = ""
if mes in ('apirila', 'maiatza'):
    estacion = 'Udaberria'

elif mes in ('uztaila', 'abuztua'):
    estacion = 'uda'

elif mes in ('urria', 'azaroa'):
    estacion = 'udazkena'

elif mes in ('uartarrila', 'otsaila'):
    estacion = 'Negua'



if (mes == 'martxoa') and (dia >= 21):
    estacion = 'Udaberria'
else:
    estacion='Negua'

if (mes == 'ekaina') and (dia >= 21):
    estacion = 'Uda'
else:
    estacion="Udaberria"


if (mes == 'iraila') and (dia >= 21):
    estacion = 'Urria'
else:
    estacion= 'Uda'

if (mes == 'abendua') and (dia >= 21):
    estacion = 'Negua'
else: "Udazkena"


print(mes, 'ren ', dia, ' ', estacion, ' da')
