'''
08/12/2020 Asier Blazquez

Write a Python program to construct the following pattern, using a nested for loop.

'''
zabalera = 5;
for i in range(zabalera):
    for j in range(i):
        print('* ', end="")
    print('')
for i in range(zabalera):
    for j in range(zabalera):
        print('* ', end="")
    zabalera=zabalera-1
    print('')


