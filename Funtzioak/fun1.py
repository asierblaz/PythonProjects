'''
21/01/2021 Asier Blazquez

1.	Idatzi zenbaki oso positibo bat jaso eta bere faktoriala itzultzen duen programa.
'''
def faktoriala (n):
    emaitza = 1
    i = 1
    while i <= n:
        emaitza = emaitza * i
        i = i + 1
    return emaitza


n= int (input("Sartu zenbaki oso positibo bat: "))

print(n," zenbakiaren faktoriala = ", faktoriala(n))



