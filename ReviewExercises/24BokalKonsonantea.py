'''
08/12/2020 Asier Blazquez

Write a Python program to check whether an alphabet is a vowel or consonant.Expected Output:'''

letra= input("Input a letter of the alphabet ").lower()

if letra in ('a','e','i','o','u'):
    print(letra,' letter is vocal')
else:
    print(letra,' letter is consonant')
