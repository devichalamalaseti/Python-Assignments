'''Write a Python function that finds the median of a list of
numbers.
Sample Input: number_list = [7, 2, 5, 1, 9, 3]
Sample Output: Median: 4.0'''

def median_num(num1):
    num1.sort()
    l1=len(num1)
    if l1%2==1:
        median=num1[l1//2]
    else:
        middle1=num1[l1//2-1]
        middle2=num1[l1//2]
        median=(middle1+middle2)/2
    return median
num1=[7,2,5,1,9,3]
median=median_num(num1)
print(median)