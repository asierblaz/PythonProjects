
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


ancho1=ancho
for i in range (altura):#filas
    for j in range (ancho):#columnas
        if(i==0 or i==altura-1 or j==0 or j==ancho-1 or ((i==altura-grosor)and j>=ancho1-1) ):
            print('* ', end='')
        else:
            print('  ', end='')

    if(i==altura-grosor-1):
            ancho=base
    print()