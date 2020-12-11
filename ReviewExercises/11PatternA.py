'''
09/12/2020 Asier Blazquez

Write a Python program to print alphabet pattern 'A'.:'''


for i in range(1,8):
    for j in range(1,8):
        if (((j == 2 or j == 6) and i != 1) or ((i == 1 or i == 4) and (j >2  and j < 6))):
             print("*",end='')
        else:
            print(" ",end='')
    print("")
