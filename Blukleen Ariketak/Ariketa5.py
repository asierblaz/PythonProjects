'''
04/12/2020 Asier Blazquez

5.-Zenbaki bat jaso eta alderantzizkoa bueltatuko duen programa

'''

n = int(input("Sartu zenbaki bat: "))

resto = 0
result = 0
while (n != 0):
    resto = n % 10
    result = result * 10 + resto
    n=n//10
print("Zenbakia alderantziz",result)
