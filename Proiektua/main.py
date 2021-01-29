'''22/01/2021 Asier Blazquez
Filmoteka izeneko Proiektu lista baten dauden pelikulak gure bilduma pertsonalera sartuko ditugu.
 Bi erabiltzaile bereizten dira batetik administratzailea , honek pelikulen lista aldatu dezake
pelikulak gehituz eta ezabatuz eta erabiltzaile normala , bere bilduman operazioak egiteko gai izango da.

Filmoteka.pdf irakurri funtzionamendua hobeto ulertzeko.
'''
pelikulak= ["El rey leon", "El Señor de Los anillos", "Interestellar","Alone","El Ilusionista","Spiderman"]

pelikulakHizt = {"El rey leon": 'IKUSITA','El señor de los anillos':'PENDIENTE','Spiderman': 'IKUSITA'}


def pelikulaIkusi(): #Zenbaki bat sartuta posizio horretan dagoen filmari balioa aldatzen dio Ikusita jarriz
    print("Aukeratu zure bildumatik zein pelikula ikusi nahi duzun: \n ")
    bildumaIkusi()

    pelis=[]
    for i in pelikulakHizt.keys():
        pelis.append(i)
    aukera = int(input("\nZure aukera: "))
    pelikulakHizt[pelis[aukera-1]]='IKUSITA'

    print("Zure bilduma eguneratu da. \n")

    bildumaIkusi()


def bildumaraSartu(): #listan dauden pelikuletatik ikusita edo pendiente bezala hiztegian sartu.
    ("Aukeratu pelikula hauetatik zein sartu nahi duzun biludmara: ")
    pelikulakImprimatu()
    aukera= int( input("Zure aukera: "))
    ikusi= input("Ikusita daukazu filma ? (B/E)")
    if (ikusi.upper()=='B'):
     pelikulakHizt[pelikulak[aukera-1]]='IKUSITA'
     print("Filma bilduman gorde da.")
    else:
        pelikulakHizt[pelikulak[aukera - 1]] = 'PENDIENTE'
        print("Filma pendiente bezala gorde da.")


def bildumaIkusi(): #Hiztegian dauden pelikulak imprimatzen ditu

    i=1
    for peli, estado in pelikulakHizt.items():
        print (i,"." ,peli, ":", estado)
        i = i + 1


def pelikulakImprimatu(): #listan dauden pelikulak imprimatzen ditu
    for cont, val in enumerate(pelikulak):
        print(cont+1, val)
    print("\n")

def pelikulaGehitu(): #listara pelikulak sartzen ditu
    pelikulak.append(input("Sartu pelikula berriaren izena:"))
    print("Pelikulen lista eguneratu egin da")
    pelikulakImprimatu()

def pelikulakEzabatu(): #listatik pelikula bat ezabatzen du
    print("Zein pelikula ezabatu nahi duzu?")
    pelikulakImprimatu()
    aukera= int( input("\n Sartu ezabatu nahi duzun pelikularen zenbakia."))
    if pelikulak[aukera-1] in pelikulakHizt.keys():
        print("Erabiltzailearen bildumatik ere ezabatu da\n.")
        del pelikulakHizt[pelikulak[aukera-1]]


    pelikulak.pop(aukera-1)
    print("Pelikulen lista eguneratu egin da")
    pelikulakImprimatu()



def administrazioa(): #admin pass jarrita administraziora sartzen dira
    print("Ongi etorri bideoklubaren administraziora")
    print("*  1. Pelikulak gehitu \n"
    + "*  2. Pelikulak Ezabatu \n"
      "*  3. Irten")

    n = int(input("Aukeratu zenbaki bat: "))

    while n != 3:
        if n == 1:
            print("Pelikulak gehitu: \n ")
            pelikulaGehitu();

        if n == 2:
            print("Pelikulak ezabatu")
            pelikulakEzabatu()

        print("*  1. Pelikulak gehitu \n"+  "*  2. Pelikulak Ezabatu \n*  3. Irten")
        n = int(input("Aukeratu zenbaki bat: "))


'''MENUA '''
print(
    "\n==========================================================================================================="
    , "\n                     Filmoteka                               ",
    "\n===========================================================================================================")

print("*  1. Pelikulen lista ikusi \n"
          + "*  2. Nire Bilduma \n"
          + "*  3. Bildumara sartu\n"
          + "*  4. Pelikula bat ikusi \n"
          + "*  5. Administrazioa\n"
          + "*  6. Irten\n"
      + "*  =======================================================================================================\n")

n = int(input("Aukeratu zenbaki bat: "))
print(" ")

while n != 6:
    if n == 1:
        print("\nHauek dira katalogoan dauden pelikulak")
        pelikulakImprimatu()
    if n == 2:
        print("Hauek dira zure bilduman dauden filmak: \n")
        bildumaIkusi()
    if n == 3:
        bildumaraSartu()
    if n == 4:
        pelikulaIkusi()
    if n == 5:
        contra = input("Sartu administrariaren pasahitza ")
        if contra == "admin":
            administrazioa()
        else:
            print("sartutako pasahitza ez da zuzena")




    print("\n\n\n==========================================================================================================="
        , "\n                     Filmoteka                               ",
        "\n===========================================================================================================")

    print("*  1. Pelikulen lista ikusi \n"
          + "*  2. Nire Bilduma \n"
          + "*  3. Bildumara sartu\n"
          + "*  4. Pelikula bat ikusi \n"
          + "*  5. Administrazioa\n"
          + "*  6. Irten\n"
          + "*  =======================================================================================================\n")
    n = int(input("Aukeratu zenbaki bat: "))

print("ESKERRIKASKO FILMOTEKA ERABILTZEAGAITIK")

