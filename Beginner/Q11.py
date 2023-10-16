'''Write a Python program to calculate the sum of digits of a given
number until the sum becomes a single-digit number.
Sample Input: num = 987
Sample Output: Sum_of_digits = 24,
Again compute the sum of digits so that it can be reduced to
on single digit.
Final Output: 6'''

def digit_sum(num):
    while num>=10:
        sum=0
        while num>0:
            sum+=num%10
            num//10
            num=sum
            return num
num=int(input("Enter the number"))

result = digit_sum(num)
print(result)