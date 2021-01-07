'''

4.	Idatzi  hiztegi batean fruitu hauen prezioak kiloko.
 Galdetu erabiltzaileari fruitu bat, kilo kopuru bat eta erakutsi pantailan kiloko fruitu kopuru horren prezioa.
 Fruta hiztegian ez badago mezu horren berri eman beharko zenioke.
'''

fruta ={'Banana': '1,35','Sagarra': '0.8', 'Udarea': '0.85', 'Laranja': '0.7'};

sarrera = input("sartu fruitu bat: ")

if (sarrera in fruta):
    print(fruta[sarrera])
else:
    print(sarrera, "ez dago hiztegian")