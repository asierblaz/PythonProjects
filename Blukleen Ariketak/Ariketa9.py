'''
04/12/2020 Asier Blazquez

9-Bi zenbakiren artean dauden zenbaki lehenak bistaratzeko programa
'''


def lehenaDa(n):
    cont = 0
    i = 1

    while (i <= n):
        if (n % i == 0):
            cont = cont + 1
        i = i + 1
    if (cont <= 2):
        return True
    else:
        return False


n = int(input("Sartu tarte baten lehenengo zenbakia: "))
n1 = int(input("Sartu tarte baten bigarren zenbakia: "))

for i in range(n, n1 + 1):
    if (lehenaDa(i) == True):
        print(i, end=' ')

