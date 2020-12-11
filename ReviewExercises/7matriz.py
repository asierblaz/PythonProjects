'''
04/12/2020 Asier Blazquez


Write a Python program which takes two digits m (row) and n (column)
as input and generates a two-dimensional array. The element value in the i-th row and
 j-th column of the array should be i*jNote :i = 0,1.., m-1j = 0,1, n-1.Test Data :
Rows = 3, Columns = 4Expected Result : [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]
'''

fila = int(input("Sartu filak: "))
columna = int(input("Sartu zutabeak: "))


for row in range(fila):
    for col in range(columna):
        array[row][col]= row*col

print(array)