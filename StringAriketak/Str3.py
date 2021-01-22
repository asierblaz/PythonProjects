'''
08/01/2021 Asier Blazquez

3.	A partir de  un parámetro s y otro n, que separe quite el caracter n-ésimo en s y retorne el string a partir de la posición n+1 en adelante.'''
texto= "LEOMessi"

texto2= texto.split('M')

nuevo = texto.find(texto2)


print(texto2[nuevo+1:len(texto)])