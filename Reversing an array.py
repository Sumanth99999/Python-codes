# Reversing an array without using inbuilt Functions

from array import *
arr = array('i',[])
a = int(input('Enter the range of the array:'))
for i in range(a):
    x= int(input("Enter the next number:"))
    arr.append(x)

print(arr[::-1])

