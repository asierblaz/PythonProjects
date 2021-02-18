

altura= 10
ancho =5
grosor= 5
base =10



for i in range (altura):#filas
    for j in range (ancho):#columnas

        if(i==altura-grosor-1):
            ancho=base


        if(i==0 or i==altura-1 or j==0 or j==ancho-1):
            print('* ', end='')
        else:
            print('  ', end='')

    print()