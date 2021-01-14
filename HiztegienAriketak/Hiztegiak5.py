'''
5.	Idatzi enpresa baten fakturak kudeatuko dituen programa. Fakturak hiztegian gordeko dira, faktura bakoitzaren gakoa fakturaren zenbakia eta
fakturaren kostua balioa izango delarik. Programak erabiltzaileari galdetu beharko dio faktura berri bat gehitu nahi duen, lehendik dagoen bat ordaindu edo bukatu.
a.	Faktura berria gehitu nahi badugu, fakturaren zenbakia eta horren kostua eskatuko zaizkizu eta hiztegian gehitu beharko dira.
b.	Faktura bat ordaindu nahi badugu fakturaren zenbakia eskatuko digu eta hiztegitik kenduko da.
c.	Eragiketa bakoitzaren ondoren, programak orain arte kobratutako zenbatekoa eta ordaindu beharreko zenbatekoa erakutsi behar ditu pantailan.

'''

factura ={'Fact1': '450','Fact2': '830', 'Fact3': '40', 'Fact5': '700'};


print(factura)

ordaindu =0
kobratu =0
opcion= int(input("\nAukeratu bat: "
      "\n 1) Faktura Berria gehitu"
      "\n 2) Faktura Ordaindu"
      "\n 3) irten"
                  ""
                  "\n"));
while( opcion!=3):
    if (opcion == 1):
     kodea= str(input("sartu fakturaren kodea "))
     prezioa= float(input("sartu fakturaren prezioa "))
     factura[kodea]=prezioa
     ordaindu=ordaindu+ prezioa
     print(factura)
     print("Ordaindu Beharrekoa: ", ordaindu)
     print("Ordaindu Kobratuta: ", kobratu)
     opcion = int(input("\nAukeratu bat: "
                        "\n 1) Faktura Berria gehitu"
                        "\n 2) Faktura Ordaindu"
                        "\n 3) irten"
                        ""
                        "\n"));

    else:
        kodea = str(input("sartu fakturaren kodea  "))
        kobratu= kobratu+ int(factura[kodea])
        factura.pop(kodea)
        print(factura)
        print("Ordaindu Beharrekoa: ", ordaindu)
        print("Ordaindu Kobratuta: ", kobratu)
        opcion = int(input("\nAukeratu bat: "
                           "\n 1) Faktura Berria gehitu"
                           "\n 2) Faktura Ordaindu"
                           "\n 3) irten"
                           ""
                           "\n"));

    print("Ordaindu Beharrekoa: " ,ordaindu)
    print("Ordaindu Kobratuta: " ,kobratu)
    print("\n")