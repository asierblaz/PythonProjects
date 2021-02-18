

'''
altura = int(input ('altura '))
ancho = int(input ('ancho '))
grosor=int(input ('grosor '))
base = int(input ('base '))
'''
altura= 10
ancho =5
grosor= 5
base =10





for i in range (altura):#filas
    for j in range (ancho):#columnas
        print('* ', end='')
        if(i==altura-grosor-1):
            ancho=base

    print()
