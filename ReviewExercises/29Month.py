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
if mes in ('apirila', 'maiatza','ekaina'):
    estacion = 'Udaberria'

elif mes in ('uztaila', 'abuztua','irala'):
    estacion = 'uda'

elif mes in ('urria', 'azaroa','abendua'):
    estacion = 'udazkena'

elif mes in ('uartarrila', 'otsaila','martxoa'):
    estacion = 'Negua'


if (mes == 'martxoa') and (dia >= 21):
    estacion = 'Udaberria'

if (mes == 'ekaina') and (dia >= 21):
    estacion = 'Uda'


if (mes == 'iraila') and (dia >= 21):
    estacion = 'Urria'


if (mes == 'abendua') and (dia >= 21):
    estacion = 'Negua'

print(mes, 'ren ', dia, ' ', estacion, ' da')
