'''Write a Python program to calculate the LCM (Least Common
Multiple) of two numbers.
number1 = 12, number2 = 18
LCM of 12 and 18 are: 36'''

import math
def lcm(a,b):
    c= (a*b)//math.gcd(a,b)
    return c
num1=int(input("Enter the number1"))
num2=int(input("Enter the number2"))
result=lcm(num1,num2)
print(result)