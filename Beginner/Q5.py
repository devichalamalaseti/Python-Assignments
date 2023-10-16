#Write a Python program to find the factorial of a number using a
#for loop.

a=int(input("Enter the num"))
factorial=1
for i in range(1,a+1):
    factorial *= i
print("factorial is",factorial)