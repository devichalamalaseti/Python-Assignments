'''Write a Python function that counts the number of vowels in a
given string.
Sample Input: string = "Hello, World!"
Sample Output: Number of vowels: 3'''

def vowelcount(s1):
    s1=s1.lower()
    vowels="aeiou"
    count=0
    for char in s1:
        if char in vowels:
            count+=1
    return count
s1="Hello, World!"
count=vowelcount(s1)
print(count)