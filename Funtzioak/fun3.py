'''
21/01/2021 Asier Blazquez
3.	Idatzi zenbaki lista bat jasotzen duen funtzioa eta batez bestekoa itzultzen duena.
'''

def media(lista):
    sum = 0.0
    for i in range(0, len(lista)):
        sum = sum + lista[i]
    return sum / len(lista)


lista= []

n= int (input("sartu zenbakiak listan (-1) bukatzeko: "))

while n!=-1:
    lista.append(n)

    n= int (input("Beste elementu bat:  "))


print(lista, "-ren bataz bestekoa ",media(lista))
