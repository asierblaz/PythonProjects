'''

2.	Idatzi programa bat erabiltzaileari bere izena, adina, helbidea eta telefono zenbakia eskatzen dizkiona
eta datuak hiztegi batean gorde. Ondoren mezu hau atera: “ <izena> k <adina> urte ditu,  <helbidean>    bizi da
  eta bere teléfono zenbakia ondorengoa da: <telefonoa>.

'''
persona={};
persona['izena']= input('Sartu izena: ')
persona['adina']= input('Sartu adina: ')
persona['helbidea']= input('Sartu helbidea: ')
persona['telefonoa']= input('Sartu telefonoa: ')

print(persona['izena'] ,"k", persona['adina'] ,"urte ditu",  persona['helbidea'] ,"  bizi da  eta bere teléfono zenbakia ondorengoa da:",persona['izena'])
