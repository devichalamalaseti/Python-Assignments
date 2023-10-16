'''Write a Python program to find the sum of all odd numbers
between two given numbers.
Start = 1, stop = 10
Sum of odd numbers: 25'''

a=int(input("Enter 1st number"))
b=int(input("Enter 2nd number"))
sum=0
if a%2==0:
    a+=1
for i in range(a,b+1,2):
    sum+=i
print(f"Sum of odd numbers between {a} and {b} is {sum}")