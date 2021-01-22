'''
21/01/2021 Asier Blazquez
2.	Zirkulu baten azalera kalkulatzen duen funtzio bat idatzi.
 Ondoren beste funtzio bat idatzi, aurreko funtzioa erabiliz, zirkuluaren bolumena kalkulatuko duena.
'''
import math
def azalera (erradioa):

    area = math.pi * erradioa ** 2;
    return area


def bolumen ():
    print(erradioa, "erradioa duen zirkulu baten azalera ",azalera(erradioa)," da baina ezin da zirkulu baten bolumena kalkulatu")

erradioa= float (input("Sartu zenbaki oso positibo bat: "))

bolumen()