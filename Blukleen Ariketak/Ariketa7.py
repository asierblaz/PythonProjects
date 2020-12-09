'''
04/12/2020 Asier Blazquez

7.- Zenbakia Palindromoa den edo ez egiaztatzeko prgrama
'''

n = int(input("Sartu zenbaki bat: "))
aux=n
resto = 0
result = 0
while (n != 0):
    resto = n % 10
    result = result * 10 + resto
    n=n//10

if(result==aux):
    print(aux, " Zenbakia palindromoa da")
else:
    print(aux, " Zenbakia ez palindromoa da")

