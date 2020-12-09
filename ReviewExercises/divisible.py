'''
04/12/2020 Asier Blazquez

Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included)
'''

n1=1500
n2=2700


print("\nHauek dira 1500 eta 2700 artean dauden zenbakiak: ")
for i in range(n1, n2+1):
    if(i%7==0 and i%5==0):
        print(i,end=' ')