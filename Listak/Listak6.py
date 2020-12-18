'''
17/12/2020 Asier Blazquez
Write a Python program to remove duplicates from a list.
'''


list= ['a','e','e','i','o','u']

list2=[]
for i in list:
    if i not in list2:
        list2.append(i)
list=list2

print(list)