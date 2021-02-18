
'''for i in range(altura - grosor):
    for j in range(ancho):
        if (j == 0 or j == ancho - 1 or i == 0 ):
             print('* ', end='')
        else:
            print('  ', end='')
    print()

for i in range(grosor):

    for j in range(base):

        if (j == 0 or j == base - 1 or i == 0 or i == grosor - 1):
            print('* ', end='')
        else:
             print('  ', end='')
    print()'''

altura= 10
ancho =5
grosor= 5
base =10

for i in range(altura - grosor):
    for j in range(ancho):
        if (j == 0 or j == ancho - 1 or i == 0 ):
             print('* ', end='')
        else:
            print('  ', end='')

    print()

for i in range(grosor):

    for j in range(base):

        if (j == 0 or j == base - 1 or i == 0 or i == grosor - 1):
            print('* ', end='')
        else:
             print('  ', end='')
    print()