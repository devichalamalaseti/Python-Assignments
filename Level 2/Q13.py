'''Write a Python program to find if a given string starts with a
given character using Lambda.
Sample input: input_string = "Hello, World!", given_char = "H"
Sample Output: True'''

lamstart=lambda str,s1:str.startswith(s1)
input_string="Hello,World!"
given_char="H"
result=lamstart(input_string,given_char)
print(result)