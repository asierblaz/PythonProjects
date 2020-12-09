'''
04/12/2020 Asier Blazquez

6.-Zenbaki baten potentzia kalkulatzeko programa
'''

n = int(input("Sartu zenbaki bat: "))
pot = int(input("Sartu nahi duzun potentzia: "))
result = 1
for i in range(1, pot + 1):
    result = result * n
print(n, "ber", pot, "=", result)
