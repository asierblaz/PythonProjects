'''
17/12/2020 Asier Blazquez
Write a Python program access the index of a list'''


list = [2, 4,4, 6, 8]
list2 = []
encontrado= False
for cont, val in enumerate(list):
    for j,val2 in enumerate(list2):
        if(val==val2):
            encontrado=True
if(encontrado==False):
    list2.append(val)
print(list2)
