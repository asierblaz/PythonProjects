'''
04/12/2020 Asier Blazquez

10.-Zenbaki baten faktoreak bistaratzeko programa'''


def zatitzaileaDa(n,zat):
    if(n%zat==0):
        return True
    else:
        return False



n=int(input("Sartu zenbaki bat "))

for i in range(1,n+1):
    if(zatitzaileaDa(n,i)==True):
        print(i,end=' ')


