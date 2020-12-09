'''
03/12/2020 Asier Blazquez

Make   a   program   that   asks   the   number   between   1   and   10. If  the  number  is  out  of  range  the  program  should display  "invalid number".
'''

n= int(input("Sartu zenbaki bat: "))

if(n<1 or n>10):
    print("invalid number")