'''Write a Python program to reverse the order of words in a given
sentence.
Input_sentence = “Hello, World! Welcome to Python
programming.”
Output after reverse = “programming. Python to Welcome
World! Hello,”'''

input_sentence= "Hello, World! Welcome to Python programming."
words=input_sentence.split()
reversed_order=' '.join(reversed(words))
print(reversed_order)