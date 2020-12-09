'''
03/12/2020 Asier Blazquez

2.-Zenbaki baten faktoriala aurkitzeko programa
'''

n = int(input("Sartu zenbaki bat: "))
multi = 1

for i in range(1, n + 1):
    multi = multi * i
print(n, "zenbakiaren faktoriala:", multi, " da")
