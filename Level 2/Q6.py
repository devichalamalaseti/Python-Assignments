'''Write a Python program to check if a number is a power of two
using recursion.'''

def recursion(n):
    if n==1:
        return True
    elif n<1 or n%2!=0:
        return False
    else:
        return recursion(n//2)       
num=int(input("Enter the num"))
if recursion(num):
    print(f"Given num {num}is recursive")
else:
    print(f"Given num {num}is not recursive")