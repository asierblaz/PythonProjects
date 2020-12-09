'''
03/12/2020 Asier Blazquez

3.-Zenbaki baten Biderketa taula  sortzeko programa
'''

n = int(input("Sartu zenbaki bat: "))
emaitza = 1

for i in range(1, 10):
    emaitza = n * i
    print(n,'x',i,'=',emaitza)
