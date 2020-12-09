'''
09/12/2020 Asier Blazquez

Write a Python program to print alphabet pattern 'A'.:'''

res=' '
for i in range (1,8):
    for j in range(1,8):
        if (((j == 2 or j == 6) and i != 1) or ((j == 1 or i == 4) and (j >= 1 and i <= 5))):
            print('*',end='')
        else:
            print(' ')

