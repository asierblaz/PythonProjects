'''
04/12/2020 Asier Blazquez

Write a Python program which iterates the integers
 from 1 to 50. For multiples of three print "Fizz"
 instead of the number and for the multiples of five print
 "Buzz". For numbers which are multiples of both three and
 five print "FizzBuzz".Sample Output:fizzbuzz12fizz4buzz
'''

for i in range(1,50+1):
    if(i%5==0 and i%3==0):
        print('FizzBuzz')
    elif(i%3==0):
        print('Fizz')
    elif(i%5==0):
        print('Buzz')
    else:
        print(i)