


altura = int(input ('altura '))
ancho = int(input ('ancho '))
grosor=int(input ('grosor '))
base = int(input ('base '))


for i in range (altura-grosor):
    for j in range (ancho):
     print('*', end='')
    print()
for i in range (grosor):
    for j in range (base):
     print('*', end='')
    print()