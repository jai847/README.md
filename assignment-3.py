#TASK 1- Calculate Factorial Using a Function

def factorial(n):
    if n<2:
        return n
    else:
        return n * factorial(n-1)

result=factorial(7)
print(result)


#task 2- Using the Math Module for Calculations

import math
num1=float(input("enter the value"))
num2= math.sqrt(num1)
num3= math.log(num1)
num4= math.sin(num1)
print(num2)
print(num3)
print(num4)
