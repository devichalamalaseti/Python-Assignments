'''Write a Python program to count the frequency of each element
in a list.
Input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]
Frequency count: {1: 2, 2: 3, 3: 1, 4: 2, 5: 1}'''

from collections import Counter
input_list=[1,2,3,4,5,6,7,7,7,3,3,7,1,2,4]
frequency_count=Counter(input_list)
print(dict(frequency_count))