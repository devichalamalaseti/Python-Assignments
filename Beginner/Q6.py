'''Write a Python program to check if a given number is a perfect
number.
A Perfect number is a positive integer that is equal to the sum of
its proper divisors. For instance, 6 has divisors 1, 2, and 3, and 1 + 2 +
3 = 6, so 6 is a perfect number.'''

def is_perfect_number(number):
    if number <= 0:
        return False
    
    divisors = [1]  
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            divisors.append(i)
            if i != number // i:  
                divisors.append(number // i)
    return sum(divisors) == number
num = int(input("Enter a number: "))
if is_perfect_number(num):
    print("Output: Yes")
else:
    print("Output: No")