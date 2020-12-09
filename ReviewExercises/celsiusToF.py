'''
27/11/2020 Asier Blazquez

5- Celsius Farenheitera pasatzen du
'''

print('Programa honek Celsius gradutatik \n Farenheit-era pasatzen du\n')
celsius = float(input("Sartu Celsius: "))

far =0.0

if (celsius==0):
    far=32.0
    print(celsius, " ºC ", far, "F dira ");
else:
    far = celsius * 33.80;
    print(celsius, " ºC ", far, "F dira ");

