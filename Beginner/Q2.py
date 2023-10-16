'''Write a program that accepts a string as input from the user and
calculates the number of digits and letters.
Input: Hello123
Output: Alphabets: 5 & Number : 3'''
x=input("Enter the string")
alph=0
Num=0
for char in x:
    if char.isalpha():
        alph+=1
    elif char.isdigit():
        Num+=1
print(f"alphabets {alph}: & Numbers: {Num}")