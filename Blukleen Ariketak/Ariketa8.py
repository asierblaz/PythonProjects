'''
04/12/2020 Asier Blazquez

8.- Zenbaki bat lehena den edo ez egiaztatzeko programa
'''

n = int(input("Sartu zenbaki bat: "))
cont = 0
i=1
while(i<=n):
    if(n%i==0):
        cont=cont+1
    i=i+1

if (cont<=2):
    print("Zenbakia lehena da")
else:
    print("Zenbakia ez da lehena")