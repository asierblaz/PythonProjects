'''
04/01/2021 Asier Blazquez
1.	Idatzi aldagai batean ondorengo hiztegia
{'Euro' hiztegia: '€', 'Dollar': '$', 'Yen': '¥'} gordetzen duen programa. ç
Eskatu erabiltzaileari moneta eta erakutsi bere ikurra edo mezua. Hiztegian ez badago ohar bat atera.
'''

diccionario = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}

entrada= input('sartu moneta ')


print(diccionario[entrada])