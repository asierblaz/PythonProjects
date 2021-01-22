'''
21/01/2021 Asier Blazquez
4.	Idatzi zenbaki lista bat jaso eta beste zerrenda bat baloreen karratuekin itzultzen duen funtzioa.
'''



def listaberbi(lista):
    sum = 0.0
    lista2=[]
    for i in range(0, len(lista)):

        lista2.append(lista[i]**2)
    return lista2


lista= []

n= int (input("sartu zenbakiak listan (-1) bukatzeko: "))

while n!=-1:
    lista.append(n)

    n= int (input("Beste elementu bat:  "))


print(lista, "-ren bataz bestekoa ",listaberbi(lista))
