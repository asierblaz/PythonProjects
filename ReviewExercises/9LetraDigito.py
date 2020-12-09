'''
08/12/2020 Asier Blazquez


Write a Python program that accepts a string and calculate the number
of digits and letters  (isalpha() and is digit() functions)
Sample Data : Python 3.2Expected Output :Letters 6Digits 2

'''

sarrera = input("Sartu String bat: ")
num = 0
letra = 0
for i in sarrera:
    if (i.isdigit()):
        num = num + 1
    if (i.isalpha()):
        letra = letra + 1

print('Letrak: ', letra)
print('digitoak: ', num)
