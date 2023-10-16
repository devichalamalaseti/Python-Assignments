'''Write a Python program to reverse a number using a while
loop.
Sample Input: num = 12345
Sample Output: revnum = 54321'''

def reverse(num):
    a= 0
    while num> 0:
        digit = num % 10
        a=  a* 10 + digit
        num //= 10
    return a
num = int(input("Enter the num"))
result = reverse(num)
print("Result is ", result)