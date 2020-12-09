'''
04/12/2020 Asier Blazquez

Write a Python program to count the number of even and odd numbers from
a series of numbers.Sample numbers: numbers=(1,2,3,4,5,6,7,8,9)
Expected Output:Number of even numbers : 5Number of odd numbers : 4

'''
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

par=0;

impar=0;

for i in numbers:
    if(i %2 ==0):
        par=par+1
    else:
        impar=impar+1

print("Zenbaki bakoitiak: ",impar)
print("Zenbaki bakoitiak: ",par)