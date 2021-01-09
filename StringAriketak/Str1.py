'''
07/01/2021 Asier Blazquez

1.	Partiendo de  un string,  contar el número de caracteres en mayúsculas y minúsculas que tiene el string respectivamente.

'''

texto= "ASDfgdsdh"
minus=0
mayus=0
for i in texto:
    if(i.islower()):
        minus= minus+1
    if(i.isupper()):
        mayus=mayus+1

print('Mayuskulak = ', mayus)
print('Minuskulak = ',minus)