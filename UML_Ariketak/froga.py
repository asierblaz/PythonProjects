



puntuazioa= {'a': 1,'b': 2, 'c': 2};


def balioaKalkulatu(palabra):
    balioa=0
    for i in palabra:
        balioa= balioa+puntuazioa[i]
    return balioa


palabra = input ("palabra: ")
print("hau da", palabra,"-ren balioa ",balioaKalkulatu(palabra))


