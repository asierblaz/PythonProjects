'''
11/12/2020 Asier Blazquez

Write  a  Python  program  to  get  a  list,
 sorted  in  increasing  order  by  the  last element
 in each tuple from a given list of non-empty tuples.
 Sample List :[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
'''

list= [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
listaberria=[]
listaemaitza=[]


for i in list:
    listaberria.append(i[-1])
print(listaberria)
listaberria.sort()
print(listaberria)

for i in listaberria:
    for j in list:
        if (i== int(j[-1])):
         listaemaitza.append(j)
print(listaemaitza)


