'''22/01/2021 Asier Blazquez

Funtzioen proiektua
'''
pelikulak= ["El rey leon"]


def peliculaGehitu():
    print("sartu")
    pelikulak.append("hola")


def administrazioa():
    print("Ongi etorri bideoklubaren administraziora")
    print("*  1. Pelikulak gehitu \n"
    + "*  2. Pelikulak Aldatu \n"
     + "* 3. Pelikulak Ezabatu \n* 4. Irten")

    n = int(input("Aukeratu zenbaki bat: "))

    while n != 4:
        if n == 1:
            print("Pelikulak gehitu: \n ")
            peliculaGehitu();
        if n == 2:
            print("Pelikulak Aldatu")
        if n == 3:
            print("Pelikulak ezabatu")

        print("*  1. Pelikulak gehitu \n"+ "*  2. Pelikulak Aldatu \n" + "*  2. Pelikulak Ezabatu \n")
        n = int(input("Aukeratu zenbaki bat: "))

'''MENUA '''
print(
    "\n==========================================================================================================="
    , "\n                     Bideoklub                               ",
    "\n===========================================================================================================")

print("*  1. Pelikulak ikusi 1\n"
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
        print("1")
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

    print("*  1. Pelikulak ikusi 1\n"
          + "*  2. Aukera 2\n"
          + "*  3. Aukera 3\n"
          + "*  4. Aukera 4\n"
          + "*  5. Administrazioa\n"
          + "*  6. Irten\n"
          + "*  =======================================================================================================\n")
    n = int(input("Aukeratu zenbaki bat: "))


print(pelikulak)