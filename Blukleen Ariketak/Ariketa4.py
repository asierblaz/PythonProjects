'''
04/12/2020 Asier Blazquez

4.-Programa honek, zenbaki oso baten zenbaki kopurua zenbatzeko
'''
n = int(input("Sartu zenbaki bat: "))

cont = 0

while(n!=0):
    n=n//10
    cont=cont+1

print("Zenbaki kopurua ",cont," da")