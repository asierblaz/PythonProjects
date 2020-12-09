
n= int(input("Sartu zenbakia "))
n1=0
n2=1
aux=0
for i in range(0,n):
    print(n1,end=' ')
    aux=n1+n2
    n1=n2
    n2=aux

