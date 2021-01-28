'''22/01/2021 Asier Blazquez

Funtzioen proiektua
'''
pelikulak= ["El rey leon", "El Señor de Los anillos", "Interestellar"]

pelikulakHizt = {""}


def pelikulakImprimatu():
    for cont, val in enumerate(pelikulak):
        print(cont+1, val)
    print("\n")

def pelikulaGehitu():
    pelikulak.append(input("Sartu pelikula berriaren izena:"))
    print("Pelikulen lista eguneratu egin da")
    pelikulakImprimatu()

def pelikulakEzabatu():
    print("Zein pelikula ezabatu nahi duzu?")
    pelikulakImprimatu()
    aukera= int( input("\n Sartu ezabatu nahi duzun pelikularen zenbakia."))
    pelikulak.pop(aukera-1)
    print("Pelikulen lista eguneratu egin da")
    pelikulakImprimatu()



def administrazioa():
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
    , "\n                     Bideoklub                               ",
    "\n===========================================================================================================")

print("*  1. Pelikulak ikusi \n"
      + "*  2. Aukera 2\n"
      + "*  3. Aukera 3\n"
      + "*  4. Aukera 4\n"
      + "*  5. Administrazioa\n"
      + "*  6. Irten\n"
      + "*  =======================================================================================================\n")

n = int(input("Aukeratu zenbaki bat: "))
print(" ")

while n != 6:
    if n == 1:
        print("\nHauek dira katalogoan daudel pelikulak")
        pelikulakImprimatu()
    if n == 2:
        print("2")
    if n == 3:
        print("3")
    if n == 4:
        print("4")
    if n == 5:
        contra = input("Sartu administrariaren pasahitza ")
        if contra == "admin":
            administrazioa()
        else:
            print("sartutako pasahitza ez da zuzena")

    if n == 6:
        print("6")


    print("\n\n\n==========================================================================================================="
        , "\n                     Bideoklub                               ",
        "\n===========================================================================================================")

    print("*  1. Pelikulak ikusi \n"
          + "*  2. Aukera 2\n"
          + "*  3. Aukera 3\n"
          + "*  4. Aukera 4\n"
          + "*  5. Administrazioa\n"
          + "*  6. Irten\n"
          + "*  =======================================================================================================\n")
    n = int(input("Aukeratu zenbaki bat: "))


