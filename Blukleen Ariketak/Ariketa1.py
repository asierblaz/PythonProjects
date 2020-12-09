'''
03/12/2020 Asier Blazquez

1.-Zenbaki naturalen batura aurkitzeko programa
'''

n=int(input("Sartu zenbaki bat: "))
sum=0

for i in range (1,n+1) :
    sum=sum+i
print("Zenbaki naturalen batuketa",n ,"-raino:" ,sum," da")